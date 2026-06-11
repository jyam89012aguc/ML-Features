"""insider_selling_trajectory d2 features 001-075 — order-2 difference of corresponding base features.

Each function inlines the base body and wraps the return value with .diff().diff(). Self-contained; helpers redefined locally per HANDOFF."""
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
    idx = num.index if hasattr(num, 'index') else None
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

def f27_istj_001_insider_sell_value_sum_21d_d2(insider_sell_value):
    return insider_sell_value.rolling(21, min_periods=5).sum().diff().diff()

def f27_istj_002_insider_sell_value_sum_63d_d2(insider_sell_value):
    return insider_sell_value.rolling(63, min_periods=15).sum().diff().diff()

def f27_istj_003_insider_sell_value_sum_126d_d2(insider_sell_value):
    return insider_sell_value.rolling(126, min_periods=30).sum().diff().diff()

def f27_istj_004_insider_sell_value_sum_252d_d2(insider_sell_value):
    return insider_sell_value.rolling(252, min_periods=60).sum().diff().diff()

def f27_istj_005_insider_sell_count_sum_63d_d2(insider_sell_count):
    return insider_sell_count.rolling(63, min_periods=15).sum().diff().diff()

def f27_istj_006_insider_sell_shares_sum_63d_d2(insider_sell_shares):
    return insider_sell_shares.rolling(63, min_periods=15).sum().diff().diff()

def f27_istj_007_insider_sell_value_sum_21d_to_mcap_d2(insider_sell_value, marketcap):
    return _safe_div(insider_sell_value.rolling(21, min_periods=5).sum(), marketcap).diff().diff()

def f27_istj_008_insider_sell_value_sum_63d_to_mcap_d2(insider_sell_value, marketcap):
    return _safe_div(insider_sell_value.rolling(63, min_periods=15).sum(), marketcap).diff().diff()

def f27_istj_009_insider_sell_value_sum_252d_to_mcap_d2(insider_sell_value, marketcap):
    return _safe_div(insider_sell_value.rolling(252, min_periods=60).sum(), marketcap).diff().diff()

def f27_istj_010_insider_sell_value_max_5d_rolling_63d_d2(insider_sell_value):
    return insider_sell_value.rolling(5, min_periods=1).sum().rolling(63, min_periods=15).max().diff().diff()

def f27_istj_011_insider_sell_value_max_21d_rolling_252d_d2(insider_sell_value):
    return insider_sell_value.rolling(21, min_periods=5).sum().rolling(252, min_periods=60).max().diff().diff()

def f27_istj_012_insider_sell_value_breadth_63d_d2(insider_sell_value):
    return (insider_sell_value > 0).astype(float).rolling(63, min_periods=15).mean().diff().diff()

def f27_istj_013_insider_sell_value_breadth_252d_d2(insider_sell_value):
    return (insider_sell_value > 0).astype(float).rolling(252, min_periods=60).mean().diff().diff()

def f27_istj_014_insider_sell_value_concentration_top1_63d_d2(insider_sell_value):
    top = insider_sell_value.rolling(63, min_periods=15).max()
    tot = insider_sell_value.rolling(63, min_periods=15).sum()
    return _safe_div(top, tot).diff().diff()

def f27_istj_015_insider_sell_value_concentration_top5_63d_d2(insider_sell_value):
    top5 = insider_sell_value.rolling(63, min_periods=15).apply(lambda y: float(np.nansum(np.sort(y)[-5:])) if np.isfinite(y).sum() >= 5 else np.nan, raw=True)
    tot = insider_sell_value.rolling(63, min_periods=15).sum()
    return _safe_div(top5, tot).diff().diff()

def f27_istj_016_insider_net_value_21d_d2(insider_buy_value, insider_sell_value):
    return (insider_buy_value - insider_sell_value).rolling(21, min_periods=5).sum().diff().diff()

def f27_istj_017_insider_net_value_63d_d2(insider_buy_value, insider_sell_value):
    return (insider_buy_value - insider_sell_value).rolling(63, min_periods=15).sum().diff().diff()

def f27_istj_018_insider_net_value_252d_d2(insider_buy_value, insider_sell_value):
    return (insider_buy_value - insider_sell_value).rolling(252, min_periods=60).sum().diff().diff()

def f27_istj_019_insider_buy_to_sell_value_ratio_63d_d2(insider_buy_value, insider_sell_value):
    return _safe_div(insider_buy_value.rolling(63, min_periods=15).sum(), insider_sell_value.rolling(63, min_periods=15).sum()).diff().diff()

def f27_istj_020_insider_buy_to_sell_value_ratio_252d_d2(insider_buy_value, insider_sell_value):
    return _safe_div(insider_buy_value.rolling(252, min_periods=60).sum(), insider_sell_value.rolling(252, min_periods=60).sum()).diff().diff()

def f27_istj_021_insider_buy_to_sell_count_ratio_63d_d2(insider_buy_count, insider_sell_count):
    return _safe_div(insider_buy_count.rolling(63, min_periods=15).sum(), insider_sell_count.rolling(63, min_periods=15).sum()).diff().diff()

def f27_istj_022_insider_buy_to_sell_count_ratio_252d_d2(insider_buy_count, insider_sell_count):
    return _safe_div(insider_buy_count.rolling(252, min_periods=60).sum(), insider_sell_count.rolling(252, min_periods=60).sum()).diff().diff()

def f27_istj_023_insider_sell_to_buy_share_ratio_63d_d2(insider_sell_shares, insider_buy_shares):
    return _safe_div(insider_sell_shares.rolling(63, min_periods=15).sum(), insider_buy_shares.rolling(63, min_periods=15).sum()).diff().diff()

def f27_istj_024_insider_net_value_to_mcap_63d_d2(insider_buy_value, insider_sell_value, marketcap):
    return _safe_div((insider_buy_value - insider_sell_value).rolling(63, min_periods=15).sum(), marketcap).diff().diff()

def f27_istj_025_insider_net_value_to_mcap_252d_d2(insider_buy_value, insider_sell_value, marketcap):
    return _safe_div((insider_buy_value - insider_sell_value).rolling(252, min_periods=60).sum(), marketcap).diff().diff()

def f27_istj_026_insider_sell_value_minus_buy_value_zscore_252d_d2(insider_sell_value, insider_buy_value):
    return _rolling_zscore(insider_sell_value - insider_buy_value, 252, min_periods=60).diff().diff()

def f27_istj_027_insider_buys_absent_streak_d2(insider_buy_value):
    return _runlen_zero(insider_buy_value).diff().diff()

def f27_istj_028_insider_sells_absent_streak_d2(insider_sell_value):
    return _runlen_zero(insider_sell_value).diff().diff()

def f27_istj_029_insider_buy_dry_up_63d_d2(insider_buy_value):
    return (insider_buy_value.rolling(63, min_periods=15).sum() == 0).astype(float).diff().diff()

def f27_istj_030_insider_sell_persistence_63d_d2(insider_sell_value):
    weekly = insider_sell_value.rolling(5, min_periods=1).sum()
    return (weekly > 0).astype(float).rolling(63, min_periods=15).mean().diff().diff()

def f27_istj_031_officer_sell_value_sum_63d_d2(insider_officer_sell_value):
    return insider_officer_sell_value.rolling(63, min_periods=15).sum().diff().diff()

def f27_istj_032_director_sell_value_sum_63d_d2(insider_director_sell_value):
    return insider_director_sell_value.rolling(63, min_periods=15).sum().diff().diff()

def f27_istj_033_tenpct_sell_value_sum_63d_d2(insider_tenpct_sell_value):
    return insider_tenpct_sell_value.rolling(63, min_periods=15).sum().diff().diff()

def f27_istj_034_officer_sell_value_share_63d_d2(insider_officer_sell_value, insider_sell_value):
    return _safe_div(insider_officer_sell_value.rolling(63, min_periods=15).sum(), insider_sell_value.rolling(63, min_periods=15).sum()).diff().diff()

def f27_istj_035_director_sell_value_share_63d_d2(insider_director_sell_value, insider_sell_value):
    return _safe_div(insider_director_sell_value.rolling(63, min_periods=15).sum(), insider_sell_value.rolling(63, min_periods=15).sum()).diff().diff()

def f27_istj_036_tenpct_sell_value_share_63d_d2(insider_tenpct_sell_value, insider_sell_value):
    return _safe_div(insider_tenpct_sell_value.rolling(63, min_periods=15).sum(), insider_sell_value.rolling(63, min_periods=15).sum()).diff().diff()

def f27_istj_037_officer_sell_to_mcap_63d_d2(insider_officer_sell_value, marketcap):
    return _safe_div(insider_officer_sell_value.rolling(63, min_periods=15).sum(), marketcap).diff().diff()

def f27_istj_038_director_sell_to_mcap_63d_d2(insider_director_sell_value, marketcap):
    return _safe_div(insider_director_sell_value.rolling(63, min_periods=15).sum(), marketcap).diff().diff()

def f27_istj_039_tenpct_sell_to_mcap_63d_d2(insider_tenpct_sell_value, marketcap):
    return _safe_div(insider_tenpct_sell_value.rolling(63, min_periods=15).sum(), marketcap).diff().diff()

def f27_istj_040_officer_sell_concentration_growth_d2(insider_officer_sell_value, insider_sell_value):
    r63 = _safe_div(insider_officer_sell_value.rolling(63, min_periods=15).sum(), insider_sell_value.rolling(63, min_periods=15).sum())
    r252 = _safe_div(insider_officer_sell_value.rolling(252, min_periods=60).sum(), insider_sell_value.rolling(252, min_periods=60).sum())
    return (r63 - r252).diff().diff()

def f27_istj_041_director_sell_concentration_growth_d2(insider_director_sell_value, insider_sell_value):
    r63 = _safe_div(insider_director_sell_value.rolling(63, min_periods=15).sum(), insider_sell_value.rolling(63, min_periods=15).sum())
    r252 = _safe_div(insider_director_sell_value.rolling(252, min_periods=60).sum(), insider_sell_value.rolling(252, min_periods=60).sum())
    return (r63 - r252).diff().diff()

def f27_istj_042_tenpct_sell_to_total_sell_252d_d2(insider_tenpct_sell_value, insider_sell_value):
    return _safe_div(insider_tenpct_sell_value.rolling(252, min_periods=60).sum(), insider_sell_value.rolling(252, min_periods=60).sum()).diff().diff()

def f27_istj_043_officer_buy_value_share_63d_d2(insider_officer_buy_value, insider_buy_value):
    return _safe_div(insider_officer_buy_value.rolling(63, min_periods=15).sum(), insider_buy_value.rolling(63, min_periods=15).sum()).diff().diff()

def f27_istj_044_officer_buy_vs_sell_disagreement_d2(insider_officer_buy_value, insider_sell_value):
    buy = insider_officer_buy_value.rolling(63, min_periods=15).sum()
    sell = insider_sell_value.rolling(63, min_periods=15).sum()
    return _safe_div(buy - sell, (buy + sell).abs()).diff().diff()

def f27_istj_045_multi_role_sell_coincidence_d2(insider_officer_sell_value, insider_director_sell_value):
    of_w = (insider_officer_sell_value.rolling(5, min_periods=1).sum() > 0).astype(float)
    di_w = (insider_director_sell_value.rolling(5, min_periods=1).sum() > 0).astype(float)
    return (of_w * di_w).rolling(63, min_periods=15).sum().diff().diff()

def f27_istj_046_insider_total_owned_yoy_change_d2(insider_total_shares_owned):
    return _safe_div(insider_total_shares_owned - insider_total_shares_owned.shift(252), insider_total_shares_owned.shift(252).abs()).diff().diff()

def f27_istj_047_insider_total_owned_qoq_change_d2(insider_total_shares_owned):
    return _safe_div(insider_total_shares_owned - insider_total_shares_owned.shift(63), insider_total_shares_owned.shift(63).abs()).diff().diff()

def f27_istj_048_insider_total_owned_drawdown_252d_d2(insider_total_shares_owned):
    hi = insider_total_shares_owned.rolling(252, min_periods=60).max()
    return _safe_div(insider_total_shares_owned - hi, hi.abs()).diff().diff()

def f27_istj_049_insider_total_owned_drawdown_504d_d2(insider_total_shares_owned):
    hi = insider_total_shares_owned.rolling(504, min_periods=120).max()
    return _safe_div(insider_total_shares_owned - hi, hi.abs()).diff().diff()

def f27_istj_050_insider_n_reporters_change_252d_d2(insider_n_reporters):
    return (insider_n_reporters - insider_n_reporters.shift(252)).diff().diff()

def f27_istj_051_insider_sellers_unique_rolling_63d_sum_d2(insider_sellers_unique):
    return insider_sellers_unique.rolling(63, min_periods=15).sum().diff().diff()

def f27_istj_052_insider_unique_sellers_to_unique_buyers_63d_d2(insider_sellers_unique, insider_buyers_unique):
    return _safe_div(insider_sellers_unique.rolling(63, min_periods=15).sum(), insider_buyers_unique.rolling(63, min_periods=15).sum()).diff().diff()

def f27_istj_053_insider_unique_sellers_growth_252d_d2(insider_sellers_unique):
    cur = insider_sellers_unique.rolling(63, min_periods=15).sum()
    return _safe_div(cur - cur.shift(252), cur.shift(252).abs()).diff().diff()

def f27_istj_054_insider_sell_breadth_acceleration_d2(insider_sell_value):
    b63 = (insider_sell_value > 0).astype(float).rolling(63, min_periods=15).mean()
    b252 = (insider_sell_value > 0).astype(float).rolling(252, min_periods=60).mean()
    return (b63 - b252).diff().diff()

def f27_istj_055_insider_participation_in_decline_d2(insider_sell_value, close):
    falling = (close < close.shift(21)).astype(float)
    return (insider_sell_value * falling).rolling(63, min_periods=15).sum().diff().diff()

def f27_istj_056_insider_directors_exiting_count_252d_d2(insider_director_sell_value, insider_director_buy_value):
    net = insider_director_sell_value - insider_director_buy_value
    return (net > 0).astype(float).rolling(252, min_periods=60).sum().diff().diff()

def f27_istj_057_insider_officers_exiting_count_252d_d2(insider_officer_sell_value, insider_officer_buy_value):
    net = insider_officer_sell_value - insider_officer_buy_value
    return (net > 0).astype(float).rolling(252, min_periods=60).sum().diff().diff()

def f27_istj_058_insider_total_owned_zscore_252d_d2(insider_total_shares_owned):
    return _rolling_zscore(insider_total_shares_owned, 252, min_periods=60).diff().diff()

def f27_istj_059_insider_ownership_decline_rate_252d_d2(insider_total_shares_owned):
    return _safe_div(insider_total_shares_owned.diff(252), insider_total_shares_owned.shift(252).abs()).diff().diff()

def f27_istj_060_insider_buyer_exhaustion_index_d2(insider_buyers_unique, insider_sellers_unique):
    return _safe_div(insider_buyers_unique.rolling(252, min_periods=60).sum(), (insider_buyers_unique + insider_sellers_unique).rolling(252, min_periods=60).sum()).diff().diff()

def f27_istj_061_insider_sell_cluster_score_5d_d2(insider_sellers_unique):
    return insider_sellers_unique.rolling(5, min_periods=1).sum().diff().diff()

def f27_istj_062_insider_sell_cluster_score_21d_d2(insider_sellers_unique):
    return insider_sellers_unique.rolling(21, min_periods=5).sum().diff().diff()

def f27_istj_063_insider_sell_cluster_score_63d_d2(insider_sellers_unique):
    return insider_sellers_unique.rolling(63, min_periods=15).sum().diff().diff()

def f27_istj_064_insider_sell_cluster_max_5d_in_63d_d2(insider_sellers_unique):
    return insider_sellers_unique.rolling(5, min_periods=1).sum().rolling(63, min_periods=15).max().diff().diff()

def f27_istj_065_insider_consecutive_sell_weeks_d2(insider_sell_value):
    weekly = insider_sell_value.rolling(5, min_periods=1).sum()
    return _runlen_pos(weekly).diff().diff()

def f27_istj_066_insider_consecutive_no_buy_weeks_d2(insider_buy_value):
    weekly = insider_buy_value.rolling(5, min_periods=1).sum()
    return _runlen_zero(weekly).diff().diff()

def f27_istj_067_insider_sells_per_week_avg_63d_d2(insider_sell_count):
    return (insider_sell_count.rolling(63, min_periods=15).sum() / (63.0 / 5.0)).diff().diff()

def f27_istj_068_insider_sell_value_per_seller_63d_d2(insider_sell_value, insider_sellers_unique):
    return _safe_div(insider_sell_value.rolling(63, min_periods=15).sum(), insider_sellers_unique.rolling(63, min_periods=15).sum()).diff().diff()

def f27_istj_069_insider_sell_value_per_seller_252d_d2(insider_sell_value, insider_sellers_unique):
    return _safe_div(insider_sell_value.rolling(252, min_periods=60).sum(), insider_sellers_unique.rolling(252, min_periods=60).sum()).diff().diff()

def f27_istj_070_insider_burst_count_63d_d2(insider_sell_value, marketcap):
    weekly_pct = _safe_div(insider_sell_value.rolling(5, min_periods=1).sum(), marketcap)
    return (weekly_pct > 0.01).astype(float).rolling(63, min_periods=15).sum().diff().diff()

def f27_istj_071_insider_cluster_breadth_4w_then_8w_d2(insider_sellers_unique):
    s4 = insider_sellers_unique.rolling(21, min_periods=5).sum()
    s8 = insider_sellers_unique.rolling(42, min_periods=10).sum()
    return _safe_div(s4, s8).diff().diff()

def f27_istj_072_days_since_last_insider_buy_d2(insider_buy_value):
    return _runlen_zero(insider_buy_value).diff().diff()

def f27_istj_073_days_since_last_insider_sell_d2(insider_sell_value):
    return _runlen_zero(insider_sell_value).diff().diff()

def f27_istj_074_days_since_last_officer_buy_d2(insider_officer_buy_value):
    return _runlen_zero(insider_officer_buy_value).diff().diff()

def f27_istj_075_days_since_last_cluster_buy_5d_d2(insider_buy_value):
    weekly = insider_buy_value.rolling(5, min_periods=1).sum()
    return _runlen_zero(weekly).diff().diff()
INSIDER_SELLING_TRAJECTORY_D2_REGISTRY_001_075 = {'f27_istj_001_insider_sell_value_sum_21d_d2': {'inputs': ['insider_sell_value'], 'func': f27_istj_001_insider_sell_value_sum_21d_d2}, 'f27_istj_002_insider_sell_value_sum_63d_d2': {'inputs': ['insider_sell_value'], 'func': f27_istj_002_insider_sell_value_sum_63d_d2}, 'f27_istj_003_insider_sell_value_sum_126d_d2': {'inputs': ['insider_sell_value'], 'func': f27_istj_003_insider_sell_value_sum_126d_d2}, 'f27_istj_004_insider_sell_value_sum_252d_d2': {'inputs': ['insider_sell_value'], 'func': f27_istj_004_insider_sell_value_sum_252d_d2}, 'f27_istj_005_insider_sell_count_sum_63d_d2': {'inputs': ['insider_sell_count'], 'func': f27_istj_005_insider_sell_count_sum_63d_d2}, 'f27_istj_006_insider_sell_shares_sum_63d_d2': {'inputs': ['insider_sell_shares'], 'func': f27_istj_006_insider_sell_shares_sum_63d_d2}, 'f27_istj_007_insider_sell_value_sum_21d_to_mcap_d2': {'inputs': ['insider_sell_value', 'marketcap'], 'func': f27_istj_007_insider_sell_value_sum_21d_to_mcap_d2}, 'f27_istj_008_insider_sell_value_sum_63d_to_mcap_d2': {'inputs': ['insider_sell_value', 'marketcap'], 'func': f27_istj_008_insider_sell_value_sum_63d_to_mcap_d2}, 'f27_istj_009_insider_sell_value_sum_252d_to_mcap_d2': {'inputs': ['insider_sell_value', 'marketcap'], 'func': f27_istj_009_insider_sell_value_sum_252d_to_mcap_d2}, 'f27_istj_010_insider_sell_value_max_5d_rolling_63d_d2': {'inputs': ['insider_sell_value'], 'func': f27_istj_010_insider_sell_value_max_5d_rolling_63d_d2}, 'f27_istj_011_insider_sell_value_max_21d_rolling_252d_d2': {'inputs': ['insider_sell_value'], 'func': f27_istj_011_insider_sell_value_max_21d_rolling_252d_d2}, 'f27_istj_012_insider_sell_value_breadth_63d_d2': {'inputs': ['insider_sell_value'], 'func': f27_istj_012_insider_sell_value_breadth_63d_d2}, 'f27_istj_013_insider_sell_value_breadth_252d_d2': {'inputs': ['insider_sell_value'], 'func': f27_istj_013_insider_sell_value_breadth_252d_d2}, 'f27_istj_014_insider_sell_value_concentration_top1_63d_d2': {'inputs': ['insider_sell_value'], 'func': f27_istj_014_insider_sell_value_concentration_top1_63d_d2}, 'f27_istj_015_insider_sell_value_concentration_top5_63d_d2': {'inputs': ['insider_sell_value'], 'func': f27_istj_015_insider_sell_value_concentration_top5_63d_d2}, 'f27_istj_016_insider_net_value_21d_d2': {'inputs': ['insider_buy_value', 'insider_sell_value'], 'func': f27_istj_016_insider_net_value_21d_d2}, 'f27_istj_017_insider_net_value_63d_d2': {'inputs': ['insider_buy_value', 'insider_sell_value'], 'func': f27_istj_017_insider_net_value_63d_d2}, 'f27_istj_018_insider_net_value_252d_d2': {'inputs': ['insider_buy_value', 'insider_sell_value'], 'func': f27_istj_018_insider_net_value_252d_d2}, 'f27_istj_019_insider_buy_to_sell_value_ratio_63d_d2': {'inputs': ['insider_buy_value', 'insider_sell_value'], 'func': f27_istj_019_insider_buy_to_sell_value_ratio_63d_d2}, 'f27_istj_020_insider_buy_to_sell_value_ratio_252d_d2': {'inputs': ['insider_buy_value', 'insider_sell_value'], 'func': f27_istj_020_insider_buy_to_sell_value_ratio_252d_d2}, 'f27_istj_021_insider_buy_to_sell_count_ratio_63d_d2': {'inputs': ['insider_buy_count', 'insider_sell_count'], 'func': f27_istj_021_insider_buy_to_sell_count_ratio_63d_d2}, 'f27_istj_022_insider_buy_to_sell_count_ratio_252d_d2': {'inputs': ['insider_buy_count', 'insider_sell_count'], 'func': f27_istj_022_insider_buy_to_sell_count_ratio_252d_d2}, 'f27_istj_023_insider_sell_to_buy_share_ratio_63d_d2': {'inputs': ['insider_sell_shares', 'insider_buy_shares'], 'func': f27_istj_023_insider_sell_to_buy_share_ratio_63d_d2}, 'f27_istj_024_insider_net_value_to_mcap_63d_d2': {'inputs': ['insider_buy_value', 'insider_sell_value', 'marketcap'], 'func': f27_istj_024_insider_net_value_to_mcap_63d_d2}, 'f27_istj_025_insider_net_value_to_mcap_252d_d2': {'inputs': ['insider_buy_value', 'insider_sell_value', 'marketcap'], 'func': f27_istj_025_insider_net_value_to_mcap_252d_d2}, 'f27_istj_026_insider_sell_value_minus_buy_value_zscore_252d_d2': {'inputs': ['insider_sell_value', 'insider_buy_value'], 'func': f27_istj_026_insider_sell_value_minus_buy_value_zscore_252d_d2}, 'f27_istj_027_insider_buys_absent_streak_d2': {'inputs': ['insider_buy_value'], 'func': f27_istj_027_insider_buys_absent_streak_d2}, 'f27_istj_028_insider_sells_absent_streak_d2': {'inputs': ['insider_sell_value'], 'func': f27_istj_028_insider_sells_absent_streak_d2}, 'f27_istj_029_insider_buy_dry_up_63d_d2': {'inputs': ['insider_buy_value'], 'func': f27_istj_029_insider_buy_dry_up_63d_d2}, 'f27_istj_030_insider_sell_persistence_63d_d2': {'inputs': ['insider_sell_value'], 'func': f27_istj_030_insider_sell_persistence_63d_d2}, 'f27_istj_031_officer_sell_value_sum_63d_d2': {'inputs': ['insider_officer_sell_value'], 'func': f27_istj_031_officer_sell_value_sum_63d_d2}, 'f27_istj_032_director_sell_value_sum_63d_d2': {'inputs': ['insider_director_sell_value'], 'func': f27_istj_032_director_sell_value_sum_63d_d2}, 'f27_istj_033_tenpct_sell_value_sum_63d_d2': {'inputs': ['insider_tenpct_sell_value'], 'func': f27_istj_033_tenpct_sell_value_sum_63d_d2}, 'f27_istj_034_officer_sell_value_share_63d_d2': {'inputs': ['insider_officer_sell_value', 'insider_sell_value'], 'func': f27_istj_034_officer_sell_value_share_63d_d2}, 'f27_istj_035_director_sell_value_share_63d_d2': {'inputs': ['insider_director_sell_value', 'insider_sell_value'], 'func': f27_istj_035_director_sell_value_share_63d_d2}, 'f27_istj_036_tenpct_sell_value_share_63d_d2': {'inputs': ['insider_tenpct_sell_value', 'insider_sell_value'], 'func': f27_istj_036_tenpct_sell_value_share_63d_d2}, 'f27_istj_037_officer_sell_to_mcap_63d_d2': {'inputs': ['insider_officer_sell_value', 'marketcap'], 'func': f27_istj_037_officer_sell_to_mcap_63d_d2}, 'f27_istj_038_director_sell_to_mcap_63d_d2': {'inputs': ['insider_director_sell_value', 'marketcap'], 'func': f27_istj_038_director_sell_to_mcap_63d_d2}, 'f27_istj_039_tenpct_sell_to_mcap_63d_d2': {'inputs': ['insider_tenpct_sell_value', 'marketcap'], 'func': f27_istj_039_tenpct_sell_to_mcap_63d_d2}, 'f27_istj_040_officer_sell_concentration_growth_d2': {'inputs': ['insider_officer_sell_value', 'insider_sell_value'], 'func': f27_istj_040_officer_sell_concentration_growth_d2}, 'f27_istj_041_director_sell_concentration_growth_d2': {'inputs': ['insider_director_sell_value', 'insider_sell_value'], 'func': f27_istj_041_director_sell_concentration_growth_d2}, 'f27_istj_042_tenpct_sell_to_total_sell_252d_d2': {'inputs': ['insider_tenpct_sell_value', 'insider_sell_value'], 'func': f27_istj_042_tenpct_sell_to_total_sell_252d_d2}, 'f27_istj_043_officer_buy_value_share_63d_d2': {'inputs': ['insider_officer_buy_value', 'insider_buy_value'], 'func': f27_istj_043_officer_buy_value_share_63d_d2}, 'f27_istj_044_officer_buy_vs_sell_disagreement_d2': {'inputs': ['insider_officer_buy_value', 'insider_sell_value'], 'func': f27_istj_044_officer_buy_vs_sell_disagreement_d2}, 'f27_istj_045_multi_role_sell_coincidence_d2': {'inputs': ['insider_officer_sell_value', 'insider_director_sell_value'], 'func': f27_istj_045_multi_role_sell_coincidence_d2}, 'f27_istj_046_insider_total_owned_yoy_change_d2': {'inputs': ['insider_total_shares_owned'], 'func': f27_istj_046_insider_total_owned_yoy_change_d2}, 'f27_istj_047_insider_total_owned_qoq_change_d2': {'inputs': ['insider_total_shares_owned'], 'func': f27_istj_047_insider_total_owned_qoq_change_d2}, 'f27_istj_048_insider_total_owned_drawdown_252d_d2': {'inputs': ['insider_total_shares_owned'], 'func': f27_istj_048_insider_total_owned_drawdown_252d_d2}, 'f27_istj_049_insider_total_owned_drawdown_504d_d2': {'inputs': ['insider_total_shares_owned'], 'func': f27_istj_049_insider_total_owned_drawdown_504d_d2}, 'f27_istj_050_insider_n_reporters_change_252d_d2': {'inputs': ['insider_n_reporters'], 'func': f27_istj_050_insider_n_reporters_change_252d_d2}, 'f27_istj_051_insider_sellers_unique_rolling_63d_sum_d2': {'inputs': ['insider_sellers_unique'], 'func': f27_istj_051_insider_sellers_unique_rolling_63d_sum_d2}, 'f27_istj_052_insider_unique_sellers_to_unique_buyers_63d_d2': {'inputs': ['insider_sellers_unique', 'insider_buyers_unique'], 'func': f27_istj_052_insider_unique_sellers_to_unique_buyers_63d_d2}, 'f27_istj_053_insider_unique_sellers_growth_252d_d2': {'inputs': ['insider_sellers_unique'], 'func': f27_istj_053_insider_unique_sellers_growth_252d_d2}, 'f27_istj_054_insider_sell_breadth_acceleration_d2': {'inputs': ['insider_sell_value'], 'func': f27_istj_054_insider_sell_breadth_acceleration_d2}, 'f27_istj_055_insider_participation_in_decline_d2': {'inputs': ['insider_sell_value', 'close'], 'func': f27_istj_055_insider_participation_in_decline_d2}, 'f27_istj_056_insider_directors_exiting_count_252d_d2': {'inputs': ['insider_director_sell_value', 'insider_director_buy_value'], 'func': f27_istj_056_insider_directors_exiting_count_252d_d2}, 'f27_istj_057_insider_officers_exiting_count_252d_d2': {'inputs': ['insider_officer_sell_value', 'insider_officer_buy_value'], 'func': f27_istj_057_insider_officers_exiting_count_252d_d2}, 'f27_istj_058_insider_total_owned_zscore_252d_d2': {'inputs': ['insider_total_shares_owned'], 'func': f27_istj_058_insider_total_owned_zscore_252d_d2}, 'f27_istj_059_insider_ownership_decline_rate_252d_d2': {'inputs': ['insider_total_shares_owned'], 'func': f27_istj_059_insider_ownership_decline_rate_252d_d2}, 'f27_istj_060_insider_buyer_exhaustion_index_d2': {'inputs': ['insider_buyers_unique', 'insider_sellers_unique'], 'func': f27_istj_060_insider_buyer_exhaustion_index_d2}, 'f27_istj_061_insider_sell_cluster_score_5d_d2': {'inputs': ['insider_sellers_unique'], 'func': f27_istj_061_insider_sell_cluster_score_5d_d2}, 'f27_istj_062_insider_sell_cluster_score_21d_d2': {'inputs': ['insider_sellers_unique'], 'func': f27_istj_062_insider_sell_cluster_score_21d_d2}, 'f27_istj_063_insider_sell_cluster_score_63d_d2': {'inputs': ['insider_sellers_unique'], 'func': f27_istj_063_insider_sell_cluster_score_63d_d2}, 'f27_istj_064_insider_sell_cluster_max_5d_in_63d_d2': {'inputs': ['insider_sellers_unique'], 'func': f27_istj_064_insider_sell_cluster_max_5d_in_63d_d2}, 'f27_istj_065_insider_consecutive_sell_weeks_d2': {'inputs': ['insider_sell_value'], 'func': f27_istj_065_insider_consecutive_sell_weeks_d2}, 'f27_istj_066_insider_consecutive_no_buy_weeks_d2': {'inputs': ['insider_buy_value'], 'func': f27_istj_066_insider_consecutive_no_buy_weeks_d2}, 'f27_istj_067_insider_sells_per_week_avg_63d_d2': {'inputs': ['insider_sell_count'], 'func': f27_istj_067_insider_sells_per_week_avg_63d_d2}, 'f27_istj_068_insider_sell_value_per_seller_63d_d2': {'inputs': ['insider_sell_value', 'insider_sellers_unique'], 'func': f27_istj_068_insider_sell_value_per_seller_63d_d2}, 'f27_istj_069_insider_sell_value_per_seller_252d_d2': {'inputs': ['insider_sell_value', 'insider_sellers_unique'], 'func': f27_istj_069_insider_sell_value_per_seller_252d_d2}, 'f27_istj_070_insider_burst_count_63d_d2': {'inputs': ['insider_sell_value', 'marketcap'], 'func': f27_istj_070_insider_burst_count_63d_d2}, 'f27_istj_071_insider_cluster_breadth_4w_then_8w_d2': {'inputs': ['insider_sellers_unique'], 'func': f27_istj_071_insider_cluster_breadth_4w_then_8w_d2}, 'f27_istj_072_days_since_last_insider_buy_d2': {'inputs': ['insider_buy_value'], 'func': f27_istj_072_days_since_last_insider_buy_d2}, 'f27_istj_073_days_since_last_insider_sell_d2': {'inputs': ['insider_sell_value'], 'func': f27_istj_073_days_since_last_insider_sell_d2}, 'f27_istj_074_days_since_last_officer_buy_d2': {'inputs': ['insider_officer_buy_value'], 'func': f27_istj_074_days_since_last_officer_buy_d2}, 'f27_istj_075_days_since_last_cluster_buy_5d_d2': {'inputs': ['insider_buy_value'], 'func': f27_istj_075_days_since_last_cluster_buy_5d_d2}}