"""
86_insider_buy_sell_ratio — Base Features 076-200
Domain: insider buy/sell balance — net insider sentiment from the balance of buying vs selling
Asset class: US equities | Sharadar SF2 insider transactions (daily-aggregated)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.

SF2 Daily-Aggregated Insider Series Contract
--------------------------------------------
Inputs to all feature functions are daily-frequency pandas Series aggregated
from Sharadar SF2 insider transaction filings.  Each row represents one
(ticker, date); most days have ZERO activity — positive values appear only on
filing days.  Do NOT forward-fill these series.  Aggregate over trailing
windows using rolling SUMS.  Window constants follow the standard trading-day
calendar: 1 week = 5 days, 1 month = 21 days, 1 quarter = 63 days,
1 year = 252 days.

Primary fields used in this file (all lowercase canonical names):
  insider_buy_count, insider_sell_count,
  insider_buy_shares, insider_sell_shares,
  insider_buy_value, insider_sell_value,
  insider_buyers, insider_sellers,
  officer_buy_value, officer_sell_value,
  director_buy_value, director_sell_value
"""
import numpy as np
import pandas as pd

# ── Constants ─────────────────────────────────────────────────────────────────
_W5   = 5
_W21  = 21
_W63  = 63
_W126 = 126
_W252 = 252
_W504 = 504
_EPS  = 1e-9

# ── Utility helpers ───────────────────────────────────────────────────────────

def _safe_div(num: pd.Series, den: pd.Series) -> pd.Series:
    """Element-wise division; replaces zero (and NaN-producing) denominators with NaN.
    Buy/sell ratios frequently have zero sell totals — return NaN deliberately."""
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


def _rolling_rank_pct(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(2, w // 4)).rank(pct=True)


def _zscore_rolling(s: pd.Series, w: int) -> pd.Series:
    m  = _rolling_mean(s, w)
    sd = _rolling_std(s, w)
    return _safe_div(s - m, sd)


def _net_value_flow(buy_val: pd.Series, sell_val: pd.Series, w: int) -> pd.Series:
    return _rolling_sum(buy_val, w) - _rolling_sum(sell_val, w)


def _buy_fraction(buy: pd.Series, sell: pd.Series, w: int) -> pd.Series:
    sb = _rolling_sum(buy, w)
    ss = _rolling_sum(sell, w)
    return _safe_div(sb, sb + ss)


# ── Feature functions 076-150 ─────────────────────────────────────────────────

# --- Group F (076-090): Normalized net-flow scores and extreme ratio detection ---

def ibr_076_value_net_flow_norm_21d(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """Net dollar flow over 21 days normalized by total (buy+sell) volume — centered at 0."""
    sb = _rolling_sum(insider_buy_value, _W21)
    ss = _rolling_sum(insider_sell_value, _W21)
    net = sb - ss
    total = sb + ss
    return _safe_div(net, total)


def ibr_077_value_net_flow_norm_63d(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """Net dollar flow over 63 days normalized by total (buy+sell) volume."""
    sb = _rolling_sum(insider_buy_value, _W63)
    ss = _rolling_sum(insider_sell_value, _W63)
    net = sb - ss
    total = sb + ss
    return _safe_div(net, total)


def ibr_078_value_net_flow_norm_252d(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """Net dollar flow over 252 days normalized by total (buy+sell) volume."""
    sb = _rolling_sum(insider_buy_value, _W252)
    ss = _rolling_sum(insider_sell_value, _W252)
    net = sb - ss
    total = sb + ss
    return _safe_div(net, total)


def ibr_079_count_net_flow_norm_21d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Net transaction count over 21 days normalized by total transaction count."""
    sb = _rolling_sum(insider_buy_count, _W21)
    ss = _rolling_sum(insider_sell_count, _W21)
    net = sb - ss
    total = sb + ss
    return _safe_div(net, total)


def ibr_080_count_net_flow_norm_63d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Net transaction count over 63 days normalized by total transaction count."""
    sb = _rolling_sum(insider_buy_count, _W63)
    ss = _rolling_sum(insider_sell_count, _W63)
    net = sb - ss
    total = sb + ss
    return _safe_div(net, total)


def ibr_081_count_net_flow_norm_252d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Net transaction count over 252 days normalized by total transaction count."""
    sb = _rolling_sum(insider_buy_count, _W252)
    ss = _rolling_sum(insider_sell_count, _W252)
    net = sb - ss
    total = sb + ss
    return _safe_div(net, total)


def ibr_082_share_net_flow_norm_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series) -> pd.Series:
    """Net share flow over 63 days normalized by total share volume transacted."""
    sb = _rolling_sum(insider_buy_shares, _W63)
    ss = _rolling_sum(insider_sell_shares, _W63)
    net = sb - ss
    total = sb + ss
    return _safe_div(net, total)


def ibr_083_share_net_flow_norm_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series) -> pd.Series:
    """Net share flow over 252 days normalized by total share volume transacted."""
    sb = _rolling_sum(insider_buy_shares, _W252)
    ss = _rolling_sum(insider_sell_shares, _W252)
    net = sb - ss
    total = sb + ss
    return _safe_div(net, total)


def ibr_084_value_ratio_peak_21_in_252(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """Rolling 21-day value ratio at its 252-day trailing maximum — recent buy surge."""
    ratio21 = _safe_div(_rolling_sum(insider_buy_value, _W21), _rolling_sum(insider_sell_value, _W21))
    return _rolling_max(ratio21, _W252)


def ibr_085_value_ratio_trough_21_in_252(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """Rolling 21-day value ratio at its 252-day trailing minimum — captures sell dominance episodes."""
    ratio21 = _safe_div(_rolling_sum(insider_buy_value, _W21), _rolling_sum(insider_sell_value, _W21))
    return _rolling_min(ratio21, _W252)


def ibr_086_count_ratio_peak_21_in_252(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Rolling 21-day count ratio at its 252-day trailing maximum."""
    ratio21 = _safe_div(_rolling_sum(insider_buy_count, _W21), _rolling_sum(insider_sell_count, _W21))
    return _rolling_max(ratio21, _W252)


def ibr_087_count_ratio_trough_21_in_252(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Rolling 21-day count ratio at its 252-day trailing minimum."""
    ratio21 = _safe_div(_rolling_sum(insider_buy_count, _W21), _rolling_sum(insider_sell_count, _W21))
    return _rolling_min(ratio21, _W252)


def ibr_088_value_ratio_pct_rank_252d(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """Percentile rank of the rolling 63-day value ratio within its 252-day history."""
    ratio63 = _safe_div(_rolling_sum(insider_buy_value, _W63), _rolling_sum(insider_sell_value, _W63))
    return _rolling_rank_pct(ratio63, _W252)


def ibr_089_count_ratio_pct_rank_252d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Percentile rank of the rolling 63-day count ratio within its 252-day history."""
    ratio63 = _safe_div(_rolling_sum(insider_buy_count, _W63), _rolling_sum(insider_sell_count, _W63))
    return _rolling_rank_pct(ratio63, _W252)


def ibr_090_buyer_fraction_pct_rank_252d(insider_buyers: pd.Series, insider_sellers: pd.Series) -> pd.Series:
    """Percentile rank of the rolling 63-day buyer fraction within its 252-day history."""
    bf63 = _buy_fraction(insider_buyers, insider_sellers, _W63)
    return _rolling_rank_pct(bf63, _W252)


# --- Group G (091-105): Net-flow streaks and regime changes ---

def ibr_091_value_net_flow_positive_days_21d(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """Count of days with positive net insider dollar flow in trailing 21-day window."""
    net_daily = insider_buy_value - insider_sell_value
    pos = (net_daily > 0).astype(float)
    return _rolling_sum(pos, _W21)


def ibr_092_value_net_flow_positive_days_63d(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """Count of days with positive net insider dollar flow in trailing 63-day window."""
    net_daily = insider_buy_value - insider_sell_value
    pos = (net_daily > 0).astype(float)
    return _rolling_sum(pos, _W63)


def ibr_093_value_net_flow_positive_days_252d(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """Count of days with positive net insider dollar flow in trailing 252-day window."""
    net_daily = insider_buy_value - insider_sell_value
    pos = (net_daily > 0).astype(float)
    return _rolling_sum(pos, _W252)


def ibr_094_value_net_flow_negative_days_63d(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """Count of days with negative net insider dollar flow in trailing 63-day window."""
    net_daily = insider_buy_value - insider_sell_value
    neg = (net_daily < 0).astype(float)
    return _rolling_sum(neg, _W63)


def ibr_095_count_buy_dominant_days_63d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Count of days where buy-count exceeds sell-count in trailing 63-day window."""
    dom = (insider_buy_count > insider_sell_count).astype(float)
    return _rolling_sum(dom, _W63)


def ibr_096_count_sell_dominant_days_63d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Count of days where sell-count exceeds buy-count in trailing 63-day window."""
    dom = (insider_sell_count > insider_buy_count).astype(float)
    return _rolling_sum(dom, _W63)


def ibr_097_count_buy_dominant_days_252d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Count of days where buy-count exceeds sell-count in trailing 252-day window."""
    dom = (insider_buy_count > insider_sell_count).astype(float)
    return _rolling_sum(dom, _W252)


def ibr_098_value_buy_dominant_days_252d(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """Count of days where buy-value exceeds sell-value in trailing 252-day window."""
    dom = (insider_buy_value > insider_sell_value).astype(float)
    return _rolling_sum(dom, _W252)


def ibr_099_value_flow_buy_streak(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """Current consecutive streak of days with net buy flow > 0 (resets on any net-sell day)."""
    net_daily = insider_buy_value - insider_sell_value
    is_buy = (net_daily > 0).astype(int)
    arr = is_buy.values
    streak = np.zeros(len(arr), dtype=float)
    for i in range(1, len(arr)):
        streak[i] = (streak[i - 1] + 1) * arr[i]
    return pd.Series(streak, index=insider_buy_value.index)


def ibr_100_value_flow_sell_streak(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """Current consecutive streak of days with net sell flow > 0 (resets on any net-buy day)."""
    net_daily = insider_buy_value - insider_sell_value
    is_sell = (net_daily < 0).astype(int)
    arr = is_sell.values
    streak = np.zeros(len(arr), dtype=float)
    for i in range(1, len(arr)):
        streak[i] = (streak[i - 1] + 1) * arr[i]
    return pd.Series(streak, index=insider_buy_value.index)


def ibr_101_count_buy_streak(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Current consecutive streak of days where buy-count exceeds sell-count."""
    is_buy_dom = (insider_buy_count > insider_sell_count).astype(int)
    arr = is_buy_dom.values
    streak = np.zeros(len(arr), dtype=float)
    for i in range(1, len(arr)):
        streak[i] = (streak[i - 1] + 1) * arr[i]
    return pd.Series(streak, index=insider_buy_count.index)


def ibr_102_count_sell_streak(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Current consecutive streak of days where sell-count exceeds buy-count."""
    is_sell_dom = (insider_sell_count > insider_buy_count).astype(int)
    arr = is_sell_dom.values
    streak = np.zeros(len(arr), dtype=float)
    for i in range(1, len(arr)):
        streak[i] = (streak[i - 1] + 1) * arr[i]
    return pd.Series(streak, index=insider_buy_count.index)


def ibr_103_value_regime_flip_to_buy_21d(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """1 when 21-day net flow is positive but 63-day net flow is negative — recent buy shift."""
    net21 = _rolling_sum(insider_buy_value, _W21) - _rolling_sum(insider_sell_value, _W21)
    net63 = _rolling_sum(insider_buy_value, _W63) - _rolling_sum(insider_sell_value, _W63)
    return ((net21 > 0) & (net63 <= 0)).astype(float)


def ibr_104_value_regime_flip_to_sell_21d(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """1 when 21-day net flow is negative but 63-day net flow is positive — recent sell shift."""
    net21 = _rolling_sum(insider_buy_value, _W21) - _rolling_sum(insider_sell_value, _W21)
    net63 = _rolling_sum(insider_buy_value, _W63) - _rolling_sum(insider_sell_value, _W63)
    return ((net21 <= 0) & (net63 > 0)).astype(float)


def ibr_105_buyer_fraction_above_half_63d(insider_buyers: pd.Series, insider_sellers: pd.Series) -> pd.Series:
    """1 when 63-day buyer fraction exceeds 0.5 (more distinct buyers than sellers)."""
    bf = _buy_fraction(insider_buyers, insider_sellers, _W63)
    return (bf > 0.5).astype(float)


# --- Group H (106-120): Cross-window ratio comparisons and momentum ---

def ibr_106_value_ratio_21_vs_252(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """Ratio of 21-day value ratio to 252-day value ratio — short vs long-term sentiment."""
    r21  = _safe_div(_rolling_sum(insider_buy_value, _W21),  _rolling_sum(insider_sell_value, _W21))
    r252 = _safe_div(_rolling_sum(insider_buy_value, _W252), _rolling_sum(insider_sell_value, _W252))
    return _safe_div(r21, r252)


def ibr_107_value_ratio_63_vs_252(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """Ratio of 63-day value ratio to 252-day value ratio — quarter vs year sentiment."""
    r63  = _safe_div(_rolling_sum(insider_buy_value, _W63),  _rolling_sum(insider_sell_value, _W63))
    r252 = _safe_div(_rolling_sum(insider_buy_value, _W252), _rolling_sum(insider_sell_value, _W252))
    return _safe_div(r63, r252)


def ibr_108_count_ratio_21_vs_252(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Ratio of 21-day count ratio to 252-day count ratio."""
    r21  = _safe_div(_rolling_sum(insider_buy_count, _W21),  _rolling_sum(insider_sell_count, _W21))
    r252 = _safe_div(_rolling_sum(insider_buy_count, _W252), _rolling_sum(insider_sell_count, _W252))
    return _safe_div(r21, r252)


def ibr_109_count_ratio_63_vs_252(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Ratio of 63-day count ratio to 252-day count ratio."""
    r63  = _safe_div(_rolling_sum(insider_buy_count, _W63),  _rolling_sum(insider_sell_count, _W63))
    r252 = _safe_div(_rolling_sum(insider_buy_count, _W252), _rolling_sum(insider_sell_count, _W252))
    return _safe_div(r63, r252)


def ibr_110_value_net_flow_21_vs_63(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """Net dollar flow 21-day minus 63-day (short minus medium-term flow)."""
    net21 = _rolling_sum(insider_buy_value, _W21) - _rolling_sum(insider_sell_value, _W21)
    net63 = _rolling_sum(insider_buy_value, _W63) - _rolling_sum(insider_sell_value, _W63)
    return net21 - net63


def ibr_111_value_net_flow_63_vs_252(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """Net dollar flow 63-day minus 252-day (quarter minus year flow)."""
    net63  = _rolling_sum(insider_buy_value, _W63)  - _rolling_sum(insider_sell_value, _W63)
    net252 = _rolling_sum(insider_buy_value, _W252) - _rolling_sum(insider_sell_value, _W252)
    return net63 - net252


def ibr_112_buy_fraction_21_minus_63(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Buy fraction at 21-day window minus buy fraction at 63-day window (momentum signal)."""
    bf21 = _buy_fraction(insider_buy_count, insider_sell_count, _W21)
    bf63 = _buy_fraction(insider_buy_count, insider_sell_count, _W63)
    return bf21 - bf63


def ibr_113_buy_fraction_63_minus_252(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Buy fraction at 63-day window minus buy fraction at 252-day window."""
    bf63  = _buy_fraction(insider_buy_count, insider_sell_count, _W63)
    bf252 = _buy_fraction(insider_buy_count, insider_sell_count, _W252)
    return bf63 - bf252


def ibr_114_officer_vs_director_value_ratio_252d(
    officer_buy_value: pd.Series,
    officer_sell_value: pd.Series,
    director_buy_value: pd.Series,
    director_sell_value: pd.Series,
) -> pd.Series:
    """Officer 252-day value ratio minus director 252-day value ratio (differential sentiment)."""
    r_off = _safe_div(_rolling_sum(officer_buy_value, _W252), _rolling_sum(officer_sell_value, _W252))
    r_dir = _safe_div(_rolling_sum(director_buy_value, _W252), _rolling_sum(director_sell_value, _W252))
    return r_off - r_dir


def ibr_115_value_ratio_ewm21(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """EWM-smoothed (span=21) daily buy/sell value ratio."""
    daily_ratio = _safe_div(insider_buy_value, insider_sell_value)
    return daily_ratio.ewm(span=_W21, min_periods=max(1, _W21 // 4)).mean()


def ibr_116_value_ratio_ewm63(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """EWM-smoothed (span=63) daily buy/sell value ratio."""
    daily_ratio = _safe_div(insider_buy_value, insider_sell_value)
    return daily_ratio.ewm(span=_W63, min_periods=max(1, _W63 // 4)).mean()


def ibr_117_count_ratio_ewm63(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """EWM-smoothed (span=63) daily buy/sell count ratio."""
    daily_ratio = _safe_div(insider_buy_count, insider_sell_count)
    return daily_ratio.ewm(span=_W63, min_periods=max(1, _W63 // 4)).mean()


def ibr_118_value_net_flow_ewm63(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """EWM-smoothed (span=63) daily net insider dollar flow."""
    net_daily = insider_buy_value - insider_sell_value
    return net_daily.ewm(span=_W63, min_periods=max(1, _W63 // 4)).mean()


def ibr_119_value_net_flow_ewm252(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """EWM-smoothed (span=252) daily net insider dollar flow."""
    net_daily = insider_buy_value - insider_sell_value
    return net_daily.ewm(span=_W252, min_periods=max(1, _W252 // 4)).mean()


def ibr_120_count_net_flow_ewm63(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """EWM-smoothed (span=63) daily net insider count flow."""
    net_daily = insider_buy_count - insider_sell_count
    return net_daily.ewm(span=_W63, min_periods=max(1, _W63 // 4)).mean()


# --- Group I (121-135): Sell-pressure intensity and imbalance metrics ---

def ibr_121_sell_pressure_intensity_21d(insider_sell_value: pd.Series, insider_buy_value: pd.Series) -> pd.Series:
    """Sell-pressure intensity over 21 days: sell-value / (buy+sell) value."""
    ss = _rolling_sum(insider_sell_value, _W21)
    sb = _rolling_sum(insider_buy_value, _W21)
    return _safe_div(ss, sb + ss)


def ibr_122_sell_pressure_intensity_126d(insider_sell_value: pd.Series, insider_buy_value: pd.Series) -> pd.Series:
    """Sell-pressure intensity over 126 days: sell-value / (buy+sell) value."""
    ss = _rolling_sum(insider_sell_value, _W126)
    sb = _rolling_sum(insider_buy_value, _W126)
    return _safe_div(ss, sb + ss)


def ibr_123_sell_pressure_intensity_252d(insider_sell_value: pd.Series, insider_buy_value: pd.Series) -> pd.Series:
    """Sell-pressure intensity over 252 days: sell-value / (buy+sell) value."""
    ss = _rolling_sum(insider_sell_value, _W252)
    sb = _rolling_sum(insider_buy_value, _W252)
    return _safe_div(ss, sb + ss)


def ibr_124_sell_count_dominance_21d(insider_sell_count: pd.Series, insider_buy_count: pd.Series) -> pd.Series:
    """Sell-count as fraction of total count (sell-count dominance) over 21 days."""
    ss = _rolling_sum(insider_sell_count, _W21)
    sb = _rolling_sum(insider_buy_count, _W21)
    return _safe_div(ss, sb + ss)


def ibr_125_sell_count_dominance_252d(insider_sell_count: pd.Series, insider_buy_count: pd.Series) -> pd.Series:
    """Sell-count as fraction of total count over 252 days."""
    ss = _rolling_sum(insider_sell_count, _W252)
    sb = _rolling_sum(insider_buy_count, _W252)
    return _safe_div(ss, sb + ss)


def ibr_126_share_sell_dominance_63d(insider_sell_shares: pd.Series, insider_buy_shares: pd.Series) -> pd.Series:
    """Sell-shares as fraction of total share volume over 63 days."""
    ss = _rolling_sum(insider_sell_shares, _W63)
    sb = _rolling_sum(insider_buy_shares, _W63)
    return _safe_div(ss, sb + ss)


def ibr_127_share_sell_dominance_252d(insider_sell_shares: pd.Series, insider_buy_shares: pd.Series) -> pd.Series:
    """Sell-shares as fraction of total share volume over 252 days."""
    ss = _rolling_sum(insider_sell_shares, _W252)
    sb = _rolling_sum(insider_buy_shares, _W252)
    return _safe_div(ss, sb + ss)


def ibr_128_officer_sell_dominance_252d(officer_sell_value: pd.Series, officer_buy_value: pd.Series) -> pd.Series:
    """Officer sell-value as fraction of total officer dollar activity over 252 days."""
    ss = _rolling_sum(officer_sell_value, _W252)
    sb = _rolling_sum(officer_buy_value, _W252)
    return _safe_div(ss, sb + ss)


def ibr_129_director_sell_dominance_252d(director_sell_value: pd.Series, director_buy_value: pd.Series) -> pd.Series:
    """Director sell-value as fraction of total director dollar activity over 252 days."""
    ss = _rolling_sum(director_sell_value, _W252)
    sb = _rolling_sum(director_buy_value, _W252)
    return _safe_div(ss, sb + ss)


def ibr_130_sell_value_expanding_max(insider_sell_value: pd.Series) -> pd.Series:
    """Expanding maximum of rolling 63-day sell-value sum — highest sell activity ever seen."""
    rs = _rolling_sum(insider_sell_value, _W63)
    return rs.expanding(min_periods=1).max()


def ibr_131_buy_value_expanding_max(insider_buy_value: pd.Series) -> pd.Series:
    """Expanding maximum of rolling 63-day buy-value sum — highest buy activity ever seen."""
    rs = _rolling_sum(insider_buy_value, _W63)
    return rs.expanding(min_periods=1).max()


def ibr_132_value_net_flow_vs_expanding_max(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """Current 63-day net dollar flow relative to its all-history maximum."""
    net63 = _rolling_sum(insider_buy_value, _W63) - _rolling_sum(insider_sell_value, _W63)
    peak  = net63.expanding(min_periods=1).max()
    return _safe_div(net63, peak.abs().replace(0, np.nan))


def ibr_133_value_net_flow_expanding_zscore(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """Expanding z-score of daily net insider dollar flow vs all history."""
    net_daily = insider_buy_value - insider_sell_value
    m  = net_daily.expanding(min_periods=2).mean()
    sd = net_daily.expanding(min_periods=2).std()
    return _safe_div(net_daily - m, sd)


def ibr_134_count_net_flow_expanding_zscore(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Expanding z-score of daily net insider count flow vs all history."""
    net_daily = insider_buy_count - insider_sell_count
    m  = net_daily.expanding(min_periods=2).mean()
    sd = net_daily.expanding(min_periods=2).std()
    return _safe_div(net_daily - m, sd)


def ibr_135_buyer_fraction_expanding_rank(insider_buyers: pd.Series, insider_sellers: pd.Series) -> pd.Series:
    """Expanding percentile rank of the rolling 63-day buyer fraction."""
    bf63 = _buy_fraction(insider_buyers, insider_sellers, _W63)
    return bf63.expanding(min_periods=2).rank(pct=True)


# --- Group J (136-150): Rolling averages of ratios and composite indicators ---

def ibr_136_value_ratio_63d_mean_252d(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """252-day rolling mean of the daily (raw) buy/sell value ratio — trend in sentiment."""
    daily_ratio = _safe_div(insider_buy_value, insider_sell_value)
    return _rolling_mean(daily_ratio, _W252)


def ibr_137_count_ratio_63d_mean_252d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """252-day rolling mean of the daily buy/sell count ratio."""
    daily_ratio = _safe_div(insider_buy_count, insider_sell_count)
    return _rolling_mean(daily_ratio, _W252)


def ibr_138_value_buy_fraction_mean_252d(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """252-day mean of rolling 21-day buy-fraction signal (smoothed buy-fraction trend)."""
    bf21 = _buy_fraction(insider_buy_value, insider_sell_value, _W21)
    return _rolling_mean(bf21, _W252)


def ibr_139_count_buy_fraction_mean_252d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """252-day mean of rolling 21-day count buy-fraction signal."""
    bf21 = _buy_fraction(insider_buy_count, insider_sell_count, _W21)
    return _rolling_mean(bf21, _W252)


def ibr_140_value_net_flow_std_252d(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """252-day rolling standard deviation of daily net insider dollar flow — volatility of sentiment."""
    net_daily = insider_buy_value - insider_sell_value
    return _rolling_std(net_daily, _W252)


def ibr_141_count_net_flow_std_252d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """252-day rolling std of daily net count flow."""
    net_daily = insider_buy_count - insider_sell_count
    return _rolling_std(net_daily, _W252)


def ibr_142_officer_net_flow_126d(officer_buy_value: pd.Series, officer_sell_value: pd.Series) -> pd.Series:
    """Net officer dollar flow over 126-day window."""
    return _rolling_sum(officer_buy_value, _W126) - _rolling_sum(officer_sell_value, _W126)


def ibr_143_director_net_flow_126d(director_buy_value: pd.Series, director_sell_value: pd.Series) -> pd.Series:
    """Net director dollar flow over 126-day window."""
    return _rolling_sum(director_buy_value, _W126) - _rolling_sum(director_sell_value, _W126)


def ibr_144_officer_buy_fraction_63d(officer_buy_value: pd.Series, officer_sell_value: pd.Series) -> pd.Series:
    """Fraction of officer dollar activity that is buy-side over 63 days."""
    sb = _rolling_sum(officer_buy_value, _W63)
    ss = _rolling_sum(officer_sell_value, _W63)
    return _safe_div(sb, sb + ss)


def ibr_145_director_buy_fraction_63d(director_buy_value: pd.Series, director_sell_value: pd.Series) -> pd.Series:
    """Fraction of director dollar activity that is buy-side over 63 days."""
    sb = _rolling_sum(director_buy_value, _W63)
    ss = _rolling_sum(director_sell_value, _W63)
    return _safe_div(sb, sb + ss)


def ibr_146_officer_net_flow_sign_63d(officer_buy_value: pd.Series, officer_sell_value: pd.Series) -> pd.Series:
    """Sign of net officer dollar flow over 63 days."""
    net = _rolling_sum(officer_buy_value, _W63) - _rolling_sum(officer_sell_value, _W63)
    return np.sign(net)


def ibr_147_director_net_flow_sign_63d(director_buy_value: pd.Series, director_sell_value: pd.Series) -> pd.Series:
    """Sign of net director dollar flow over 63 days."""
    net = _rolling_sum(director_buy_value, _W63) - _rolling_sum(director_sell_value, _W63)
    return np.sign(net)


def ibr_148_composite_balance_score_252d(
    insider_buy_count: pd.Series,
    insider_sell_count: pd.Series,
    insider_buy_value: pd.Series,
    insider_sell_value: pd.Series,
    insider_buyers: pd.Series,
    insider_sellers: pd.Series,
) -> pd.Series:
    """
    Composite buy-balance score over 252-day window: equal-weight average of
    buy fraction by count, buy fraction by value, and buyer fraction by persons.
    Scores above 0.5 indicate buy-tilted insider posture.
    """
    bf_count  = _buy_fraction(insider_buy_count,  insider_sell_count,  _W252)
    bf_value  = _buy_fraction(insider_buy_value,  insider_sell_value,  _W252)
    bf_buyers = _buy_fraction(insider_buyers,      insider_sellers,     _W252)
    total = bf_count.fillna(0) + bf_value.fillna(0) + bf_buyers.fillna(0)
    n     = bf_count.notna().astype(float) + bf_value.notna().astype(float) + bf_buyers.notna().astype(float)
    return _safe_div(pd.Series(total.values, index=insider_buy_count.index),
                     pd.Series(n.values,     index=insider_buy_count.index))


def ibr_149_value_ratio_126d_vs_peak_252d(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """Current 126-day value ratio as a fraction of its 252-day trailing maximum."""
    r126 = _safe_div(_rolling_sum(insider_buy_value, _W126), _rolling_sum(insider_sell_value, _W126))
    peak = _rolling_max(r126, _W252)
    return _safe_div(r126, peak.replace(0, np.nan))


def ibr_150_net_sentiment_balance_63d(
    insider_buy_count: pd.Series,
    insider_sell_count: pd.Series,
    insider_buy_value: pd.Series,
    insider_sell_value: pd.Series,
) -> pd.Series:
    """
    Net sentiment balance: (buy_fraction_by_count + buy_fraction_by_value - 1.0) over 63 days.
    Positive = net buy sentiment, negative = net sell sentiment.
    """
    bf_count = _buy_fraction(insider_buy_count, insider_sell_count, _W63)
    bf_value = _buy_fraction(insider_buy_value, insider_sell_value, _W63)
    combined = bf_count.fillna(0.5) + bf_value.fillna(0.5) - 1.0
    return combined


# --- Group K2 (176-190): EWM variants, multi-horizon composites, extreme-day counts ---

def ibr_176_value_net_flow_ewm21(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """EWM-smoothed (span=21) daily net insider dollar flow."""
    net_daily = insider_buy_value - insider_sell_value
    return net_daily.ewm(span=_W21, min_periods=max(1, _W21 // 4)).mean()


def ibr_177_count_net_flow_ewm21(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """EWM-smoothed (span=21) daily net insider count flow."""
    net_daily = insider_buy_count - insider_sell_count
    return net_daily.ewm(span=_W21, min_periods=max(1, _W21 // 4)).mean()


def ibr_178_share_net_flow_ewm63(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series) -> pd.Series:
    """EWM-smoothed (span=63) daily net insider share flow."""
    net_daily = insider_buy_shares - insider_sell_shares
    return net_daily.ewm(span=_W63, min_periods=max(1, _W63 // 4)).mean()


def ibr_179_buyer_fraction_ewm63(insider_buyers: pd.Series, insider_sellers: pd.Series) -> pd.Series:
    """EWM-smoothed (span=63) daily buyer fraction (distinct persons)."""
    daily_frac = _safe_div(insider_buyers, insider_buyers + insider_sellers)
    return daily_frac.ewm(span=_W63, min_periods=max(1, _W63 // 4)).mean()


def ibr_180_officer_value_ratio_ewm63(officer_buy_value: pd.Series, officer_sell_value: pd.Series) -> pd.Series:
    """EWM-smoothed (span=63) daily officer buy/sell value ratio."""
    daily_ratio = _safe_div(officer_buy_value, officer_sell_value)
    return daily_ratio.ewm(span=_W63, min_periods=max(1, _W63 // 4)).mean()


def ibr_181_director_value_ratio_ewm63(director_buy_value: pd.Series, director_sell_value: pd.Series) -> pd.Series:
    """EWM-smoothed (span=63) daily director buy/sell value ratio."""
    daily_ratio = _safe_div(director_buy_value, director_sell_value)
    return daily_ratio.ewm(span=_W63, min_periods=max(1, _W63 // 4)).mean()


def ibr_182_value_net_flow_ewm_vs_rolling_63d(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """EWM (span=63) net dollar flow minus rolling 63-day mean net dollar flow — deviation from trend."""
    net_daily = insider_buy_value - insider_sell_value
    ewm = net_daily.ewm(span=_W63, min_periods=max(1, _W63 // 4)).mean()
    roll = _rolling_mean(net_daily, _W63)
    return ewm - roll


def ibr_183_value_net_flow_positive_days_126d(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """Count of days with positive net insider dollar flow in trailing 126-day window."""
    pos = (insider_buy_value - insider_sell_value > 0).astype(float)
    return _rolling_sum(pos, _W126)


def ibr_184_count_buy_dominant_days_126d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Count of days where buy-count exceeds sell-count in trailing 126-day window."""
    dom = (insider_buy_count > insider_sell_count).astype(float)
    return _rolling_sum(dom, _W126)


def ibr_185_value_buy_dominant_days_63d(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """Count of days where buy-value exceeds sell-value in trailing 63-day window."""
    dom = (insider_buy_value > insider_sell_value).astype(float)
    return _rolling_sum(dom, _W63)


def ibr_186_value_net_flow_negative_days_252d(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """Count of days with negative net insider dollar flow in trailing 252-day window."""
    neg = (insider_buy_value - insider_sell_value < 0).astype(float)
    return _rolling_sum(neg, _W252)


def ibr_187_value_dominant_day_fraction_63d(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """Fraction of 63-day window where buy-value exceeds sell-value."""
    dom = (insider_buy_value > insider_sell_value).astype(float)
    cnt = (insider_buy_value + insider_sell_value > 0).astype(float)
    sb  = _rolling_sum(dom, _W63)
    sc  = _rolling_sum(cnt, _W63)
    return _safe_div(sb, sc)


def ibr_188_count_dominant_day_fraction_252d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Fraction of 252-day window where buy-count exceeds sell-count (active days only)."""
    dom = (insider_buy_count > insider_sell_count).astype(float)
    act = (insider_buy_count + insider_sell_count > 0).astype(float)
    return _safe_div(_rolling_sum(dom, _W252), _rolling_sum(act, _W252))


def ibr_189_share_buy_dominant_days_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series) -> pd.Series:
    """Count of days where buy-shares exceed sell-shares in trailing 252-day window."""
    dom = (insider_buy_shares > insider_sell_shares).astype(float)
    return _rolling_sum(dom, _W252)


def ibr_190_buyer_majority_days_252d(insider_buyers: pd.Series, insider_sellers: pd.Series) -> pd.Series:
    """Count of days where distinct buyers exceed distinct sellers in trailing 252-day window."""
    dom = (insider_buyers > insider_sellers).astype(float)
    return _rolling_sum(dom, _W252)


# --- Group L2 (191-200): Cross-signal comparisons and long-horizon normalized measures ---

def ibr_191_value_ratio_126d_vs_252d(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """Ratio of 126-day value ratio to 252-day value ratio — half-year vs full-year sentiment."""
    r126 = _safe_div(_rolling_sum(insider_buy_value, _W126), _rolling_sum(insider_sell_value, _W126))
    r252 = _safe_div(_rolling_sum(insider_buy_value, _W252), _rolling_sum(insider_sell_value, _W252))
    return _safe_div(r126, r252)


def ibr_192_count_ratio_126d_vs_252d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Ratio of 126-day count ratio to 252-day count ratio."""
    r126 = _safe_div(_rolling_sum(insider_buy_count, _W126), _rolling_sum(insider_sell_count, _W126))
    r252 = _safe_div(_rolling_sum(insider_buy_count, _W252), _rolling_sum(insider_sell_count, _W252))
    return _safe_div(r126, r252)


def ibr_193_share_ratio_126d_vs_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series) -> pd.Series:
    """Ratio of 126-day share ratio to 252-day share ratio."""
    r126 = _safe_div(_rolling_sum(insider_buy_shares, _W126), _rolling_sum(insider_sell_shares, _W126))
    r252 = _safe_div(_rolling_sum(insider_buy_shares, _W252), _rolling_sum(insider_sell_shares, _W252))
    return _safe_div(r126, r252)


def ibr_194_value_net_flow_norm_504d(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """Net dollar flow over 504 days normalized by total (buy+sell) volume."""
    sb = _rolling_sum(insider_buy_value, _W504)
    ss = _rolling_sum(insider_sell_value, _W504)
    return _safe_div(sb - ss, sb + ss)


def ibr_195_count_net_flow_norm_504d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Net transaction count over 504 days normalized by total count."""
    sb = _rolling_sum(insider_buy_count, _W504)
    ss = _rolling_sum(insider_sell_count, _W504)
    return _safe_div(sb - ss, sb + ss)


def ibr_196_share_net_flow_norm_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series) -> pd.Series:
    """Net share flow over 21 days normalized by total share volume transacted."""
    sb = _rolling_sum(insider_buy_shares, _W21)
    ss = _rolling_sum(insider_sell_shares, _W21)
    return _safe_div(sb - ss, sb + ss)


def ibr_197_officer_buy_fraction_126d(officer_buy_value: pd.Series, officer_sell_value: pd.Series) -> pd.Series:
    """Fraction of officer dollar activity that is buy-side over 126-day window."""
    sb = _rolling_sum(officer_buy_value, _W126)
    ss = _rolling_sum(officer_sell_value, _W126)
    return _safe_div(sb, sb + ss)


def ibr_198_director_buy_fraction_126d(director_buy_value: pd.Series, director_sell_value: pd.Series) -> pd.Series:
    """Fraction of director dollar activity that is buy-side over 126-day window."""
    sb = _rolling_sum(director_buy_value, _W126)
    ss = _rolling_sum(director_sell_value, _W126)
    return _safe_div(sb, sb + ss)


def ibr_199_value_net_flow_504d_vs_252d(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """Net dollar flow over 504-day window minus 252-day window — long-horizon momentum."""
    nf504 = _rolling_sum(insider_buy_value, _W504) - _rolling_sum(insider_sell_value, _W504)
    nf252 = _rolling_sum(insider_buy_value, _W252) - _rolling_sum(insider_sell_value, _W252)
    return nf504 - nf252


def ibr_200_composite_balance_score_63d(
    insider_buy_count: pd.Series,
    insider_sell_count: pd.Series,
    insider_buy_value: pd.Series,
    insider_sell_value: pd.Series,
    insider_buyers: pd.Series,
    insider_sellers: pd.Series,
) -> pd.Series:
    """
    Composite buy-balance score over 63-day window: equal-weight average of
    buy fraction by count, by value, and by distinct persons.
    Scores above 0.5 indicate buy-tilted insider posture.
    """
    bf_count  = _buy_fraction(insider_buy_count,  insider_sell_count,  _W63)
    bf_value  = _buy_fraction(insider_buy_value,  insider_sell_value,  _W63)
    bf_buyers = _buy_fraction(insider_buyers,      insider_sellers,     _W63)
    total = bf_count.fillna(0) + bf_value.fillna(0) + bf_buyers.fillna(0)
    n     = bf_count.notna().astype(float) + bf_value.notna().astype(float) + bf_buyers.notna().astype(float)
    return _safe_div(pd.Series(total.values, index=insider_buy_count.index),
                     pd.Series(n.values,     index=insider_buy_count.index))


# ── Registry 076-150 ──────────────────────────────────────────────────────────

INSIDER_BUY_SELL_RATIO_REGISTRY_076_150 = {
    "ibr_076_value_net_flow_norm_21d":         {"inputs": ["insider_buy_value", "insider_sell_value"],   "func": ibr_076_value_net_flow_norm_21d},
    "ibr_077_value_net_flow_norm_63d":         {"inputs": ["insider_buy_value", "insider_sell_value"],   "func": ibr_077_value_net_flow_norm_63d},
    "ibr_078_value_net_flow_norm_252d":        {"inputs": ["insider_buy_value", "insider_sell_value"],   "func": ibr_078_value_net_flow_norm_252d},
    "ibr_079_count_net_flow_norm_21d":         {"inputs": ["insider_buy_count", "insider_sell_count"],   "func": ibr_079_count_net_flow_norm_21d},
    "ibr_080_count_net_flow_norm_63d":         {"inputs": ["insider_buy_count", "insider_sell_count"],   "func": ibr_080_count_net_flow_norm_63d},
    "ibr_081_count_net_flow_norm_252d":        {"inputs": ["insider_buy_count", "insider_sell_count"],   "func": ibr_081_count_net_flow_norm_252d},
    "ibr_082_share_net_flow_norm_63d":         {"inputs": ["insider_buy_shares", "insider_sell_shares"], "func": ibr_082_share_net_flow_norm_63d},
    "ibr_083_share_net_flow_norm_252d":        {"inputs": ["insider_buy_shares", "insider_sell_shares"], "func": ibr_083_share_net_flow_norm_252d},
    "ibr_084_value_ratio_peak_21_in_252":      {"inputs": ["insider_buy_value", "insider_sell_value"],   "func": ibr_084_value_ratio_peak_21_in_252},
    "ibr_085_value_ratio_trough_21_in_252":    {"inputs": ["insider_buy_value", "insider_sell_value"],   "func": ibr_085_value_ratio_trough_21_in_252},
    "ibr_086_count_ratio_peak_21_in_252":      {"inputs": ["insider_buy_count", "insider_sell_count"],   "func": ibr_086_count_ratio_peak_21_in_252},
    "ibr_087_count_ratio_trough_21_in_252":    {"inputs": ["insider_buy_count", "insider_sell_count"],   "func": ibr_087_count_ratio_trough_21_in_252},
    "ibr_088_value_ratio_pct_rank_252d":       {"inputs": ["insider_buy_value", "insider_sell_value"],   "func": ibr_088_value_ratio_pct_rank_252d},
    "ibr_089_count_ratio_pct_rank_252d":       {"inputs": ["insider_buy_count", "insider_sell_count"],   "func": ibr_089_count_ratio_pct_rank_252d},
    "ibr_090_buyer_fraction_pct_rank_252d":    {"inputs": ["insider_buyers", "insider_sellers"],         "func": ibr_090_buyer_fraction_pct_rank_252d},
    "ibr_091_value_net_flow_positive_days_21d":{"inputs": ["insider_buy_value", "insider_sell_value"],   "func": ibr_091_value_net_flow_positive_days_21d},
    "ibr_092_value_net_flow_positive_days_63d":{"inputs": ["insider_buy_value", "insider_sell_value"],   "func": ibr_092_value_net_flow_positive_days_63d},
    "ibr_093_value_net_flow_positive_days_252d":{"inputs": ["insider_buy_value", "insider_sell_value"],  "func": ibr_093_value_net_flow_positive_days_252d},
    "ibr_094_value_net_flow_negative_days_63d":{"inputs": ["insider_buy_value", "insider_sell_value"],   "func": ibr_094_value_net_flow_negative_days_63d},
    "ibr_095_count_buy_dominant_days_63d":     {"inputs": ["insider_buy_count", "insider_sell_count"],   "func": ibr_095_count_buy_dominant_days_63d},
    "ibr_096_count_sell_dominant_days_63d":    {"inputs": ["insider_buy_count", "insider_sell_count"],   "func": ibr_096_count_sell_dominant_days_63d},
    "ibr_097_count_buy_dominant_days_252d":    {"inputs": ["insider_buy_count", "insider_sell_count"],   "func": ibr_097_count_buy_dominant_days_252d},
    "ibr_098_value_buy_dominant_days_252d":    {"inputs": ["insider_buy_value", "insider_sell_value"],   "func": ibr_098_value_buy_dominant_days_252d},
    "ibr_099_value_flow_buy_streak":           {"inputs": ["insider_buy_value", "insider_sell_value"],   "func": ibr_099_value_flow_buy_streak},
    "ibr_100_value_flow_sell_streak":          {"inputs": ["insider_buy_value", "insider_sell_value"],   "func": ibr_100_value_flow_sell_streak},
    "ibr_101_count_buy_streak":                {"inputs": ["insider_buy_count", "insider_sell_count"],   "func": ibr_101_count_buy_streak},
    "ibr_102_count_sell_streak":               {"inputs": ["insider_buy_count", "insider_sell_count"],   "func": ibr_102_count_sell_streak},
    "ibr_103_value_regime_flip_to_buy_21d":    {"inputs": ["insider_buy_value", "insider_sell_value"],   "func": ibr_103_value_regime_flip_to_buy_21d},
    "ibr_104_value_regime_flip_to_sell_21d":   {"inputs": ["insider_buy_value", "insider_sell_value"],   "func": ibr_104_value_regime_flip_to_sell_21d},
    "ibr_105_buyer_fraction_above_half_63d":   {"inputs": ["insider_buyers", "insider_sellers"],         "func": ibr_105_buyer_fraction_above_half_63d},
    "ibr_106_value_ratio_21_vs_252":           {"inputs": ["insider_buy_value", "insider_sell_value"],   "func": ibr_106_value_ratio_21_vs_252},
    "ibr_107_value_ratio_63_vs_252":           {"inputs": ["insider_buy_value", "insider_sell_value"],   "func": ibr_107_value_ratio_63_vs_252},
    "ibr_108_count_ratio_21_vs_252":           {"inputs": ["insider_buy_count", "insider_sell_count"],   "func": ibr_108_count_ratio_21_vs_252},
    "ibr_109_count_ratio_63_vs_252":           {"inputs": ["insider_buy_count", "insider_sell_count"],   "func": ibr_109_count_ratio_63_vs_252},
    "ibr_110_value_net_flow_21_vs_63":         {"inputs": ["insider_buy_value", "insider_sell_value"],   "func": ibr_110_value_net_flow_21_vs_63},
    "ibr_111_value_net_flow_63_vs_252":        {"inputs": ["insider_buy_value", "insider_sell_value"],   "func": ibr_111_value_net_flow_63_vs_252},
    "ibr_112_buy_fraction_21_minus_63":        {"inputs": ["insider_buy_count", "insider_sell_count"],   "func": ibr_112_buy_fraction_21_minus_63},
    "ibr_113_buy_fraction_63_minus_252":       {"inputs": ["insider_buy_count", "insider_sell_count"],   "func": ibr_113_buy_fraction_63_minus_252},
    "ibr_114_officer_vs_director_value_ratio_252d": {"inputs": ["officer_buy_value", "officer_sell_value", "director_buy_value", "director_sell_value"], "func": ibr_114_officer_vs_director_value_ratio_252d},
    "ibr_115_value_ratio_ewm21":               {"inputs": ["insider_buy_value", "insider_sell_value"],   "func": ibr_115_value_ratio_ewm21},
    "ibr_116_value_ratio_ewm63":               {"inputs": ["insider_buy_value", "insider_sell_value"],   "func": ibr_116_value_ratio_ewm63},
    "ibr_117_count_ratio_ewm63":               {"inputs": ["insider_buy_count", "insider_sell_count"],   "func": ibr_117_count_ratio_ewm63},
    "ibr_118_value_net_flow_ewm63":            {"inputs": ["insider_buy_value", "insider_sell_value"],   "func": ibr_118_value_net_flow_ewm63},
    "ibr_119_value_net_flow_ewm252":           {"inputs": ["insider_buy_value", "insider_sell_value"],   "func": ibr_119_value_net_flow_ewm252},
    "ibr_120_count_net_flow_ewm63":            {"inputs": ["insider_buy_count", "insider_sell_count"],   "func": ibr_120_count_net_flow_ewm63},
    "ibr_121_sell_pressure_intensity_21d":     {"inputs": ["insider_sell_value", "insider_buy_value"],   "func": ibr_121_sell_pressure_intensity_21d},
    "ibr_122_sell_pressure_intensity_126d":    {"inputs": ["insider_sell_value", "insider_buy_value"],   "func": ibr_122_sell_pressure_intensity_126d},
    "ibr_123_sell_pressure_intensity_252d":    {"inputs": ["insider_sell_value", "insider_buy_value"],   "func": ibr_123_sell_pressure_intensity_252d},
    "ibr_124_sell_count_dominance_21d":        {"inputs": ["insider_sell_count", "insider_buy_count"],   "func": ibr_124_sell_count_dominance_21d},
    "ibr_125_sell_count_dominance_252d":       {"inputs": ["insider_sell_count", "insider_buy_count"],   "func": ibr_125_sell_count_dominance_252d},
    "ibr_126_share_sell_dominance_63d":        {"inputs": ["insider_sell_shares", "insider_buy_shares"], "func": ibr_126_share_sell_dominance_63d},
    "ibr_127_share_sell_dominance_252d":       {"inputs": ["insider_sell_shares", "insider_buy_shares"], "func": ibr_127_share_sell_dominance_252d},
    "ibr_128_officer_sell_dominance_252d":     {"inputs": ["officer_sell_value", "officer_buy_value"],   "func": ibr_128_officer_sell_dominance_252d},
    "ibr_129_director_sell_dominance_252d":    {"inputs": ["director_sell_value", "director_buy_value"], "func": ibr_129_director_sell_dominance_252d},
    "ibr_130_sell_value_expanding_max":        {"inputs": ["insider_sell_value"],                        "func": ibr_130_sell_value_expanding_max},
    "ibr_131_buy_value_expanding_max":         {"inputs": ["insider_buy_value"],                         "func": ibr_131_buy_value_expanding_max},
    "ibr_132_value_net_flow_vs_expanding_max": {"inputs": ["insider_buy_value", "insider_sell_value"],   "func": ibr_132_value_net_flow_vs_expanding_max},
    "ibr_133_value_net_flow_expanding_zscore": {"inputs": ["insider_buy_value", "insider_sell_value"],   "func": ibr_133_value_net_flow_expanding_zscore},
    "ibr_134_count_net_flow_expanding_zscore": {"inputs": ["insider_buy_count", "insider_sell_count"],   "func": ibr_134_count_net_flow_expanding_zscore},
    "ibr_135_buyer_fraction_expanding_rank":   {"inputs": ["insider_buyers", "insider_sellers"],         "func": ibr_135_buyer_fraction_expanding_rank},
    "ibr_136_value_ratio_63d_mean_252d":       {"inputs": ["insider_buy_value", "insider_sell_value"],   "func": ibr_136_value_ratio_63d_mean_252d},
    "ibr_137_count_ratio_63d_mean_252d":       {"inputs": ["insider_buy_count", "insider_sell_count"],   "func": ibr_137_count_ratio_63d_mean_252d},
    "ibr_138_value_buy_fraction_mean_252d":    {"inputs": ["insider_buy_value", "insider_sell_value"],   "func": ibr_138_value_buy_fraction_mean_252d},
    "ibr_139_count_buy_fraction_mean_252d":    {"inputs": ["insider_buy_count", "insider_sell_count"],   "func": ibr_139_count_buy_fraction_mean_252d},
    "ibr_140_value_net_flow_std_252d":         {"inputs": ["insider_buy_value", "insider_sell_value"],   "func": ibr_140_value_net_flow_std_252d},
    "ibr_141_count_net_flow_std_252d":         {"inputs": ["insider_buy_count", "insider_sell_count"],   "func": ibr_141_count_net_flow_std_252d},
    "ibr_142_officer_net_flow_126d":           {"inputs": ["officer_buy_value", "officer_sell_value"],   "func": ibr_142_officer_net_flow_126d},
    "ibr_143_director_net_flow_126d":          {"inputs": ["director_buy_value", "director_sell_value"], "func": ibr_143_director_net_flow_126d},
    "ibr_144_officer_buy_fraction_63d":        {"inputs": ["officer_buy_value", "officer_sell_value"],   "func": ibr_144_officer_buy_fraction_63d},
    "ibr_145_director_buy_fraction_63d":       {"inputs": ["director_buy_value", "director_sell_value"], "func": ibr_145_director_buy_fraction_63d},
    "ibr_146_officer_net_flow_sign_63d":       {"inputs": ["officer_buy_value", "officer_sell_value"],   "func": ibr_146_officer_net_flow_sign_63d},
    "ibr_147_director_net_flow_sign_63d":      {"inputs": ["director_buy_value", "director_sell_value"], "func": ibr_147_director_net_flow_sign_63d},
    "ibr_148_composite_balance_score_252d":    {"inputs": ["insider_buy_count", "insider_sell_count", "insider_buy_value", "insider_sell_value", "insider_buyers", "insider_sellers"], "func": ibr_148_composite_balance_score_252d},
    "ibr_149_value_ratio_126d_vs_peak_252d":   {"inputs": ["insider_buy_value", "insider_sell_value"],   "func": ibr_149_value_ratio_126d_vs_peak_252d},
    "ibr_150_net_sentiment_balance_63d":       {"inputs": ["insider_buy_count", "insider_sell_count", "insider_buy_value", "insider_sell_value"], "func": ibr_150_net_sentiment_balance_63d},
    "ibr_176_value_net_flow_ewm21":             {"inputs": ["insider_buy_value", "insider_sell_value"],   "func": ibr_176_value_net_flow_ewm21},
    "ibr_177_count_net_flow_ewm21":             {"inputs": ["insider_buy_count", "insider_sell_count"],   "func": ibr_177_count_net_flow_ewm21},
    "ibr_178_share_net_flow_ewm63":             {"inputs": ["insider_buy_shares", "insider_sell_shares"], "func": ibr_178_share_net_flow_ewm63},
    "ibr_179_buyer_fraction_ewm63":             {"inputs": ["insider_buyers", "insider_sellers"],         "func": ibr_179_buyer_fraction_ewm63},
    "ibr_180_officer_value_ratio_ewm63":        {"inputs": ["officer_buy_value", "officer_sell_value"],   "func": ibr_180_officer_value_ratio_ewm63},
    "ibr_181_director_value_ratio_ewm63":       {"inputs": ["director_buy_value", "director_sell_value"], "func": ibr_181_director_value_ratio_ewm63},
    "ibr_182_value_net_flow_ewm_vs_rolling_63d":{"inputs": ["insider_buy_value", "insider_sell_value"],   "func": ibr_182_value_net_flow_ewm_vs_rolling_63d},
    "ibr_183_value_net_flow_positive_days_126d":{"inputs": ["insider_buy_value", "insider_sell_value"],   "func": ibr_183_value_net_flow_positive_days_126d},
    "ibr_184_count_buy_dominant_days_126d":     {"inputs": ["insider_buy_count", "insider_sell_count"],   "func": ibr_184_count_buy_dominant_days_126d},
    "ibr_185_value_buy_dominant_days_63d":      {"inputs": ["insider_buy_value", "insider_sell_value"],   "func": ibr_185_value_buy_dominant_days_63d},
    "ibr_186_value_net_flow_negative_days_252d":{"inputs": ["insider_buy_value", "insider_sell_value"],   "func": ibr_186_value_net_flow_negative_days_252d},
    "ibr_187_value_dominant_day_fraction_63d":  {"inputs": ["insider_buy_value", "insider_sell_value"],   "func": ibr_187_value_dominant_day_fraction_63d},
    "ibr_188_count_dominant_day_fraction_252d": {"inputs": ["insider_buy_count", "insider_sell_count"],   "func": ibr_188_count_dominant_day_fraction_252d},
    "ibr_189_share_buy_dominant_days_252d":     {"inputs": ["insider_buy_shares", "insider_sell_shares"], "func": ibr_189_share_buy_dominant_days_252d},
    "ibr_190_buyer_majority_days_252d":         {"inputs": ["insider_buyers", "insider_sellers"],         "func": ibr_190_buyer_majority_days_252d},
    "ibr_191_value_ratio_126d_vs_252d":         {"inputs": ["insider_buy_value", "insider_sell_value"],   "func": ibr_191_value_ratio_126d_vs_252d},
    "ibr_192_count_ratio_126d_vs_252d":         {"inputs": ["insider_buy_count", "insider_sell_count"],   "func": ibr_192_count_ratio_126d_vs_252d},
    "ibr_193_share_ratio_126d_vs_252d":         {"inputs": ["insider_buy_shares", "insider_sell_shares"], "func": ibr_193_share_ratio_126d_vs_252d},
    "ibr_194_value_net_flow_norm_504d":         {"inputs": ["insider_buy_value", "insider_sell_value"],   "func": ibr_194_value_net_flow_norm_504d},
    "ibr_195_count_net_flow_norm_504d":         {"inputs": ["insider_buy_count", "insider_sell_count"],   "func": ibr_195_count_net_flow_norm_504d},
    "ibr_196_share_net_flow_norm_21d":          {"inputs": ["insider_buy_shares", "insider_sell_shares"], "func": ibr_196_share_net_flow_norm_21d},
    "ibr_197_officer_buy_fraction_126d":        {"inputs": ["officer_buy_value", "officer_sell_value"],   "func": ibr_197_officer_buy_fraction_126d},
    "ibr_198_director_buy_fraction_126d":       {"inputs": ["director_buy_value", "director_sell_value"], "func": ibr_198_director_buy_fraction_126d},
    "ibr_199_value_net_flow_504d_vs_252d":      {"inputs": ["insider_buy_value", "insider_sell_value"],   "func": ibr_199_value_net_flow_504d_vs_252d},
    "ibr_200_composite_balance_score_63d":      {"inputs": ["insider_buy_count", "insider_sell_count", "insider_buy_value", "insider_sell_value", "insider_buyers", "insider_sellers"], "func": ibr_200_composite_balance_score_63d},
}
