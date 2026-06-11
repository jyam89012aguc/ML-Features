"""
86_insider_buy_sell_ratio — Extended Features 001-075
Domain: insider buy/sell balance — additional variants: new windows, log/normalized
        ratios, net-flow streaks, drought timing, dominance flags, dispersion,
        percentile/z-score angles, cross-metric agreement and composites.
Asset class: US equities | Sharadar SF2 insider transactions (daily-aggregated)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.

SF2 Daily-Aggregated Insider Series Contract
--------------------------------------------
Inputs are daily-frequency pandas Series aggregated from Sharadar SF2 insider
transaction filings — one row per (ticker, date).  These are EVENT-DRIVEN
series: most days have ZERO activity, positive values appear only on filing
days.  Do NOT forward-fill.  Aggregate over trailing windows using rolling
SUMS.  Functions look strictly backward using .shift(positive), .rolling(), or
.expanding().  Trading-day cadence: 1 week = 5, 1 month = 21, 1 quarter = 63,
1 year = 252, 2 years = 504.

Primary fields used (all lowercase canonical names):
  insider_buy_count, insider_sell_count, insider_buy_shares, insider_sell_shares,
  insider_buy_value, insider_sell_value, insider_buyers, insider_sellers,
  officer_buy_value, officer_sell_value, director_buy_value, director_sell_value
"""
import numpy as np
import pandas as pd

# ── Constants ─────────────────────────────────────────────────────────────────
_W5   = 5     # 1 week
_W10  = 10    # 2 weeks
_W21  = 21    # 1 month
_W42  = 42    # 2 months
_W63  = 63    # 1 quarter
_W126 = 126   # 2 quarters
_W189 = 189   # 3 quarters
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


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 4)).mean()


def _buy_fraction(buy: pd.Series, sell: pd.Series, w: int) -> pd.Series:
    """Fraction of insider activity that is buys: sum_buys / (sum_buys + sum_sells)."""
    sb = _rolling_sum(buy, w)
    ss = _rolling_sum(sell, w)
    return _safe_div(sb, sb + ss)


def _norm_net_flow(buy: pd.Series, sell: pd.Series, w: int) -> pd.Series:
    """Normalized net flow: (sum_buys - sum_sells) / (sum_buys + sum_sells), range -1..1."""
    sb = _rolling_sum(buy, w)
    ss = _rolling_sum(sell, w)
    return _safe_div(sb - ss, sb + ss)


def _consec_true(cond: pd.Series) -> pd.Series:
    """Count consecutive True values up to each row (backward-looking streak)."""
    grp = (~cond).cumsum()
    return cond.astype(int).groupby(grp).cumsum().astype(float)


def _days_since_positive(s: pd.Series) -> pd.Series:
    """Days elapsed since the series was last strictly positive (0 = today positive)."""
    pos = (s > 0).astype(float)
    idx = pd.Series(np.arange(len(s), dtype=float), index=s.index)
    last = idx.where(pos == 1.0).ffill()
    return (idx - last)


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-012): Buy/sell ratios on new windows ---

def ibr_ext_001_count_ratio_10d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Rolling 10-day buy-count / sell-count ratio."""
    return _safe_div(_rolling_sum(insider_buy_count, _W10), _rolling_sum(insider_sell_count, _W10))


def ibr_ext_002_count_ratio_42d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Rolling 42-day buy-count / sell-count ratio."""
    return _safe_div(_rolling_sum(insider_buy_count, _W42), _rolling_sum(insider_sell_count, _W42))


def ibr_ext_003_count_ratio_189d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Rolling 189-day buy-count / sell-count ratio."""
    return _safe_div(_rolling_sum(insider_buy_count, _W189), _rolling_sum(insider_sell_count, _W189))


def ibr_ext_004_value_ratio_42d(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """Rolling 42-day buy-value / sell-value ratio."""
    return _safe_div(_rolling_sum(insider_buy_value, _W42), _rolling_sum(insider_sell_value, _W42))


def ibr_ext_005_value_ratio_189d(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """Rolling 189-day buy-value / sell-value ratio."""
    return _safe_div(_rolling_sum(insider_buy_value, _W189), _rolling_sum(insider_sell_value, _W189))


def ibr_ext_006_share_ratio_42d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series) -> pd.Series:
    """Rolling 42-day buy-shares / sell-shares ratio."""
    return _safe_div(_rolling_sum(insider_buy_shares, _W42), _rolling_sum(insider_sell_shares, _W42))


def ibr_ext_007_share_ratio_504d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series) -> pd.Series:
    """Rolling 504-day buy-shares / sell-shares ratio (2-year view)."""
    return _safe_div(_rolling_sum(insider_buy_shares, _W504), _rolling_sum(insider_sell_shares, _W504))


def ibr_ext_008_value_ratio_10d(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """Rolling 10-day buy-value / sell-value ratio (very short-term sentiment)."""
    return _safe_div(_rolling_sum(insider_buy_value, _W10), _rolling_sum(insider_sell_value, _W10))


def ibr_ext_009_buyer_seller_ratio_42d(insider_buyers: pd.Series, insider_sellers: pd.Series) -> pd.Series:
    """Rolling 42-day distinct buyers / distinct sellers ratio."""
    return _safe_div(_rolling_sum(insider_buyers, _W42), _rolling_sum(insider_sellers, _W42))


def ibr_ext_010_buyer_seller_ratio_189d(insider_buyers: pd.Series, insider_sellers: pd.Series) -> pd.Series:
    """Rolling 189-day distinct buyers / distinct sellers ratio."""
    return _safe_div(_rolling_sum(insider_buyers, _W189), _rolling_sum(insider_sellers, _W189))


def ibr_ext_011_officer_value_ratio_126d(officer_buy_value: pd.Series, officer_sell_value: pd.Series) -> pd.Series:
    """Rolling 126-day officer buy-value / sell-value ratio."""
    return _safe_div(_rolling_sum(officer_buy_value, _W126), _rolling_sum(officer_sell_value, _W126))


def ibr_ext_012_director_value_ratio_126d(director_buy_value: pd.Series, director_sell_value: pd.Series) -> pd.Series:
    """Rolling 126-day director buy-value / sell-value ratio."""
    return _safe_div(_rolling_sum(director_buy_value, _W126), _rolling_sum(director_sell_value, _W126))


# --- Group B (013-022): Log ratios and normalized net flows ---

def ibr_ext_013_log_value_ratio_63d(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """Log of the 63-day buy-value / sell-value ratio (symmetric around zero)."""
    ratio = _safe_div(_rolling_sum(insider_buy_value, _W63), _rolling_sum(insider_sell_value, _W63))
    return np.log(ratio.clip(lower=_EPS))


def ibr_ext_014_log_value_ratio_252d(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """Log of the 252-day buy-value / sell-value ratio."""
    ratio = _safe_div(_rolling_sum(insider_buy_value, _W252), _rolling_sum(insider_sell_value, _W252))
    return np.log(ratio.clip(lower=_EPS))


def ibr_ext_015_log_count_ratio_63d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Log of the 63-day buy-count / sell-count ratio."""
    ratio = _safe_div(_rolling_sum(insider_buy_count, _W63), _rolling_sum(insider_sell_count, _W63))
    return np.log(ratio.clip(lower=_EPS))


def ibr_ext_016_norm_value_net_flow_63d(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """Normalized net dollar flow over 63 days: (buys-sells)/(buys+sells), range -1..1."""
    return _norm_net_flow(insider_buy_value, insider_sell_value, _W63)


def ibr_ext_017_norm_value_net_flow_252d(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """Normalized net dollar flow over 252 days: (buys-sells)/(buys+sells)."""
    return _norm_net_flow(insider_buy_value, insider_sell_value, _W252)


def ibr_ext_018_norm_count_net_flow_63d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Normalized net transaction-count flow over 63 days: (buys-sells)/(buys+sells)."""
    return _norm_net_flow(insider_buy_count, insider_sell_count, _W63)


def ibr_ext_019_norm_share_net_flow_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series) -> pd.Series:
    """Normalized net share flow over 252 days: (buy-shares minus sell-shares) over total."""
    return _norm_net_flow(insider_buy_shares, insider_sell_shares, _W252)


def ibr_ext_020_norm_buyer_net_flow_63d(insider_buyers: pd.Series, insider_sellers: pd.Series) -> pd.Series:
    """Normalized net distinct-participant flow over 63 days: (buyers-sellers)/(buyers+sellers)."""
    return _norm_net_flow(insider_buyers, insider_sellers, _W63)


def ibr_ext_021_norm_value_net_flow_42d(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """Normalized net dollar flow over 42 days: (buys-sells)/(buys+sells)."""
    return _norm_net_flow(insider_buy_value, insider_sell_value, _W42)


def ibr_ext_022_norm_value_net_flow_504d(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """Normalized net dollar flow over 504 days: (buys-sells)/(buys+sells)."""
    return _norm_net_flow(insider_buy_value, insider_sell_value, _W504)


# --- Group C (023-034): Net-flow sign streaks, drought timing, dominance flags ---

def ibr_ext_023_consec_days_net_buyer_value_63d(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """Consecutive days the 63-day net dollar flow has been positive (net-buyer streak)."""
    net = _rolling_sum(insider_buy_value, _W63) - _rolling_sum(insider_sell_value, _W63)
    return _consec_true(net > 0)


def ibr_ext_024_consec_days_net_seller_value_63d(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """Consecutive days the 63-day net dollar flow has been negative (net-seller streak)."""
    net = _rolling_sum(insider_buy_value, _W63) - _rolling_sum(insider_sell_value, _W63)
    return _consec_true(net < 0)


def ibr_ext_025_consec_days_net_buyer_count_63d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Consecutive days the 63-day net transaction-count flow has been positive."""
    net = _rolling_sum(insider_buy_count, _W63) - _rolling_sum(insider_sell_count, _W63)
    return _consec_true(net > 0)


def ibr_ext_026_consec_days_value_ratio_above_1_63d(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """Consecutive days the 63-day buy/sell value ratio has stayed above 1.0."""
    ratio = _safe_div(_rolling_sum(insider_buy_value, _W63), _rolling_sum(insider_sell_value, _W63))
    return _consec_true(ratio > 1.0)


def ibr_ext_027_days_since_net_buyer_value_63d(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """Days elapsed since the 63-day net dollar flow was last positive."""
    net = _rolling_sum(insider_buy_value, _W63) - _rolling_sum(insider_sell_value, _W63)
    return _days_since_positive((net > 0).astype(float))


def ibr_ext_028_days_since_buy_filing(insider_buy_value: pd.Series) -> pd.Series:
    """Days elapsed since the last insider buy filing day (buy-side drought timing)."""
    return _days_since_positive(insider_buy_value)


def ibr_ext_029_days_since_sell_filing(insider_sell_value: pd.Series) -> pd.Series:
    """Days elapsed since the last insider sell filing day (sell-side drought timing)."""
    return _days_since_positive(insider_sell_value)


def ibr_ext_030_net_buyer_flag_504d(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """Binary flag: insiders are net dollar buyers over the trailing 504-day window."""
    net = _rolling_sum(insider_buy_value, _W504) - _rolling_sum(insider_sell_value, _W504)
    return (net > 0).astype(float)


def ibr_ext_031_strong_buy_dominance_flag_252d(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """Binary flag: 252-day buy value exceeds 3x sell value (strong buy dominance)."""
    sb = _rolling_sum(insider_buy_value, _W252)
    ss = _rolling_sum(insider_sell_value, _W252)
    return (sb > 3.0 * ss).astype(float)


def ibr_ext_032_no_sell_flag_252d(insider_sell_value: pd.Series) -> pd.Series:
    """Binary flag: zero insider sell value over the trailing 252-day window."""
    return (_rolling_sum(insider_sell_value, _W252) <= _EPS).astype(float)


def ibr_ext_033_buy_only_regime_flag_252d(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """Binary flag: insiders bought but did not sell at all over the trailing 252-day window."""
    sb = _rolling_sum(insider_buy_value, _W252)
    ss = _rolling_sum(insider_sell_value, _W252)
    return ((sb > 0) & (ss <= _EPS)).astype(float)


def ibr_ext_034_count_net_flow_active_fraction_252d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Fraction of trailing 252 days with any insider transaction (buy or sell) activity."""
    active = ((insider_buy_count + insider_sell_count) > 0).astype(float)
    return _rolling_sum(active, _W252) / float(_W252)


# --- Group D (035-046): Percentile-rank and z-score angles on new windows ---

def ibr_ext_035_value_ratio_pct_rank_252d(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """Percentile rank of the 63-day buy/sell value ratio within a 252-day window."""
    ratio = _safe_div(_rolling_sum(insider_buy_value, _W63), _rolling_sum(insider_sell_value, _W63))
    return _rolling_rank_pct(ratio, _W252)


def ibr_ext_036_count_ratio_pct_rank_252d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Percentile rank of the 63-day buy/sell count ratio within a 252-day window."""
    ratio = _safe_div(_rolling_sum(insider_buy_count, _W63), _rolling_sum(insider_sell_count, _W63))
    return _rolling_rank_pct(ratio, _W252)


def ibr_ext_037_norm_value_net_flow_pct_rank_504d(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """Percentile rank of the 63-day normalized net dollar flow within a 504-day window."""
    return _rolling_rank_pct(_norm_net_flow(insider_buy_value, insider_sell_value, _W63), _W504)


def ibr_ext_038_buy_fraction_value_pct_rank_504d(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """Percentile rank of the 63-day value buy-fraction within a 504-day window."""
    return _rolling_rank_pct(_buy_fraction(insider_buy_value, insider_sell_value, _W63), _W504)


def ibr_ext_039_buyer_fraction_pct_rank_504d(insider_buyers: pd.Series, insider_sellers: pd.Series) -> pd.Series:
    """Percentile rank of the 63-day buyer fraction within a 504-day window."""
    return _rolling_rank_pct(_buy_fraction(insider_buyers, insider_sellers, _W63), _W504)


def ibr_ext_040_value_ratio_zscore_126d(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """Z-score of the 63-day buy/sell value ratio within a 126-day window."""
    ratio = _safe_div(_rolling_sum(insider_buy_value, _W63), _rolling_sum(insider_sell_value, _W63))
    return _zscore_rolling(ratio, _W126)


def ibr_ext_041_norm_net_flow_zscore_252d(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """Z-score of the 21-day normalized net dollar flow within a 252-day window."""
    return _zscore_rolling(_norm_net_flow(insider_buy_value, insider_sell_value, _W21), _W252)


def ibr_ext_042_count_ratio_zscore_252d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Z-score of the 63-day buy/sell count ratio within a 252-day window."""
    ratio = _safe_div(_rolling_sum(insider_buy_count, _W63), _rolling_sum(insider_sell_count, _W63))
    return _zscore_rolling(ratio, _W252)


def ibr_ext_043_value_net_flow_expanding_pct_rank(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """Expanding all-history percentile rank of the 63-day net dollar flow."""
    net = _rolling_sum(insider_buy_value, _W63) - _rolling_sum(insider_sell_value, _W63)
    return net.expanding(min_periods=2).rank(pct=True)


def ibr_ext_044_buy_fraction_value_zscore_504d(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """Z-score of the 63-day value buy-fraction within a 504-day window."""
    return _zscore_rolling(_buy_fraction(insider_buy_value, insider_sell_value, _W63), _W504)


def ibr_ext_045_share_ratio_pct_rank_504d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series) -> pd.Series:
    """Percentile rank of the 63-day buy/sell share ratio within a 504-day window."""
    ratio = _safe_div(_rolling_sum(insider_buy_shares, _W63), _rolling_sum(insider_sell_shares, _W63))
    return _rolling_rank_pct(ratio, _W504)


def ibr_ext_046_buyer_seller_ratio_zscore_252d(insider_buyers: pd.Series, insider_sellers: pd.Series) -> pd.Series:
    """Z-score of the 63-day distinct-buyer / distinct-seller ratio within a 252-day window."""
    ratio = _safe_div(_rolling_sum(insider_buyers, _W63), _rolling_sum(insider_sellers, _W63))
    return _zscore_rolling(ratio, _W252)


# --- Group E (047-056): Cross-window momentum and ratio spreads ---

def ibr_ext_047_value_ratio_21d_vs_252d(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """Ratio of 21-day buy/sell value ratio to 252-day buy/sell value ratio (recent tilt)."""
    short = _safe_div(_rolling_sum(insider_buy_value, _W21), _rolling_sum(insider_sell_value, _W21))
    base  = _safe_div(_rolling_sum(insider_buy_value, _W252), _rolling_sum(insider_sell_value, _W252))
    return _safe_div(short, base)


def ibr_ext_048_norm_net_flow_21d_minus_252d(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """21-day normalized net dollar flow minus 252-day normalized net dollar flow (sentiment shift)."""
    return (_norm_net_flow(insider_buy_value, insider_sell_value, _W21)
            - _norm_net_flow(insider_buy_value, insider_sell_value, _W252))


def ibr_ext_049_buy_fraction_63d_minus_252d_value(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """63-day value buy-fraction minus 252-day value buy-fraction (recent buy-tilt change)."""
    return (_buy_fraction(insider_buy_value, insider_sell_value, _W63)
            - _buy_fraction(insider_buy_value, insider_sell_value, _W252))


def ibr_ext_050_buy_fraction_21d_minus_63d_count(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """21-day count buy-fraction minus 63-day count buy-fraction (very recent tilt change)."""
    return (_buy_fraction(insider_buy_count, insider_sell_count, _W21)
            - _buy_fraction(insider_buy_count, insider_sell_count, _W63))


def ibr_ext_051_value_net_flow_63d_ewm_ratio(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """63-day net dollar flow divided by its 252-day EWM (net-flow momentum ratio)."""
    net = _rolling_sum(insider_buy_value, _W63) - _rolling_sum(insider_sell_value, _W63)
    return _safe_div(net, _ewm_mean(net, _W252))


def ibr_ext_052_value_ratio_63d_minus_504d(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """63-day buy/sell value ratio minus 504-day buy/sell value ratio (ratio spread)."""
    short = _safe_div(_rolling_sum(insider_buy_value, _W63), _rolling_sum(insider_sell_value, _W63))
    base  = _safe_div(_rolling_sum(insider_buy_value, _W504), _rolling_sum(insider_sell_value, _W504))
    return short - base


def ibr_ext_053_norm_net_flow_value_ewm(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """EWM (span=63) of the daily normalized net dollar flow (smoothed sentiment)."""
    daily = _safe_div(insider_buy_value - insider_sell_value,
                      (insider_buy_value + insider_sell_value).replace(0, np.nan))
    return _ewm_mean(daily.fillna(0.0), _W63)


def ibr_ext_054_count_net_flow_42d_vs_252d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """42-day net transaction-count flow normalized by 252-day mean daily net count."""
    net42 = _rolling_sum(insider_buy_count, _W42) - _rolling_sum(insider_sell_count, _W42)
    base  = _rolling_mean(insider_buy_count - insider_sell_count, _W252) * float(_W42)
    return _safe_div(net42, base)


def ibr_ext_055_buyer_fraction_42d_minus_252d(insider_buyers: pd.Series, insider_sellers: pd.Series) -> pd.Series:
    """42-day buyer fraction minus 252-day buyer fraction (recent participation tilt)."""
    return (_buy_fraction(insider_buyers, insider_sellers, _W42)
            - _buy_fraction(insider_buyers, insider_sellers, _W252))


def ibr_ext_056_value_ratio_log_spread_63d_252d(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """Log of 63-day buy/sell ratio minus log of 252-day buy/sell ratio (log ratio spread)."""
    short = _safe_div(_rolling_sum(insider_buy_value, _W63), _rolling_sum(insider_sell_value, _W63))
    base  = _safe_div(_rolling_sum(insider_buy_value, _W252), _rolling_sum(insider_sell_value, _W252))
    return np.log(short.clip(lower=_EPS)) - np.log(base.clip(lower=_EPS))


# --- Group F (057-066): Officer/director balance variants ---

def ibr_ext_057_officer_value_ratio_42d(officer_buy_value: pd.Series, officer_sell_value: pd.Series) -> pd.Series:
    """Rolling 42-day officer buy-value / sell-value ratio."""
    return _safe_div(_rolling_sum(officer_buy_value, _W42), _rolling_sum(officer_sell_value, _W42))


def ibr_ext_058_director_value_ratio_42d(director_buy_value: pd.Series, director_sell_value: pd.Series) -> pd.Series:
    """Rolling 42-day director buy-value / sell-value ratio."""
    return _safe_div(_rolling_sum(director_buy_value, _W42), _rolling_sum(director_sell_value, _W42))


def ibr_ext_059_officer_norm_net_flow_63d(officer_buy_value: pd.Series, officer_sell_value: pd.Series) -> pd.Series:
    """Normalized net officer dollar flow over 63 days: (buy-sell)/(buy+sell)."""
    return _norm_net_flow(officer_buy_value, officer_sell_value, _W63)


def ibr_ext_060_director_norm_net_flow_63d(director_buy_value: pd.Series, director_sell_value: pd.Series) -> pd.Series:
    """Normalized net director dollar flow over 63 days: (buy-sell)/(buy+sell)."""
    return _norm_net_flow(director_buy_value, director_sell_value, _W63)


def ibr_ext_061_officer_net_flow_126d(officer_buy_value: pd.Series, officer_sell_value: pd.Series) -> pd.Series:
    """Net officer dollar flow (buy minus sell) over 126-day window."""
    return _rolling_sum(officer_buy_value, _W126) - _rolling_sum(officer_sell_value, _W126)


def ibr_ext_062_director_net_flow_126d(director_buy_value: pd.Series, director_sell_value: pd.Series) -> pd.Series:
    """Net director dollar flow (buy minus sell) over 126-day window."""
    return _rolling_sum(director_buy_value, _W126) - _rolling_sum(director_sell_value, _W126)


def ibr_ext_063_officer_minus_director_norm_flow_252d(
    officer_buy_value: pd.Series, officer_sell_value: pd.Series,
    director_buy_value: pd.Series, director_sell_value: pd.Series,
) -> pd.Series:
    """Officer normalized net flow minus director normalized net flow over 252 days (role gap)."""
    off = _norm_net_flow(officer_buy_value, officer_sell_value, _W252).fillna(0.0)
    dirr = _norm_net_flow(director_buy_value, director_sell_value, _W252).fillna(0.0)
    return off - dirr


def ibr_ext_064_officer_director_combined_ratio_252d(
    officer_buy_value: pd.Series, officer_sell_value: pd.Series,
    director_buy_value: pd.Series, director_sell_value: pd.Series,
) -> pd.Series:
    """Combined officer+director buy/sell value ratio over 252 days."""
    sb = _rolling_sum(officer_buy_value + director_buy_value, _W252)
    ss = _rolling_sum(officer_sell_value + director_sell_value, _W252)
    return _safe_div(sb, ss)


def ibr_ext_065_officer_net_buyer_flag_63d(officer_buy_value: pd.Series, officer_sell_value: pd.Series) -> pd.Series:
    """Binary flag: officers are net dollar buyers over the trailing 63-day window."""
    return (_rolling_sum(officer_buy_value, _W63) > _rolling_sum(officer_sell_value, _W63)).astype(float)


def ibr_ext_066_director_net_buyer_flag_63d(director_buy_value: pd.Series, director_sell_value: pd.Series) -> pd.Series:
    """Binary flag: directors are net dollar buyers over the trailing 63-day window."""
    return (_rolling_sum(director_buy_value, _W63) > _rolling_sum(director_sell_value, _W63)).astype(float)


# --- Group G (067-075): Cross-metric agreement, dispersion, composites ---

def ibr_ext_067_buy_tilt_agreement_count_63d(
    insider_buy_count: pd.Series, insider_sell_count: pd.Series,
    insider_buy_value: pd.Series, insider_sell_value: pd.Series,
    insider_buy_shares: pd.Series, insider_sell_shares: pd.Series,
) -> pd.Series:
    """Count (0-3) of metrics — count, value, shares — that are buy-tilted over 63 days."""
    by_count = (_rolling_sum(insider_buy_count, _W63) > _rolling_sum(insider_sell_count, _W63)).astype(float)
    by_value = (_rolling_sum(insider_buy_value, _W63) > _rolling_sum(insider_sell_value, _W63)).astype(float)
    by_share = (_rolling_sum(insider_buy_shares, _W63) > _rolling_sum(insider_sell_shares, _W63)).astype(float)
    return by_count + by_value + by_share


def ibr_ext_068_full_buy_agreement_flag_252d(
    insider_buy_count: pd.Series, insider_sell_count: pd.Series,
    insider_buy_value: pd.Series, insider_sell_value: pd.Series,
    insider_buyers: pd.Series, insider_sellers: pd.Series,
) -> pd.Series:
    """Binary: count, value AND distinct-participant metrics all buy-tilted over 252 days."""
    by_count = _rolling_sum(insider_buy_count, _W252) > _rolling_sum(insider_sell_count, _W252)
    by_value = _rolling_sum(insider_buy_value, _W252) > _rolling_sum(insider_sell_value, _W252)
    by_part  = _rolling_sum(insider_buyers, _W252) > _rolling_sum(insider_sellers, _W252)
    return (by_count & by_value & by_part).astype(float)


def ibr_ext_069_count_value_buy_fraction_gap_63d(
    insider_buy_count: pd.Series, insider_sell_count: pd.Series,
    insider_buy_value: pd.Series, insider_sell_value: pd.Series,
) -> pd.Series:
    """Value buy-fraction minus count buy-fraction over 63 days (large-vs-many divergence)."""
    return (_buy_fraction(insider_buy_value, insider_sell_value, _W63)
            - _buy_fraction(insider_buy_count, insider_sell_count, _W63))


def ibr_ext_070_value_ratio_dispersion_252d(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """Rolling std of the 21-day buy/sell value ratio over a 252-day window (ratio volatility)."""
    ratio21 = _safe_div(_rolling_sum(insider_buy_value, _W21), _rolling_sum(insider_sell_value, _W21))
    return _rolling_std(ratio21, _W252)


def ibr_ext_071_norm_net_flow_range_252d(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """Range (max minus min) of the 21-day normalized net dollar flow over 252 days."""
    nf21 = _norm_net_flow(insider_buy_value, insider_sell_value, _W21)
    return _rolling_max(nf21, _W252) - _rolling_min(nf21, _W252)


def ibr_ext_072_sell_pressure_intensity_252d(insider_sell_value: pd.Series, insider_buy_value: pd.Series) -> pd.Series:
    """Sell-pressure intensity over 252 days: sell value as fraction of total (buy+sell) value."""
    ss = _rolling_sum(insider_sell_value, _W252)
    sb = _rolling_sum(insider_buy_value, _W252)
    return _safe_div(ss, sb + ss)


def ibr_ext_073_buy_fraction_min_63d_over_252d(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """Minimum of the 63-day value buy-fraction over a trailing 252-day window (worst tilt)."""
    bf = _buy_fraction(insider_buy_value, insider_sell_value, _W63)
    return _rolling_min(bf, _W252)


def ibr_ext_074_composite_buy_balance_252d(
    insider_buy_count: pd.Series, insider_sell_count: pd.Series,
    insider_buy_value: pd.Series, insider_sell_value: pd.Series,
    insider_buyers: pd.Series, insider_sellers: pd.Series,
) -> pd.Series:
    """
    Composite buy-balance score over 252 days: equally-weighted average of the
    count buy-fraction, the value buy-fraction and the buyer fraction. Score
    above 0.5 indicates broadly buy-tilted insider activity.
    """
    fc = _buy_fraction(insider_buy_count, insider_sell_count, _W252).fillna(0.5)
    fv = _buy_fraction(insider_buy_value, insider_sell_value, _W252).fillna(0.5)
    fp = _buy_fraction(insider_buyers, insider_sellers, _W252).fillna(0.5)
    return (fc + fv + fp) / 3.0


def ibr_ext_075_buy_capitulation_composite(
    insider_buy_value: pd.Series, insider_sell_value: pd.Series,
    insider_buy_count: pd.Series, insider_sell_count: pd.Series,
) -> pd.Series:
    """
    Buy-capitulation composite: equally-weighted average of the 63-day value
    buy-fraction percentile rank, the 63-day count buy-fraction percentile rank,
    and the 63-day normalized net dollar flow rescaled to 0..1 — all over a
    252-day reference. Higher = stronger, historically extreme insider buy tilt.
    """
    fv_rank = _rolling_rank_pct(_buy_fraction(insider_buy_value, insider_sell_value, _W63), _W252).fillna(0.5)
    fc_rank = _rolling_rank_pct(_buy_fraction(insider_buy_count, insider_sell_count, _W63), _W252).fillna(0.5)
    nf = _norm_net_flow(insider_buy_value, insider_sell_value, _W63).fillna(0.0)
    nf_scaled = ((nf + 1.0) / 2.0).clip(lower=0.0, upper=1.0)
    return (fv_rank + fc_rank + nf_scaled) / 3.0


# ── Registry ──────────────────────────────────────────────────────────────────

INSIDER_BUY_SELL_RATIO_EXTENDED_REGISTRY_001_075 = {
    "ibr_ext_001_count_ratio_10d": {"inputs": ["insider_buy_count", "insider_sell_count"], "func": ibr_ext_001_count_ratio_10d},
    "ibr_ext_002_count_ratio_42d": {"inputs": ["insider_buy_count", "insider_sell_count"], "func": ibr_ext_002_count_ratio_42d},
    "ibr_ext_003_count_ratio_189d": {"inputs": ["insider_buy_count", "insider_sell_count"], "func": ibr_ext_003_count_ratio_189d},
    "ibr_ext_004_value_ratio_42d": {"inputs": ["insider_buy_value", "insider_sell_value"], "func": ibr_ext_004_value_ratio_42d},
    "ibr_ext_005_value_ratio_189d": {"inputs": ["insider_buy_value", "insider_sell_value"], "func": ibr_ext_005_value_ratio_189d},
    "ibr_ext_006_share_ratio_42d": {"inputs": ["insider_buy_shares", "insider_sell_shares"], "func": ibr_ext_006_share_ratio_42d},
    "ibr_ext_007_share_ratio_504d": {"inputs": ["insider_buy_shares", "insider_sell_shares"], "func": ibr_ext_007_share_ratio_504d},
    "ibr_ext_008_value_ratio_10d": {"inputs": ["insider_buy_value", "insider_sell_value"], "func": ibr_ext_008_value_ratio_10d},
    "ibr_ext_009_buyer_seller_ratio_42d": {"inputs": ["insider_buyers", "insider_sellers"], "func": ibr_ext_009_buyer_seller_ratio_42d},
    "ibr_ext_010_buyer_seller_ratio_189d": {"inputs": ["insider_buyers", "insider_sellers"], "func": ibr_ext_010_buyer_seller_ratio_189d},
    "ibr_ext_011_officer_value_ratio_126d": {"inputs": ["officer_buy_value", "officer_sell_value"], "func": ibr_ext_011_officer_value_ratio_126d},
    "ibr_ext_012_director_value_ratio_126d": {"inputs": ["director_buy_value", "director_sell_value"], "func": ibr_ext_012_director_value_ratio_126d},
    "ibr_ext_013_log_value_ratio_63d": {"inputs": ["insider_buy_value", "insider_sell_value"], "func": ibr_ext_013_log_value_ratio_63d},
    "ibr_ext_014_log_value_ratio_252d": {"inputs": ["insider_buy_value", "insider_sell_value"], "func": ibr_ext_014_log_value_ratio_252d},
    "ibr_ext_015_log_count_ratio_63d": {"inputs": ["insider_buy_count", "insider_sell_count"], "func": ibr_ext_015_log_count_ratio_63d},
    "ibr_ext_016_norm_value_net_flow_63d": {"inputs": ["insider_buy_value", "insider_sell_value"], "func": ibr_ext_016_norm_value_net_flow_63d},
    "ibr_ext_017_norm_value_net_flow_252d": {"inputs": ["insider_buy_value", "insider_sell_value"], "func": ibr_ext_017_norm_value_net_flow_252d},
    "ibr_ext_018_norm_count_net_flow_63d": {"inputs": ["insider_buy_count", "insider_sell_count"], "func": ibr_ext_018_norm_count_net_flow_63d},
    "ibr_ext_019_norm_share_net_flow_252d": {"inputs": ["insider_buy_shares", "insider_sell_shares"], "func": ibr_ext_019_norm_share_net_flow_252d},
    "ibr_ext_020_norm_buyer_net_flow_63d": {"inputs": ["insider_buyers", "insider_sellers"], "func": ibr_ext_020_norm_buyer_net_flow_63d},
    "ibr_ext_021_norm_value_net_flow_42d": {"inputs": ["insider_buy_value", "insider_sell_value"], "func": ibr_ext_021_norm_value_net_flow_42d},
    "ibr_ext_022_norm_value_net_flow_504d": {"inputs": ["insider_buy_value", "insider_sell_value"], "func": ibr_ext_022_norm_value_net_flow_504d},
    "ibr_ext_023_consec_days_net_buyer_value_63d": {"inputs": ["insider_buy_value", "insider_sell_value"], "func": ibr_ext_023_consec_days_net_buyer_value_63d},
    "ibr_ext_024_consec_days_net_seller_value_63d": {"inputs": ["insider_buy_value", "insider_sell_value"], "func": ibr_ext_024_consec_days_net_seller_value_63d},
    "ibr_ext_025_consec_days_net_buyer_count_63d": {"inputs": ["insider_buy_count", "insider_sell_count"], "func": ibr_ext_025_consec_days_net_buyer_count_63d},
    "ibr_ext_026_consec_days_value_ratio_above_1_63d": {"inputs": ["insider_buy_value", "insider_sell_value"], "func": ibr_ext_026_consec_days_value_ratio_above_1_63d},
    "ibr_ext_027_days_since_net_buyer_value_63d": {"inputs": ["insider_buy_value", "insider_sell_value"], "func": ibr_ext_027_days_since_net_buyer_value_63d},
    "ibr_ext_028_days_since_buy_filing": {"inputs": ["insider_buy_value"], "func": ibr_ext_028_days_since_buy_filing},
    "ibr_ext_029_days_since_sell_filing": {"inputs": ["insider_sell_value"], "func": ibr_ext_029_days_since_sell_filing},
    "ibr_ext_030_net_buyer_flag_504d": {"inputs": ["insider_buy_value", "insider_sell_value"], "func": ibr_ext_030_net_buyer_flag_504d},
    "ibr_ext_031_strong_buy_dominance_flag_252d": {"inputs": ["insider_buy_value", "insider_sell_value"], "func": ibr_ext_031_strong_buy_dominance_flag_252d},
    "ibr_ext_032_no_sell_flag_252d": {"inputs": ["insider_sell_value"], "func": ibr_ext_032_no_sell_flag_252d},
    "ibr_ext_033_buy_only_regime_flag_252d": {"inputs": ["insider_buy_value", "insider_sell_value"], "func": ibr_ext_033_buy_only_regime_flag_252d},
    "ibr_ext_034_count_net_flow_active_fraction_252d": {"inputs": ["insider_buy_count", "insider_sell_count"], "func": ibr_ext_034_count_net_flow_active_fraction_252d},
    "ibr_ext_035_value_ratio_pct_rank_252d": {"inputs": ["insider_buy_value", "insider_sell_value"], "func": ibr_ext_035_value_ratio_pct_rank_252d},
    "ibr_ext_036_count_ratio_pct_rank_252d": {"inputs": ["insider_buy_count", "insider_sell_count"], "func": ibr_ext_036_count_ratio_pct_rank_252d},
    "ibr_ext_037_norm_value_net_flow_pct_rank_504d": {"inputs": ["insider_buy_value", "insider_sell_value"], "func": ibr_ext_037_norm_value_net_flow_pct_rank_504d},
    "ibr_ext_038_buy_fraction_value_pct_rank_504d": {"inputs": ["insider_buy_value", "insider_sell_value"], "func": ibr_ext_038_buy_fraction_value_pct_rank_504d},
    "ibr_ext_039_buyer_fraction_pct_rank_504d": {"inputs": ["insider_buyers", "insider_sellers"], "func": ibr_ext_039_buyer_fraction_pct_rank_504d},
    "ibr_ext_040_value_ratio_zscore_126d": {"inputs": ["insider_buy_value", "insider_sell_value"], "func": ibr_ext_040_value_ratio_zscore_126d},
    "ibr_ext_041_norm_net_flow_zscore_252d": {"inputs": ["insider_buy_value", "insider_sell_value"], "func": ibr_ext_041_norm_net_flow_zscore_252d},
    "ibr_ext_042_count_ratio_zscore_252d": {"inputs": ["insider_buy_count", "insider_sell_count"], "func": ibr_ext_042_count_ratio_zscore_252d},
    "ibr_ext_043_value_net_flow_expanding_pct_rank": {"inputs": ["insider_buy_value", "insider_sell_value"], "func": ibr_ext_043_value_net_flow_expanding_pct_rank},
    "ibr_ext_044_buy_fraction_value_zscore_504d": {"inputs": ["insider_buy_value", "insider_sell_value"], "func": ibr_ext_044_buy_fraction_value_zscore_504d},
    "ibr_ext_045_share_ratio_pct_rank_504d": {"inputs": ["insider_buy_shares", "insider_sell_shares"], "func": ibr_ext_045_share_ratio_pct_rank_504d},
    "ibr_ext_046_buyer_seller_ratio_zscore_252d": {"inputs": ["insider_buyers", "insider_sellers"], "func": ibr_ext_046_buyer_seller_ratio_zscore_252d},
    "ibr_ext_047_value_ratio_21d_vs_252d": {"inputs": ["insider_buy_value", "insider_sell_value"], "func": ibr_ext_047_value_ratio_21d_vs_252d},
    "ibr_ext_048_norm_net_flow_21d_minus_252d": {"inputs": ["insider_buy_value", "insider_sell_value"], "func": ibr_ext_048_norm_net_flow_21d_minus_252d},
    "ibr_ext_049_buy_fraction_63d_minus_252d_value": {"inputs": ["insider_buy_value", "insider_sell_value"], "func": ibr_ext_049_buy_fraction_63d_minus_252d_value},
    "ibr_ext_050_buy_fraction_21d_minus_63d_count": {"inputs": ["insider_buy_count", "insider_sell_count"], "func": ibr_ext_050_buy_fraction_21d_minus_63d_count},
    "ibr_ext_051_value_net_flow_63d_ewm_ratio": {"inputs": ["insider_buy_value", "insider_sell_value"], "func": ibr_ext_051_value_net_flow_63d_ewm_ratio},
    "ibr_ext_052_value_ratio_63d_minus_504d": {"inputs": ["insider_buy_value", "insider_sell_value"], "func": ibr_ext_052_value_ratio_63d_minus_504d},
    "ibr_ext_053_norm_net_flow_value_ewm": {"inputs": ["insider_buy_value", "insider_sell_value"], "func": ibr_ext_053_norm_net_flow_value_ewm},
    "ibr_ext_054_count_net_flow_42d_vs_252d": {"inputs": ["insider_buy_count", "insider_sell_count"], "func": ibr_ext_054_count_net_flow_42d_vs_252d},
    "ibr_ext_055_buyer_fraction_42d_minus_252d": {"inputs": ["insider_buyers", "insider_sellers"], "func": ibr_ext_055_buyer_fraction_42d_minus_252d},
    "ibr_ext_056_value_ratio_log_spread_63d_252d": {"inputs": ["insider_buy_value", "insider_sell_value"], "func": ibr_ext_056_value_ratio_log_spread_63d_252d},
    "ibr_ext_057_officer_value_ratio_42d": {"inputs": ["officer_buy_value", "officer_sell_value"], "func": ibr_ext_057_officer_value_ratio_42d},
    "ibr_ext_058_director_value_ratio_42d": {"inputs": ["director_buy_value", "director_sell_value"], "func": ibr_ext_058_director_value_ratio_42d},
    "ibr_ext_059_officer_norm_net_flow_63d": {"inputs": ["officer_buy_value", "officer_sell_value"], "func": ibr_ext_059_officer_norm_net_flow_63d},
    "ibr_ext_060_director_norm_net_flow_63d": {"inputs": ["director_buy_value", "director_sell_value"], "func": ibr_ext_060_director_norm_net_flow_63d},
    "ibr_ext_061_officer_net_flow_126d": {"inputs": ["officer_buy_value", "officer_sell_value"], "func": ibr_ext_061_officer_net_flow_126d},
    "ibr_ext_062_director_net_flow_126d": {"inputs": ["director_buy_value", "director_sell_value"], "func": ibr_ext_062_director_net_flow_126d},
    "ibr_ext_063_officer_minus_director_norm_flow_252d": {"inputs": ["officer_buy_value", "officer_sell_value", "director_buy_value", "director_sell_value"], "func": ibr_ext_063_officer_minus_director_norm_flow_252d},
    "ibr_ext_064_officer_director_combined_ratio_252d": {"inputs": ["officer_buy_value", "officer_sell_value", "director_buy_value", "director_sell_value"], "func": ibr_ext_064_officer_director_combined_ratio_252d},
    "ibr_ext_065_officer_net_buyer_flag_63d": {"inputs": ["officer_buy_value", "officer_sell_value"], "func": ibr_ext_065_officer_net_buyer_flag_63d},
    "ibr_ext_066_director_net_buyer_flag_63d": {"inputs": ["director_buy_value", "director_sell_value"], "func": ibr_ext_066_director_net_buyer_flag_63d},
    "ibr_ext_067_buy_tilt_agreement_count_63d": {"inputs": ["insider_buy_count", "insider_sell_count", "insider_buy_value", "insider_sell_value", "insider_buy_shares", "insider_sell_shares"], "func": ibr_ext_067_buy_tilt_agreement_count_63d},
    "ibr_ext_068_full_buy_agreement_flag_252d": {"inputs": ["insider_buy_count", "insider_sell_count", "insider_buy_value", "insider_sell_value", "insider_buyers", "insider_sellers"], "func": ibr_ext_068_full_buy_agreement_flag_252d},
    "ibr_ext_069_count_value_buy_fraction_gap_63d": {"inputs": ["insider_buy_count", "insider_sell_count", "insider_buy_value", "insider_sell_value"], "func": ibr_ext_069_count_value_buy_fraction_gap_63d},
    "ibr_ext_070_value_ratio_dispersion_252d": {"inputs": ["insider_buy_value", "insider_sell_value"], "func": ibr_ext_070_value_ratio_dispersion_252d},
    "ibr_ext_071_norm_net_flow_range_252d": {"inputs": ["insider_buy_value", "insider_sell_value"], "func": ibr_ext_071_norm_net_flow_range_252d},
    "ibr_ext_072_sell_pressure_intensity_252d": {"inputs": ["insider_sell_value", "insider_buy_value"], "func": ibr_ext_072_sell_pressure_intensity_252d},
    "ibr_ext_073_buy_fraction_min_63d_over_252d": {"inputs": ["insider_buy_value", "insider_sell_value"], "func": ibr_ext_073_buy_fraction_min_63d_over_252d},
    "ibr_ext_074_composite_buy_balance_252d": {"inputs": ["insider_buy_count", "insider_sell_count", "insider_buy_value", "insider_sell_value", "insider_buyers", "insider_sellers"], "func": ibr_ext_074_composite_buy_balance_252d},
    "ibr_ext_075_buy_capitulation_composite": {"inputs": ["insider_buy_value", "insider_sell_value", "insider_buy_count", "insider_sell_count"], "func": ibr_ext_075_buy_capitulation_composite},
}
