"""
86_insider_buy_sell_ratio — Base Features 001-100
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
_W5   = 5     # 1 week
_W21  = 21    # 1 month
_W63  = 63    # 1 quarter
_W126 = 126   # 2 quarters
_W252 = 252   # 1 year
_W504 = 504   # 2 years
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


def _net_flow_value(buy_val: pd.Series, sell_val: pd.Series, w: int) -> pd.Series:
    """Rolling net insider dollar flow: sum(buys) - sum(sells) over window."""
    return _rolling_sum(buy_val, w) - _rolling_sum(sell_val, w)


def _buy_fraction(buy_cnt: pd.Series, sell_cnt: pd.Series, w: int) -> pd.Series:
    """Fraction of insider transactions that are buys: sum_buys / (sum_buys + sum_sells)."""
    sb = _rolling_sum(buy_cnt, w)
    ss = _rolling_sum(sell_cnt, w)
    return _safe_div(sb, sb + ss)


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-015): Buy/sell count ratios over multiple windows ---

def ibr_001_count_ratio_21d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Rolling 21-day buy-count divided by sell-count ratio."""
    sb = _rolling_sum(insider_buy_count, _W21)
    ss = _rolling_sum(insider_sell_count, _W21)
    return _safe_div(sb, ss)


def ibr_002_count_ratio_63d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Rolling 63-day buy-count divided by sell-count ratio."""
    sb = _rolling_sum(insider_buy_count, _W63)
    ss = _rolling_sum(insider_sell_count, _W63)
    return _safe_div(sb, ss)


def ibr_003_count_ratio_126d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Rolling 126-day buy-count divided by sell-count ratio."""
    sb = _rolling_sum(insider_buy_count, _W126)
    ss = _rolling_sum(insider_sell_count, _W126)
    return _safe_div(sb, ss)


def ibr_004_count_ratio_252d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Rolling 252-day buy-count divided by sell-count ratio."""
    sb = _rolling_sum(insider_buy_count, _W252)
    ss = _rolling_sum(insider_sell_count, _W252)
    return _safe_div(sb, ss)


def ibr_005_count_net_flow_21d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Net transaction count (buys minus sells) over rolling 21-day window."""
    return _rolling_sum(insider_buy_count, _W21) - _rolling_sum(insider_sell_count, _W21)


def ibr_006_count_net_flow_63d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Net transaction count (buys minus sells) over rolling 63-day window."""
    return _rolling_sum(insider_buy_count, _W63) - _rolling_sum(insider_sell_count, _W63)


def ibr_007_count_net_flow_126d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Net transaction count (buys minus sells) over rolling 126-day window."""
    return _rolling_sum(insider_buy_count, _W126) - _rolling_sum(insider_sell_count, _W126)


def ibr_008_count_net_flow_252d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Net transaction count (buys minus sells) over rolling 252-day window."""
    return _rolling_sum(insider_buy_count, _W252) - _rolling_sum(insider_sell_count, _W252)


def ibr_009_buy_fraction_21d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Fraction of insider transactions that are buys over 21-day window."""
    return _buy_fraction(insider_buy_count, insider_sell_count, _W21)


def ibr_010_buy_fraction_63d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Fraction of insider transactions that are buys over 63-day window."""
    return _buy_fraction(insider_buy_count, insider_sell_count, _W63)


def ibr_011_buy_fraction_126d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Fraction of insider transactions that are buys over 126-day window."""
    return _buy_fraction(insider_buy_count, insider_sell_count, _W126)


def ibr_012_buy_fraction_252d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Fraction of insider transactions that are buys over 252-day window."""
    return _buy_fraction(insider_buy_count, insider_sell_count, _W252)


def ibr_013_sell_fraction_63d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Fraction of insider transactions that are sells over 63-day window."""
    ss = _rolling_sum(insider_sell_count, _W63)
    sb = _rolling_sum(insider_buy_count, _W63)
    return _safe_div(ss, sb + ss)


def ibr_014_count_ratio_5d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Rolling 5-day buy-count divided by sell-count ratio (very short-term sentiment)."""
    sb = _rolling_sum(insider_buy_count, _W5)
    ss = _rolling_sum(insider_sell_count, _W5)
    return _safe_div(sb, ss)


def ibr_015_count_ratio_504d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Rolling 504-day buy-count divided by sell-count ratio (2-year view)."""
    sb = _rolling_sum(insider_buy_count, _W504)
    ss = _rolling_sum(insider_sell_count, _W504)
    return _safe_div(sb, ss)


# --- Group B (016-030): Share volume buy/sell ratios and net flows ---

def ibr_016_share_ratio_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series) -> pd.Series:
    """Rolling 21-day buy-shares divided by sell-shares ratio."""
    sb = _rolling_sum(insider_buy_shares, _W21)
    ss = _rolling_sum(insider_sell_shares, _W21)
    return _safe_div(sb, ss)


def ibr_017_share_ratio_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series) -> pd.Series:
    """Rolling 63-day buy-shares divided by sell-shares ratio."""
    sb = _rolling_sum(insider_buy_shares, _W63)
    ss = _rolling_sum(insider_sell_shares, _W63)
    return _safe_div(sb, ss)


def ibr_018_share_ratio_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series) -> pd.Series:
    """Rolling 126-day buy-shares divided by sell-shares ratio."""
    sb = _rolling_sum(insider_buy_shares, _W126)
    ss = _rolling_sum(insider_sell_shares, _W126)
    return _safe_div(sb, ss)


def ibr_019_share_ratio_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series) -> pd.Series:
    """Rolling 252-day buy-shares divided by sell-shares ratio."""
    sb = _rolling_sum(insider_buy_shares, _W252)
    ss = _rolling_sum(insider_sell_shares, _W252)
    return _safe_div(sb, ss)


def ibr_020_share_net_flow_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series) -> pd.Series:
    """Net insider share flow (buy-shares minus sell-shares) over 21-day window."""
    return _rolling_sum(insider_buy_shares, _W21) - _rolling_sum(insider_sell_shares, _W21)


def ibr_021_share_net_flow_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series) -> pd.Series:
    """Net insider share flow over 63-day window."""
    return _rolling_sum(insider_buy_shares, _W63) - _rolling_sum(insider_sell_shares, _W63)


def ibr_022_share_net_flow_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series) -> pd.Series:
    """Net insider share flow over 126-day window."""
    return _rolling_sum(insider_buy_shares, _W126) - _rolling_sum(insider_sell_shares, _W126)


def ibr_023_share_net_flow_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series) -> pd.Series:
    """Net insider share flow over 252-day window."""
    return _rolling_sum(insider_buy_shares, _W252) - _rolling_sum(insider_sell_shares, _W252)


def ibr_024_share_buy_fraction_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series) -> pd.Series:
    """Fraction of total insider shares transacted that are buys over 63-day window."""
    sb = _rolling_sum(insider_buy_shares, _W63)
    ss = _rolling_sum(insider_sell_shares, _W63)
    return _safe_div(sb, sb + ss)


def ibr_025_share_buy_fraction_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series) -> pd.Series:
    """Fraction of total insider shares transacted that are buys over 252-day window."""
    sb = _rolling_sum(insider_buy_shares, _W252)
    ss = _rolling_sum(insider_sell_shares, _W252)
    return _safe_div(sb, sb + ss)


def ibr_026_share_sell_fraction_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series) -> pd.Series:
    """Fraction of total insider shares transacted that are sells over 63-day window."""
    sb = _rolling_sum(insider_buy_shares, _W63)
    ss = _rolling_sum(insider_sell_shares, _W63)
    return _safe_div(ss, sb + ss)


def ibr_027_share_net_flow_sign_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series) -> pd.Series:
    """Sign of net insider share flow over 21-day window: +1 net buyer, -1 net seller, 0 balanced."""
    net = _rolling_sum(insider_buy_shares, _W21) - _rolling_sum(insider_sell_shares, _W21)
    return np.sign(net)


def ibr_028_share_net_flow_sign_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series) -> pd.Series:
    """Sign of net insider share flow over 63-day window."""
    net = _rolling_sum(insider_buy_shares, _W63) - _rolling_sum(insider_sell_shares, _W63)
    return np.sign(net)


def ibr_029_share_ratio_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series) -> pd.Series:
    """Rolling 5-day buy-shares / sell-shares ratio."""
    sb = _rolling_sum(insider_buy_shares, _W5)
    ss = _rolling_sum(insider_sell_shares, _W5)
    return _safe_div(sb, ss)


def ibr_030_share_net_flow_504d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series) -> pd.Series:
    """Net insider share flow over 504-day (2-year) window."""
    return _rolling_sum(insider_buy_shares, _W504) - _rolling_sum(insider_sell_shares, _W504)


# --- Group C (031-045): Dollar-value buy/sell ratios and net flows ---

def ibr_031_value_ratio_21d(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """Rolling 21-day buy-value divided by sell-value ratio."""
    sb = _rolling_sum(insider_buy_value, _W21)
    ss = _rolling_sum(insider_sell_value, _W21)
    return _safe_div(sb, ss)


def ibr_032_value_ratio_63d(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """Rolling 63-day buy-value divided by sell-value ratio."""
    sb = _rolling_sum(insider_buy_value, _W63)
    ss = _rolling_sum(insider_sell_value, _W63)
    return _safe_div(sb, ss)


def ibr_033_value_ratio_126d(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """Rolling 126-day buy-value divided by sell-value ratio."""
    sb = _rolling_sum(insider_buy_value, _W126)
    ss = _rolling_sum(insider_sell_value, _W126)
    return _safe_div(sb, ss)


def ibr_034_value_ratio_252d(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """Rolling 252-day buy-value divided by sell-value ratio."""
    sb = _rolling_sum(insider_buy_value, _W252)
    ss = _rolling_sum(insider_sell_value, _W252)
    return _safe_div(sb, ss)


def ibr_035_value_net_flow_21d(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """Net insider dollar flow (buy-value minus sell-value) over 21-day window."""
    return _rolling_sum(insider_buy_value, _W21) - _rolling_sum(insider_sell_value, _W21)


def ibr_036_value_net_flow_63d(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """Net insider dollar flow over 63-day window."""
    return _rolling_sum(insider_buy_value, _W63) - _rolling_sum(insider_sell_value, _W63)


def ibr_037_value_net_flow_126d(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """Net insider dollar flow over 126-day window."""
    return _rolling_sum(insider_buy_value, _W126) - _rolling_sum(insider_sell_value, _W126)


def ibr_038_value_net_flow_252d(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """Net insider dollar flow over 252-day window."""
    return _rolling_sum(insider_buy_value, _W252) - _rolling_sum(insider_sell_value, _W252)


def ibr_039_value_buy_fraction_63d(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """Fraction of total insider dollar volume that is buy-side over 63-day window."""
    sb = _rolling_sum(insider_buy_value, _W63)
    ss = _rolling_sum(insider_sell_value, _W63)
    return _safe_div(sb, sb + ss)


def ibr_040_value_buy_fraction_252d(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """Fraction of total insider dollar volume that is buy-side over 252-day window."""
    sb = _rolling_sum(insider_buy_value, _W252)
    ss = _rolling_sum(insider_sell_value, _W252)
    return _safe_div(sb, sb + ss)


def ibr_041_value_net_flow_sign_21d(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """Sign of net insider dollar flow over 21-day window."""
    net = _rolling_sum(insider_buy_value, _W21) - _rolling_sum(insider_sell_value, _W21)
    return np.sign(net)


def ibr_042_value_net_flow_sign_63d(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """Sign of net insider dollar flow over 63-day window."""
    net = _rolling_sum(insider_buy_value, _W63) - _rolling_sum(insider_sell_value, _W63)
    return np.sign(net)


def ibr_043_value_ratio_5d(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """Rolling 5-day buy-value / sell-value ratio."""
    sb = _rolling_sum(insider_buy_value, _W5)
    ss = _rolling_sum(insider_sell_value, _W5)
    return _safe_div(sb, ss)


def ibr_044_value_net_flow_504d(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """Net insider dollar flow over 504-day (2-year) window."""
    return _rolling_sum(insider_buy_value, _W504) - _rolling_sum(insider_sell_value, _W504)


def ibr_045_value_sell_fraction_252d(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """Fraction of total insider dollar volume that is sell-side over 252-day window."""
    sb = _rolling_sum(insider_buy_value, _W252)
    ss = _rolling_sum(insider_sell_value, _W252)
    return _safe_div(ss, sb + ss)


# --- Group D (046-060): Distinct buyer/seller balance and person-level ratios ---

def ibr_046_buyer_seller_ratio_21d(insider_buyers: pd.Series, insider_sellers: pd.Series) -> pd.Series:
    """Rolling 21-day distinct buyers / distinct sellers ratio."""
    sb = _rolling_sum(insider_buyers, _W21)
    ss = _rolling_sum(insider_sellers, _W21)
    return _safe_div(sb, ss)


def ibr_047_buyer_seller_ratio_63d(insider_buyers: pd.Series, insider_sellers: pd.Series) -> pd.Series:
    """Rolling 63-day distinct buyers / distinct sellers ratio."""
    sb = _rolling_sum(insider_buyers, _W63)
    ss = _rolling_sum(insider_sellers, _W63)
    return _safe_div(sb, ss)


def ibr_048_buyer_seller_ratio_252d(insider_buyers: pd.Series, insider_sellers: pd.Series) -> pd.Series:
    """Rolling 252-day distinct buyers / distinct sellers ratio."""
    sb = _rolling_sum(insider_buyers, _W252)
    ss = _rolling_sum(insider_sellers, _W252)
    return _safe_div(sb, ss)


def ibr_049_buyer_seller_net_21d(insider_buyers: pd.Series, insider_sellers: pd.Series) -> pd.Series:
    """Net distinct insiders tilted toward buying (buyers minus sellers) over 21 days."""
    return _rolling_sum(insider_buyers, _W21) - _rolling_sum(insider_sellers, _W21)


def ibr_050_buyer_seller_net_63d(insider_buyers: pd.Series, insider_sellers: pd.Series) -> pd.Series:
    """Net distinct insiders tilted toward buying (buyers minus sellers) over 63 days."""
    return _rolling_sum(insider_buyers, _W63) - _rolling_sum(insider_sellers, _W63)


def ibr_051_buyer_seller_net_252d(insider_buyers: pd.Series, insider_sellers: pd.Series) -> pd.Series:
    """Net distinct insiders tilted toward buying (buyers minus sellers) over 252 days."""
    return _rolling_sum(insider_buyers, _W252) - _rolling_sum(insider_sellers, _W252)


def ibr_052_buyer_fraction_63d(insider_buyers: pd.Series, insider_sellers: pd.Series) -> pd.Series:
    """Fraction of total distinct insider participants who are buyers over 63-day window."""
    sb = _rolling_sum(insider_buyers, _W63)
    ss = _rolling_sum(insider_sellers, _W63)
    return _safe_div(sb, sb + ss)


def ibr_053_buyer_fraction_252d(insider_buyers: pd.Series, insider_sellers: pd.Series) -> pd.Series:
    """Fraction of total distinct insider participants who are buyers over 252-day window."""
    sb = _rolling_sum(insider_buyers, _W252)
    ss = _rolling_sum(insider_sellers, _W252)
    return _safe_div(sb, sb + ss)


def ibr_054_seller_fraction_63d(insider_buyers: pd.Series, insider_sellers: pd.Series) -> pd.Series:
    """Fraction of total distinct insider participants who are sellers over 63-day window."""
    sb = _rolling_sum(insider_buyers, _W63)
    ss = _rolling_sum(insider_sellers, _W63)
    return _safe_div(ss, sb + ss)


def ibr_055_buyer_seller_net_sign_21d(insider_buyers: pd.Series, insider_sellers: pd.Series) -> pd.Series:
    """Sign of net buyer surplus over 21 days: +1 more buyers, -1 more sellers."""
    net = _rolling_sum(insider_buyers, _W21) - _rolling_sum(insider_sellers, _W21)
    return np.sign(net)


def ibr_056_buyer_seller_net_sign_63d(insider_buyers: pd.Series, insider_sellers: pd.Series) -> pd.Series:
    """Sign of net buyer surplus over 63 days."""
    net = _rolling_sum(insider_buyers, _W63) - _rolling_sum(insider_sellers, _W63)
    return np.sign(net)


def ibr_057_buyer_seller_ratio_126d(insider_buyers: pd.Series, insider_sellers: pd.Series) -> pd.Series:
    """Rolling 126-day distinct buyers / distinct sellers ratio."""
    sb = _rolling_sum(insider_buyers, _W126)
    ss = _rolling_sum(insider_sellers, _W126)
    return _safe_div(sb, ss)


def ibr_058_buyer_seller_net_126d(insider_buyers: pd.Series, insider_sellers: pd.Series) -> pd.Series:
    """Net distinct insiders buying vs selling over 126-day window."""
    return _rolling_sum(insider_buyers, _W126) - _rolling_sum(insider_sellers, _W126)


def ibr_059_buyer_seller_ratio_504d(insider_buyers: pd.Series, insider_sellers: pd.Series) -> pd.Series:
    """Rolling 504-day distinct buyers / distinct sellers ratio."""
    sb = _rolling_sum(insider_buyers, _W504)
    ss = _rolling_sum(insider_sellers, _W504)
    return _safe_div(sb, ss)


def ibr_060_seller_fraction_252d(insider_buyers: pd.Series, insider_sellers: pd.Series) -> pd.Series:
    """Fraction of distinct insider participants who are sellers over 252-day window."""
    sb = _rolling_sum(insider_buyers, _W252)
    ss = _rolling_sum(insider_sellers, _W252)
    return _safe_div(ss, sb + ss)


# --- Group E (061-075): Officer/director buy/sell balance and composite scores ---

def ibr_061_officer_value_ratio_63d(officer_buy_value: pd.Series, officer_sell_value: pd.Series) -> pd.Series:
    """Rolling 63-day officer buy-value / officer sell-value ratio."""
    sb = _rolling_sum(officer_buy_value, _W63)
    ss = _rolling_sum(officer_sell_value, _W63)
    return _safe_div(sb, ss)


def ibr_062_officer_value_ratio_252d(officer_buy_value: pd.Series, officer_sell_value: pd.Series) -> pd.Series:
    """Rolling 252-day officer buy-value / officer sell-value ratio."""
    sb = _rolling_sum(officer_buy_value, _W252)
    ss = _rolling_sum(officer_sell_value, _W252)
    return _safe_div(sb, ss)


def ibr_063_officer_net_flow_63d(officer_buy_value: pd.Series, officer_sell_value: pd.Series) -> pd.Series:
    """Net officer dollar flow (buy minus sell) over 63-day window."""
    return _rolling_sum(officer_buy_value, _W63) - _rolling_sum(officer_sell_value, _W63)


def ibr_064_officer_net_flow_252d(officer_buy_value: pd.Series, officer_sell_value: pd.Series) -> pd.Series:
    """Net officer dollar flow over 252-day window."""
    return _rolling_sum(officer_buy_value, _W252) - _rolling_sum(officer_sell_value, _W252)


def ibr_065_director_value_ratio_63d(director_buy_value: pd.Series, director_sell_value: pd.Series) -> pd.Series:
    """Rolling 63-day director buy-value / director sell-value ratio."""
    sb = _rolling_sum(director_buy_value, _W63)
    ss = _rolling_sum(director_sell_value, _W63)
    return _safe_div(sb, ss)


def ibr_066_director_value_ratio_252d(director_buy_value: pd.Series, director_sell_value: pd.Series) -> pd.Series:
    """Rolling 252-day director buy-value / director sell-value ratio."""
    sb = _rolling_sum(director_buy_value, _W252)
    ss = _rolling_sum(director_sell_value, _W252)
    return _safe_div(sb, ss)


def ibr_067_director_net_flow_63d(director_buy_value: pd.Series, director_sell_value: pd.Series) -> pd.Series:
    """Net director dollar flow (buy minus sell) over 63-day window."""
    return _rolling_sum(director_buy_value, _W63) - _rolling_sum(director_sell_value, _W63)


def ibr_068_director_net_flow_252d(director_buy_value: pd.Series, director_sell_value: pd.Series) -> pd.Series:
    """Net director dollar flow over 252-day window."""
    return _rolling_sum(director_buy_value, _W252) - _rolling_sum(director_sell_value, _W252)


def ibr_069_officer_buy_fraction_252d(officer_buy_value: pd.Series, officer_sell_value: pd.Series) -> pd.Series:
    """Fraction of officer total dollar activity that is buys over 252-day window."""
    sb = _rolling_sum(officer_buy_value, _W252)
    ss = _rolling_sum(officer_sell_value, _W252)
    return _safe_div(sb, sb + ss)


def ibr_070_director_buy_fraction_252d(director_buy_value: pd.Series, director_sell_value: pd.Series) -> pd.Series:
    """Fraction of director total dollar activity that is buys over 252-day window."""
    sb = _rolling_sum(director_buy_value, _W252)
    ss = _rolling_sum(director_sell_value, _W252)
    return _safe_div(sb, sb + ss)


def ibr_071_value_net_flow_zscore_252d(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """Z-score of the daily net insider dollar flow within a trailing 252-day window."""
    net_daily = insider_buy_value - insider_sell_value
    return _zscore_rolling(net_daily, _W252)


def ibr_072_count_net_flow_zscore_252d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Z-score of the daily net insider transaction count within a 252-day window."""
    net_daily = insider_buy_count - insider_sell_count
    return _zscore_rolling(net_daily, _W252)


def ibr_073_value_ratio_zscore_252d(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """Z-score of the rolling 63-day value ratio within a 252-day expanding context."""
    sb63 = _rolling_sum(insider_buy_value, _W63)
    ss63 = _rolling_sum(insider_sell_value, _W63)
    ratio63 = _safe_div(sb63, ss63)
    return _zscore_rolling(ratio63, _W252)


def ibr_074_composite_buy_balance_63d(
    insider_buy_count: pd.Series,
    insider_sell_count: pd.Series,
    insider_buy_value: pd.Series,
    insider_sell_value: pd.Series,
) -> pd.Series:
    """
    Composite buy-balance score: average of buy-fraction by count and by value
    over 63-day window. Score > 0.5 indicates buy-tilted insider activity.
    """
    frac_count = _buy_fraction(insider_buy_count, insider_sell_count, _W63)
    sb = _rolling_sum(insider_buy_value, _W63)
    ss = _rolling_sum(insider_sell_value, _W63)
    frac_value = _safe_div(sb, sb + ss)
    combined = frac_count.fillna(0) + frac_value.fillna(0)
    has_count = frac_count.notna().astype(float)
    has_value = frac_value.notna().astype(float)
    denom = has_count + has_value
    return _safe_div(pd.Series(combined.values, index=insider_buy_count.index),
                     pd.Series(denom.values, index=insider_buy_count.index))


def ibr_075_sell_pressure_intensity_63d(insider_sell_value: pd.Series, insider_buy_value: pd.Series) -> pd.Series:
    """
    Sell-pressure intensity: rolling 63-day sell-value as a fraction of total
    (buy+sell) value. High values indicate heavy insider selling pressure.
    """
    ss = _rolling_sum(insider_sell_value, _W63)
    sb = _rolling_sum(insider_buy_value, _W63)
    return _safe_div(ss, sb + ss)


# --- Group K (076-090 in this file, global 151-165): Z-scores and cross-window rank ---

def ibr_151_value_net_flow_zscore_63d(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """Z-score of daily net dollar flow within a trailing 63-day window."""
    net_daily = insider_buy_value - insider_sell_value
    m  = _rolling_mean(net_daily, _W63)
    sd = _rolling_std(net_daily, _W63)
    return _safe_div(net_daily - m, sd)


def ibr_152_count_net_flow_zscore_63d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Z-score of daily net transaction count within a trailing 63-day window."""
    net_daily = insider_buy_count - insider_sell_count
    m  = _rolling_mean(net_daily, _W63)
    sd = _rolling_std(net_daily, _W63)
    return _safe_div(net_daily - m, sd)


def ibr_153_share_net_flow_zscore_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series) -> pd.Series:
    """Z-score of daily net share flow within a trailing 252-day window."""
    net_daily = insider_buy_shares - insider_sell_shares
    m  = _rolling_mean(net_daily, _W252)
    sd = _rolling_std(net_daily, _W252)
    return _safe_div(net_daily - m, sd)


def ibr_154_value_buy_fraction_zscore_252d(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """Z-score of the rolling 21-day buy-fraction (by value) within a 252-day window."""
    bf21 = _rolling_sum(insider_buy_value, _W21) / (_rolling_sum(insider_buy_value, _W21) + _rolling_sum(insider_sell_value, _W21).replace(0, np.nan))
    return _zscore_rolling(bf21, _W252)


def ibr_155_buyer_fraction_zscore_252d(insider_buyers: pd.Series, insider_sellers: pd.Series) -> pd.Series:
    """Z-score of the rolling 63-day buyer fraction within a 252-day window."""
    sb = _rolling_sum(insider_buyers, _W63)
    ss = _rolling_sum(insider_sellers, _W63)
    bf = _safe_div(sb, sb + ss)
    return _zscore_rolling(bf, _W252)


def ibr_156_value_ratio_pct_rank_504d(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """Percentile rank of the rolling 63-day value ratio within its 504-day history."""
    ratio63 = _safe_div(_rolling_sum(insider_buy_value, _W63), _rolling_sum(insider_sell_value, _W63))
    return _rolling_rank_pct(ratio63, _W504)


def ibr_157_count_ratio_pct_rank_504d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Percentile rank of the rolling 63-day count ratio within its 504-day history."""
    ratio63 = _safe_div(_rolling_sum(insider_buy_count, _W63), _rolling_sum(insider_sell_count, _W63))
    return _rolling_rank_pct(ratio63, _W504)


def ibr_158_share_buy_fraction_zscore_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series) -> pd.Series:
    """Z-score of rolling 63-day share buy-fraction within a 252-day window."""
    sb = _rolling_sum(insider_buy_shares, _W63)
    ss = _rolling_sum(insider_sell_shares, _W63)
    bf = _safe_div(sb, sb + ss)
    return _zscore_rolling(bf, _W252)


def ibr_159_officer_net_flow_zscore_252d(officer_buy_value: pd.Series, officer_sell_value: pd.Series) -> pd.Series:
    """Z-score of daily net officer dollar flow within a 252-day window."""
    net_daily = officer_buy_value - officer_sell_value
    return _zscore_rolling(net_daily, _W252)


def ibr_160_director_net_flow_zscore_252d(director_buy_value: pd.Series, director_sell_value: pd.Series) -> pd.Series:
    """Z-score of daily net director dollar flow within a 252-day window."""
    net_daily = director_buy_value - director_sell_value
    return _zscore_rolling(net_daily, _W252)


def ibr_161_value_net_flow_norm_pct_rank_252d(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """Percentile rank of the 21-day normalized net dollar flow within 252-day history."""
    sb = _rolling_sum(insider_buy_value, _W21)
    ss = _rolling_sum(insider_sell_value, _W21)
    norm21 = _safe_div(sb - ss, sb + ss)
    return _rolling_rank_pct(norm21, _W252)


def ibr_162_count_net_flow_norm_pct_rank_252d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Percentile rank of the 21-day normalized net count flow within 252-day history."""
    sb = _rolling_sum(insider_buy_count, _W21)
    ss = _rolling_sum(insider_sell_count, _W21)
    norm21 = _safe_div(sb - ss, sb + ss)
    return _rolling_rank_pct(norm21, _W252)


def ibr_163_buyer_seller_net_pct_rank_252d(insider_buyers: pd.Series, insider_sellers: pd.Series) -> pd.Series:
    """Percentile rank of rolling 63-day net buyer surplus within 252-day history."""
    net63 = _rolling_sum(insider_buyers, _W63) - _rolling_sum(insider_sellers, _W63)
    return _rolling_rank_pct(net63, _W252)


def ibr_164_value_ratio_zscore_504d(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """Z-score of the rolling 63-day value ratio within a 504-day window."""
    ratio63 = _safe_div(_rolling_sum(insider_buy_value, _W63), _rolling_sum(insider_sell_value, _W63))
    return _zscore_rolling(ratio63, _W504)


def ibr_165_count_buy_fraction_zscore_252d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Z-score of rolling 63-day buy-fraction (by count) within a 252-day window."""
    sb = _rolling_sum(insider_buy_count, _W63)
    ss = _rolling_sum(insider_sell_count, _W63)
    bf = _safe_div(sb, sb + ss)
    return _zscore_rolling(bf, _W252)


# --- Group L (091-100 in this file, global 166-175): Rolling OLS slopes over base concepts ---

def ibr_166_value_ratio_21d_slope_252d(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """OLS slope of rolling 21-day value ratio over a trailing 252-day window."""
    ratio21 = _safe_div(_rolling_sum(insider_buy_value, _W21), _rolling_sum(insider_sell_value, _W21))
    def _slope(arr):
        n = len(arr)
        if n < 2:
            return np.nan
        x = np.arange(n, dtype=float)
        xm = x.mean(); ym = np.nanmean(arr)
        d = ((x - xm) ** 2).sum()
        return np.nan if d == 0 else float(np.nansum((x - xm) * (arr - ym)) / d)
    return ratio21.rolling(_W252, min_periods=max(2, _W252 // 4)).apply(_slope, raw=True)


def ibr_167_buy_fraction_63d_slope_252d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """OLS slope of rolling 63-day buy-fraction (by count) over a trailing 252-day window."""
    bf63 = _buy_fraction(insider_buy_count, insider_sell_count, _W63)
    def _slope(arr):
        n = len(arr)
        if n < 2:
            return np.nan
        x = np.arange(n, dtype=float)
        xm = x.mean(); ym = np.nanmean(arr)
        d = ((x - xm) ** 2).sum()
        return np.nan if d == 0 else float(np.nansum((x - xm) * (arr - ym)) / d)
    return bf63.rolling(_W252, min_periods=max(2, _W252 // 4)).apply(_slope, raw=True)


def ibr_168_value_net_flow_63d_slope_252d(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """OLS slope of rolling 63-day net dollar flow over a trailing 252-day window."""
    nf63 = _rolling_sum(insider_buy_value, _W63) - _rolling_sum(insider_sell_value, _W63)
    def _slope(arr):
        n = len(arr)
        if n < 2:
            return np.nan
        x = np.arange(n, dtype=float)
        xm = x.mean(); ym = np.nanmean(arr)
        d = ((x - xm) ** 2).sum()
        return np.nan if d == 0 else float(np.nansum((x - xm) * (arr - ym)) / d)
    return nf63.rolling(_W252, min_periods=max(2, _W252 // 4)).apply(_slope, raw=True)


def ibr_169_buyer_fraction_63d_slope_252d(insider_buyers: pd.Series, insider_sellers: pd.Series) -> pd.Series:
    """OLS slope of rolling 63-day buyer fraction (distinct persons) over a trailing 252-day window."""
    bf63 = _buy_fraction(insider_buyers, insider_sellers, _W63)
    def _slope(arr):
        n = len(arr)
        if n < 2:
            return np.nan
        x = np.arange(n, dtype=float)
        xm = x.mean(); ym = np.nanmean(arr)
        d = ((x - xm) ** 2).sum()
        return np.nan if d == 0 else float(np.nansum((x - xm) * (arr - ym)) / d)
    return bf63.rolling(_W252, min_periods=max(2, _W252 // 4)).apply(_slope, raw=True)


def ibr_170_officer_net_flow_63d_slope_252d(officer_buy_value: pd.Series, officer_sell_value: pd.Series) -> pd.Series:
    """OLS slope of rolling 63-day officer net dollar flow over a trailing 252-day window."""
    nf63 = _rolling_sum(officer_buy_value, _W63) - _rolling_sum(officer_sell_value, _W63)
    def _slope(arr):
        n = len(arr)
        if n < 2:
            return np.nan
        x = np.arange(n, dtype=float)
        xm = x.mean(); ym = np.nanmean(arr)
        d = ((x - xm) ** 2).sum()
        return np.nan if d == 0 else float(np.nansum((x - xm) * (arr - ym)) / d)
    return nf63.rolling(_W252, min_periods=max(2, _W252 // 4)).apply(_slope, raw=True)


def ibr_171_share_net_flow_63d_slope_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series) -> pd.Series:
    """OLS slope of rolling 63-day net share flow over a trailing 252-day window."""
    nf63 = _rolling_sum(insider_buy_shares, _W63) - _rolling_sum(insider_sell_shares, _W63)
    def _slope(arr):
        n = len(arr)
        if n < 2:
            return np.nan
        x = np.arange(n, dtype=float)
        xm = x.mean(); ym = np.nanmean(arr)
        d = ((x - xm) ** 2).sum()
        return np.nan if d == 0 else float(np.nansum((x - xm) * (arr - ym)) / d)
    return nf63.rolling(_W252, min_periods=max(2, _W252 // 4)).apply(_slope, raw=True)


def ibr_172_value_buy_fraction_21d_slope_63d(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """OLS slope of rolling 21-day buy-fraction (by value) over a trailing 63-day window — short-term trend."""
    sb = _rolling_sum(insider_buy_value, _W21)
    ss = _rolling_sum(insider_sell_value, _W21)
    bf21 = _safe_div(sb, sb + ss)
    def _slope(arr):
        n = len(arr)
        if n < 2:
            return np.nan
        x = np.arange(n, dtype=float)
        xm = x.mean(); ym = np.nanmean(arr)
        d = ((x - xm) ** 2).sum()
        return np.nan if d == 0 else float(np.nansum((x - xm) * (arr - ym)) / d)
    return bf21.rolling(_W63, min_periods=max(2, _W63 // 4)).apply(_slope, raw=True)


def ibr_173_director_net_flow_63d_slope_252d(director_buy_value: pd.Series, director_sell_value: pd.Series) -> pd.Series:
    """OLS slope of rolling 63-day director net dollar flow over a trailing 252-day window."""
    nf63 = _rolling_sum(director_buy_value, _W63) - _rolling_sum(director_sell_value, _W63)
    def _slope(arr):
        n = len(arr)
        if n < 2:
            return np.nan
        x = np.arange(n, dtype=float)
        xm = x.mean(); ym = np.nanmean(arr)
        d = ((x - xm) ** 2).sum()
        return np.nan if d == 0 else float(np.nansum((x - xm) * (arr - ym)) / d)
    return nf63.rolling(_W252, min_periods=max(2, _W252 // 4)).apply(_slope, raw=True)


def ibr_174_count_ratio_21d_slope_63d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """OLS slope of rolling 21-day count ratio over a trailing 63-day window — short-term momentum."""
    ratio21 = _safe_div(_rolling_sum(insider_buy_count, _W21), _rolling_sum(insider_sell_count, _W21))
    def _slope(arr):
        n = len(arr)
        if n < 2:
            return np.nan
        x = np.arange(n, dtype=float)
        xm = x.mean(); ym = np.nanmean(arr)
        d = ((x - xm) ** 2).sum()
        return np.nan if d == 0 else float(np.nansum((x - xm) * (arr - ym)) / d)
    return ratio21.rolling(_W63, min_periods=max(2, _W63 // 4)).apply(_slope, raw=True)


def ibr_175_share_buy_fraction_63d_slope_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series) -> pd.Series:
    """OLS slope of rolling 63-day buy-fraction (by shares) over a trailing 252-day window."""
    sb = _rolling_sum(insider_buy_shares, _W63)
    ss = _rolling_sum(insider_sell_shares, _W63)
    bf63 = _safe_div(sb, sb + ss)
    def _slope(arr):
        n = len(arr)
        if n < 2:
            return np.nan
        x = np.arange(n, dtype=float)
        xm = x.mean(); ym = np.nanmean(arr)
        d = ((x - xm) ** 2).sum()
        return np.nan if d == 0 else float(np.nansum((x - xm) * (arr - ym)) / d)
    return bf63.rolling(_W252, min_periods=max(2, _W252 // 4)).apply(_slope, raw=True)


# ── Registry 001-075 ──────────────────────────────────────────────────────────

INSIDER_BUY_SELL_RATIO_REGISTRY_001_075 = {
    "ibr_001_count_ratio_21d":           {"inputs": ["insider_buy_count", "insider_sell_count"],   "func": ibr_001_count_ratio_21d},
    "ibr_002_count_ratio_63d":           {"inputs": ["insider_buy_count", "insider_sell_count"],   "func": ibr_002_count_ratio_63d},
    "ibr_003_count_ratio_126d":          {"inputs": ["insider_buy_count", "insider_sell_count"],   "func": ibr_003_count_ratio_126d},
    "ibr_004_count_ratio_252d":          {"inputs": ["insider_buy_count", "insider_sell_count"],   "func": ibr_004_count_ratio_252d},
    "ibr_005_count_net_flow_21d":        {"inputs": ["insider_buy_count", "insider_sell_count"],   "func": ibr_005_count_net_flow_21d},
    "ibr_006_count_net_flow_63d":        {"inputs": ["insider_buy_count", "insider_sell_count"],   "func": ibr_006_count_net_flow_63d},
    "ibr_007_count_net_flow_126d":       {"inputs": ["insider_buy_count", "insider_sell_count"],   "func": ibr_007_count_net_flow_126d},
    "ibr_008_count_net_flow_252d":       {"inputs": ["insider_buy_count", "insider_sell_count"],   "func": ibr_008_count_net_flow_252d},
    "ibr_009_buy_fraction_21d":          {"inputs": ["insider_buy_count", "insider_sell_count"],   "func": ibr_009_buy_fraction_21d},
    "ibr_010_buy_fraction_63d":          {"inputs": ["insider_buy_count", "insider_sell_count"],   "func": ibr_010_buy_fraction_63d},
    "ibr_011_buy_fraction_126d":         {"inputs": ["insider_buy_count", "insider_sell_count"],   "func": ibr_011_buy_fraction_126d},
    "ibr_012_buy_fraction_252d":         {"inputs": ["insider_buy_count", "insider_sell_count"],   "func": ibr_012_buy_fraction_252d},
    "ibr_013_sell_fraction_63d":         {"inputs": ["insider_buy_count", "insider_sell_count"],   "func": ibr_013_sell_fraction_63d},
    "ibr_014_count_ratio_5d":            {"inputs": ["insider_buy_count", "insider_sell_count"],   "func": ibr_014_count_ratio_5d},
    "ibr_015_count_ratio_504d":          {"inputs": ["insider_buy_count", "insider_sell_count"],   "func": ibr_015_count_ratio_504d},
    "ibr_016_share_ratio_21d":           {"inputs": ["insider_buy_shares", "insider_sell_shares"], "func": ibr_016_share_ratio_21d},
    "ibr_017_share_ratio_63d":           {"inputs": ["insider_buy_shares", "insider_sell_shares"], "func": ibr_017_share_ratio_63d},
    "ibr_018_share_ratio_126d":          {"inputs": ["insider_buy_shares", "insider_sell_shares"], "func": ibr_018_share_ratio_126d},
    "ibr_019_share_ratio_252d":          {"inputs": ["insider_buy_shares", "insider_sell_shares"], "func": ibr_019_share_ratio_252d},
    "ibr_020_share_net_flow_21d":        {"inputs": ["insider_buy_shares", "insider_sell_shares"], "func": ibr_020_share_net_flow_21d},
    "ibr_021_share_net_flow_63d":        {"inputs": ["insider_buy_shares", "insider_sell_shares"], "func": ibr_021_share_net_flow_63d},
    "ibr_022_share_net_flow_126d":       {"inputs": ["insider_buy_shares", "insider_sell_shares"], "func": ibr_022_share_net_flow_126d},
    "ibr_023_share_net_flow_252d":       {"inputs": ["insider_buy_shares", "insider_sell_shares"], "func": ibr_023_share_net_flow_252d},
    "ibr_024_share_buy_fraction_63d":    {"inputs": ["insider_buy_shares", "insider_sell_shares"], "func": ibr_024_share_buy_fraction_63d},
    "ibr_025_share_buy_fraction_252d":   {"inputs": ["insider_buy_shares", "insider_sell_shares"], "func": ibr_025_share_buy_fraction_252d},
    "ibr_026_share_sell_fraction_63d":   {"inputs": ["insider_buy_shares", "insider_sell_shares"], "func": ibr_026_share_sell_fraction_63d},
    "ibr_027_share_net_flow_sign_21d":   {"inputs": ["insider_buy_shares", "insider_sell_shares"], "func": ibr_027_share_net_flow_sign_21d},
    "ibr_028_share_net_flow_sign_63d":   {"inputs": ["insider_buy_shares", "insider_sell_shares"], "func": ibr_028_share_net_flow_sign_63d},
    "ibr_029_share_ratio_5d":            {"inputs": ["insider_buy_shares", "insider_sell_shares"], "func": ibr_029_share_ratio_5d},
    "ibr_030_share_net_flow_504d":       {"inputs": ["insider_buy_shares", "insider_sell_shares"], "func": ibr_030_share_net_flow_504d},
    "ibr_031_value_ratio_21d":           {"inputs": ["insider_buy_value", "insider_sell_value"],   "func": ibr_031_value_ratio_21d},
    "ibr_032_value_ratio_63d":           {"inputs": ["insider_buy_value", "insider_sell_value"],   "func": ibr_032_value_ratio_63d},
    "ibr_033_value_ratio_126d":          {"inputs": ["insider_buy_value", "insider_sell_value"],   "func": ibr_033_value_ratio_126d},
    "ibr_034_value_ratio_252d":          {"inputs": ["insider_buy_value", "insider_sell_value"],   "func": ibr_034_value_ratio_252d},
    "ibr_035_value_net_flow_21d":        {"inputs": ["insider_buy_value", "insider_sell_value"],   "func": ibr_035_value_net_flow_21d},
    "ibr_036_value_net_flow_63d":        {"inputs": ["insider_buy_value", "insider_sell_value"],   "func": ibr_036_value_net_flow_63d},
    "ibr_037_value_net_flow_126d":       {"inputs": ["insider_buy_value", "insider_sell_value"],   "func": ibr_037_value_net_flow_126d},
    "ibr_038_value_net_flow_252d":       {"inputs": ["insider_buy_value", "insider_sell_value"],   "func": ibr_038_value_net_flow_252d},
    "ibr_039_value_buy_fraction_63d":    {"inputs": ["insider_buy_value", "insider_sell_value"],   "func": ibr_039_value_buy_fraction_63d},
    "ibr_040_value_buy_fraction_252d":   {"inputs": ["insider_buy_value", "insider_sell_value"],   "func": ibr_040_value_buy_fraction_252d},
    "ibr_041_value_net_flow_sign_21d":   {"inputs": ["insider_buy_value", "insider_sell_value"],   "func": ibr_041_value_net_flow_sign_21d},
    "ibr_042_value_net_flow_sign_63d":   {"inputs": ["insider_buy_value", "insider_sell_value"],   "func": ibr_042_value_net_flow_sign_63d},
    "ibr_043_value_ratio_5d":            {"inputs": ["insider_buy_value", "insider_sell_value"],   "func": ibr_043_value_ratio_5d},
    "ibr_044_value_net_flow_504d":       {"inputs": ["insider_buy_value", "insider_sell_value"],   "func": ibr_044_value_net_flow_504d},
    "ibr_045_value_sell_fraction_252d":  {"inputs": ["insider_buy_value", "insider_sell_value"],   "func": ibr_045_value_sell_fraction_252d},
    "ibr_046_buyer_seller_ratio_21d":    {"inputs": ["insider_buyers", "insider_sellers"],         "func": ibr_046_buyer_seller_ratio_21d},
    "ibr_047_buyer_seller_ratio_63d":    {"inputs": ["insider_buyers", "insider_sellers"],         "func": ibr_047_buyer_seller_ratio_63d},
    "ibr_048_buyer_seller_ratio_252d":   {"inputs": ["insider_buyers", "insider_sellers"],         "func": ibr_048_buyer_seller_ratio_252d},
    "ibr_049_buyer_seller_net_21d":      {"inputs": ["insider_buyers", "insider_sellers"],         "func": ibr_049_buyer_seller_net_21d},
    "ibr_050_buyer_seller_net_63d":      {"inputs": ["insider_buyers", "insider_sellers"],         "func": ibr_050_buyer_seller_net_63d},
    "ibr_051_buyer_seller_net_252d":     {"inputs": ["insider_buyers", "insider_sellers"],         "func": ibr_051_buyer_seller_net_252d},
    "ibr_052_buyer_fraction_63d":        {"inputs": ["insider_buyers", "insider_sellers"],         "func": ibr_052_buyer_fraction_63d},
    "ibr_053_buyer_fraction_252d":       {"inputs": ["insider_buyers", "insider_sellers"],         "func": ibr_053_buyer_fraction_252d},
    "ibr_054_seller_fraction_63d":       {"inputs": ["insider_buyers", "insider_sellers"],         "func": ibr_054_seller_fraction_63d},
    "ibr_055_buyer_seller_net_sign_21d": {"inputs": ["insider_buyers", "insider_sellers"],         "func": ibr_055_buyer_seller_net_sign_21d},
    "ibr_056_buyer_seller_net_sign_63d": {"inputs": ["insider_buyers", "insider_sellers"],         "func": ibr_056_buyer_seller_net_sign_63d},
    "ibr_057_buyer_seller_ratio_126d":   {"inputs": ["insider_buyers", "insider_sellers"],         "func": ibr_057_buyer_seller_ratio_126d},
    "ibr_058_buyer_seller_net_126d":     {"inputs": ["insider_buyers", "insider_sellers"],         "func": ibr_058_buyer_seller_net_126d},
    "ibr_059_buyer_seller_ratio_504d":   {"inputs": ["insider_buyers", "insider_sellers"],         "func": ibr_059_buyer_seller_ratio_504d},
    "ibr_060_seller_fraction_252d":      {"inputs": ["insider_buyers", "insider_sellers"],         "func": ibr_060_seller_fraction_252d},
    "ibr_061_officer_value_ratio_63d":   {"inputs": ["officer_buy_value", "officer_sell_value"],   "func": ibr_061_officer_value_ratio_63d},
    "ibr_062_officer_value_ratio_252d":  {"inputs": ["officer_buy_value", "officer_sell_value"],   "func": ibr_062_officer_value_ratio_252d},
    "ibr_063_officer_net_flow_63d":      {"inputs": ["officer_buy_value", "officer_sell_value"],   "func": ibr_063_officer_net_flow_63d},
    "ibr_064_officer_net_flow_252d":     {"inputs": ["officer_buy_value", "officer_sell_value"],   "func": ibr_064_officer_net_flow_252d},
    "ibr_065_director_value_ratio_63d":  {"inputs": ["director_buy_value", "director_sell_value"], "func": ibr_065_director_value_ratio_63d},
    "ibr_066_director_value_ratio_252d": {"inputs": ["director_buy_value", "director_sell_value"], "func": ibr_066_director_value_ratio_252d},
    "ibr_067_director_net_flow_63d":     {"inputs": ["director_buy_value", "director_sell_value"], "func": ibr_067_director_net_flow_63d},
    "ibr_068_director_net_flow_252d":    {"inputs": ["director_buy_value", "director_sell_value"], "func": ibr_068_director_net_flow_252d},
    "ibr_069_officer_buy_fraction_252d": {"inputs": ["officer_buy_value", "officer_sell_value"],   "func": ibr_069_officer_buy_fraction_252d},
    "ibr_070_director_buy_fraction_252d":{"inputs": ["director_buy_value", "director_sell_value"], "func": ibr_070_director_buy_fraction_252d},
    "ibr_071_value_net_flow_zscore_252d":{"inputs": ["insider_buy_value", "insider_sell_value"],   "func": ibr_071_value_net_flow_zscore_252d},
    "ibr_072_count_net_flow_zscore_252d":{"inputs": ["insider_buy_count", "insider_sell_count"],   "func": ibr_072_count_net_flow_zscore_252d},
    "ibr_073_value_ratio_zscore_252d":   {"inputs": ["insider_buy_value", "insider_sell_value"],   "func": ibr_073_value_ratio_zscore_252d},
    "ibr_074_composite_buy_balance_63d": {"inputs": ["insider_buy_count", "insider_sell_count", "insider_buy_value", "insider_sell_value"], "func": ibr_074_composite_buy_balance_63d},
    "ibr_075_sell_pressure_intensity_63d":{"inputs": ["insider_sell_value", "insider_buy_value"],  "func": ibr_075_sell_pressure_intensity_63d},
    "ibr_151_value_net_flow_zscore_63d":          {"inputs": ["insider_buy_value", "insider_sell_value"],   "func": ibr_151_value_net_flow_zscore_63d},
    "ibr_152_count_net_flow_zscore_63d":          {"inputs": ["insider_buy_count", "insider_sell_count"],   "func": ibr_152_count_net_flow_zscore_63d},
    "ibr_153_share_net_flow_zscore_252d":         {"inputs": ["insider_buy_shares", "insider_sell_shares"], "func": ibr_153_share_net_flow_zscore_252d},
    "ibr_154_value_buy_fraction_zscore_252d":     {"inputs": ["insider_buy_value", "insider_sell_value"],   "func": ibr_154_value_buy_fraction_zscore_252d},
    "ibr_155_buyer_fraction_zscore_252d":         {"inputs": ["insider_buyers", "insider_sellers"],         "func": ibr_155_buyer_fraction_zscore_252d},
    "ibr_156_value_ratio_pct_rank_504d":          {"inputs": ["insider_buy_value", "insider_sell_value"],   "func": ibr_156_value_ratio_pct_rank_504d},
    "ibr_157_count_ratio_pct_rank_504d":          {"inputs": ["insider_buy_count", "insider_sell_count"],   "func": ibr_157_count_ratio_pct_rank_504d},
    "ibr_158_share_buy_fraction_zscore_252d":     {"inputs": ["insider_buy_shares", "insider_sell_shares"], "func": ibr_158_share_buy_fraction_zscore_252d},
    "ibr_159_officer_net_flow_zscore_252d":       {"inputs": ["officer_buy_value", "officer_sell_value"],   "func": ibr_159_officer_net_flow_zscore_252d},
    "ibr_160_director_net_flow_zscore_252d":      {"inputs": ["director_buy_value", "director_sell_value"], "func": ibr_160_director_net_flow_zscore_252d},
    "ibr_161_value_net_flow_norm_pct_rank_252d":  {"inputs": ["insider_buy_value", "insider_sell_value"],   "func": ibr_161_value_net_flow_norm_pct_rank_252d},
    "ibr_162_count_net_flow_norm_pct_rank_252d":  {"inputs": ["insider_buy_count", "insider_sell_count"],   "func": ibr_162_count_net_flow_norm_pct_rank_252d},
    "ibr_163_buyer_seller_net_pct_rank_252d":     {"inputs": ["insider_buyers", "insider_sellers"],         "func": ibr_163_buyer_seller_net_pct_rank_252d},
    "ibr_164_value_ratio_zscore_504d":            {"inputs": ["insider_buy_value", "insider_sell_value"],   "func": ibr_164_value_ratio_zscore_504d},
    "ibr_165_count_buy_fraction_zscore_252d":     {"inputs": ["insider_buy_count", "insider_sell_count"],   "func": ibr_165_count_buy_fraction_zscore_252d},
    "ibr_166_value_ratio_21d_slope_252d":         {"inputs": ["insider_buy_value", "insider_sell_value"],   "func": ibr_166_value_ratio_21d_slope_252d},
    "ibr_167_buy_fraction_63d_slope_252d":        {"inputs": ["insider_buy_count", "insider_sell_count"],   "func": ibr_167_buy_fraction_63d_slope_252d},
    "ibr_168_value_net_flow_63d_slope_252d":      {"inputs": ["insider_buy_value", "insider_sell_value"],   "func": ibr_168_value_net_flow_63d_slope_252d},
    "ibr_169_buyer_fraction_63d_slope_252d":      {"inputs": ["insider_buyers", "insider_sellers"],         "func": ibr_169_buyer_fraction_63d_slope_252d},
    "ibr_170_officer_net_flow_63d_slope_252d":    {"inputs": ["officer_buy_value", "officer_sell_value"],   "func": ibr_170_officer_net_flow_63d_slope_252d},
    "ibr_171_share_net_flow_63d_slope_252d":      {"inputs": ["insider_buy_shares", "insider_sell_shares"], "func": ibr_171_share_net_flow_63d_slope_252d},
    "ibr_172_value_buy_fraction_21d_slope_63d":   {"inputs": ["insider_buy_value", "insider_sell_value"],   "func": ibr_172_value_buy_fraction_21d_slope_63d},
    "ibr_173_director_net_flow_63d_slope_252d":   {"inputs": ["director_buy_value", "director_sell_value"], "func": ibr_173_director_net_flow_63d_slope_252d},
    "ibr_174_count_ratio_21d_slope_63d":          {"inputs": ["insider_buy_count", "insider_sell_count"],   "func": ibr_174_count_ratio_21d_slope_63d},
    "ibr_175_share_buy_fraction_63d_slope_252d":  {"inputs": ["insider_buy_shares", "insider_sell_shares"], "func": ibr_175_share_buy_fraction_63d_slope_252d},
}
