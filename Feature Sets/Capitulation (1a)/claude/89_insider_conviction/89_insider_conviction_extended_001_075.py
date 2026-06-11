"""
89_insider_conviction — Extended Features 001-075
Domain: insider conviction — purchase size relative to existing insider stake.
        Additional angles: dollar-conviction vs share-conviction, value-flow
        scaled by held, role-specific conviction depth, conviction streaks and
        decay, conviction vs sell pressure, percentile/EWM/composite variants
        not present in the base files.
Asset class: US equities | Sharadar SF2 insider transactions (daily-aggregated)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.

SF2 Daily-Aggregated Insider Series Contract
--------------------------------------------
FLOW series (insider_buy_shares, insider_sell_shares, insider_buy_value,
insider_sell_value, insider_buy_count, officer_buy_value, director_buy_value,
ceo_buy_value, cfo_buy_value, tenpct_buy_value, insider_buyers):
  EVENT-DRIVEN — most days ZERO, NOT forward-filled. Aggregate with trailing
  rolling SUMS over windows like 5/21/63/126/252 trading days.

STOCK series (insider_shares_held):
  CUMULATIVE total shares held by insiders. Persists/steps; treat as a LEVEL
  series. May be read directly or smoothed; do NOT sum it.

Trading-day calendar: 252/yr, 126/half-yr, 63/qtr, 21/mo, 5/wk, 504/2y.
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
    A buy when the prior stake is zero is undefined in conviction-ratio terms."""
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


def _streak_true(cond: pd.Series) -> pd.Series:
    """Count of consecutive trailing True values up to each row."""
    arr = cond.astype(int).values
    out = np.zeros(len(arr), dtype=float)
    for i in range(len(arr)):
        out[i] = (out[i - 1] + 1) * arr[i] if i > 0 else float(arr[i])
    return pd.Series(out, index=cond.index)


def _conviction_ratio(flow: pd.Series, held: pd.Series, w: int) -> pd.Series:
    """Rolling w-day sum of an event-driven flow series divided by the
    cumulative insider_shares_held LEVEL series — the core conviction ratio."""
    return _safe_div(_rolling_sum(flow, w), held)


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-012): Dollar-value conviction scaled by held (new windows) ---

def icn_ext_001_buy_value_conviction_wk(insider_buy_value: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Weekly (5-day) buy value scaled by insider_shares_held."""
    return _conviction_ratio(insider_buy_value, insider_shares_held, _TD_WK)


def icn_ext_002_buy_value_conviction_halfyr(insider_buy_value: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Half-year (126-day) buy value scaled by insider_shares_held."""
    return _conviction_ratio(insider_buy_value, insider_shares_held, _TD_HALF)


def icn_ext_003_buy_value_conviction_2y(insider_buy_value: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Two-year (504-day) buy value scaled by insider_shares_held."""
    return _conviction_ratio(insider_buy_value, insider_shares_held, _TD_2Y)


def icn_ext_004_buy_shares_conviction_2y(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Two-year (504-day) buy shares scaled by insider_shares_held."""
    return _conviction_ratio(insider_buy_shares, insider_shares_held, _TD_2Y)


def icn_ext_005_buy_value_conviction_42d(insider_buy_value: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Two-month (42-day) buy value scaled by insider_shares_held."""
    return _conviction_ratio(insider_buy_value, insider_shares_held, 42)


def icn_ext_006_buy_value_conviction_ewm_qtr(insider_buy_value: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """EWM(span=63) of the daily (buy_value/held) conviction ratio."""
    ratio = _safe_div(insider_buy_value, insider_shares_held)
    return _ewm_mean(ratio, _TD_QTR)


def icn_ext_007_buy_shares_conviction_ewm_mo(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """EWM(span=21) of the daily (buy_shares/held) conviction ratio."""
    ratio = _safe_div(insider_buy_shares, insider_shares_held)
    return _ewm_mean(ratio, _TD_MO)


def icn_ext_008_buy_value_conviction_prior_stake_halfyr(insider_buy_value: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Half-year buy value divided by insider_shares_held lagged one half-year."""
    return _safe_div(_rolling_sum(insider_buy_value, _TD_HALF), insider_shares_held.shift(_TD_HALF))


def icn_ext_009_buy_shares_conviction_prior_stake_halfyr(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Half-year buy shares divided by insider_shares_held lagged one half-year."""
    return _safe_div(_rolling_sum(insider_buy_shares, _TD_HALF), insider_shares_held.shift(_TD_HALF))


def icn_ext_010_buy_value_conviction_prior_stake_1y(insider_buy_value: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Annual buy value divided by insider_shares_held lagged one year."""
    return _safe_div(_rolling_sum(insider_buy_value, _TD_YEAR), insider_shares_held.shift(_TD_YEAR))


def icn_ext_011_buy_value_conviction_smoothed_qtr(insider_buy_value: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Quarterly buy value scaled by the 21-day smoothed insider_shares_held level."""
    return _safe_div(_rolling_sum(insider_buy_value, _TD_QTR), _rolling_mean(insider_shares_held, _TD_MO))


def icn_ext_012_buy_shares_conviction_smoothed_qtr(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Quarterly buy shares scaled by the 21-day smoothed insider_shares_held level."""
    return _safe_div(_rolling_sum(insider_buy_shares, _TD_QTR), _rolling_mean(insider_shares_held, _TD_MO))


# --- Group B (013-024): Conviction depth flags and thresholds (new levels) ---

def icn_ext_013_flag_buy_adds_1pct_mo(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Flag: 1 if monthly buy_shares >= 1% of insider_shares_held."""
    return (_conviction_ratio(insider_buy_shares, insider_shares_held, _TD_MO) >= 0.01).astype(float)


def icn_ext_014_flag_buy_adds_15pct_qtr(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Flag: 1 if quarterly buy_shares >= 15% of insider_shares_held."""
    return (_conviction_ratio(insider_buy_shares, insider_shares_held, _TD_QTR) >= 0.15).astype(float)


def icn_ext_015_flag_buy_adds_50pct_qtr(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Flag: 1 if quarterly buy_shares >= 50% of insider_shares_held (extreme conviction)."""
    return (_conviction_ratio(insider_buy_shares, insider_shares_held, _TD_QTR) >= 0.50).astype(float)


def icn_ext_016_flag_buy_adds_100pct_1y(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Flag: 1 if annual buy_shares >= 100% of insider_shares_held (stake more than doubled)."""
    return (_conviction_ratio(insider_buy_shares, insider_shares_held, _TD_YEAR) >= 1.00).astype(float)


def icn_ext_017_flag_buy_adds_10pct_halfyr(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Flag: 1 if half-year buy_shares >= 10% of insider_shares_held."""
    return (_conviction_ratio(insider_buy_shares, insider_shares_held, _TD_HALF) >= 0.10).astype(float)


def icn_ext_018_conviction_depth_bucket_qtr(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Ordinal conviction-depth bucket (0-4) from quarterly buy_shares/held thresholds
    at 1%, 5%, 15% and 50%."""
    r = _conviction_ratio(insider_buy_shares, insider_shares_held, _TD_QTR)
    bucket = (r >= 0.01).astype(float) + (r >= 0.05).astype(float) + (r >= 0.15).astype(float) + (r >= 0.50).astype(float)
    return bucket.where(r.notna(), other=np.nan)


def icn_ext_019_flag_value_conviction_strong_mo(insider_buy_value: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Flag: 1 if the monthly (buy_value/held) ratio is in its top quartile over 252 days."""
    r = _conviction_ratio(insider_buy_value, insider_shares_held, _TD_MO)
    return (_rolling_rank_pct(r, _TD_YEAR) >= 0.75).astype(float)


def icn_ext_020_conviction_flag_any_25pct_1y(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Flag: 1 if any rolling 21-day window in the past year had buy >= 25% of held."""
    high = (_conviction_ratio(insider_buy_shares, insider_shares_held, _TD_MO) >= 0.25).astype(float)
    return _rolling_max(high, _TD_YEAR)


def icn_ext_021_conviction_flag_any_50pct_2y(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Flag: 1 if any rolling 21-day window in the past 2 years had buy >= 50% of held."""
    high = (_conviction_ratio(insider_buy_shares, insider_shares_held, _TD_MO) >= 0.50).astype(float)
    return _rolling_max(high, _TD_2Y)


def icn_ext_022_high_conviction_day_count_252d(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """252d count of days where the monthly conviction ratio is at or above 10%."""
    flag = (_conviction_ratio(insider_buy_shares, insider_shares_held, _TD_MO) >= 0.10).astype(float)
    return _rolling_sum(flag, _TD_YEAR)


def icn_ext_023_flag_officer_value_conviction_5pct_qtr(officer_buy_value: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Flag: 1 if the quarterly officer (buy_value/held) ratio is in its top quartile (252d)."""
    r = _conviction_ratio(officer_buy_value, insider_shares_held, _TD_QTR)
    return (_rolling_rank_pct(r, _TD_YEAR) >= 0.75).astype(float)


def icn_ext_024_flag_net_buy_conviction_positive_qtr(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Flag: 1 if the quarterly net (buy minus sell) share conviction ratio exceeds 5%."""
    net = _rolling_sum(insider_buy_shares, _TD_QTR) - _rolling_sum(insider_sell_shares, _TD_QTR)
    return (_safe_div(net, insider_shares_held) >= 0.05).astype(float)


# --- Group C (025-036): Role-specific conviction (CEO/CFO/director/10pct) ---

def icn_ext_025_ceo_buy_value_conviction_qtr(ceo_buy_value: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Quarterly CEO buy value scaled by insider_shares_held."""
    return _conviction_ratio(ceo_buy_value, insider_shares_held, _TD_QTR)


def icn_ext_026_cfo_buy_value_conviction_mo(cfo_buy_value: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Monthly CFO buy value scaled by insider_shares_held."""
    return _conviction_ratio(cfo_buy_value, insider_shares_held, _TD_MO)


def icn_ext_027_director_buy_value_conviction_halfyr(director_buy_value: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Half-year director buy value scaled by insider_shares_held."""
    return _conviction_ratio(director_buy_value, insider_shares_held, _TD_HALF)


def icn_ext_028_officer_buy_value_conviction_halfyr(officer_buy_value: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Half-year officer buy value scaled by insider_shares_held."""
    return _conviction_ratio(officer_buy_value, insider_shares_held, _TD_HALF)


def icn_ext_029_tenpct_buy_value_conviction_mo(tenpct_buy_value: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Monthly 10%-holder buy value scaled by insider_shares_held."""
    return _conviction_ratio(tenpct_buy_value, insider_shares_held, _TD_MO)


def icn_ext_030_ceo_buy_value_conviction_1y(ceo_buy_value: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Annual CEO buy value scaled by insider_shares_held."""
    return _conviction_ratio(ceo_buy_value, insider_shares_held, _TD_YEAR)


def icn_ext_031_ceo_share_of_buy_value_qtr(ceo_buy_value: pd.Series, insider_buy_value: pd.Series) -> pd.Series:
    """CEO buy value as a fraction of total insider buy value (quarterly)."""
    return _safe_div(_rolling_sum(ceo_buy_value, _TD_QTR), _rolling_sum(insider_buy_value, _TD_QTR))


def icn_ext_032_cfo_share_of_buy_value_qtr(cfo_buy_value: pd.Series, insider_buy_value: pd.Series) -> pd.Series:
    """CFO buy value as a fraction of total insider buy value (quarterly)."""
    return _safe_div(_rolling_sum(cfo_buy_value, _TD_QTR), _rolling_sum(insider_buy_value, _TD_QTR))


def icn_ext_033_director_share_of_buy_value_qtr(director_buy_value: pd.Series, insider_buy_value: pd.Series) -> pd.Series:
    """Director buy value as a fraction of total insider buy value (quarterly)."""
    return _safe_div(_rolling_sum(director_buy_value, _TD_QTR), _rolling_sum(insider_buy_value, _TD_QTR))


def icn_ext_034_executive_conviction_combined_qtr(ceo_buy_value: pd.Series, cfo_buy_value: pd.Series, officer_buy_value: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Combined CEO + CFO + officer quarterly buy value scaled by insider_shares_held."""
    combined = _rolling_sum(ceo_buy_value + cfo_buy_value + officer_buy_value, _TD_QTR)
    return _safe_div(combined, insider_shares_held)


def icn_ext_035_ceo_cfo_dominance_ratio_qtr(ceo_buy_value: pd.Series, cfo_buy_value: pd.Series, insider_buy_value: pd.Series) -> pd.Series:
    """Combined CEO + CFO buy value as a fraction of total insider buy value (quarterly)."""
    top = _rolling_sum(ceo_buy_value + cfo_buy_value, _TD_QTR)
    return _safe_div(top, _rolling_sum(insider_buy_value, _TD_QTR))


def icn_ext_036_tenpct_holder_dominance_qtr(tenpct_buy_value: pd.Series, insider_buy_value: pd.Series) -> pd.Series:
    """10%-holder buy value as a fraction of total insider buy value (quarterly)."""
    return _safe_div(_rolling_sum(tenpct_buy_value, _TD_QTR), _rolling_sum(insider_buy_value, _TD_QTR))


# --- Group D (037-048): Conviction streaks, persistence and decay ---

def icn_ext_037_conviction_above_threshold_streak_qtr(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Consecutive-day streak where the quarterly conviction ratio stays at/above 5%."""
    r = _conviction_ratio(insider_buy_shares, insider_shares_held, _TD_QTR)
    return _streak_true(r >= 0.05)


def icn_ext_038_conviction_value_streak_mo(insider_buy_value: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Consecutive-day streak where the monthly value-conviction ratio is positive."""
    r = _conviction_ratio(insider_buy_value, insider_shares_held, _TD_MO)
    return _streak_true(r > 0)


def icn_ext_039_consecutive_high_conviction_quarters(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Streak of days where the quarterly conviction ratio is at/above 15%."""
    r = _conviction_ratio(insider_buy_shares, insider_shares_held, _TD_QTR)
    return _streak_true(r >= 0.15)


def icn_ext_040_high_conviction_quarter_count_2y(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """504d count of days where the quarterly conviction ratio is at/above 10%."""
    flag = (_conviction_ratio(insider_buy_shares, insider_shares_held, _TD_QTR) >= 0.10).astype(float)
    return _rolling_sum(flag, _TD_2Y)


def icn_ext_041_conviction_decay_ratio_mo_vs_halfyr(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Ratio of monthly conviction ratio to half-year conviction ratio (recent vs slow)."""
    r_mo = _conviction_ratio(insider_buy_shares, insider_shares_held, _TD_MO)
    r_half = _conviction_ratio(insider_buy_shares, insider_shares_held, _TD_HALF)
    return _safe_div(r_mo, r_half)


def icn_ext_042_conviction_momentum_qtr_vs_2y(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Quarterly conviction ratio minus 2-year conviction ratio (long-horizon momentum)."""
    r_qtr = _conviction_ratio(insider_buy_shares, insider_shares_held, _TD_QTR)
    r_2y = _conviction_ratio(insider_buy_shares, insider_shares_held, _TD_2Y)
    return r_qtr - r_2y


def icn_ext_043_conviction_value_momentum_mo_vs_1y(insider_buy_value: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Monthly value-conviction ratio minus annual value-conviction ratio."""
    r_mo = _conviction_ratio(insider_buy_value, insider_shares_held, _TD_MO)
    r_1y = _conviction_ratio(insider_buy_value, insider_shares_held, _TD_YEAR)
    return r_mo - r_1y


def icn_ext_044_days_since_high_conviction_buy(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Days since the monthly conviction ratio was last at/above 10%."""
    flag = (_conviction_ratio(insider_buy_shares, insider_shares_held, _TD_MO) >= 0.10)
    idx = pd.Series(np.arange(len(flag), dtype=float), index=flag.index)
    last = idx.where(flag).ffill()
    return (idx - last)


def icn_ext_045_conviction_persistence_ratio_1y(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Fraction of the past year where the monthly conviction ratio was at/above 5%."""
    flag = (_conviction_ratio(insider_buy_shares, insider_shares_held, _TD_MO) >= 0.05).astype(float)
    return _rolling_mean(flag, _TD_YEAR)


def icn_ext_046_conviction_ratio_max_252d(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Trailing 252-day maximum of the monthly conviction ratio (peak conviction)."""
    return _rolling_max(_conviction_ratio(insider_buy_shares, insider_shares_held, _TD_MO), _TD_YEAR)


def icn_ext_047_conviction_ratio_median_252d(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Trailing 252-day median of the monthly conviction ratio (typical conviction)."""
    return _rolling_median(_conviction_ratio(insider_buy_shares, insider_shares_held, _TD_MO), _TD_YEAR)


def icn_ext_048_conviction_value_streak_x_ratio(insider_buy_value: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Current positive-conviction streak times the monthly value-conviction ratio."""
    r = _conviction_ratio(insider_buy_value, insider_shares_held, _TD_MO)
    return _streak_true(r > 0) * r.fillna(0.0)


# --- Group E (049-060): Conviction vs sell pressure / stake erosion ---

def icn_ext_049_net_value_conviction_qtr(insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Net (buy minus sell) value scaled by insider_shares_held (quarterly)."""
    net = _rolling_sum(insider_buy_value, _TD_QTR) - _rolling_sum(insider_sell_value, _TD_QTR)
    return _safe_div(net, insider_shares_held)


def icn_ext_050_net_value_conviction_1y(insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Net (buy minus sell) value scaled by insider_shares_held (annual)."""
    net = _rolling_sum(insider_buy_value, _TD_YEAR) - _rolling_sum(insider_sell_value, _TD_YEAR)
    return _safe_div(net, insider_shares_held)


def icn_ext_051_buy_to_sell_value_conviction_ratio_qtr(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """Quarterly buy value divided by quarterly sell value — value-flow conviction balance."""
    return _safe_div(_rolling_sum(insider_buy_value, _TD_QTR), _rolling_sum(insider_sell_value, _TD_QTR))


def icn_ext_052_buy_to_sell_share_conviction_ratio_qtr(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series) -> pd.Series:
    """Quarterly buy shares divided by quarterly sell shares — share-flow conviction balance."""
    return _safe_div(_rolling_sum(insider_buy_shares, _TD_QTR), _rolling_sum(insider_sell_shares, _TD_QTR))


def icn_ext_053_sell_shares_pct_of_held_qtr(insider_sell_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Quarterly sell shares as a percent of insider_shares_held — stake-erosion intensity."""
    return _conviction_ratio(insider_sell_shares, insider_shares_held, _TD_QTR)


def icn_ext_054_net_share_conviction_ewm_qtr(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """EWM(span=63) of the daily net (buy minus sell) share conviction ratio."""
    net = (insider_buy_shares - insider_sell_shares)
    return _ewm_mean(_safe_div(net, insider_shares_held), _TD_QTR)


def icn_ext_055_conviction_dominates_selling_flag_qtr(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """Flag: 1 when quarterly buy value exceeds twice the quarterly sell value."""
    buy = _rolling_sum(insider_buy_value, _TD_QTR)
    sell = _rolling_sum(insider_sell_value, _TD_QTR)
    return (buy > 2.0 * sell).astype(float)


def icn_ext_056_net_buy_conviction_positive_fraction_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Fraction of the past year where the quarterly net share conviction ratio was positive."""
    net = _rolling_sum(insider_buy_shares, _TD_QTR) - _rolling_sum(insider_sell_shares, _TD_QTR)
    pos = (_safe_div(net, insider_shares_held) > 0).astype(float)
    return _rolling_mean(pos, _TD_YEAR)


def icn_ext_057_buy_minus_sell_value_conviction_zscore_1y(insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Z-score (252d) of the quarterly net value-conviction ratio."""
    net = _rolling_sum(insider_buy_value, _TD_QTR) - _rolling_sum(insider_sell_value, _TD_QTR)
    return _zscore_rolling(_safe_div(net, insider_shares_held), _TD_YEAR)


def icn_ext_058_held_erosion_from_selling_qtr(insider_sell_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Quarterly sell shares divided by insider_shares_held lagged one quarter."""
    return _safe_div(_rolling_sum(insider_sell_shares, _TD_QTR), insider_shares_held.shift(_TD_QTR))


def icn_ext_059_conviction_vs_sell_pressure_spread_qtr(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Quarterly buy-share conviction ratio minus quarterly sell-share erosion ratio."""
    buy_r = _conviction_ratio(insider_buy_shares, insider_shares_held, _TD_QTR)
    sell_r = _conviction_ratio(insider_sell_shares, insider_shares_held, _TD_QTR)
    return buy_r - sell_r


def icn_ext_060_clean_conviction_flag_qtr(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Flag: 1 when quarterly buy conviction >= 5% of held AND there were zero sell shares."""
    buy_r = _conviction_ratio(insider_buy_shares, insider_shares_held, _TD_QTR)
    no_sell = (_rolling_sum(insider_sell_shares, _TD_QTR) <= 0)
    return ((buy_r >= 0.05) & no_sell).astype(float)


# --- Group F (061-075): Normalized conviction, breadth and composites ---

def icn_ext_061_buy_value_conviction_zscore_2y(insider_buy_value: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Z-score of the monthly value-conviction ratio within a trailing 2-year window."""
    return _zscore_rolling(_conviction_ratio(insider_buy_value, insider_shares_held, _TD_MO), _TD_2Y)


def icn_ext_062_buy_shares_conviction_zscore_qtr_window(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Z-score of the monthly share-conviction ratio within a trailing 63-day window."""
    return _zscore_rolling(_conviction_ratio(insider_buy_shares, insider_shares_held, _TD_MO), _TD_QTR)


def icn_ext_063_buy_value_conviction_pct_rank_2y(insider_buy_value: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Percentile rank of the monthly value-conviction ratio within a trailing 2-year window."""
    return _rolling_rank_pct(_conviction_ratio(insider_buy_value, insider_shares_held, _TD_MO), _TD_2Y)


def icn_ext_064_quarterly_conviction_pct_rank_1y(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Percentile rank of the quarterly share-conviction ratio within a trailing 1-year window."""
    return _rolling_rank_pct(_conviction_ratio(insider_buy_shares, insider_shares_held, _TD_QTR), _TD_YEAR)


def icn_ext_065_conviction_breadth_buyers_x_ratio_qtr(insider_buy_shares: pd.Series, insider_shares_held: pd.Series, insider_buyers: pd.Series) -> pd.Series:
    """Quarterly share-conviction ratio times the 63-day unique buyer sum (breadth-weighted)."""
    r = _conviction_ratio(insider_buy_shares, insider_shares_held, _TD_QTR)
    return r * _rolling_sum(insider_buyers, _TD_QTR)


def icn_ext_066_conviction_per_buy_event_qtr(insider_buy_shares: pd.Series, insider_shares_held: pd.Series, insider_buy_count: pd.Series) -> pd.Series:
    """Quarterly share-conviction ratio divided by the 63-day buy count — per-event conviction."""
    r = _conviction_ratio(insider_buy_shares, insider_shares_held, _TD_QTR)
    return _safe_div(r, _rolling_sum(insider_buy_count, _TD_QTR))


def icn_ext_067_value_conviction_per_buy_event_qtr(insider_buy_value: pd.Series, insider_shares_held: pd.Series, insider_buy_count: pd.Series) -> pd.Series:
    """Quarterly value-conviction ratio divided by the 63-day buy count."""
    r = _conviction_ratio(insider_buy_value, insider_shares_held, _TD_QTR)
    return _safe_div(r, _rolling_sum(insider_buy_count, _TD_QTR))


def icn_ext_068_conviction_value_acceleration_mo_vs_qtr(insider_buy_value: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Monthly value-conviction ratio minus quarterly value-conviction ratio scaled to monthly."""
    r_mo = _conviction_ratio(insider_buy_value, insider_shares_held, _TD_MO)
    r_qtr_scaled = _conviction_ratio(insider_buy_value, insider_shares_held, _TD_QTR) / 3.0
    return r_mo - r_qtr_scaled


def icn_ext_069_officer_conviction_zscore_1y(officer_buy_value: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Z-score of the quarterly officer value-conviction ratio within a trailing 1-year window."""
    return _zscore_rolling(_conviction_ratio(officer_buy_value, insider_shares_held, _TD_QTR), _TD_YEAR)


def icn_ext_070_conviction_ratio_range_252d(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Trailing 252-day range (max minus min) of the monthly share-conviction ratio."""
    r = _conviction_ratio(insider_buy_shares, insider_shares_held, _TD_MO)
    return _rolling_max(r, _TD_YEAR) - _rolling_min(r, _TD_YEAR)


def icn_ext_071_conviction_ratio_vs_252d_peak(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Monthly share-conviction ratio divided by its trailing 252-day rolling peak."""
    r = _conviction_ratio(insider_buy_shares, insider_shares_held, _TD_MO)
    return _safe_div(r, _rolling_max(r, _TD_YEAR))


def icn_ext_072_value_conviction_ewm_ratio_21v126(insider_buy_value: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Ratio of EWM(21) to EWM(126) of the daily value-conviction ratio."""
    r = _safe_div(insider_buy_value, insider_shares_held)
    return _safe_div(_ewm_mean(r, _TD_MO), _ewm_mean(r, _TD_HALF))


def icn_ext_073_conviction_intensity_value_x_breadth_qtr(insider_buy_value: pd.Series, insider_shares_held: pd.Series, insider_buyers: pd.Series) -> pd.Series:
    """Quarterly value-conviction ratio times the 63-day unique buyer sum."""
    r = _conviction_ratio(insider_buy_value, insider_shares_held, _TD_QTR)
    return r * _rolling_sum(insider_buyers, _TD_QTR)


def icn_ext_074_extended_conviction_zcomposite(insider_buy_shares: pd.Series, insider_buy_value: pd.Series, insider_shares_held: pd.Series, insider_buyers: pd.Series) -> pd.Series:
    """Composite: average of 252d z-scores of (quarterly share-conviction ratio),
    (quarterly value-conviction ratio), and (quarterly breadth-weighted conviction)."""
    s1 = _conviction_ratio(insider_buy_shares, insider_shares_held, _TD_QTR)
    s2 = _conviction_ratio(insider_buy_value, insider_shares_held, _TD_QTR)
    s3 = s1 * _rolling_sum(insider_buyers, _TD_QTR)
    z1, z2, z3 = _zscore_rolling(s1, _TD_YEAR), _zscore_rolling(s2, _TD_YEAR), _zscore_rolling(s3, _TD_YEAR)
    cnt = z1.notna().astype(float) + z2.notna().astype(float) + z3.notna().astype(float)
    return _safe_div(z1.fillna(0) + z2.fillna(0) + z3.fillna(0), cnt)


def icn_ext_075_capitulation_conviction_intensity(insider_buy_shares: pd.Series, insider_buy_value: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Capitulation conviction intensity: quarterly share-conviction and value-conviction
    ratios each normalized by their 252d max, summed (higher = more extreme accumulation)."""
    s = _conviction_ratio(insider_buy_shares, insider_shares_held, _TD_QTR)
    v = _conviction_ratio(insider_buy_value, insider_shares_held, _TD_QTR)
    s_norm = _safe_div(s, _rolling_max(s, _TD_YEAR))
    v_norm = _safe_div(v, _rolling_max(v, _TD_YEAR))
    return s_norm.fillna(0.0) + v_norm.fillna(0.0)


# ── Registry ──────────────────────────────────────────────────────────────────

INSIDER_CONVICTION_EXTENDED_REGISTRY_001_075 = {
    "icn_ext_001_buy_value_conviction_wk": {"inputs": ["insider_buy_value", "insider_shares_held"], "func": icn_ext_001_buy_value_conviction_wk},
    "icn_ext_002_buy_value_conviction_halfyr": {"inputs": ["insider_buy_value", "insider_shares_held"], "func": icn_ext_002_buy_value_conviction_halfyr},
    "icn_ext_003_buy_value_conviction_2y": {"inputs": ["insider_buy_value", "insider_shares_held"], "func": icn_ext_003_buy_value_conviction_2y},
    "icn_ext_004_buy_shares_conviction_2y": {"inputs": ["insider_buy_shares", "insider_shares_held"], "func": icn_ext_004_buy_shares_conviction_2y},
    "icn_ext_005_buy_value_conviction_42d": {"inputs": ["insider_buy_value", "insider_shares_held"], "func": icn_ext_005_buy_value_conviction_42d},
    "icn_ext_006_buy_value_conviction_ewm_qtr": {"inputs": ["insider_buy_value", "insider_shares_held"], "func": icn_ext_006_buy_value_conviction_ewm_qtr},
    "icn_ext_007_buy_shares_conviction_ewm_mo": {"inputs": ["insider_buy_shares", "insider_shares_held"], "func": icn_ext_007_buy_shares_conviction_ewm_mo},
    "icn_ext_008_buy_value_conviction_prior_stake_halfyr": {"inputs": ["insider_buy_value", "insider_shares_held"], "func": icn_ext_008_buy_value_conviction_prior_stake_halfyr},
    "icn_ext_009_buy_shares_conviction_prior_stake_halfyr": {"inputs": ["insider_buy_shares", "insider_shares_held"], "func": icn_ext_009_buy_shares_conviction_prior_stake_halfyr},
    "icn_ext_010_buy_value_conviction_prior_stake_1y": {"inputs": ["insider_buy_value", "insider_shares_held"], "func": icn_ext_010_buy_value_conviction_prior_stake_1y},
    "icn_ext_011_buy_value_conviction_smoothed_qtr": {"inputs": ["insider_buy_value", "insider_shares_held"], "func": icn_ext_011_buy_value_conviction_smoothed_qtr},
    "icn_ext_012_buy_shares_conviction_smoothed_qtr": {"inputs": ["insider_buy_shares", "insider_shares_held"], "func": icn_ext_012_buy_shares_conviction_smoothed_qtr},
    "icn_ext_013_flag_buy_adds_1pct_mo": {"inputs": ["insider_buy_shares", "insider_shares_held"], "func": icn_ext_013_flag_buy_adds_1pct_mo},
    "icn_ext_014_flag_buy_adds_15pct_qtr": {"inputs": ["insider_buy_shares", "insider_shares_held"], "func": icn_ext_014_flag_buy_adds_15pct_qtr},
    "icn_ext_015_flag_buy_adds_50pct_qtr": {"inputs": ["insider_buy_shares", "insider_shares_held"], "func": icn_ext_015_flag_buy_adds_50pct_qtr},
    "icn_ext_016_flag_buy_adds_100pct_1y": {"inputs": ["insider_buy_shares", "insider_shares_held"], "func": icn_ext_016_flag_buy_adds_100pct_1y},
    "icn_ext_017_flag_buy_adds_10pct_halfyr": {"inputs": ["insider_buy_shares", "insider_shares_held"], "func": icn_ext_017_flag_buy_adds_10pct_halfyr},
    "icn_ext_018_conviction_depth_bucket_qtr": {"inputs": ["insider_buy_shares", "insider_shares_held"], "func": icn_ext_018_conviction_depth_bucket_qtr},
    "icn_ext_019_flag_value_conviction_strong_mo": {"inputs": ["insider_buy_value", "insider_shares_held"], "func": icn_ext_019_flag_value_conviction_strong_mo},
    "icn_ext_020_conviction_flag_any_25pct_1y": {"inputs": ["insider_buy_shares", "insider_shares_held"], "func": icn_ext_020_conviction_flag_any_25pct_1y},
    "icn_ext_021_conviction_flag_any_50pct_2y": {"inputs": ["insider_buy_shares", "insider_shares_held"], "func": icn_ext_021_conviction_flag_any_50pct_2y},
    "icn_ext_022_high_conviction_day_count_252d": {"inputs": ["insider_buy_shares", "insider_shares_held"], "func": icn_ext_022_high_conviction_day_count_252d},
    "icn_ext_023_flag_officer_value_conviction_5pct_qtr": {"inputs": ["officer_buy_value", "insider_shares_held"], "func": icn_ext_023_flag_officer_value_conviction_5pct_qtr},
    "icn_ext_024_flag_net_buy_conviction_positive_qtr": {"inputs": ["insider_buy_shares", "insider_sell_shares", "insider_shares_held"], "func": icn_ext_024_flag_net_buy_conviction_positive_qtr},
    "icn_ext_025_ceo_buy_value_conviction_qtr": {"inputs": ["ceo_buy_value", "insider_shares_held"], "func": icn_ext_025_ceo_buy_value_conviction_qtr},
    "icn_ext_026_cfo_buy_value_conviction_mo": {"inputs": ["cfo_buy_value", "insider_shares_held"], "func": icn_ext_026_cfo_buy_value_conviction_mo},
    "icn_ext_027_director_buy_value_conviction_halfyr": {"inputs": ["director_buy_value", "insider_shares_held"], "func": icn_ext_027_director_buy_value_conviction_halfyr},
    "icn_ext_028_officer_buy_value_conviction_halfyr": {"inputs": ["officer_buy_value", "insider_shares_held"], "func": icn_ext_028_officer_buy_value_conviction_halfyr},
    "icn_ext_029_tenpct_buy_value_conviction_mo": {"inputs": ["tenpct_buy_value", "insider_shares_held"], "func": icn_ext_029_tenpct_buy_value_conviction_mo},
    "icn_ext_030_ceo_buy_value_conviction_1y": {"inputs": ["ceo_buy_value", "insider_shares_held"], "func": icn_ext_030_ceo_buy_value_conviction_1y},
    "icn_ext_031_ceo_share_of_buy_value_qtr": {"inputs": ["ceo_buy_value", "insider_buy_value"], "func": icn_ext_031_ceo_share_of_buy_value_qtr},
    "icn_ext_032_cfo_share_of_buy_value_qtr": {"inputs": ["cfo_buy_value", "insider_buy_value"], "func": icn_ext_032_cfo_share_of_buy_value_qtr},
    "icn_ext_033_director_share_of_buy_value_qtr": {"inputs": ["director_buy_value", "insider_buy_value"], "func": icn_ext_033_director_share_of_buy_value_qtr},
    "icn_ext_034_executive_conviction_combined_qtr": {"inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "insider_shares_held"], "func": icn_ext_034_executive_conviction_combined_qtr},
    "icn_ext_035_ceo_cfo_dominance_ratio_qtr": {"inputs": ["ceo_buy_value", "cfo_buy_value", "insider_buy_value"], "func": icn_ext_035_ceo_cfo_dominance_ratio_qtr},
    "icn_ext_036_tenpct_holder_dominance_qtr": {"inputs": ["tenpct_buy_value", "insider_buy_value"], "func": icn_ext_036_tenpct_holder_dominance_qtr},
    "icn_ext_037_conviction_above_threshold_streak_qtr": {"inputs": ["insider_buy_shares", "insider_shares_held"], "func": icn_ext_037_conviction_above_threshold_streak_qtr},
    "icn_ext_038_conviction_value_streak_mo": {"inputs": ["insider_buy_value", "insider_shares_held"], "func": icn_ext_038_conviction_value_streak_mo},
    "icn_ext_039_consecutive_high_conviction_quarters": {"inputs": ["insider_buy_shares", "insider_shares_held"], "func": icn_ext_039_consecutive_high_conviction_quarters},
    "icn_ext_040_high_conviction_quarter_count_2y": {"inputs": ["insider_buy_shares", "insider_shares_held"], "func": icn_ext_040_high_conviction_quarter_count_2y},
    "icn_ext_041_conviction_decay_ratio_mo_vs_halfyr": {"inputs": ["insider_buy_shares", "insider_shares_held"], "func": icn_ext_041_conviction_decay_ratio_mo_vs_halfyr},
    "icn_ext_042_conviction_momentum_qtr_vs_2y": {"inputs": ["insider_buy_shares", "insider_shares_held"], "func": icn_ext_042_conviction_momentum_qtr_vs_2y},
    "icn_ext_043_conviction_value_momentum_mo_vs_1y": {"inputs": ["insider_buy_value", "insider_shares_held"], "func": icn_ext_043_conviction_value_momentum_mo_vs_1y},
    "icn_ext_044_days_since_high_conviction_buy": {"inputs": ["insider_buy_shares", "insider_shares_held"], "func": icn_ext_044_days_since_high_conviction_buy},
    "icn_ext_045_conviction_persistence_ratio_1y": {"inputs": ["insider_buy_shares", "insider_shares_held"], "func": icn_ext_045_conviction_persistence_ratio_1y},
    "icn_ext_046_conviction_ratio_max_252d": {"inputs": ["insider_buy_shares", "insider_shares_held"], "func": icn_ext_046_conviction_ratio_max_252d},
    "icn_ext_047_conviction_ratio_median_252d": {"inputs": ["insider_buy_shares", "insider_shares_held"], "func": icn_ext_047_conviction_ratio_median_252d},
    "icn_ext_048_conviction_value_streak_x_ratio": {"inputs": ["insider_buy_value", "insider_shares_held"], "func": icn_ext_048_conviction_value_streak_x_ratio},
    "icn_ext_049_net_value_conviction_qtr": {"inputs": ["insider_buy_value", "insider_sell_value", "insider_shares_held"], "func": icn_ext_049_net_value_conviction_qtr},
    "icn_ext_050_net_value_conviction_1y": {"inputs": ["insider_buy_value", "insider_sell_value", "insider_shares_held"], "func": icn_ext_050_net_value_conviction_1y},
    "icn_ext_051_buy_to_sell_value_conviction_ratio_qtr": {"inputs": ["insider_buy_value", "insider_sell_value"], "func": icn_ext_051_buy_to_sell_value_conviction_ratio_qtr},
    "icn_ext_052_buy_to_sell_share_conviction_ratio_qtr": {"inputs": ["insider_buy_shares", "insider_sell_shares"], "func": icn_ext_052_buy_to_sell_share_conviction_ratio_qtr},
    "icn_ext_053_sell_shares_pct_of_held_qtr": {"inputs": ["insider_sell_shares", "insider_shares_held"], "func": icn_ext_053_sell_shares_pct_of_held_qtr},
    "icn_ext_054_net_share_conviction_ewm_qtr": {"inputs": ["insider_buy_shares", "insider_sell_shares", "insider_shares_held"], "func": icn_ext_054_net_share_conviction_ewm_qtr},
    "icn_ext_055_conviction_dominates_selling_flag_qtr": {"inputs": ["insider_buy_value", "insider_sell_value"], "func": icn_ext_055_conviction_dominates_selling_flag_qtr},
    "icn_ext_056_net_buy_conviction_positive_fraction_252d": {"inputs": ["insider_buy_shares", "insider_sell_shares", "insider_shares_held"], "func": icn_ext_056_net_buy_conviction_positive_fraction_252d},
    "icn_ext_057_buy_minus_sell_value_conviction_zscore_1y": {"inputs": ["insider_buy_value", "insider_sell_value", "insider_shares_held"], "func": icn_ext_057_buy_minus_sell_value_conviction_zscore_1y},
    "icn_ext_058_held_erosion_from_selling_qtr": {"inputs": ["insider_sell_shares", "insider_shares_held"], "func": icn_ext_058_held_erosion_from_selling_qtr},
    "icn_ext_059_conviction_vs_sell_pressure_spread_qtr": {"inputs": ["insider_buy_shares", "insider_sell_shares", "insider_shares_held"], "func": icn_ext_059_conviction_vs_sell_pressure_spread_qtr},
    "icn_ext_060_clean_conviction_flag_qtr": {"inputs": ["insider_buy_shares", "insider_sell_shares", "insider_shares_held"], "func": icn_ext_060_clean_conviction_flag_qtr},
    "icn_ext_061_buy_value_conviction_zscore_2y": {"inputs": ["insider_buy_value", "insider_shares_held"], "func": icn_ext_061_buy_value_conviction_zscore_2y},
    "icn_ext_062_buy_shares_conviction_zscore_qtr_window": {"inputs": ["insider_buy_shares", "insider_shares_held"], "func": icn_ext_062_buy_shares_conviction_zscore_qtr_window},
    "icn_ext_063_buy_value_conviction_pct_rank_2y": {"inputs": ["insider_buy_value", "insider_shares_held"], "func": icn_ext_063_buy_value_conviction_pct_rank_2y},
    "icn_ext_064_quarterly_conviction_pct_rank_1y": {"inputs": ["insider_buy_shares", "insider_shares_held"], "func": icn_ext_064_quarterly_conviction_pct_rank_1y},
    "icn_ext_065_conviction_breadth_buyers_x_ratio_qtr": {"inputs": ["insider_buy_shares", "insider_shares_held", "insider_buyers"], "func": icn_ext_065_conviction_breadth_buyers_x_ratio_qtr},
    "icn_ext_066_conviction_per_buy_event_qtr": {"inputs": ["insider_buy_shares", "insider_shares_held", "insider_buy_count"], "func": icn_ext_066_conviction_per_buy_event_qtr},
    "icn_ext_067_value_conviction_per_buy_event_qtr": {"inputs": ["insider_buy_value", "insider_shares_held", "insider_buy_count"], "func": icn_ext_067_value_conviction_per_buy_event_qtr},
    "icn_ext_068_conviction_value_acceleration_mo_vs_qtr": {"inputs": ["insider_buy_value", "insider_shares_held"], "func": icn_ext_068_conviction_value_acceleration_mo_vs_qtr},
    "icn_ext_069_officer_conviction_zscore_1y": {"inputs": ["officer_buy_value", "insider_shares_held"], "func": icn_ext_069_officer_conviction_zscore_1y},
    "icn_ext_070_conviction_ratio_range_252d": {"inputs": ["insider_buy_shares", "insider_shares_held"], "func": icn_ext_070_conviction_ratio_range_252d},
    "icn_ext_071_conviction_ratio_vs_252d_peak": {"inputs": ["insider_buy_shares", "insider_shares_held"], "func": icn_ext_071_conviction_ratio_vs_252d_peak},
    "icn_ext_072_value_conviction_ewm_ratio_21v126": {"inputs": ["insider_buy_value", "insider_shares_held"], "func": icn_ext_072_value_conviction_ewm_ratio_21v126},
    "icn_ext_073_conviction_intensity_value_x_breadth_qtr": {"inputs": ["insider_buy_value", "insider_shares_held", "insider_buyers"], "func": icn_ext_073_conviction_intensity_value_x_breadth_qtr},
    "icn_ext_074_extended_conviction_zcomposite": {"inputs": ["insider_buy_shares", "insider_buy_value", "insider_shares_held", "insider_buyers"], "func": icn_ext_074_extended_conviction_zcomposite},
    "icn_ext_075_capitulation_conviction_intensity": {"inputs": ["insider_buy_shares", "insider_buy_value", "insider_shares_held"], "func": icn_ext_075_capitulation_conviction_intensity},
}
