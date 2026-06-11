"""insider_selling_trajectory base features 001-075 — Pipeline 1a-inverse short-side blowup family.

75 distinct hypotheses about the *trajectory* of insider Form-4 selling at peak (continued in __base__076_150.py).
Inputs: daily-aggregated SF2 series (per-day sums/counts) projected onto the price calendar.
Expected input columns supplied by harness:
  insider_sell_value, insider_buy_value, insider_sell_shares, insider_buy_shares,
  insider_sell_count, insider_buy_count, insider_sellers_unique, insider_buyers_unique,
  insider_officer_sell_value, insider_director_sell_value, insider_tenpct_sell_value,
  insider_officer_buy_value, insider_director_buy_value, insider_tenpct_buy_value,
  insider_total_shares_owned, insider_n_reporters,
  close, volume, marketcap
PIT-clean: right-anchored .rolling(), explicit min_periods, no centered windows.
"""
import numpy as np
import pandas as pd

YDAYS = 252
QDAYS = 63
MDAYS = 21
WDAYS = 5


def _safe_div(num, den):
    if isinstance(den, pd.Series):
        d = den.replace(0, np.nan)
    else:
        d = np.where(den == 0, np.nan, den)
    out = num / d
    if isinstance(out, pd.Series):
        return out.replace([np.inf, -np.inf], np.nan)
    idx = num.index if hasattr(num, "index") else None
    return pd.Series(out, index=idx).replace([np.inf, -np.inf], np.nan)


def _safe_log(s, eps=1e-12):
    if isinstance(s, pd.Series):
        return np.log(s.where(s > eps, np.nan))
    arr = np.where(s > eps, s, np.nan)
    return np.log(arr)


def _rolling_zscore(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    m = s.rolling(window, min_periods=min_periods).mean()
    sd = s.rolling(window, min_periods=min_periods).std()
    return (s - m) / sd.replace(0, np.nan)


def _ema(s, span):
    return s.ewm(span=span, min_periods=max(span // 3, 2), adjust=False).mean()


def _runlen_pos(s):
    pos = (s > 0).astype(float)
    grp = (pos != pos.shift()).cumsum()
    return pos.groupby(grp).cumsum() * pos


def _runlen_zero(s):
    zero = (s == 0).astype(float)
    grp = (zero != zero.shift()).cumsum()
    return zero.groupby(grp).cumsum() * zero


# ============================================================
#                    FEATURES 001-075
# ============================================================

def f27_istj_001_insider_sell_value_sum_21d(insider_sell_value):
    return insider_sell_value.rolling(21, min_periods=5).sum()


def f27_istj_002_insider_sell_value_sum_63d(insider_sell_value):
    return insider_sell_value.rolling(63, min_periods=15).sum()


def f27_istj_003_insider_sell_value_sum_126d(insider_sell_value):
    return insider_sell_value.rolling(126, min_periods=30).sum()


def f27_istj_004_insider_sell_value_sum_252d(insider_sell_value):
    return insider_sell_value.rolling(252, min_periods=60).sum()


def f27_istj_005_insider_sell_count_sum_63d(insider_sell_count):
    return insider_sell_count.rolling(63, min_periods=15).sum()


def f27_istj_006_insider_sell_shares_sum_63d(insider_sell_shares):
    return insider_sell_shares.rolling(63, min_periods=15).sum()


def f27_istj_007_insider_sell_value_sum_21d_to_mcap(insider_sell_value, marketcap):
    return _safe_div(insider_sell_value.rolling(21, min_periods=5).sum(), marketcap)


def f27_istj_008_insider_sell_value_sum_63d_to_mcap(insider_sell_value, marketcap):
    return _safe_div(insider_sell_value.rolling(63, min_periods=15).sum(), marketcap)


def f27_istj_009_insider_sell_value_sum_252d_to_mcap(insider_sell_value, marketcap):
    return _safe_div(insider_sell_value.rolling(252, min_periods=60).sum(), marketcap)


def f27_istj_010_insider_sell_value_max_5d_rolling_63d(insider_sell_value):
    return insider_sell_value.rolling(5, min_periods=1).sum().rolling(63, min_periods=15).max()


def f27_istj_011_insider_sell_value_max_21d_rolling_252d(insider_sell_value):
    return insider_sell_value.rolling(21, min_periods=5).sum().rolling(252, min_periods=60).max()


def f27_istj_012_insider_sell_value_breadth_63d(insider_sell_value):
    return (insider_sell_value > 0).astype(float).rolling(63, min_periods=15).mean()


def f27_istj_013_insider_sell_value_breadth_252d(insider_sell_value):
    return (insider_sell_value > 0).astype(float).rolling(252, min_periods=60).mean()


def f27_istj_014_insider_sell_value_concentration_top1_63d(insider_sell_value):
    top = insider_sell_value.rolling(63, min_periods=15).max()
    tot = insider_sell_value.rolling(63, min_periods=15).sum()
    return _safe_div(top, tot)


def f27_istj_015_insider_sell_value_concentration_top5_63d(insider_sell_value):
    top5 = insider_sell_value.rolling(63, min_periods=15).apply(
        lambda y: float(np.nansum(np.sort(y)[-5:])) if np.isfinite(y).sum() >= 5 else np.nan, raw=True)
    tot = insider_sell_value.rolling(63, min_periods=15).sum()
    return _safe_div(top5, tot)


def f27_istj_016_insider_net_value_21d(insider_buy_value, insider_sell_value):
    return (insider_buy_value - insider_sell_value).rolling(21, min_periods=5).sum()


def f27_istj_017_insider_net_value_63d(insider_buy_value, insider_sell_value):
    return (insider_buy_value - insider_sell_value).rolling(63, min_periods=15).sum()


def f27_istj_018_insider_net_value_252d(insider_buy_value, insider_sell_value):
    return (insider_buy_value - insider_sell_value).rolling(252, min_periods=60).sum()


def f27_istj_019_insider_buy_to_sell_value_ratio_63d(insider_buy_value, insider_sell_value):
    return _safe_div(insider_buy_value.rolling(63, min_periods=15).sum(), insider_sell_value.rolling(63, min_periods=15).sum())


def f27_istj_020_insider_buy_to_sell_value_ratio_252d(insider_buy_value, insider_sell_value):
    return _safe_div(insider_buy_value.rolling(252, min_periods=60).sum(), insider_sell_value.rolling(252, min_periods=60).sum())


def f27_istj_021_insider_buy_to_sell_count_ratio_63d(insider_buy_count, insider_sell_count):
    return _safe_div(insider_buy_count.rolling(63, min_periods=15).sum(), insider_sell_count.rolling(63, min_periods=15).sum())


def f27_istj_022_insider_buy_to_sell_count_ratio_252d(insider_buy_count, insider_sell_count):
    return _safe_div(insider_buy_count.rolling(252, min_periods=60).sum(), insider_sell_count.rolling(252, min_periods=60).sum())


def f27_istj_023_insider_sell_to_buy_share_ratio_63d(insider_sell_shares, insider_buy_shares):
    return _safe_div(insider_sell_shares.rolling(63, min_periods=15).sum(), insider_buy_shares.rolling(63, min_periods=15).sum())


def f27_istj_024_insider_net_value_to_mcap_63d(insider_buy_value, insider_sell_value, marketcap):
    return _safe_div((insider_buy_value - insider_sell_value).rolling(63, min_periods=15).sum(), marketcap)


def f27_istj_025_insider_net_value_to_mcap_252d(insider_buy_value, insider_sell_value, marketcap):
    return _safe_div((insider_buy_value - insider_sell_value).rolling(252, min_periods=60).sum(), marketcap)


def f27_istj_026_insider_sell_value_minus_buy_value_zscore_252d(insider_sell_value, insider_buy_value):
    return _rolling_zscore(insider_sell_value - insider_buy_value, 252, min_periods=60)


def f27_istj_027_insider_buys_absent_streak(insider_buy_value):
    return _runlen_zero(insider_buy_value)


def f27_istj_028_insider_sells_absent_streak(insider_sell_value):
    return _runlen_zero(insider_sell_value)


def f27_istj_029_insider_buy_dry_up_63d(insider_buy_value):
    return (insider_buy_value.rolling(63, min_periods=15).sum() == 0).astype(float)


def f27_istj_030_insider_sell_persistence_63d(insider_sell_value):
    weekly = insider_sell_value.rolling(5, min_periods=1).sum()
    return (weekly > 0).astype(float).rolling(63, min_periods=15).mean()


def f27_istj_031_officer_sell_value_sum_63d(insider_officer_sell_value):
    return insider_officer_sell_value.rolling(63, min_periods=15).sum()


def f27_istj_032_director_sell_value_sum_63d(insider_director_sell_value):
    return insider_director_sell_value.rolling(63, min_periods=15).sum()


def f27_istj_033_tenpct_sell_value_sum_63d(insider_tenpct_sell_value):
    return insider_tenpct_sell_value.rolling(63, min_periods=15).sum()


def f27_istj_034_officer_sell_value_share_63d(insider_officer_sell_value, insider_sell_value):
    return _safe_div(insider_officer_sell_value.rolling(63, min_periods=15).sum(), insider_sell_value.rolling(63, min_periods=15).sum())


def f27_istj_035_director_sell_value_share_63d(insider_director_sell_value, insider_sell_value):
    return _safe_div(insider_director_sell_value.rolling(63, min_periods=15).sum(), insider_sell_value.rolling(63, min_periods=15).sum())


def f27_istj_036_tenpct_sell_value_share_63d(insider_tenpct_sell_value, insider_sell_value):
    return _safe_div(insider_tenpct_sell_value.rolling(63, min_periods=15).sum(), insider_sell_value.rolling(63, min_periods=15).sum())


def f27_istj_037_officer_sell_to_mcap_63d(insider_officer_sell_value, marketcap):
    return _safe_div(insider_officer_sell_value.rolling(63, min_periods=15).sum(), marketcap)


def f27_istj_038_director_sell_to_mcap_63d(insider_director_sell_value, marketcap):
    return _safe_div(insider_director_sell_value.rolling(63, min_periods=15).sum(), marketcap)


def f27_istj_039_tenpct_sell_to_mcap_63d(insider_tenpct_sell_value, marketcap):
    return _safe_div(insider_tenpct_sell_value.rolling(63, min_periods=15).sum(), marketcap)


def f27_istj_040_officer_sell_concentration_growth(insider_officer_sell_value, insider_sell_value):
    r63 = _safe_div(insider_officer_sell_value.rolling(63, min_periods=15).sum(), insider_sell_value.rolling(63, min_periods=15).sum())
    r252 = _safe_div(insider_officer_sell_value.rolling(252, min_periods=60).sum(), insider_sell_value.rolling(252, min_periods=60).sum())
    return r63 - r252


def f27_istj_041_director_sell_concentration_growth(insider_director_sell_value, insider_sell_value):
    r63 = _safe_div(insider_director_sell_value.rolling(63, min_periods=15).sum(), insider_sell_value.rolling(63, min_periods=15).sum())
    r252 = _safe_div(insider_director_sell_value.rolling(252, min_periods=60).sum(), insider_sell_value.rolling(252, min_periods=60).sum())
    return r63 - r252


def f27_istj_042_tenpct_sell_to_total_sell_252d(insider_tenpct_sell_value, insider_sell_value):
    return _safe_div(insider_tenpct_sell_value.rolling(252, min_periods=60).sum(), insider_sell_value.rolling(252, min_periods=60).sum())


def f27_istj_043_officer_buy_value_share_63d(insider_officer_buy_value, insider_buy_value):
    return _safe_div(insider_officer_buy_value.rolling(63, min_periods=15).sum(), insider_buy_value.rolling(63, min_periods=15).sum())


def f27_istj_044_officer_buy_vs_sell_disagreement(insider_officer_buy_value, insider_sell_value):
    buy = insider_officer_buy_value.rolling(63, min_periods=15).sum()
    sell = insider_sell_value.rolling(63, min_periods=15).sum()
    return _safe_div(buy - sell, (buy + sell).abs())


def f27_istj_045_multi_role_sell_coincidence(insider_officer_sell_value, insider_director_sell_value):
    of_w = (insider_officer_sell_value.rolling(5, min_periods=1).sum() > 0).astype(float)
    di_w = (insider_director_sell_value.rolling(5, min_periods=1).sum() > 0).astype(float)
    return (of_w * di_w).rolling(63, min_periods=15).sum()


def f27_istj_046_insider_total_owned_yoy_change(insider_total_shares_owned):
    return _safe_div(insider_total_shares_owned - insider_total_shares_owned.shift(252), insider_total_shares_owned.shift(252).abs())


def f27_istj_047_insider_total_owned_qoq_change(insider_total_shares_owned):
    return _safe_div(insider_total_shares_owned - insider_total_shares_owned.shift(63), insider_total_shares_owned.shift(63).abs())


def f27_istj_048_insider_total_owned_drawdown_252d(insider_total_shares_owned):
    hi = insider_total_shares_owned.rolling(252, min_periods=60).max()
    return _safe_div(insider_total_shares_owned - hi, hi.abs())


def f27_istj_049_insider_total_owned_drawdown_504d(insider_total_shares_owned):
    hi = insider_total_shares_owned.rolling(504, min_periods=120).max()
    return _safe_div(insider_total_shares_owned - hi, hi.abs())


def f27_istj_050_insider_n_reporters_change_252d(insider_n_reporters):
    return insider_n_reporters - insider_n_reporters.shift(252)


def f27_istj_051_insider_sellers_unique_rolling_63d_sum(insider_sellers_unique):
    return insider_sellers_unique.rolling(63, min_periods=15).sum()


def f27_istj_052_insider_unique_sellers_to_unique_buyers_63d(insider_sellers_unique, insider_buyers_unique):
    return _safe_div(insider_sellers_unique.rolling(63, min_periods=15).sum(), insider_buyers_unique.rolling(63, min_periods=15).sum())


def f27_istj_053_insider_unique_sellers_growth_252d(insider_sellers_unique):
    cur = insider_sellers_unique.rolling(63, min_periods=15).sum()
    return _safe_div(cur - cur.shift(252), cur.shift(252).abs())


def f27_istj_054_insider_sell_breadth_acceleration(insider_sell_value):
    b63 = (insider_sell_value > 0).astype(float).rolling(63, min_periods=15).mean()
    b252 = (insider_sell_value > 0).astype(float).rolling(252, min_periods=60).mean()
    return b63 - b252


def f27_istj_055_insider_participation_in_decline(insider_sell_value, close):
    falling = (close < close.shift(21)).astype(float)
    return (insider_sell_value * falling).rolling(63, min_periods=15).sum()


def f27_istj_056_insider_directors_exiting_count_252d(insider_director_sell_value, insider_director_buy_value):
    net = insider_director_sell_value - insider_director_buy_value
    return (net > 0).astype(float).rolling(252, min_periods=60).sum()


def f27_istj_057_insider_officers_exiting_count_252d(insider_officer_sell_value, insider_officer_buy_value):
    net = insider_officer_sell_value - insider_officer_buy_value
    return (net > 0).astype(float).rolling(252, min_periods=60).sum()


def f27_istj_058_insider_total_owned_zscore_252d(insider_total_shares_owned):
    return _rolling_zscore(insider_total_shares_owned, 252, min_periods=60)


def f27_istj_059_insider_ownership_decline_rate_252d(insider_total_shares_owned):
    return _safe_div(insider_total_shares_owned.diff(252), insider_total_shares_owned.shift(252).abs())


def f27_istj_060_insider_buyer_exhaustion_index(insider_buyers_unique, insider_sellers_unique):
    return _safe_div(insider_buyers_unique.rolling(252, min_periods=60).sum(),
                     (insider_buyers_unique + insider_sellers_unique).rolling(252, min_periods=60).sum())


def f27_istj_061_insider_sell_cluster_score_5d(insider_sellers_unique):
    return insider_sellers_unique.rolling(5, min_periods=1).sum()


def f27_istj_062_insider_sell_cluster_score_21d(insider_sellers_unique):
    return insider_sellers_unique.rolling(21, min_periods=5).sum()


def f27_istj_063_insider_sell_cluster_score_63d(insider_sellers_unique):
    return insider_sellers_unique.rolling(63, min_periods=15).sum()


def f27_istj_064_insider_sell_cluster_max_5d_in_63d(insider_sellers_unique):
    return insider_sellers_unique.rolling(5, min_periods=1).sum().rolling(63, min_periods=15).max()


def f27_istj_065_insider_consecutive_sell_weeks(insider_sell_value):
    weekly = insider_sell_value.rolling(5, min_periods=1).sum()
    return _runlen_pos(weekly)


def f27_istj_066_insider_consecutive_no_buy_weeks(insider_buy_value):
    weekly = insider_buy_value.rolling(5, min_periods=1).sum()
    return _runlen_zero(weekly)


def f27_istj_067_insider_sells_per_week_avg_63d(insider_sell_count):
    return insider_sell_count.rolling(63, min_periods=15).sum() / (63.0 / 5.0)


def f27_istj_068_insider_sell_value_per_seller_63d(insider_sell_value, insider_sellers_unique):
    return _safe_div(insider_sell_value.rolling(63, min_periods=15).sum(), insider_sellers_unique.rolling(63, min_periods=15).sum())


def f27_istj_069_insider_sell_value_per_seller_252d(insider_sell_value, insider_sellers_unique):
    return _safe_div(insider_sell_value.rolling(252, min_periods=60).sum(), insider_sellers_unique.rolling(252, min_periods=60).sum())


def f27_istj_070_insider_burst_count_63d(insider_sell_value, marketcap):
    weekly_pct = _safe_div(insider_sell_value.rolling(5, min_periods=1).sum(), marketcap)
    return (weekly_pct > 0.01).astype(float).rolling(63, min_periods=15).sum()


def f27_istj_071_insider_cluster_breadth_4w_then_8w(insider_sellers_unique):
    s4 = insider_sellers_unique.rolling(21, min_periods=5).sum()
    s8 = insider_sellers_unique.rolling(42, min_periods=10).sum()
    return _safe_div(s4, s8)


def f27_istj_072_days_since_last_insider_buy(insider_buy_value):
    return _runlen_zero(insider_buy_value)


def f27_istj_073_days_since_last_insider_sell(insider_sell_value):
    return _runlen_zero(insider_sell_value)


def f27_istj_074_days_since_last_officer_buy(insider_officer_buy_value):
    return _runlen_zero(insider_officer_buy_value)


def f27_istj_075_days_since_last_cluster_buy_5d(insider_buy_value):
    weekly = insider_buy_value.rolling(5, min_periods=1).sum()
    return _runlen_zero(weekly)


INSIDER_SELLING_TRAJECTORY_BASE_REGISTRY_001_075 = {
    "f27_istj_001_insider_sell_value_sum_21d": {"inputs": ["insider_sell_value"], "func": f27_istj_001_insider_sell_value_sum_21d},
    "f27_istj_002_insider_sell_value_sum_63d": {"inputs": ["insider_sell_value"], "func": f27_istj_002_insider_sell_value_sum_63d},
    "f27_istj_003_insider_sell_value_sum_126d": {"inputs": ["insider_sell_value"], "func": f27_istj_003_insider_sell_value_sum_126d},
    "f27_istj_004_insider_sell_value_sum_252d": {"inputs": ["insider_sell_value"], "func": f27_istj_004_insider_sell_value_sum_252d},
    "f27_istj_005_insider_sell_count_sum_63d": {"inputs": ["insider_sell_count"], "func": f27_istj_005_insider_sell_count_sum_63d},
    "f27_istj_006_insider_sell_shares_sum_63d": {"inputs": ["insider_sell_shares"], "func": f27_istj_006_insider_sell_shares_sum_63d},
    "f27_istj_007_insider_sell_value_sum_21d_to_mcap": {"inputs": ["insider_sell_value", "marketcap"], "func": f27_istj_007_insider_sell_value_sum_21d_to_mcap},
    "f27_istj_008_insider_sell_value_sum_63d_to_mcap": {"inputs": ["insider_sell_value", "marketcap"], "func": f27_istj_008_insider_sell_value_sum_63d_to_mcap},
    "f27_istj_009_insider_sell_value_sum_252d_to_mcap": {"inputs": ["insider_sell_value", "marketcap"], "func": f27_istj_009_insider_sell_value_sum_252d_to_mcap},
    "f27_istj_010_insider_sell_value_max_5d_rolling_63d": {"inputs": ["insider_sell_value"], "func": f27_istj_010_insider_sell_value_max_5d_rolling_63d},
    "f27_istj_011_insider_sell_value_max_21d_rolling_252d": {"inputs": ["insider_sell_value"], "func": f27_istj_011_insider_sell_value_max_21d_rolling_252d},
    "f27_istj_012_insider_sell_value_breadth_63d": {"inputs": ["insider_sell_value"], "func": f27_istj_012_insider_sell_value_breadth_63d},
    "f27_istj_013_insider_sell_value_breadth_252d": {"inputs": ["insider_sell_value"], "func": f27_istj_013_insider_sell_value_breadth_252d},
    "f27_istj_014_insider_sell_value_concentration_top1_63d": {"inputs": ["insider_sell_value"], "func": f27_istj_014_insider_sell_value_concentration_top1_63d},
    "f27_istj_015_insider_sell_value_concentration_top5_63d": {"inputs": ["insider_sell_value"], "func": f27_istj_015_insider_sell_value_concentration_top5_63d},
    "f27_istj_016_insider_net_value_21d": {"inputs": ["insider_buy_value", "insider_sell_value"], "func": f27_istj_016_insider_net_value_21d},
    "f27_istj_017_insider_net_value_63d": {"inputs": ["insider_buy_value", "insider_sell_value"], "func": f27_istj_017_insider_net_value_63d},
    "f27_istj_018_insider_net_value_252d": {"inputs": ["insider_buy_value", "insider_sell_value"], "func": f27_istj_018_insider_net_value_252d},
    "f27_istj_019_insider_buy_to_sell_value_ratio_63d": {"inputs": ["insider_buy_value", "insider_sell_value"], "func": f27_istj_019_insider_buy_to_sell_value_ratio_63d},
    "f27_istj_020_insider_buy_to_sell_value_ratio_252d": {"inputs": ["insider_buy_value", "insider_sell_value"], "func": f27_istj_020_insider_buy_to_sell_value_ratio_252d},
    "f27_istj_021_insider_buy_to_sell_count_ratio_63d": {"inputs": ["insider_buy_count", "insider_sell_count"], "func": f27_istj_021_insider_buy_to_sell_count_ratio_63d},
    "f27_istj_022_insider_buy_to_sell_count_ratio_252d": {"inputs": ["insider_buy_count", "insider_sell_count"], "func": f27_istj_022_insider_buy_to_sell_count_ratio_252d},
    "f27_istj_023_insider_sell_to_buy_share_ratio_63d": {"inputs": ["insider_sell_shares", "insider_buy_shares"], "func": f27_istj_023_insider_sell_to_buy_share_ratio_63d},
    "f27_istj_024_insider_net_value_to_mcap_63d": {"inputs": ["insider_buy_value", "insider_sell_value", "marketcap"], "func": f27_istj_024_insider_net_value_to_mcap_63d},
    "f27_istj_025_insider_net_value_to_mcap_252d": {"inputs": ["insider_buy_value", "insider_sell_value", "marketcap"], "func": f27_istj_025_insider_net_value_to_mcap_252d},
    "f27_istj_026_insider_sell_value_minus_buy_value_zscore_252d": {"inputs": ["insider_sell_value", "insider_buy_value"], "func": f27_istj_026_insider_sell_value_minus_buy_value_zscore_252d},
    "f27_istj_027_insider_buys_absent_streak": {"inputs": ["insider_buy_value"], "func": f27_istj_027_insider_buys_absent_streak},
    "f27_istj_028_insider_sells_absent_streak": {"inputs": ["insider_sell_value"], "func": f27_istj_028_insider_sells_absent_streak},
    "f27_istj_029_insider_buy_dry_up_63d": {"inputs": ["insider_buy_value"], "func": f27_istj_029_insider_buy_dry_up_63d},
    "f27_istj_030_insider_sell_persistence_63d": {"inputs": ["insider_sell_value"], "func": f27_istj_030_insider_sell_persistence_63d},
    "f27_istj_031_officer_sell_value_sum_63d": {"inputs": ["insider_officer_sell_value"], "func": f27_istj_031_officer_sell_value_sum_63d},
    "f27_istj_032_director_sell_value_sum_63d": {"inputs": ["insider_director_sell_value"], "func": f27_istj_032_director_sell_value_sum_63d},
    "f27_istj_033_tenpct_sell_value_sum_63d": {"inputs": ["insider_tenpct_sell_value"], "func": f27_istj_033_tenpct_sell_value_sum_63d},
    "f27_istj_034_officer_sell_value_share_63d": {"inputs": ["insider_officer_sell_value", "insider_sell_value"], "func": f27_istj_034_officer_sell_value_share_63d},
    "f27_istj_035_director_sell_value_share_63d": {"inputs": ["insider_director_sell_value", "insider_sell_value"], "func": f27_istj_035_director_sell_value_share_63d},
    "f27_istj_036_tenpct_sell_value_share_63d": {"inputs": ["insider_tenpct_sell_value", "insider_sell_value"], "func": f27_istj_036_tenpct_sell_value_share_63d},
    "f27_istj_037_officer_sell_to_mcap_63d": {"inputs": ["insider_officer_sell_value", "marketcap"], "func": f27_istj_037_officer_sell_to_mcap_63d},
    "f27_istj_038_director_sell_to_mcap_63d": {"inputs": ["insider_director_sell_value", "marketcap"], "func": f27_istj_038_director_sell_to_mcap_63d},
    "f27_istj_039_tenpct_sell_to_mcap_63d": {"inputs": ["insider_tenpct_sell_value", "marketcap"], "func": f27_istj_039_tenpct_sell_to_mcap_63d},
    "f27_istj_040_officer_sell_concentration_growth": {"inputs": ["insider_officer_sell_value", "insider_sell_value"], "func": f27_istj_040_officer_sell_concentration_growth},
    "f27_istj_041_director_sell_concentration_growth": {"inputs": ["insider_director_sell_value", "insider_sell_value"], "func": f27_istj_041_director_sell_concentration_growth},
    "f27_istj_042_tenpct_sell_to_total_sell_252d": {"inputs": ["insider_tenpct_sell_value", "insider_sell_value"], "func": f27_istj_042_tenpct_sell_to_total_sell_252d},
    "f27_istj_043_officer_buy_value_share_63d": {"inputs": ["insider_officer_buy_value", "insider_buy_value"], "func": f27_istj_043_officer_buy_value_share_63d},
    "f27_istj_044_officer_buy_vs_sell_disagreement": {"inputs": ["insider_officer_buy_value", "insider_sell_value"], "func": f27_istj_044_officer_buy_vs_sell_disagreement},
    "f27_istj_045_multi_role_sell_coincidence": {"inputs": ["insider_officer_sell_value", "insider_director_sell_value"], "func": f27_istj_045_multi_role_sell_coincidence},
    "f27_istj_046_insider_total_owned_yoy_change": {"inputs": ["insider_total_shares_owned"], "func": f27_istj_046_insider_total_owned_yoy_change},
    "f27_istj_047_insider_total_owned_qoq_change": {"inputs": ["insider_total_shares_owned"], "func": f27_istj_047_insider_total_owned_qoq_change},
    "f27_istj_048_insider_total_owned_drawdown_252d": {"inputs": ["insider_total_shares_owned"], "func": f27_istj_048_insider_total_owned_drawdown_252d},
    "f27_istj_049_insider_total_owned_drawdown_504d": {"inputs": ["insider_total_shares_owned"], "func": f27_istj_049_insider_total_owned_drawdown_504d},
    "f27_istj_050_insider_n_reporters_change_252d": {"inputs": ["insider_n_reporters"], "func": f27_istj_050_insider_n_reporters_change_252d},
    "f27_istj_051_insider_sellers_unique_rolling_63d_sum": {"inputs": ["insider_sellers_unique"], "func": f27_istj_051_insider_sellers_unique_rolling_63d_sum},
    "f27_istj_052_insider_unique_sellers_to_unique_buyers_63d": {"inputs": ["insider_sellers_unique", "insider_buyers_unique"], "func": f27_istj_052_insider_unique_sellers_to_unique_buyers_63d},
    "f27_istj_053_insider_unique_sellers_growth_252d": {"inputs": ["insider_sellers_unique"], "func": f27_istj_053_insider_unique_sellers_growth_252d},
    "f27_istj_054_insider_sell_breadth_acceleration": {"inputs": ["insider_sell_value"], "func": f27_istj_054_insider_sell_breadth_acceleration},
    "f27_istj_055_insider_participation_in_decline": {"inputs": ["insider_sell_value", "close"], "func": f27_istj_055_insider_participation_in_decline},
    "f27_istj_056_insider_directors_exiting_count_252d": {"inputs": ["insider_director_sell_value", "insider_director_buy_value"], "func": f27_istj_056_insider_directors_exiting_count_252d},
    "f27_istj_057_insider_officers_exiting_count_252d": {"inputs": ["insider_officer_sell_value", "insider_officer_buy_value"], "func": f27_istj_057_insider_officers_exiting_count_252d},
    "f27_istj_058_insider_total_owned_zscore_252d": {"inputs": ["insider_total_shares_owned"], "func": f27_istj_058_insider_total_owned_zscore_252d},
    "f27_istj_059_insider_ownership_decline_rate_252d": {"inputs": ["insider_total_shares_owned"], "func": f27_istj_059_insider_ownership_decline_rate_252d},
    "f27_istj_060_insider_buyer_exhaustion_index": {"inputs": ["insider_buyers_unique", "insider_sellers_unique"], "func": f27_istj_060_insider_buyer_exhaustion_index},
    "f27_istj_061_insider_sell_cluster_score_5d": {"inputs": ["insider_sellers_unique"], "func": f27_istj_061_insider_sell_cluster_score_5d},
    "f27_istj_062_insider_sell_cluster_score_21d": {"inputs": ["insider_sellers_unique"], "func": f27_istj_062_insider_sell_cluster_score_21d},
    "f27_istj_063_insider_sell_cluster_score_63d": {"inputs": ["insider_sellers_unique"], "func": f27_istj_063_insider_sell_cluster_score_63d},
    "f27_istj_064_insider_sell_cluster_max_5d_in_63d": {"inputs": ["insider_sellers_unique"], "func": f27_istj_064_insider_sell_cluster_max_5d_in_63d},
    "f27_istj_065_insider_consecutive_sell_weeks": {"inputs": ["insider_sell_value"], "func": f27_istj_065_insider_consecutive_sell_weeks},
    "f27_istj_066_insider_consecutive_no_buy_weeks": {"inputs": ["insider_buy_value"], "func": f27_istj_066_insider_consecutive_no_buy_weeks},
    "f27_istj_067_insider_sells_per_week_avg_63d": {"inputs": ["insider_sell_count"], "func": f27_istj_067_insider_sells_per_week_avg_63d},
    "f27_istj_068_insider_sell_value_per_seller_63d": {"inputs": ["insider_sell_value", "insider_sellers_unique"], "func": f27_istj_068_insider_sell_value_per_seller_63d},
    "f27_istj_069_insider_sell_value_per_seller_252d": {"inputs": ["insider_sell_value", "insider_sellers_unique"], "func": f27_istj_069_insider_sell_value_per_seller_252d},
    "f27_istj_070_insider_burst_count_63d": {"inputs": ["insider_sell_value", "marketcap"], "func": f27_istj_070_insider_burst_count_63d},
    "f27_istj_071_insider_cluster_breadth_4w_then_8w": {"inputs": ["insider_sellers_unique"], "func": f27_istj_071_insider_cluster_breadth_4w_then_8w},
    "f27_istj_072_days_since_last_insider_buy": {"inputs": ["insider_buy_value"], "func": f27_istj_072_days_since_last_insider_buy},
    "f27_istj_073_days_since_last_insider_sell": {"inputs": ["insider_sell_value"], "func": f27_istj_073_days_since_last_insider_sell},
    "f27_istj_074_days_since_last_officer_buy": {"inputs": ["insider_officer_buy_value"], "func": f27_istj_074_days_since_last_officer_buy},
    "f27_istj_075_days_since_last_cluster_buy_5d": {"inputs": ["insider_buy_value"], "func": f27_istj_075_days_since_last_cluster_buy_5d},
}
