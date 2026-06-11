"""
89_insider_conviction — Base Features 001-100
Domain: insider conviction — purchase size relative to existing insider stake
Asset class: US equities | Sharadar SF2 insider transactions (daily-aggregated)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.

SF2 Daily-Aggregated Insider Series Contract
--------------------------------------------
Inputs are daily-frequency pandas Series aggregated from Sharadar SF2 insider
transaction records to one row per (ticker, date).

FLOW series (insider_buy_count, insider_sell_count, insider_buy_shares,
insider_sell_shares, insider_buy_value, insider_sell_value, insider_buyers,
insider_sellers, officer_buy_count, officer_buy_value, officer_sell_value,
director_buy_count, director_buy_value, director_sell_value, ceo_buy_value,
cfo_buy_value, tenpct_buy_count, tenpct_buy_value):
  EVENT-DRIVEN — most days are ZERO. Not forward-filled. Aggregate with
  trailing rolling SUMS over windows like 5/21/63/126/252 trading days.

STOCK series (insider_shares_held):
  CUMULATIVE total shares held by insiders following all transactions known
  as of each date. Persists/steps; treat as a LEVEL series. May be read
  directly or smoothed; do NOT sum it.

Trading-day calendar: 252/yr, 126/half-yr, 63/qtr, 21/mo, 5/wk.
All feature functions look strictly backward.
"""
import numpy as np
import pandas as pd

# ── Constants ─────────────────────────────────────────────────────────────────
_TD_YEAR  = 252
_TD_HALF  = 126
_TD_QTR   = 63
_TD_2Y    = 504
_TD_MO    = 21
_TD_WK    = 5
_EPS      = 1e-9

# ── Utility helpers ───────────────────────────────────────────────────────────

def _safe_div(num: pd.Series, den: pd.Series) -> pd.Series:
    """Element-wise division; returns NaN wherever denominator is zero or NaN.
    Deliberately returns NaN (not zero) when the prior stake is zero — a buy
    when there are zero prior shares is undefined in conviction-ratio terms."""
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


def _rolling_median(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).median()


def _rolling_rank_pct(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(2, w // 4)).rank(pct=True)


def _zscore_rolling(s: pd.Series, w: int) -> pd.Series:
    m  = _rolling_mean(s, w)
    sd = _rolling_std(s, w)
    return _safe_div(s - m, sd)


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 4)).mean()


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-015): Buy-shares as fraction of existing stake level ---

def icn_001_buy_shares_pct_of_held_mo(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Monthly (21-day) rolling sum of buy_shares divided by current insider_shares_held.
    Measures how much the recent buying would expand the existing insider ownership base."""
    buys = _rolling_sum(insider_buy_shares, _TD_MO)
    return _safe_div(buys, insider_shares_held)


def icn_002_buy_shares_pct_of_held_qtr(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Quarterly (63-day) rolling sum of buy_shares divided by insider_shares_held."""
    buys = _rolling_sum(insider_buy_shares, _TD_QTR)
    return _safe_div(buys, insider_shares_held)


def icn_003_buy_shares_pct_of_held_halfyr(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Half-year (126-day) rolling sum of buy_shares divided by insider_shares_held."""
    buys = _rolling_sum(insider_buy_shares, _TD_HALF)
    return _safe_div(buys, insider_shares_held)


def icn_004_buy_shares_pct_of_held_1y(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Annual (252-day) rolling sum of buy_shares divided by insider_shares_held."""
    buys = _rolling_sum(insider_buy_shares, _TD_YEAR)
    return _safe_div(buys, insider_shares_held)


def icn_005_buy_shares_pct_of_held_wk(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Weekly (5-day) rolling sum of buy_shares divided by insider_shares_held."""
    buys = _rolling_sum(insider_buy_shares, _TD_WK)
    return _safe_div(buys, insider_shares_held)


def icn_006_buy_value_pct_of_held_value_mo(insider_buy_value: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Monthly buy value as fraction of insider_shares_held (proxy for stake value scaling).
    Numerator is dollar flow; denominator is share count — a cross-unit ratio capturing
    commitment intensity per share of existing stake."""
    buys = _rolling_sum(insider_buy_value, _TD_MO)
    return _safe_div(buys, insider_shares_held)


def icn_007_buy_value_pct_of_held_value_qtr(insider_buy_value: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Quarterly buy value scaled by insider_shares_held."""
    buys = _rolling_sum(insider_buy_value, _TD_QTR)
    return _safe_div(buys, insider_shares_held)


def icn_008_buy_value_pct_of_held_value_1y(insider_buy_value: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Annual buy value scaled by insider_shares_held."""
    buys = _rolling_sum(insider_buy_value, _TD_YEAR)
    return _safe_div(buys, insider_shares_held)


def icn_009_buy_shares_prior_stake_lagged_mo(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Monthly buy shares divided by insider_shares_held lagged one month.
    Using the prior stake level to avoid look-ahead within the event window."""
    buys = _rolling_sum(insider_buy_shares, _TD_MO)
    prior_held = insider_shares_held.shift(_TD_MO)
    return _safe_div(buys, prior_held)


def icn_010_buy_shares_prior_stake_lagged_qtr(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Quarterly buy shares divided by insider_shares_held lagged one quarter."""
    buys = _rolling_sum(insider_buy_shares, _TD_QTR)
    prior_held = insider_shares_held.shift(_TD_QTR)
    return _safe_div(buys, prior_held)


def icn_011_officer_buy_value_pct_of_held_mo(officer_buy_value: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Monthly officer buy value scaled by insider_shares_held — officer-specific conviction."""
    buys = _rolling_sum(officer_buy_value, _TD_MO)
    return _safe_div(buys, insider_shares_held)


def icn_012_officer_buy_value_pct_of_held_qtr(officer_buy_value: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Quarterly officer buy value scaled by insider_shares_held."""
    buys = _rolling_sum(officer_buy_value, _TD_QTR)
    return _safe_div(buys, insider_shares_held)


def icn_013_director_buy_value_pct_of_held_mo(director_buy_value: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Monthly director buy value scaled by insider_shares_held — director conviction."""
    buys = _rolling_sum(director_buy_value, _TD_MO)
    return _safe_div(buys, insider_shares_held)


def icn_014_director_buy_value_pct_of_held_qtr(director_buy_value: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Quarterly director buy value scaled by insider_shares_held."""
    buys = _rolling_sum(director_buy_value, _TD_QTR)
    return _safe_div(buys, insider_shares_held)


def icn_015_ceo_buy_value_pct_of_held_mo(ceo_buy_value: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Monthly CEO buy value scaled by insider_shares_held — highest-conviction signal."""
    buys = _rolling_sum(ceo_buy_value, _TD_MO)
    return _safe_div(buys, insider_shares_held)


# --- Group B (016-030): Meaningful-stake-increase flags ---

def icn_016_flag_buy_adds_5pct_mo(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Flag: 1 if monthly buy_shares >= 5% of insider_shares_held (material stake increase)."""
    ratio = _safe_div(_rolling_sum(insider_buy_shares, _TD_MO), insider_shares_held)
    return (ratio >= 0.05).astype(float)


def icn_017_flag_buy_adds_10pct_mo(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Flag: 1 if monthly buy_shares >= 10% of insider_shares_held."""
    ratio = _safe_div(_rolling_sum(insider_buy_shares, _TD_MO), insider_shares_held)
    return (ratio >= 0.10).astype(float)


def icn_018_flag_buy_adds_25pct_mo(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Flag: 1 if monthly buy_shares >= 25% of insider_shares_held (very high conviction)."""
    ratio = _safe_div(_rolling_sum(insider_buy_shares, _TD_MO), insider_shares_held)
    return (ratio >= 0.25).astype(float)


def icn_019_flag_buy_adds_5pct_qtr(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Flag: 1 if quarterly buy_shares >= 5% of insider_shares_held."""
    ratio = _safe_div(_rolling_sum(insider_buy_shares, _TD_QTR), insider_shares_held)
    return (ratio >= 0.05).astype(float)


def icn_020_flag_buy_adds_10pct_qtr(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Flag: 1 if quarterly buy_shares >= 10% of insider_shares_held."""
    ratio = _safe_div(_rolling_sum(insider_buy_shares, _TD_QTR), insider_shares_held)
    return (ratio >= 0.10).astype(float)


def icn_021_flag_buy_adds_25pct_qtr(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Flag: 1 if quarterly buy_shares >= 25% of insider_shares_held."""
    ratio = _safe_div(_rolling_sum(insider_buy_shares, _TD_QTR), insider_shares_held)
    return (ratio >= 0.25).astype(float)


def icn_022_flag_buy_adds_50pct_1y(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Flag: 1 if annual buy_shares >= 50% of insider_shares_held (doubling the stake)."""
    ratio = _safe_div(_rolling_sum(insider_buy_shares, _TD_YEAR), insider_shares_held)
    return (ratio >= 0.50).astype(float)


def icn_023_flag_officer_buy_adds_5pct_mo(officer_buy_value: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Flag: 1 if monthly officer buy value exceeds 5% of insider_shares_held (scaled units)."""
    ratio = _safe_div(_rolling_sum(officer_buy_value, _TD_MO), insider_shares_held)
    return (ratio > 0.0).astype(float) * (ratio >= ratio.expanding(min_periods=1).quantile(0.75).fillna(0))


def icn_024_conviction_flag_any_5pct_1y(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Flag: 1 if any rolling 21-day window in the past year had buy >= 5% of held."""
    ratio_mo = _safe_div(_rolling_sum(insider_buy_shares, _TD_MO), insider_shares_held)
    high_conv = (ratio_mo >= 0.05).astype(float)
    return _rolling_max(high_conv, _TD_YEAR)


def icn_025_conviction_flag_any_10pct_1y(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Flag: 1 if any rolling 21-day window in the past year had buy >= 10% of held."""
    ratio_mo = _safe_div(_rolling_sum(insider_buy_shares, _TD_MO), insider_shares_held)
    high_conv = (ratio_mo >= 0.10).astype(float)
    return _rolling_max(high_conv, _TD_YEAR)


# --- Group C (026-040): Conviction-weighted buy scores ---

def icn_026_conviction_score_mo(insider_buy_shares: pd.Series, insider_shares_held: pd.Series, insider_buy_count: pd.Series) -> pd.Series:
    """Conviction score: (buy_shares/held) * buy_count over 21 days.
    Combines stake-relative size with frequency of buying events."""
    ratio = _safe_div(_rolling_sum(insider_buy_shares, _TD_MO), insider_shares_held)
    count = _rolling_sum(insider_buy_count, _TD_MO)
    return ratio * count


def icn_027_conviction_score_qtr(insider_buy_shares: pd.Series, insider_shares_held: pd.Series, insider_buy_count: pd.Series) -> pd.Series:
    """Conviction score: (buy_shares/held) * buy_count over 63 days."""
    ratio = _safe_div(_rolling_sum(insider_buy_shares, _TD_QTR), insider_shares_held)
    count = _rolling_sum(insider_buy_count, _TD_QTR)
    return ratio * count


def icn_028_conviction_intensity_mo(insider_buy_value: pd.Series, insider_shares_held: pd.Series, insider_buy_count: pd.Series) -> pd.Series:
    """Conviction intensity: buy_value per insider_shares_held per buy event (monthly)."""
    val = _rolling_sum(insider_buy_value, _TD_MO)
    cnt = _rolling_sum(insider_buy_count, _TD_MO).replace(0, np.nan)
    return _safe_div(val, insider_shares_held * cnt)


def icn_029_conviction_intensity_qtr(insider_buy_value: pd.Series, insider_shares_held: pd.Series, insider_buy_count: pd.Series) -> pd.Series:
    """Conviction intensity: buy_value per insider_shares_held per buy event (quarterly)."""
    val = _rolling_sum(insider_buy_value, _TD_QTR)
    cnt = _rolling_sum(insider_buy_count, _TD_QTR).replace(0, np.nan)
    return _safe_div(val, insider_shares_held * cnt)


def icn_030_officer_conviction_ratio_qtr(officer_buy_value: pd.Series, insider_buy_value: pd.Series) -> pd.Series:
    """Officer buy value as share of total insider buy value (quarterly).
    High values indicate senior-officer-led buying rather than peripheral insiders."""
    off_val = _rolling_sum(officer_buy_value, _TD_QTR)
    tot_val = _rolling_sum(insider_buy_value, _TD_QTR)
    return _safe_div(off_val, tot_val)


def icn_031_cfo_buy_value_pct_of_held_qtr(cfo_buy_value: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Quarterly CFO buy value scaled by insider_shares_held — CFO-specific conviction."""
    buys = _rolling_sum(cfo_buy_value, _TD_QTR)
    return _safe_div(buys, insider_shares_held)


def icn_032_tenpct_buy_value_pct_of_held_qtr(tenpct_buy_value: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Quarterly 10%-holder buy value scaled by insider_shares_held."""
    buys = _rolling_sum(tenpct_buy_value, _TD_QTR)
    return _safe_div(buys, insider_shares_held)


def icn_033_net_buy_shares_pct_held_mo(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Net (buy - sell) shares as percent of insider_shares_held over 21 days.
    Positive means net accumulation relative to stake."""
    net = _rolling_sum(insider_buy_shares, _TD_MO) - _rolling_sum(insider_sell_shares, _TD_MO)
    return _safe_div(net, insider_shares_held)


def icn_034_net_buy_shares_pct_held_qtr(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Net (buy - sell) shares as percent of insider_shares_held over 63 days."""
    net = _rolling_sum(insider_buy_shares, _TD_QTR) - _rolling_sum(insider_sell_shares, _TD_QTR)
    return _safe_div(net, insider_shares_held)


def icn_035_net_buy_shares_pct_held_1y(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Net (buy - sell) shares as percent of insider_shares_held over 252 days."""
    net = _rolling_sum(insider_buy_shares, _TD_YEAR) - _rolling_sum(insider_sell_shares, _TD_YEAR)
    return _safe_div(net, insider_shares_held)


def icn_036_buy_to_sell_ratio_pct_held(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """(buy_shares - sell_shares) / insider_shares_held ratio (quarterly), bounded conviction."""
    net = _rolling_sum(insider_buy_shares, _TD_QTR) - _rolling_sum(insider_sell_shares, _TD_QTR)
    return _safe_div(net, insider_shares_held).clip(lower=-1.0, upper=5.0)


def icn_037_conviction_weighted_by_buyers_mo(insider_buy_shares: pd.Series, insider_shares_held: pd.Series, insider_buyers: pd.Series) -> pd.Series:
    """(buy_shares/held) weighted by number of distinct buyers (monthly).
    More buyers raising their stake = broader conviction."""
    ratio = _safe_div(_rolling_sum(insider_buy_shares, _TD_MO), insider_shares_held)
    buyers = _rolling_sum(insider_buyers, _TD_MO)
    return ratio * buyers


def icn_038_conviction_weighted_by_buyers_qtr(insider_buy_shares: pd.Series, insider_shares_held: pd.Series, insider_buyers: pd.Series) -> pd.Series:
    """(buy_shares/held) weighted by number of distinct buyers (quarterly)."""
    ratio = _safe_div(_rolling_sum(insider_buy_shares, _TD_QTR), insider_shares_held)
    buyers = _rolling_sum(insider_buyers, _TD_QTR)
    return ratio * buyers


def icn_039_avg_conviction_per_buyer_mo(insider_buy_shares: pd.Series, insider_shares_held: pd.Series, insider_buyers: pd.Series) -> pd.Series:
    """Average per-buyer conviction: (buy_shares/held) / distinct_buyers (monthly)."""
    ratio = _safe_div(_rolling_sum(insider_buy_shares, _TD_MO), insider_shares_held)
    buyers = _rolling_sum(insider_buyers, _TD_MO).replace(0, np.nan)
    return ratio / buyers


def icn_040_avg_conviction_per_buyer_qtr(insider_buy_shares: pd.Series, insider_shares_held: pd.Series, insider_buyers: pd.Series) -> pd.Series:
    """Average per-buyer conviction: (buy_shares/held) / distinct_buyers (quarterly)."""
    ratio = _safe_div(_rolling_sum(insider_buy_shares, _TD_QTR), insider_shares_held)
    buyers = _rolling_sum(insider_buyers, _TD_QTR).replace(0, np.nan)
    return ratio / buyers


# --- Group D (041-055): Trajectory of insider_shares_held rising from buying ---

def icn_041_held_shares_growth_mo(insider_shares_held: pd.Series) -> pd.Series:
    """Absolute growth in insider_shares_held over 21 days (buying-driven accumulation)."""
    return insider_shares_held - insider_shares_held.shift(_TD_MO)


def icn_042_held_shares_growth_qtr(insider_shares_held: pd.Series) -> pd.Series:
    """Absolute growth in insider_shares_held over 63 days."""
    return insider_shares_held - insider_shares_held.shift(_TD_QTR)


def icn_043_held_shares_growth_halfyr(insider_shares_held: pd.Series) -> pd.Series:
    """Absolute growth in insider_shares_held over 126 days."""
    return insider_shares_held - insider_shares_held.shift(_TD_HALF)


def icn_044_held_shares_growth_1y(insider_shares_held: pd.Series) -> pd.Series:
    """Absolute growth in insider_shares_held over 252 days."""
    return insider_shares_held - insider_shares_held.shift(_TD_YEAR)


def icn_045_held_shares_pct_growth_mo(insider_shares_held: pd.Series) -> pd.Series:
    """Percent growth in insider_shares_held over 21 days."""
    prior = insider_shares_held.shift(_TD_MO)
    return _safe_div(insider_shares_held - prior, prior)


def icn_046_held_shares_pct_growth_qtr(insider_shares_held: pd.Series) -> pd.Series:
    """Percent growth in insider_shares_held over 63 days."""
    prior = insider_shares_held.shift(_TD_QTR)
    return _safe_div(insider_shares_held - prior, prior)


def icn_047_held_shares_pct_growth_1y(insider_shares_held: pd.Series) -> pd.Series:
    """Percent growth in insider_shares_held over 252 days."""
    prior = insider_shares_held.shift(_TD_YEAR)
    return _safe_div(insider_shares_held - prior, prior)


def icn_048_held_above_mo_avg(insider_shares_held: pd.Series) -> pd.Series:
    """insider_shares_held minus its 21-day rolling mean — deviation from short-term trend."""
    return insider_shares_held - _rolling_mean(insider_shares_held, _TD_MO)


def icn_049_held_above_qtr_avg(insider_shares_held: pd.Series) -> pd.Series:
    """insider_shares_held minus its 63-day rolling mean."""
    return insider_shares_held - _rolling_mean(insider_shares_held, _TD_QTR)


def icn_050_held_shares_expanding_max_ratio(insider_shares_held: pd.Series) -> pd.Series:
    """insider_shares_held divided by its all-history expanding max — near-peak buying."""
    exp_max = insider_shares_held.expanding(min_periods=1).max()
    return _safe_div(insider_shares_held, exp_max)


def icn_051_held_shares_at_1y_high_flag(insider_shares_held: pd.Series) -> pd.Series:
    """Flag: 1 if insider_shares_held equals its 252-day rolling maximum (accumulation high)."""
    max_1y = _rolling_max(insider_shares_held, _TD_YEAR)
    return (insider_shares_held >= max_1y - _EPS).astype(float)


def icn_052_held_shares_consecutive_gains(insider_shares_held: pd.Series) -> pd.Series:
    """Count of consecutive days insider_shares_held has been rising (buying streak length)."""
    gain = (insider_shares_held.diff(1) > 0).astype(int)
    streak = np.zeros(len(gain), dtype=float)
    arr = gain.values
    for i in range(1, len(arr)):
        streak[i] = (streak[i - 1] + 1) * arr[i]
    return pd.Series(streak, index=insider_shares_held.index)


def icn_053_held_shares_fraction_above_1y_avg(insider_shares_held: pd.Series) -> pd.Series:
    """Fraction of the past 252 days insider_shares_held was above its 252-day mean."""
    avg = _rolling_mean(insider_shares_held, _TD_YEAR)
    above = (insider_shares_held > avg).astype(float)
    return _rolling_mean(above, _TD_YEAR)


def icn_054_held_shares_acceleration_qtr(insider_shares_held: pd.Series) -> pd.Series:
    """Second difference of insider_shares_held over 63-day steps — acceleration of accumulation."""
    d1 = insider_shares_held - insider_shares_held.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def icn_055_held_shares_vs_2y_peak_ratio(insider_shares_held: pd.Series) -> pd.Series:
    """insider_shares_held divided by its 2-year rolling maximum."""
    max_2y = _rolling_max(insider_shares_held, _TD_2Y)
    return _safe_div(insider_shares_held, max_2y)


# --- Group E (056-065): First-time and stake-building buys vs marginal top-ups ---

def icn_056_first_buy_after_gap_flag(insider_buy_shares: pd.Series) -> pd.Series:
    """Flag: 1 on days with nonzero buy_shares preceded by 63+ days of zero buying.
    Captures resumption of buying after a long pause — potential first-time conviction signal."""
    has_buy = (insider_buy_shares > 0).astype(float)
    prior_sum = _rolling_sum(insider_buy_shares, _TD_QTR).shift(1)
    return (has_buy * (prior_sum <= 0)).astype(float)


def icn_057_buy_after_no_buy_21d_flag(insider_buy_shares: pd.Series) -> pd.Series:
    """Flag: 1 on buy days preceded by at least 21 days of zero buying."""
    has_buy = (insider_buy_shares > 0).astype(float)
    prior_sum = _rolling_sum(insider_buy_shares, _TD_MO).shift(1)
    return (has_buy * (prior_sum <= 0)).astype(float)


def icn_058_stake_building_ratio_qtr(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Quarterly buy_shares / held ratio ONLY on days with active buying.
    Returns NaN on no-buy days — isolates the conviction magnitude of actual purchase events."""
    buys = _rolling_sum(insider_buy_shares, _TD_QTR)
    ratio = _safe_div(buys, insider_shares_held)
    active = (buys > 0).astype(float)
    return ratio.where(active > 0, other=np.nan)


def icn_059_marginal_topup_flag(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Flag: 1 if monthly buy_shares < 1% of insider_shares_held (token / marginal buy)."""
    ratio = _safe_div(_rolling_sum(insider_buy_shares, _TD_MO), insider_shares_held)
    return ((ratio > 0) & (ratio < 0.01)).astype(float)


def icn_060_high_conviction_buy_flag(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Flag: 1 if monthly buy_shares > 5% of held AND insider_shares_held is rising."""
    ratio = _safe_div(_rolling_sum(insider_buy_shares, _TD_MO), insider_shares_held)
    held_rising = (insider_shares_held.diff(1) > 0).astype(float)
    return ((ratio >= 0.05) & (held_rising > 0)).astype(float)


def icn_061_stake_build_frequency_1y(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Count of months in the past year where buy_shares >= 5% of held.
    Measures how persistently insiders are building their stake."""
    ratio_mo = _safe_div(_rolling_sum(insider_buy_shares, _TD_MO), insider_shares_held)
    flag = (ratio_mo >= 0.05).astype(float)
    return _rolling_sum(flag, _TD_YEAR)


def icn_062_stake_build_frequency_2y(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Count of months in the past 2 years where buy_shares >= 5% of held."""
    ratio_mo = _safe_div(_rolling_sum(insider_buy_shares, _TD_MO), insider_shares_held)
    flag = (ratio_mo >= 0.05).astype(float)
    return _rolling_sum(flag, _TD_2Y)


def icn_063_consecutive_conviction_months(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Streak length of consecutive months with buy_shares >= 5% of held (daily resolution).
    Resets when conviction drops below threshold."""
    ratio_mo = _safe_div(_rolling_sum(insider_buy_shares, _TD_MO), insider_shares_held)
    flag = (ratio_mo >= 0.05).astype(int)
    streak = np.zeros(len(flag), dtype=float)
    arr = flag.values
    for i in range(1, len(arr)):
        streak[i] = (streak[i - 1] + 1) * arr[i]
    return pd.Series(streak, index=insider_buy_shares.index)


def icn_064_tenpct_holder_conviction_qtr(tenpct_buy_value: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """10%-holder quarterly buy value scaled by insider_shares_held."""
    buys = _rolling_sum(tenpct_buy_value, _TD_QTR)
    return _safe_div(buys, insider_shares_held)


def icn_065_ceo_cfo_combined_conviction_qtr(ceo_buy_value: pd.Series, cfo_buy_value: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Combined CEO + CFO quarterly buy value scaled by insider_shares_held.
    Joint executive conviction is a particularly strong signal."""
    combined = _rolling_sum(ceo_buy_value + cfo_buy_value, _TD_QTR)
    return _safe_div(combined, insider_shares_held)


# --- Group F (066-075): Conviction intensity over trailing windows / composite ---

def icn_066_buy_conviction_zscore_1y(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Z-score of monthly (buy_shares/held) ratio within trailing 1-year window."""
    ratio = _safe_div(_rolling_sum(insider_buy_shares, _TD_MO), insider_shares_held)
    return _zscore_rolling(ratio, _TD_YEAR)


def icn_067_buy_conviction_zscore_2y(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Z-score of monthly (buy_shares/held) ratio within trailing 2-year window."""
    ratio = _safe_div(_rolling_sum(insider_buy_shares, _TD_MO), insider_shares_held)
    return _zscore_rolling(ratio, _TD_2Y)


def icn_068_buy_conviction_pct_rank_1y(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Percentile rank of monthly (buy_shares/held) ratio within trailing 1-year window."""
    ratio = _safe_div(_rolling_sum(insider_buy_shares, _TD_MO), insider_shares_held)
    return _rolling_rank_pct(ratio, _TD_YEAR)


def icn_069_buy_value_conviction_zscore_1y(insider_buy_value: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Z-score of monthly (buy_value/held) ratio within trailing 1-year window."""
    ratio = _safe_div(_rolling_sum(insider_buy_value, _TD_MO), insider_shares_held)
    return _zscore_rolling(ratio, _TD_YEAR)


def icn_070_held_growth_qtr_zscore_1y(insider_shares_held: pd.Series) -> pd.Series:
    """Z-score of quarterly held_shares growth within a trailing 1-year window."""
    growth = insider_shares_held - insider_shares_held.shift(_TD_QTR)
    return _zscore_rolling(growth, _TD_YEAR)


def icn_071_net_buy_conviction_ewm_mo(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """EWM (span=21) of monthly net-buy conviction ratio (net_buy/held).
    Smooths the sparse event-driven signal into a continuous level."""
    net = _rolling_sum(insider_buy_shares, _TD_MO) - _rolling_sum(insider_sell_shares, _TD_MO)
    ratio = _safe_div(net, insider_shares_held)
    return _ewm_mean(ratio, _TD_MO)


def icn_072_net_buy_conviction_ewm_qtr(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """EWM (span=63) of quarterly net-buy conviction ratio."""
    net = _rolling_sum(insider_buy_shares, _TD_QTR) - _rolling_sum(insider_sell_shares, _TD_QTR)
    ratio = _safe_div(net, insider_shares_held)
    return _ewm_mean(ratio, _TD_QTR)


def icn_073_conviction_momentum_qtr_vs_1y(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Quarterly buy conviction ratio minus annual buy conviction ratio.
    Positive = recent conviction is higher than long-run average."""
    ratio_qtr = _safe_div(_rolling_sum(insider_buy_shares, _TD_QTR), insider_shares_held)
    ratio_1y  = _safe_div(_rolling_sum(insider_buy_shares, _TD_YEAR), insider_shares_held)
    return ratio_qtr - ratio_1y


def icn_074_composite_conviction_score(insider_buy_shares: pd.Series, insider_shares_held: pd.Series, insider_buy_count: pd.Series, officer_buy_value: pd.Series) -> pd.Series:
    """Composite insider conviction score combining four signals:
    1) buy_shares/held (quarterly), 2) held percent growth (quarterly),
    3) buy frequency, 4) officer participation scaled to held.
    Each sub-signal is z-scored then averaged."""
    z1 = _zscore_rolling(_safe_div(_rolling_sum(insider_buy_shares, _TD_QTR), insider_shares_held), _TD_YEAR)
    z2 = _zscore_rolling(insider_shares_held - insider_shares_held.shift(_TD_QTR), _TD_YEAR)
    z3 = _zscore_rolling(_rolling_sum(insider_buy_count, _TD_QTR), _TD_YEAR)
    z4 = _zscore_rolling(_safe_div(_rolling_sum(officer_buy_value, _TD_QTR), insider_shares_held), _TD_YEAR)
    count_valid = z1.notna().astype(float) + z2.notna().astype(float) + z3.notna().astype(float) + z4.notna().astype(float)
    total = z1.fillna(0) + z2.fillna(0) + z3.fillna(0) + z4.fillna(0)
    return _safe_div(total, count_valid)


def icn_075_conviction_persistence_score(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Conviction persistence: sum of monthly conviction flags (buy >= 5% of held) over 2 years,
    normalized by 24 (months in 2 years), giving a 0-1 persistence ratio."""
    ratio_mo = _safe_div(_rolling_sum(insider_buy_shares, _TD_MO), insider_shares_held)
    flag = (ratio_mo >= 0.05).astype(float)
    return _rolling_sum(flag, _TD_2Y) / 24.0


# --- Group G (076-100 in this file, numbered 151-175 globally): New conviction features ---

def icn_151_buy_value_per_buy_event_mo(insider_buy_value: pd.Series, insider_buy_count: pd.Series) -> pd.Series:
    """Average dollar value per buy transaction over 21 days — per-event deal size."""
    val = _rolling_sum(insider_buy_value, _TD_MO)
    cnt = _rolling_sum(insider_buy_count, _TD_MO).replace(0, np.nan)
    return val / cnt


def icn_152_buy_value_per_buy_event_qtr(insider_buy_value: pd.Series, insider_buy_count: pd.Series) -> pd.Series:
    """Average dollar value per buy transaction over 63 days."""
    val = _rolling_sum(insider_buy_value, _TD_QTR)
    cnt = _rolling_sum(insider_buy_count, _TD_QTR).replace(0, np.nan)
    return val / cnt


def icn_153_sell_value_per_sell_event_mo(insider_sell_value: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Average dollar value per sell transaction over 21 days — per-event deal size on exit."""
    val = _rolling_sum(insider_sell_value, _TD_MO)
    cnt = _rolling_sum(insider_sell_count, _TD_MO).replace(0, np.nan)
    return val / cnt


def icn_154_buy_to_sell_event_size_ratio_mo(insider_buy_value: pd.Series, insider_buy_count: pd.Series, insider_sell_value: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Ratio of average buy-event size to average sell-event size over 21 days.
    High values imply each purchase is larger than each sale — quality conviction."""
    avg_buy  = _safe_div(_rolling_sum(insider_buy_value, _TD_MO), _rolling_sum(insider_buy_count, _TD_MO).replace(0, np.nan))
    avg_sell = _safe_div(_rolling_sum(insider_sell_value, _TD_MO), _rolling_sum(insider_sell_count, _TD_MO).replace(0, np.nan))
    return _safe_div(avg_buy, avg_sell)


def icn_155_officer_buy_count_per_buyer_mo(officer_buy_count: pd.Series, insider_buyers: pd.Series) -> pd.Series:
    """Monthly officer buy transaction count divided by distinct buyers — officer buying frequency."""
    cnt = _rolling_sum(officer_buy_count, _TD_MO)
    buyers = _rolling_sum(insider_buyers, _TD_MO).replace(0, np.nan)
    return cnt / buyers


def icn_156_director_buy_count_mo(director_buy_count: pd.Series) -> pd.Series:
    """Rolling 21-day sum of director buy transaction count — director activity frequency."""
    return _rolling_sum(director_buy_count, _TD_MO)


def icn_157_director_buy_count_qtr(director_buy_count: pd.Series) -> pd.Series:
    """Rolling 63-day sum of director buy transaction count."""
    return _rolling_sum(director_buy_count, _TD_QTR)


def icn_158_tenpct_buy_count_mo(tenpct_buy_count: pd.Series) -> pd.Series:
    """Rolling 21-day sum of 10%-holder buy transaction count."""
    return _rolling_sum(tenpct_buy_count, _TD_MO)


def icn_159_buy_count_per_buyer_ratio_qtr(insider_buy_count: pd.Series, insider_buyers: pd.Series) -> pd.Series:
    """Quarterly buy transaction count divided by distinct buyers — average repeat-buy frequency."""
    cnt = _rolling_sum(insider_buy_count, _TD_QTR)
    buyers = _rolling_sum(insider_buyers, _TD_QTR).replace(0, np.nan)
    return cnt / buyers


def icn_160_sell_count_per_seller_ratio_qtr(insider_sell_count: pd.Series, insider_sellers: pd.Series) -> pd.Series:
    """Quarterly sell transaction count divided by distinct sellers — seller activity rate."""
    cnt = _rolling_sum(insider_sell_count, _TD_QTR)
    sellers = _rolling_sum(insider_sellers, _TD_QTR).replace(0, np.nan)
    return cnt / sellers


def icn_161_buyers_minus_sellers_mo(insider_buyers: pd.Series, insider_sellers: pd.Series) -> pd.Series:
    """Monthly (distinct buyers - distinct sellers) — net headcount conviction."""
    return _rolling_sum(insider_buyers, _TD_MO) - _rolling_sum(insider_sellers, _TD_MO)


def icn_162_buyers_minus_sellers_qtr(insider_buyers: pd.Series, insider_sellers: pd.Series) -> pd.Series:
    """Quarterly (distinct buyers - distinct sellers)."""
    return _rolling_sum(insider_buyers, _TD_QTR) - _rolling_sum(insider_sellers, _TD_QTR)


def icn_163_buyer_fraction_of_all_insiders_mo(insider_buyers: pd.Series, insider_sellers: pd.Series) -> pd.Series:
    """Monthly buyers / (buyers + sellers) — fraction of active insiders who are buying."""
    b = _rolling_sum(insider_buyers, _TD_MO)
    s = _rolling_sum(insider_sellers, _TD_MO)
    return _safe_div(b, b + s)


def icn_164_ceo_buy_value_mo(ceo_buy_value: pd.Series) -> pd.Series:
    """Rolling 21-day sum of CEO buy value — raw CEO activity level."""
    return _rolling_sum(ceo_buy_value, _TD_MO)


def icn_165_cfo_buy_value_mo(cfo_buy_value: pd.Series) -> pd.Series:
    """Rolling 21-day sum of CFO buy value — raw CFO activity level."""
    return _rolling_sum(cfo_buy_value, _TD_MO)


def icn_166_ceo_to_total_buy_value_ratio_mo(ceo_buy_value: pd.Series, insider_buy_value: pd.Series) -> pd.Series:
    """CEO monthly buy value as share of total insider monthly buy value — CEO dominance."""
    return _safe_div(_rolling_sum(ceo_buy_value, _TD_MO), _rolling_sum(insider_buy_value, _TD_MO))


def icn_167_cfo_to_total_buy_value_ratio_mo(cfo_buy_value: pd.Series, insider_buy_value: pd.Series) -> pd.Series:
    """CFO monthly buy value as share of total insider monthly buy value."""
    return _safe_div(_rolling_sum(cfo_buy_value, _TD_MO), _rolling_sum(insider_buy_value, _TD_MO))


def icn_168_director_to_officer_buy_ratio_qtr(director_buy_value: pd.Series, officer_buy_value: pd.Series) -> pd.Series:
    """Quarterly director buy value divided by officer buy value — board vs. management buying."""
    return _safe_div(_rolling_sum(director_buy_value, _TD_QTR), _rolling_sum(officer_buy_value, _TD_QTR))


def icn_169_tenpct_to_total_buy_value_ratio_qtr(tenpct_buy_value: pd.Series, insider_buy_value: pd.Series) -> pd.Series:
    """10%-holder quarterly buy value as share of total insider quarterly buy value."""
    return _safe_div(_rolling_sum(tenpct_buy_value, _TD_QTR), _rolling_sum(insider_buy_value, _TD_QTR))


def icn_170_net_buy_value_mo(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """Rolling 21-day net (buy_value - sell_value) in dollars — absolute net commitment flow."""
    return _rolling_sum(insider_buy_value, _TD_MO) - _rolling_sum(insider_sell_value, _TD_MO)


def icn_171_net_buy_value_qtr(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """Rolling 63-day net (buy_value - sell_value) in dollars."""
    return _rolling_sum(insider_buy_value, _TD_QTR) - _rolling_sum(insider_sell_value, _TD_QTR)


def icn_172_net_buy_value_halfyr(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """Rolling 126-day net (buy_value - sell_value) in dollars."""
    return _rolling_sum(insider_buy_value, _TD_HALF) - _rolling_sum(insider_sell_value, _TD_HALF)


def icn_173_buy_value_zscore_1y(insider_buy_value: pd.Series) -> pd.Series:
    """Z-score of monthly insider buy value within trailing 1-year window."""
    return _zscore_rolling(_rolling_sum(insider_buy_value, _TD_MO), _TD_YEAR)


def icn_174_officer_sell_value_pct_held_qtr(officer_sell_value: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Quarterly officer sell value scaled by insider_shares_held — officer liquidation intensity."""
    sells = _rolling_sum(officer_sell_value, _TD_QTR)
    return _safe_div(sells, insider_shares_held)


def icn_175_net_officer_conviction_mo(officer_buy_value: pd.Series, officer_sell_value: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Monthly net (officer_buy_value - officer_sell_value) / insider_shares_held."""
    net = _rolling_sum(officer_buy_value, _TD_MO) - _rolling_sum(officer_sell_value, _TD_MO)
    return _safe_div(net, insider_shares_held)


# ── Registry 001-075 ──────────────────────────────────────────────────────────

INSIDER_CONVICTION_REGISTRY_001_075 = {
    "icn_001_buy_shares_pct_of_held_mo":           {"inputs": ["insider_buy_shares", "insider_shares_held"],                                         "func": icn_001_buy_shares_pct_of_held_mo},
    "icn_002_buy_shares_pct_of_held_qtr":          {"inputs": ["insider_buy_shares", "insider_shares_held"],                                         "func": icn_002_buy_shares_pct_of_held_qtr},
    "icn_003_buy_shares_pct_of_held_halfyr":       {"inputs": ["insider_buy_shares", "insider_shares_held"],                                         "func": icn_003_buy_shares_pct_of_held_halfyr},
    "icn_004_buy_shares_pct_of_held_1y":           {"inputs": ["insider_buy_shares", "insider_shares_held"],                                         "func": icn_004_buy_shares_pct_of_held_1y},
    "icn_005_buy_shares_pct_of_held_wk":           {"inputs": ["insider_buy_shares", "insider_shares_held"],                                         "func": icn_005_buy_shares_pct_of_held_wk},
    "icn_006_buy_value_pct_of_held_value_mo":      {"inputs": ["insider_buy_value", "insider_shares_held"],                                          "func": icn_006_buy_value_pct_of_held_value_mo},
    "icn_007_buy_value_pct_of_held_value_qtr":     {"inputs": ["insider_buy_value", "insider_shares_held"],                                          "func": icn_007_buy_value_pct_of_held_value_qtr},
    "icn_008_buy_value_pct_of_held_value_1y":      {"inputs": ["insider_buy_value", "insider_shares_held"],                                          "func": icn_008_buy_value_pct_of_held_value_1y},
    "icn_009_buy_shares_prior_stake_lagged_mo":    {"inputs": ["insider_buy_shares", "insider_shares_held"],                                         "func": icn_009_buy_shares_prior_stake_lagged_mo},
    "icn_010_buy_shares_prior_stake_lagged_qtr":   {"inputs": ["insider_buy_shares", "insider_shares_held"],                                         "func": icn_010_buy_shares_prior_stake_lagged_qtr},
    "icn_011_officer_buy_value_pct_of_held_mo":    {"inputs": ["officer_buy_value", "insider_shares_held"],                                          "func": icn_011_officer_buy_value_pct_of_held_mo},
    "icn_012_officer_buy_value_pct_of_held_qtr":   {"inputs": ["officer_buy_value", "insider_shares_held"],                                          "func": icn_012_officer_buy_value_pct_of_held_qtr},
    "icn_013_director_buy_value_pct_of_held_mo":   {"inputs": ["director_buy_value", "insider_shares_held"],                                         "func": icn_013_director_buy_value_pct_of_held_mo},
    "icn_014_director_buy_value_pct_of_held_qtr":  {"inputs": ["director_buy_value", "insider_shares_held"],                                         "func": icn_014_director_buy_value_pct_of_held_qtr},
    "icn_015_ceo_buy_value_pct_of_held_mo":        {"inputs": ["ceo_buy_value", "insider_shares_held"],                                              "func": icn_015_ceo_buy_value_pct_of_held_mo},
    "icn_016_flag_buy_adds_5pct_mo":               {"inputs": ["insider_buy_shares", "insider_shares_held"],                                         "func": icn_016_flag_buy_adds_5pct_mo},
    "icn_017_flag_buy_adds_10pct_mo":              {"inputs": ["insider_buy_shares", "insider_shares_held"],                                         "func": icn_017_flag_buy_adds_10pct_mo},
    "icn_018_flag_buy_adds_25pct_mo":              {"inputs": ["insider_buy_shares", "insider_shares_held"],                                         "func": icn_018_flag_buy_adds_25pct_mo},
    "icn_019_flag_buy_adds_5pct_qtr":              {"inputs": ["insider_buy_shares", "insider_shares_held"],                                         "func": icn_019_flag_buy_adds_5pct_qtr},
    "icn_020_flag_buy_adds_10pct_qtr":             {"inputs": ["insider_buy_shares", "insider_shares_held"],                                         "func": icn_020_flag_buy_adds_10pct_qtr},
    "icn_021_flag_buy_adds_25pct_qtr":             {"inputs": ["insider_buy_shares", "insider_shares_held"],                                         "func": icn_021_flag_buy_adds_25pct_qtr},
    "icn_022_flag_buy_adds_50pct_1y":              {"inputs": ["insider_buy_shares", "insider_shares_held"],                                         "func": icn_022_flag_buy_adds_50pct_1y},
    "icn_023_flag_officer_buy_adds_5pct_mo":       {"inputs": ["officer_buy_value", "insider_shares_held"],                                          "func": icn_023_flag_officer_buy_adds_5pct_mo},
    "icn_024_conviction_flag_any_5pct_1y":         {"inputs": ["insider_buy_shares", "insider_shares_held"],                                         "func": icn_024_conviction_flag_any_5pct_1y},
    "icn_025_conviction_flag_any_10pct_1y":        {"inputs": ["insider_buy_shares", "insider_shares_held"],                                         "func": icn_025_conviction_flag_any_10pct_1y},
    "icn_026_conviction_score_mo":                 {"inputs": ["insider_buy_shares", "insider_shares_held", "insider_buy_count"],                    "func": icn_026_conviction_score_mo},
    "icn_027_conviction_score_qtr":                {"inputs": ["insider_buy_shares", "insider_shares_held", "insider_buy_count"],                    "func": icn_027_conviction_score_qtr},
    "icn_028_conviction_intensity_mo":             {"inputs": ["insider_buy_value", "insider_shares_held", "insider_buy_count"],                     "func": icn_028_conviction_intensity_mo},
    "icn_029_conviction_intensity_qtr":            {"inputs": ["insider_buy_value", "insider_shares_held", "insider_buy_count"],                     "func": icn_029_conviction_intensity_qtr},
    "icn_030_officer_conviction_ratio_qtr":        {"inputs": ["officer_buy_value", "insider_buy_value"],                                            "func": icn_030_officer_conviction_ratio_qtr},
    "icn_031_cfo_buy_value_pct_of_held_qtr":       {"inputs": ["cfo_buy_value", "insider_shares_held"],                                              "func": icn_031_cfo_buy_value_pct_of_held_qtr},
    "icn_032_tenpct_buy_value_pct_of_held_qtr":    {"inputs": ["tenpct_buy_value", "insider_shares_held"],                                           "func": icn_032_tenpct_buy_value_pct_of_held_qtr},
    "icn_033_net_buy_shares_pct_held_mo":          {"inputs": ["insider_buy_shares", "insider_sell_shares", "insider_shares_held"],                  "func": icn_033_net_buy_shares_pct_held_mo},
    "icn_034_net_buy_shares_pct_held_qtr":         {"inputs": ["insider_buy_shares", "insider_sell_shares", "insider_shares_held"],                  "func": icn_034_net_buy_shares_pct_held_qtr},
    "icn_035_net_buy_shares_pct_held_1y":          {"inputs": ["insider_buy_shares", "insider_sell_shares", "insider_shares_held"],                  "func": icn_035_net_buy_shares_pct_held_1y},
    "icn_036_buy_to_sell_ratio_pct_held":          {"inputs": ["insider_buy_shares", "insider_sell_shares", "insider_shares_held"],                  "func": icn_036_buy_to_sell_ratio_pct_held},
    "icn_037_conviction_weighted_by_buyers_mo":    {"inputs": ["insider_buy_shares", "insider_shares_held", "insider_buyers"],                      "func": icn_037_conviction_weighted_by_buyers_mo},
    "icn_038_conviction_weighted_by_buyers_qtr":   {"inputs": ["insider_buy_shares", "insider_shares_held", "insider_buyers"],                      "func": icn_038_conviction_weighted_by_buyers_qtr},
    "icn_039_avg_conviction_per_buyer_mo":         {"inputs": ["insider_buy_shares", "insider_shares_held", "insider_buyers"],                      "func": icn_039_avg_conviction_per_buyer_mo},
    "icn_040_avg_conviction_per_buyer_qtr":        {"inputs": ["insider_buy_shares", "insider_shares_held", "insider_buyers"],                      "func": icn_040_avg_conviction_per_buyer_qtr},
    "icn_041_held_shares_growth_mo":               {"inputs": ["insider_shares_held"],                                                               "func": icn_041_held_shares_growth_mo},
    "icn_042_held_shares_growth_qtr":              {"inputs": ["insider_shares_held"],                                                               "func": icn_042_held_shares_growth_qtr},
    "icn_043_held_shares_growth_halfyr":           {"inputs": ["insider_shares_held"],                                                               "func": icn_043_held_shares_growth_halfyr},
    "icn_044_held_shares_growth_1y":               {"inputs": ["insider_shares_held"],                                                               "func": icn_044_held_shares_growth_1y},
    "icn_045_held_shares_pct_growth_mo":           {"inputs": ["insider_shares_held"],                                                               "func": icn_045_held_shares_pct_growth_mo},
    "icn_046_held_shares_pct_growth_qtr":          {"inputs": ["insider_shares_held"],                                                               "func": icn_046_held_shares_pct_growth_qtr},
    "icn_047_held_shares_pct_growth_1y":           {"inputs": ["insider_shares_held"],                                                               "func": icn_047_held_shares_pct_growth_1y},
    "icn_048_held_above_mo_avg":                   {"inputs": ["insider_shares_held"],                                                               "func": icn_048_held_above_mo_avg},
    "icn_049_held_above_qtr_avg":                  {"inputs": ["insider_shares_held"],                                                               "func": icn_049_held_above_qtr_avg},
    "icn_050_held_shares_expanding_max_ratio":     {"inputs": ["insider_shares_held"],                                                               "func": icn_050_held_shares_expanding_max_ratio},
    "icn_051_held_shares_at_1y_high_flag":         {"inputs": ["insider_shares_held"],                                                               "func": icn_051_held_shares_at_1y_high_flag},
    "icn_052_held_shares_consecutive_gains":       {"inputs": ["insider_shares_held"],                                                               "func": icn_052_held_shares_consecutive_gains},
    "icn_053_held_shares_fraction_above_1y_avg":   {"inputs": ["insider_shares_held"],                                                               "func": icn_053_held_shares_fraction_above_1y_avg},
    "icn_054_held_shares_acceleration_qtr":        {"inputs": ["insider_shares_held"],                                                               "func": icn_054_held_shares_acceleration_qtr},
    "icn_055_held_shares_vs_2y_peak_ratio":        {"inputs": ["insider_shares_held"],                                                               "func": icn_055_held_shares_vs_2y_peak_ratio},
    "icn_056_first_buy_after_gap_flag":            {"inputs": ["insider_buy_shares"],                                                                "func": icn_056_first_buy_after_gap_flag},
    "icn_057_buy_after_no_buy_21d_flag":           {"inputs": ["insider_buy_shares"],                                                                "func": icn_057_buy_after_no_buy_21d_flag},
    "icn_058_stake_building_ratio_qtr":            {"inputs": ["insider_buy_shares", "insider_shares_held"],                                         "func": icn_058_stake_building_ratio_qtr},
    "icn_059_marginal_topup_flag":                 {"inputs": ["insider_buy_shares", "insider_shares_held"],                                         "func": icn_059_marginal_topup_flag},
    "icn_060_high_conviction_buy_flag":            {"inputs": ["insider_buy_shares", "insider_shares_held"],                                         "func": icn_060_high_conviction_buy_flag},
    "icn_061_stake_build_frequency_1y":            {"inputs": ["insider_buy_shares", "insider_shares_held"],                                         "func": icn_061_stake_build_frequency_1y},
    "icn_062_stake_build_frequency_2y":            {"inputs": ["insider_buy_shares", "insider_shares_held"],                                         "func": icn_062_stake_build_frequency_2y},
    "icn_063_consecutive_conviction_months":       {"inputs": ["insider_buy_shares", "insider_shares_held"],                                         "func": icn_063_consecutive_conviction_months},
    "icn_064_tenpct_holder_conviction_qtr":        {"inputs": ["tenpct_buy_value", "insider_shares_held"],                                           "func": icn_064_tenpct_holder_conviction_qtr},
    "icn_065_ceo_cfo_combined_conviction_qtr":     {"inputs": ["ceo_buy_value", "cfo_buy_value", "insider_shares_held"],                             "func": icn_065_ceo_cfo_combined_conviction_qtr},
    "icn_066_buy_conviction_zscore_1y":            {"inputs": ["insider_buy_shares", "insider_shares_held"],                                         "func": icn_066_buy_conviction_zscore_1y},
    "icn_067_buy_conviction_zscore_2y":            {"inputs": ["insider_buy_shares", "insider_shares_held"],                                         "func": icn_067_buy_conviction_zscore_2y},
    "icn_068_buy_conviction_pct_rank_1y":          {"inputs": ["insider_buy_shares", "insider_shares_held"],                                         "func": icn_068_buy_conviction_pct_rank_1y},
    "icn_069_buy_value_conviction_zscore_1y":      {"inputs": ["insider_buy_value", "insider_shares_held"],                                          "func": icn_069_buy_value_conviction_zscore_1y},
    "icn_070_held_growth_qtr_zscore_1y":           {"inputs": ["insider_shares_held"],                                                               "func": icn_070_held_growth_qtr_zscore_1y},
    "icn_071_net_buy_conviction_ewm_mo":           {"inputs": ["insider_buy_shares", "insider_sell_shares", "insider_shares_held"],                  "func": icn_071_net_buy_conviction_ewm_mo},
    "icn_072_net_buy_conviction_ewm_qtr":          {"inputs": ["insider_buy_shares", "insider_sell_shares", "insider_shares_held"],                  "func": icn_072_net_buy_conviction_ewm_qtr},
    "icn_073_conviction_momentum_qtr_vs_1y":       {"inputs": ["insider_buy_shares", "insider_shares_held"],                                         "func": icn_073_conviction_momentum_qtr_vs_1y},
    "icn_074_composite_conviction_score":          {"inputs": ["insider_buy_shares", "insider_shares_held", "insider_buy_count", "officer_buy_value"], "func": icn_074_composite_conviction_score},
    "icn_075_conviction_persistence_score":        {"inputs": ["insider_buy_shares", "insider_shares_held"],                                                              "func": icn_075_conviction_persistence_score},
    "icn_151_buy_value_per_buy_event_mo":          {"inputs": ["insider_buy_value", "insider_buy_count"],                                                                  "func": icn_151_buy_value_per_buy_event_mo},
    "icn_152_buy_value_per_buy_event_qtr":         {"inputs": ["insider_buy_value", "insider_buy_count"],                                                                  "func": icn_152_buy_value_per_buy_event_qtr},
    "icn_153_sell_value_per_sell_event_mo":        {"inputs": ["insider_sell_value", "insider_sell_count"],                                                                "func": icn_153_sell_value_per_sell_event_mo},
    "icn_154_buy_to_sell_event_size_ratio_mo":     {"inputs": ["insider_buy_value", "insider_buy_count", "insider_sell_value", "insider_sell_count"],                      "func": icn_154_buy_to_sell_event_size_ratio_mo},
    "icn_155_officer_buy_count_per_buyer_mo":      {"inputs": ["officer_buy_count", "insider_buyers"],                                                                     "func": icn_155_officer_buy_count_per_buyer_mo},
    "icn_156_director_buy_count_mo":               {"inputs": ["director_buy_count"],                                                                                      "func": icn_156_director_buy_count_mo},
    "icn_157_director_buy_count_qtr":              {"inputs": ["director_buy_count"],                                                                                      "func": icn_157_director_buy_count_qtr},
    "icn_158_tenpct_buy_count_mo":                 {"inputs": ["tenpct_buy_count"],                                                                                        "func": icn_158_tenpct_buy_count_mo},
    "icn_159_buy_count_per_buyer_ratio_qtr":       {"inputs": ["insider_buy_count", "insider_buyers"],                                                                     "func": icn_159_buy_count_per_buyer_ratio_qtr},
    "icn_160_sell_count_per_seller_ratio_qtr":     {"inputs": ["insider_sell_count", "insider_sellers"],                                                                   "func": icn_160_sell_count_per_seller_ratio_qtr},
    "icn_161_buyers_minus_sellers_mo":             {"inputs": ["insider_buyers", "insider_sellers"],                                                                       "func": icn_161_buyers_minus_sellers_mo},
    "icn_162_buyers_minus_sellers_qtr":            {"inputs": ["insider_buyers", "insider_sellers"],                                                                       "func": icn_162_buyers_minus_sellers_qtr},
    "icn_163_buyer_fraction_of_all_insiders_mo":   {"inputs": ["insider_buyers", "insider_sellers"],                                                                       "func": icn_163_buyer_fraction_of_all_insiders_mo},
    "icn_164_ceo_buy_value_mo":                    {"inputs": ["ceo_buy_value"],                                                                                           "func": icn_164_ceo_buy_value_mo},
    "icn_165_cfo_buy_value_mo":                    {"inputs": ["cfo_buy_value"],                                                                                           "func": icn_165_cfo_buy_value_mo},
    "icn_166_ceo_to_total_buy_value_ratio_mo":     {"inputs": ["ceo_buy_value", "insider_buy_value"],                                                                      "func": icn_166_ceo_to_total_buy_value_ratio_mo},
    "icn_167_cfo_to_total_buy_value_ratio_mo":     {"inputs": ["cfo_buy_value", "insider_buy_value"],                                                                      "func": icn_167_cfo_to_total_buy_value_ratio_mo},
    "icn_168_director_to_officer_buy_ratio_qtr":   {"inputs": ["director_buy_value", "officer_buy_value"],                                                                 "func": icn_168_director_to_officer_buy_ratio_qtr},
    "icn_169_tenpct_to_total_buy_value_ratio_qtr": {"inputs": ["tenpct_buy_value", "insider_buy_value"],                                                                   "func": icn_169_tenpct_to_total_buy_value_ratio_qtr},
    "icn_170_net_buy_value_mo":                    {"inputs": ["insider_buy_value", "insider_sell_value"],                                                                 "func": icn_170_net_buy_value_mo},
    "icn_171_net_buy_value_qtr":                   {"inputs": ["insider_buy_value", "insider_sell_value"],                                                                 "func": icn_171_net_buy_value_qtr},
    "icn_172_net_buy_value_halfyr":                {"inputs": ["insider_buy_value", "insider_sell_value"],                                                                 "func": icn_172_net_buy_value_halfyr},
    "icn_173_buy_value_zscore_1y":                 {"inputs": ["insider_buy_value"],                                                                                       "func": icn_173_buy_value_zscore_1y},
    "icn_174_officer_sell_value_pct_held_qtr":     {"inputs": ["officer_sell_value", "insider_shares_held"],                                                               "func": icn_174_officer_sell_value_pct_held_qtr},
    "icn_175_net_officer_conviction_mo":           {"inputs": ["officer_buy_value", "officer_sell_value", "insider_shares_held"],                                          "func": icn_175_net_officer_conviction_mo},
}
