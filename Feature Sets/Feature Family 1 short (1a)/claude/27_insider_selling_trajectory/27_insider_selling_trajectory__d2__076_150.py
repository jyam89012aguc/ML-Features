"""insider_selling_trajectory d2 features 076-150 — order-2 difference of corresponding base features.

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

def _rolling_slope(s, n, min_periods=None):
    if min_periods is None:
        min_periods = max(n // 3, 2)
    def _slope(w):
        valid = ~np.isnan(w)
        if valid.sum() < min_periods:
            return np.nan
        x = np.arange(len(w), dtype=float)
        if valid.all():
            wv = w
        else:
            x = x[valid]
            wv = w[valid]
        xm = x.mean(); wm = wv.mean()
        num = ((x - xm) * (wv - wm)).sum()
        den = ((x - xm) ** 2).sum()
        return num / den if den != 0 else np.nan
    return s.rolling(n, min_periods=min_periods).apply(_slope, raw=True)

def f27_istj_076_insider_sell_value_acceleration_63d_vs_252d_d2(insider_sell_value):
    a = insider_sell_value.rolling(63, min_periods=15).mean()
    b = insider_sell_value.rolling(252, min_periods=60).mean()
    return _safe_div(a - b, b.abs()).diff().diff()

def f27_istj_077_insider_sell_value_log_diff_252d_d2(insider_sell_value):
    cur = insider_sell_value.rolling(252, min_periods=60).sum()
    return (_safe_log(cur) - _safe_log(cur.shift(252))).diff().diff()

def f27_istj_078_insider_sell_value_rolling_63d_yoy_pct_d2(insider_sell_value):
    cur = insider_sell_value.rolling(63, min_periods=15).sum()
    return _safe_div(cur - cur.shift(252), cur.shift(252).abs()).diff().diff()

def f27_istj_079_insider_sell_value_2yr_growth_d2(insider_sell_value):
    cur = insider_sell_value.rolling(63, min_periods=15).sum()
    return _safe_div(cur - cur.shift(504), cur.shift(504).abs()).diff().diff()

def f27_istj_080_insider_sell_count_acceleration_63d_vs_252d_d2(insider_sell_count):
    a = insider_sell_count.rolling(63, min_periods=15).mean()
    b = insider_sell_count.rolling(252, min_periods=60).mean()
    return _safe_div(a - b, b.abs()).diff().diff()

def f27_istj_081_insider_sellers_breadth_acceleration_252d_d2(insider_sellers_unique):
    a = insider_sellers_unique.rolling(63, min_periods=15).sum()
    b = insider_sellers_unique.rolling(252, min_periods=60).sum() / 4.0
    return _safe_div(a - b, b.abs()).diff().diff()

def f27_istj_082_insider_sell_value_step_change_252d_d2(insider_sell_value):
    a = insider_sell_value.rolling(63, min_periods=15).mean()
    b = insider_sell_value.shift(63).rolling(189, min_periods=45).mean()
    return (a - b).diff().diff()

def f27_istj_083_insider_sell_value_regime_break_252d_d2(insider_sell_value):
    a = insider_sell_value.rolling(126, min_periods=30).mean()
    b = insider_sell_value.shift(126).rolling(126, min_periods=30).mean()
    return _safe_div(a - b, b.abs()).diff().diff()

def f27_istj_084_insider_sell_value_max_period_growth_d2(insider_sell_value):
    a = insider_sell_value.rolling(21, min_periods=5).sum()
    b = insider_sell_value.shift(21).rolling(21, min_periods=5).sum()
    return _safe_div(a - b, b.abs() + 1.0).diff().diff()

def f27_istj_085_insider_sell_burst_frequency_252d_d2(insider_sell_value):
    weekly = insider_sell_value.rolling(5, min_periods=1).sum()
    p90 = weekly.rolling(252, min_periods=60).quantile(0.9).shift(1)
    return (weekly > p90).astype(float).rolling(252, min_periods=60).sum().diff().diff()

def f27_istj_086_insider_sell_burst_intensity_252d_d2(insider_sell_value):
    weekly = insider_sell_value.rolling(5, min_periods=1).sum()
    p90 = weekly.rolling(252, min_periods=60).quantile(0.9).shift(1)
    mask = weekly > p90
    return weekly.where(mask, 0).rolling(252, min_periods=60).sum().diff().diff()

def f27_istj_087_insider_sell_intensity_trend_63d_d2(insider_sell_value):
    return _rolling_slope(insider_sell_value.rolling(21, min_periods=5).sum(), 63).diff().diff()

def f27_istj_088_insider_sell_intensity_trend_252d_d2(insider_sell_value):
    return _rolling_slope(insider_sell_value.rolling(63, min_periods=15).sum(), 252).diff().diff()

def f27_istj_089_insider_sell_value_qoq_acceleration_d2(insider_sell_value):
    return insider_sell_value.rolling(63, min_periods=15).sum().diff(63).diff().diff()

def f27_istj_090_insider_sell_value_yoy_acceleration_d2(insider_sell_value):
    return insider_sell_value.rolling(252, min_periods=60).sum().diff(252).diff().diff()

def f27_istj_091_insider_sell_value_to_volume_value_63d_d2(insider_sell_value, close, volume):
    vol_val = (close * volume).rolling(63, min_periods=15).sum()
    return _safe_div(insider_sell_value.rolling(63, min_periods=15).sum(), vol_val).diff().diff()

def f27_istj_092_insider_sell_value_to_volume_value_252d_d2(insider_sell_value, close, volume):
    vol_val = (close * volume).rolling(252, min_periods=60).sum()
    return _safe_div(insider_sell_value.rolling(252, min_periods=60).sum(), vol_val).diff().diff()

def f27_istj_093_insider_sell_value_to_float_proxy_63d_d2(insider_sell_value, marketcap):
    return _safe_div(insider_sell_value.rolling(63, min_periods=15).sum(), marketcap).diff().diff()

def f27_istj_094_insider_sell_shares_to_volume_63d_d2(insider_sell_shares, volume):
    return _safe_div(insider_sell_shares.rolling(63, min_periods=15).sum(), volume.rolling(63, min_periods=15).sum()).diff().diff()

def f27_istj_095_insider_sell_value_normalized_zscore_252d_d2(insider_sell_value):
    weekly = insider_sell_value.rolling(5, min_periods=1).sum()
    return _rolling_zscore(weekly, 252, min_periods=60).diff().diff()

def f27_istj_096_insider_sell_value_to_avg_daily_value_63d_d2(insider_sell_value, close, volume):
    adv = (close * volume).rolling(63, min_periods=15).mean()
    return _safe_div(insider_sell_value.rolling(63, min_periods=15).mean(), adv).diff().diff()

def f27_istj_097_insider_sell_value_intensity_zscore_252d_d2(insider_sell_value):
    return _rolling_zscore(insider_sell_value.rolling(63, min_periods=15).sum(), 252, min_periods=60).diff().diff()

def f27_istj_098_insider_sell_value_to_running_high_252d_d2(insider_sell_value):
    cur = insider_sell_value.rolling(63, min_periods=15).sum()
    hi = cur.rolling(252, min_periods=60).max()
    return _safe_div(cur, hi).diff().diff()

def f27_istj_099_insider_sell_value_share_of_total_ann_d2(insider_sell_value, insider_buy_value):
    s = insider_sell_value.rolling(252, min_periods=60).sum()
    b = insider_buy_value.rolling(252, min_periods=60).sum()
    return _safe_div(s, s + b).diff().diff()

def f27_istj_100_insider_sell_value_to_mcap_drawdown_252d_d2(insider_sell_value, marketcap):
    peak = marketcap.rolling(252, min_periods=60).max()
    return _safe_div(insider_sell_value.rolling(63, min_periods=15).sum(), peak).diff().diff()

def f27_istj_101_insider_sell_value_per_day_active_63d_d2(insider_sell_value):
    s = insider_sell_value.rolling(63, min_periods=15).sum()
    d = (insider_sell_value > 0).astype(float).rolling(63, min_periods=15).sum()
    return _safe_div(s, d).diff().diff()

def f27_istj_102_insider_sell_value_per_day_active_252d_d2(insider_sell_value):
    s = insider_sell_value.rolling(252, min_periods=60).sum()
    d = (insider_sell_value > 0).astype(float).rolling(252, min_periods=60).sum()
    return _safe_div(s, d).diff().diff()

def f27_istj_103_insider_sell_to_price_appreciation_63d_d2(insider_sell_value, close):
    apprec = _safe_div(close - close.shift(63), close.shift(63).abs()).clip(lower=0)
    return _safe_div(insider_sell_value.rolling(63, min_periods=15).sum(), apprec + 1e-06).diff().diff()

def f27_istj_104_insider_sell_value_premium_vs_volume_z_d2(insider_sell_value, close, volume):
    val = close * volume
    z = _rolling_zscore(val, 63, min_periods=15)
    return ((insider_sell_value > 0).astype(float) * z).diff().diff()

def f27_istj_105_insider_sell_volume_share_252d_d2(insider_sell_shares, volume):
    return _safe_div(insider_sell_shares.rolling(252, min_periods=60).sum(), volume.rolling(252, min_periods=60).sum()).diff().diff()

def f27_istj_106_insider_sell_no_buy_signature_63d_d2(insider_sell_value, insider_buy_value):
    s = insider_sell_value.rolling(63, min_periods=15).sum()
    b = insider_buy_value.rolling(63, min_periods=15).sum()
    return ((s > 0) & (b == 0)).astype(float).diff().diff()

def f27_istj_107_insider_sell_no_buy_signature_252d_d2(insider_sell_value, insider_buy_value):
    s = insider_sell_value.rolling(252, min_periods=60).sum()
    b = insider_buy_value.rolling(252, min_periods=60).sum()
    return ((s > 0) & (b == 0)).astype(float).diff().diff()

def f27_istj_108_insider_sell_no_buy_streak_d2(insider_sell_value, insider_buy_value):
    weekly_s = insider_sell_value.rolling(5, min_periods=1).sum()
    weekly_b = insider_buy_value.rolling(5, min_periods=1).sum()
    cond = ((weekly_s > 0) & (weekly_b == 0)).astype(float)
    grp = (cond != cond.shift()).cumsum()
    return (cond.groupby(grp).cumsum() * cond).diff().diff()

def f27_istj_109_insider_capitulation_score_63d_d2(insider_sell_value, insider_buy_value, insider_sell_count):
    s = insider_sell_value.rolling(63, min_periods=15).sum()
    b = insider_buy_value.rolling(63, min_periods=15).sum()
    c = insider_sell_count.rolling(63, min_periods=15).sum()
    return _safe_div(s * c, b + 1.0).diff().diff()

def f27_istj_110_insider_panic_index_63d_d2(insider_sell_value, insider_sellers_unique):
    s = insider_sell_value.rolling(63, min_periods=15).sum()
    n = insider_sellers_unique.rolling(63, min_periods=15).sum()
    return (s * n).diff().diff()

def f27_istj_111_insider_exit_velocity_63d_d2(insider_total_shares_owned):
    return _safe_div(insider_total_shares_owned.diff(63), insider_total_shares_owned.shift(63).abs()).diff().diff()

def f27_istj_112_insider_exit_velocity_252d_d2(insider_total_shares_owned):
    return _safe_div(insider_total_shares_owned.diff(252), insider_total_shares_owned.shift(252).abs()).diff().diff()

def f27_istj_113_insider_exit_count_breadth_252d_d2(insider_director_sell_value, insider_officer_sell_value, insider_tenpct_sell_value):
    have_sell = (insider_director_sell_value > 0).astype(float) + (insider_officer_sell_value > 0).astype(float) + (insider_tenpct_sell_value > 0).astype(float)
    return have_sell.rolling(252, min_periods=60).sum().diff().diff()

def f27_istj_114_insider_capitulation_count_252d_d2(insider_sellers_unique):
    weekly = insider_sellers_unique.rolling(5, min_periods=1).sum()
    return (weekly >= 3).astype(float).rolling(252, min_periods=60).sum().diff().diff()

def f27_istj_115_insider_no_buy_drought_max_in_252d_d2(insider_buy_value):
    weekly = insider_buy_value.rolling(5, min_periods=1).sum()
    no_buy = (weekly == 0).astype(int)
    grp = (no_buy != no_buy.shift()).cumsum()
    run = no_buy.groupby(grp).cumsum() * no_buy
    return run.rolling(252, min_periods=60).max().diff().diff()

def f27_istj_116_insider_no_buy_drought_growth_d2(insider_buy_value):
    weekly = insider_buy_value.rolling(5, min_periods=1).sum()
    no_buy = (weekly == 0).astype(int)
    grp = (no_buy != no_buy.shift()).cumsum()
    run = no_buy.groupby(grp).cumsum() * no_buy
    cur = run.rolling(126, min_periods=30).max()
    prev = run.shift(126).rolling(126, min_periods=30).max()
    return (cur - prev).diff().diff()

def f27_istj_117_insider_sell_dominance_ratio_252d_d2(insider_sell_value, insider_buy_value):
    s = insider_sell_value.rolling(252, min_periods=60).sum()
    b = insider_buy_value.rolling(252, min_periods=60).sum()
    return _safe_div(s, s + b).diff().diff()

def f27_istj_118_insider_sell_dominance_acceleration_d2(insider_sell_value, insider_buy_value):
    s = insider_sell_value.rolling(63, min_periods=15).sum()
    b = insider_buy_value.rolling(63, min_periods=15).sum()
    r63 = _safe_div(s, s + b)
    s2 = insider_sell_value.rolling(252, min_periods=60).sum()
    b2 = insider_buy_value.rolling(252, min_periods=60).sum()
    r252 = _safe_div(s2, s2 + b2)
    return (r63 - r252).diff().diff()

def f27_istj_119_insider_dump_event_count_63d_d2(insider_sell_value):
    z = _rolling_zscore(insider_sell_value, 252, min_periods=60)
    return (z > 2.0).astype(float).rolling(63, min_periods=15).sum().diff().diff()

def f27_istj_120_insider_dump_event_count_252d_d2(insider_sell_value):
    z = _rolling_zscore(insider_sell_value, 252, min_periods=60)
    return (z > 2.0).astype(float).rolling(252, min_periods=60).sum().diff().diff()

def f27_istj_121_insider_sell_value_in_252d_minus_prior_252d_d2(insider_sell_value):
    cur = insider_sell_value.rolling(252, min_periods=60).sum()
    prev = insider_sell_value.shift(252).rolling(252, min_periods=60).sum()
    return (cur - prev).diff().diff()

def f27_istj_122_insider_sells_count_pre_peak_pattern_d2(insider_sell_count, close):
    rising = (close > close.shift(63)).astype(float)
    return (insider_sell_count * rising).rolling(252, min_periods=60).sum().diff().diff()

def f27_istj_123_insider_sells_vs_price_corr_63d_d2(insider_sell_value, close):
    return insider_sell_value.rolling(63, min_periods=15).corr(close).diff().diff()

def f27_istj_124_insider_sells_vs_price_corr_252d_d2(insider_sell_value, close):
    return insider_sell_value.rolling(252, min_periods=60).corr(close).diff().diff()

def f27_istj_125_insider_sells_dollar_to_mcap_change_252d_d2(insider_sell_value, marketcap):
    s = insider_sell_value.rolling(252, min_periods=60).sum()
    chg = marketcap - marketcap.shift(252)
    return _safe_div(s, chg.abs()).diff().diff()

def f27_istj_126_insider_exit_during_rally_score_d2(insider_sell_value, close):
    ret63 = _safe_div(close - close.shift(63), close.shift(63).abs())
    rally = (ret63 > 0).astype(float)
    return (insider_sell_value * rally).rolling(63, min_periods=15).sum().diff().diff()

def f27_istj_127_insider_exit_during_top10pct_score_d2(insider_sell_value, close):
    hi = close.rolling(252, min_periods=60).max()
    near = (close >= 0.9 * hi).astype(float)
    return (insider_sell_value * near).rolling(63, min_periods=15).sum().diff().diff()

def f27_istj_128_insider_late_cycle_exit_index_d2(insider_sell_value):
    a = insider_sell_value.rolling(63, min_periods=15).sum()
    b = insider_sell_value.shift(63).rolling(189, min_periods=45).sum()
    return _safe_div(a, b).diff().diff()

def f27_istj_129_insider_silent_exit_signature_d2(insider_sell_value, insider_buy_value):
    prior_buy = insider_buy_value.shift(63).rolling(252, min_periods=60).sum()
    s63 = insider_sell_value.rolling(63, min_periods=15).sum()
    return _safe_div(s63, prior_buy + 1.0).diff().diff()

def f27_istj_130_insider_top_seller_concentration_252d_d2(insider_sell_value):
    max_day = insider_sell_value.rolling(252, min_periods=60).max()
    tot = insider_sell_value.rolling(252, min_periods=60).sum()
    return _safe_div(max_day, tot).diff().diff()

def f27_istj_131_insider_top3_seller_concentration_252d_d2(insider_sell_value):
    top3 = insider_sell_value.rolling(252, min_periods=60).apply(lambda y: float(np.nansum(np.sort(y)[-3:])) if np.isfinite(y).sum() >= 3 else np.nan, raw=True)
    tot = insider_sell_value.rolling(252, min_periods=60).sum()
    return _safe_div(top3, tot).diff().diff()

def f27_istj_132_insider_sellers_diversity_index_252d_d2(insider_sellers_unique):
    return insider_sellers_unique.rolling(252, min_periods=60).sum().diff().diff()

def f27_istj_133_insider_seller_inflection_252d_d2(insider_sell_value, insider_buy_value):
    net = (insider_buy_value - insider_sell_value).rolling(63, min_periods=15).sum()
    sign = np.sign(net)
    return (sign != sign.shift(63)).astype(float).diff().diff()

def f27_istj_134_insider_silent_dump_score_63d_d2(insider_sell_value, insider_buy_value, insider_sell_count):
    s = insider_sell_value.rolling(63, min_periods=15).sum()
    b = insider_buy_value.rolling(63, min_periods=15).sum()
    c = insider_sell_count.rolling(63, min_periods=15).sum()
    return _safe_div(s, (b + 1.0) * (c + 1.0)).diff().diff()

def f27_istj_135_insider_top_seller_size_to_mcap_d2(insider_sell_value, marketcap):
    max_day = insider_sell_value.rolling(252, min_periods=60).max()
    return _safe_div(max_day, marketcap).diff().diff()

def f27_istj_136_insider_sell_value_chow_break_252d_d2(insider_sell_value):
    rec = insider_sell_value.rolling(63, min_periods=15).var()
    full = insider_sell_value.rolling(252, min_periods=60).var()
    return _safe_div(rec, full).diff().diff()

def f27_istj_137_insider_sell_value_smoothed_minus_raw_63d_d2(insider_sell_value):
    return (_ema(insider_sell_value, 21) - insider_sell_value).diff().diff()

def f27_istj_138_insider_sell_value_smoothed_minus_raw_252d_d2(insider_sell_value):
    return (_ema(insider_sell_value, 63) - insider_sell_value).diff().diff()

def f27_istj_139_insider_sell_value_trend_residual_252d_d2(insider_sell_value):
    trend = insider_sell_value.rolling(252, min_periods=60).mean()
    return (insider_sell_value - trend).diff().diff()

def f27_istj_140_insider_sell_value_log_volatility_63d_d2(insider_sell_value):
    return _safe_log(insider_sell_value + 1.0).rolling(63, min_periods=15).std().diff().diff()

def f27_istj_141_insider_sell_value_log_volatility_252d_d2(insider_sell_value):
    return _safe_log(insider_sell_value + 1.0).rolling(252, min_periods=60).std().diff().diff()

def f27_istj_142_insider_sell_value_drawdown_inverse_252d_d2(insider_sell_value):
    cur = insider_sell_value.rolling(63, min_periods=15).sum()
    lo = cur.rolling(252, min_periods=60).min()
    return _safe_div(cur - lo, lo.abs() + 1.0).diff().diff()

def f27_istj_143_insider_sell_value_above_max_252d_flag_d2(insider_sell_value):
    cur = insider_sell_value.rolling(63, min_periods=15).sum()
    return (cur >= cur.rolling(252, min_periods=60).max()).astype(float).diff().diff()

def f27_istj_144_insider_sell_value_above_max_504d_flag_d2(insider_sell_value):
    cur = insider_sell_value.rolling(63, min_periods=15).sum()
    return (cur >= cur.rolling(504, min_periods=120).max()).astype(float).diff().diff()

def f27_istj_145_insider_buy_value_trough_252d_d2(insider_buy_value):
    cur = insider_buy_value.rolling(63, min_periods=15).sum()
    lo = cur.rolling(252, min_periods=60).min()
    return (cur <= lo).astype(float).diff().diff()

def f27_istj_146_insider_buy_to_sell_regime_change_252d_d2(insider_buy_value, insider_sell_value):
    r = _safe_div(insider_buy_value.rolling(63, min_periods=15).sum(), insider_sell_value.rolling(63, min_periods=15).sum() + 1.0)
    return (r - r.shift(252)).diff().diff()

def f27_istj_147_insider_sell_value_growth_step_252d_d2(insider_sell_value):
    a = insider_sell_value.rolling(126, min_periods=30).mean()
    b = insider_sell_value.shift(126).rolling(126, min_periods=30).mean()
    return _safe_div(a - b, b.abs() + 1.0).diff().diff()

def f27_istj_148_insider_sell_burst_persistence_252d_d2(insider_sell_value):
    weekly = insider_sell_value.rolling(5, min_periods=1).sum()
    p75 = weekly.rolling(252, min_periods=60).quantile(0.75).shift(1)
    burst = (weekly > p75).astype(int)
    grp = (burst != burst.shift()).cumsum()
    run = burst.groupby(grp).cumsum() * burst
    return run.rolling(252, min_periods=60).max().diff().diff()

def f27_istj_149_insider_sell_total_long_window_yoy_d2(insider_sell_value):
    cur = insider_sell_value.rolling(252, min_periods=60).sum()
    prev = insider_sell_value.shift(252).rolling(252, min_periods=60).sum()
    return _safe_div(cur - prev, prev.abs() + 1.0).diff().diff()

def f27_istj_150_insider_total_owned_trend_slope_252d_d2(insider_total_shares_owned):
    return _rolling_slope(insider_total_shares_owned, 252).diff().diff()
INSIDER_SELLING_TRAJECTORY_D2_REGISTRY_076_150 = {'f27_istj_076_insider_sell_value_acceleration_63d_vs_252d_d2': {'inputs': ['insider_sell_value'], 'func': f27_istj_076_insider_sell_value_acceleration_63d_vs_252d_d2}, 'f27_istj_077_insider_sell_value_log_diff_252d_d2': {'inputs': ['insider_sell_value'], 'func': f27_istj_077_insider_sell_value_log_diff_252d_d2}, 'f27_istj_078_insider_sell_value_rolling_63d_yoy_pct_d2': {'inputs': ['insider_sell_value'], 'func': f27_istj_078_insider_sell_value_rolling_63d_yoy_pct_d2}, 'f27_istj_079_insider_sell_value_2yr_growth_d2': {'inputs': ['insider_sell_value'], 'func': f27_istj_079_insider_sell_value_2yr_growth_d2}, 'f27_istj_080_insider_sell_count_acceleration_63d_vs_252d_d2': {'inputs': ['insider_sell_count'], 'func': f27_istj_080_insider_sell_count_acceleration_63d_vs_252d_d2}, 'f27_istj_081_insider_sellers_breadth_acceleration_252d_d2': {'inputs': ['insider_sellers_unique'], 'func': f27_istj_081_insider_sellers_breadth_acceleration_252d_d2}, 'f27_istj_082_insider_sell_value_step_change_252d_d2': {'inputs': ['insider_sell_value'], 'func': f27_istj_082_insider_sell_value_step_change_252d_d2}, 'f27_istj_083_insider_sell_value_regime_break_252d_d2': {'inputs': ['insider_sell_value'], 'func': f27_istj_083_insider_sell_value_regime_break_252d_d2}, 'f27_istj_084_insider_sell_value_max_period_growth_d2': {'inputs': ['insider_sell_value'], 'func': f27_istj_084_insider_sell_value_max_period_growth_d2}, 'f27_istj_085_insider_sell_burst_frequency_252d_d2': {'inputs': ['insider_sell_value'], 'func': f27_istj_085_insider_sell_burst_frequency_252d_d2}, 'f27_istj_086_insider_sell_burst_intensity_252d_d2': {'inputs': ['insider_sell_value'], 'func': f27_istj_086_insider_sell_burst_intensity_252d_d2}, 'f27_istj_087_insider_sell_intensity_trend_63d_d2': {'inputs': ['insider_sell_value'], 'func': f27_istj_087_insider_sell_intensity_trend_63d_d2}, 'f27_istj_088_insider_sell_intensity_trend_252d_d2': {'inputs': ['insider_sell_value'], 'func': f27_istj_088_insider_sell_intensity_trend_252d_d2}, 'f27_istj_089_insider_sell_value_qoq_acceleration_d2': {'inputs': ['insider_sell_value'], 'func': f27_istj_089_insider_sell_value_qoq_acceleration_d2}, 'f27_istj_090_insider_sell_value_yoy_acceleration_d2': {'inputs': ['insider_sell_value'], 'func': f27_istj_090_insider_sell_value_yoy_acceleration_d2}, 'f27_istj_091_insider_sell_value_to_volume_value_63d_d2': {'inputs': ['insider_sell_value', 'close', 'volume'], 'func': f27_istj_091_insider_sell_value_to_volume_value_63d_d2}, 'f27_istj_092_insider_sell_value_to_volume_value_252d_d2': {'inputs': ['insider_sell_value', 'close', 'volume'], 'func': f27_istj_092_insider_sell_value_to_volume_value_252d_d2}, 'f27_istj_093_insider_sell_value_to_float_proxy_63d_d2': {'inputs': ['insider_sell_value', 'marketcap'], 'func': f27_istj_093_insider_sell_value_to_float_proxy_63d_d2}, 'f27_istj_094_insider_sell_shares_to_volume_63d_d2': {'inputs': ['insider_sell_shares', 'volume'], 'func': f27_istj_094_insider_sell_shares_to_volume_63d_d2}, 'f27_istj_095_insider_sell_value_normalized_zscore_252d_d2': {'inputs': ['insider_sell_value'], 'func': f27_istj_095_insider_sell_value_normalized_zscore_252d_d2}, 'f27_istj_096_insider_sell_value_to_avg_daily_value_63d_d2': {'inputs': ['insider_sell_value', 'close', 'volume'], 'func': f27_istj_096_insider_sell_value_to_avg_daily_value_63d_d2}, 'f27_istj_097_insider_sell_value_intensity_zscore_252d_d2': {'inputs': ['insider_sell_value'], 'func': f27_istj_097_insider_sell_value_intensity_zscore_252d_d2}, 'f27_istj_098_insider_sell_value_to_running_high_252d_d2': {'inputs': ['insider_sell_value'], 'func': f27_istj_098_insider_sell_value_to_running_high_252d_d2}, 'f27_istj_099_insider_sell_value_share_of_total_ann_d2': {'inputs': ['insider_sell_value', 'insider_buy_value'], 'func': f27_istj_099_insider_sell_value_share_of_total_ann_d2}, 'f27_istj_100_insider_sell_value_to_mcap_drawdown_252d_d2': {'inputs': ['insider_sell_value', 'marketcap'], 'func': f27_istj_100_insider_sell_value_to_mcap_drawdown_252d_d2}, 'f27_istj_101_insider_sell_value_per_day_active_63d_d2': {'inputs': ['insider_sell_value'], 'func': f27_istj_101_insider_sell_value_per_day_active_63d_d2}, 'f27_istj_102_insider_sell_value_per_day_active_252d_d2': {'inputs': ['insider_sell_value'], 'func': f27_istj_102_insider_sell_value_per_day_active_252d_d2}, 'f27_istj_103_insider_sell_to_price_appreciation_63d_d2': {'inputs': ['insider_sell_value', 'close'], 'func': f27_istj_103_insider_sell_to_price_appreciation_63d_d2}, 'f27_istj_104_insider_sell_value_premium_vs_volume_z_d2': {'inputs': ['insider_sell_value', 'close', 'volume'], 'func': f27_istj_104_insider_sell_value_premium_vs_volume_z_d2}, 'f27_istj_105_insider_sell_volume_share_252d_d2': {'inputs': ['insider_sell_shares', 'volume'], 'func': f27_istj_105_insider_sell_volume_share_252d_d2}, 'f27_istj_106_insider_sell_no_buy_signature_63d_d2': {'inputs': ['insider_sell_value', 'insider_buy_value'], 'func': f27_istj_106_insider_sell_no_buy_signature_63d_d2}, 'f27_istj_107_insider_sell_no_buy_signature_252d_d2': {'inputs': ['insider_sell_value', 'insider_buy_value'], 'func': f27_istj_107_insider_sell_no_buy_signature_252d_d2}, 'f27_istj_108_insider_sell_no_buy_streak_d2': {'inputs': ['insider_sell_value', 'insider_buy_value'], 'func': f27_istj_108_insider_sell_no_buy_streak_d2}, 'f27_istj_109_insider_capitulation_score_63d_d2': {'inputs': ['insider_sell_value', 'insider_buy_value', 'insider_sell_count'], 'func': f27_istj_109_insider_capitulation_score_63d_d2}, 'f27_istj_110_insider_panic_index_63d_d2': {'inputs': ['insider_sell_value', 'insider_sellers_unique'], 'func': f27_istj_110_insider_panic_index_63d_d2}, 'f27_istj_111_insider_exit_velocity_63d_d2': {'inputs': ['insider_total_shares_owned'], 'func': f27_istj_111_insider_exit_velocity_63d_d2}, 'f27_istj_112_insider_exit_velocity_252d_d2': {'inputs': ['insider_total_shares_owned'], 'func': f27_istj_112_insider_exit_velocity_252d_d2}, 'f27_istj_113_insider_exit_count_breadth_252d_d2': {'inputs': ['insider_director_sell_value', 'insider_officer_sell_value', 'insider_tenpct_sell_value'], 'func': f27_istj_113_insider_exit_count_breadth_252d_d2}, 'f27_istj_114_insider_capitulation_count_252d_d2': {'inputs': ['insider_sellers_unique'], 'func': f27_istj_114_insider_capitulation_count_252d_d2}, 'f27_istj_115_insider_no_buy_drought_max_in_252d_d2': {'inputs': ['insider_buy_value'], 'func': f27_istj_115_insider_no_buy_drought_max_in_252d_d2}, 'f27_istj_116_insider_no_buy_drought_growth_d2': {'inputs': ['insider_buy_value'], 'func': f27_istj_116_insider_no_buy_drought_growth_d2}, 'f27_istj_117_insider_sell_dominance_ratio_252d_d2': {'inputs': ['insider_sell_value', 'insider_buy_value'], 'func': f27_istj_117_insider_sell_dominance_ratio_252d_d2}, 'f27_istj_118_insider_sell_dominance_acceleration_d2': {'inputs': ['insider_sell_value', 'insider_buy_value'], 'func': f27_istj_118_insider_sell_dominance_acceleration_d2}, 'f27_istj_119_insider_dump_event_count_63d_d2': {'inputs': ['insider_sell_value'], 'func': f27_istj_119_insider_dump_event_count_63d_d2}, 'f27_istj_120_insider_dump_event_count_252d_d2': {'inputs': ['insider_sell_value'], 'func': f27_istj_120_insider_dump_event_count_252d_d2}, 'f27_istj_121_insider_sell_value_in_252d_minus_prior_252d_d2': {'inputs': ['insider_sell_value'], 'func': f27_istj_121_insider_sell_value_in_252d_minus_prior_252d_d2}, 'f27_istj_122_insider_sells_count_pre_peak_pattern_d2': {'inputs': ['insider_sell_count', 'close'], 'func': f27_istj_122_insider_sells_count_pre_peak_pattern_d2}, 'f27_istj_123_insider_sells_vs_price_corr_63d_d2': {'inputs': ['insider_sell_value', 'close'], 'func': f27_istj_123_insider_sells_vs_price_corr_63d_d2}, 'f27_istj_124_insider_sells_vs_price_corr_252d_d2': {'inputs': ['insider_sell_value', 'close'], 'func': f27_istj_124_insider_sells_vs_price_corr_252d_d2}, 'f27_istj_125_insider_sells_dollar_to_mcap_change_252d_d2': {'inputs': ['insider_sell_value', 'marketcap'], 'func': f27_istj_125_insider_sells_dollar_to_mcap_change_252d_d2}, 'f27_istj_126_insider_exit_during_rally_score_d2': {'inputs': ['insider_sell_value', 'close'], 'func': f27_istj_126_insider_exit_during_rally_score_d2}, 'f27_istj_127_insider_exit_during_top10pct_score_d2': {'inputs': ['insider_sell_value', 'close'], 'func': f27_istj_127_insider_exit_during_top10pct_score_d2}, 'f27_istj_128_insider_late_cycle_exit_index_d2': {'inputs': ['insider_sell_value'], 'func': f27_istj_128_insider_late_cycle_exit_index_d2}, 'f27_istj_129_insider_silent_exit_signature_d2': {'inputs': ['insider_sell_value', 'insider_buy_value'], 'func': f27_istj_129_insider_silent_exit_signature_d2}, 'f27_istj_130_insider_top_seller_concentration_252d_d2': {'inputs': ['insider_sell_value'], 'func': f27_istj_130_insider_top_seller_concentration_252d_d2}, 'f27_istj_131_insider_top3_seller_concentration_252d_d2': {'inputs': ['insider_sell_value'], 'func': f27_istj_131_insider_top3_seller_concentration_252d_d2}, 'f27_istj_132_insider_sellers_diversity_index_252d_d2': {'inputs': ['insider_sellers_unique'], 'func': f27_istj_132_insider_sellers_diversity_index_252d_d2}, 'f27_istj_133_insider_seller_inflection_252d_d2': {'inputs': ['insider_sell_value', 'insider_buy_value'], 'func': f27_istj_133_insider_seller_inflection_252d_d2}, 'f27_istj_134_insider_silent_dump_score_63d_d2': {'inputs': ['insider_sell_value', 'insider_buy_value', 'insider_sell_count'], 'func': f27_istj_134_insider_silent_dump_score_63d_d2}, 'f27_istj_135_insider_top_seller_size_to_mcap_d2': {'inputs': ['insider_sell_value', 'marketcap'], 'func': f27_istj_135_insider_top_seller_size_to_mcap_d2}, 'f27_istj_136_insider_sell_value_chow_break_252d_d2': {'inputs': ['insider_sell_value'], 'func': f27_istj_136_insider_sell_value_chow_break_252d_d2}, 'f27_istj_137_insider_sell_value_smoothed_minus_raw_63d_d2': {'inputs': ['insider_sell_value'], 'func': f27_istj_137_insider_sell_value_smoothed_minus_raw_63d_d2}, 'f27_istj_138_insider_sell_value_smoothed_minus_raw_252d_d2': {'inputs': ['insider_sell_value'], 'func': f27_istj_138_insider_sell_value_smoothed_minus_raw_252d_d2}, 'f27_istj_139_insider_sell_value_trend_residual_252d_d2': {'inputs': ['insider_sell_value'], 'func': f27_istj_139_insider_sell_value_trend_residual_252d_d2}, 'f27_istj_140_insider_sell_value_log_volatility_63d_d2': {'inputs': ['insider_sell_value'], 'func': f27_istj_140_insider_sell_value_log_volatility_63d_d2}, 'f27_istj_141_insider_sell_value_log_volatility_252d_d2': {'inputs': ['insider_sell_value'], 'func': f27_istj_141_insider_sell_value_log_volatility_252d_d2}, 'f27_istj_142_insider_sell_value_drawdown_inverse_252d_d2': {'inputs': ['insider_sell_value'], 'func': f27_istj_142_insider_sell_value_drawdown_inverse_252d_d2}, 'f27_istj_143_insider_sell_value_above_max_252d_flag_d2': {'inputs': ['insider_sell_value'], 'func': f27_istj_143_insider_sell_value_above_max_252d_flag_d2}, 'f27_istj_144_insider_sell_value_above_max_504d_flag_d2': {'inputs': ['insider_sell_value'], 'func': f27_istj_144_insider_sell_value_above_max_504d_flag_d2}, 'f27_istj_145_insider_buy_value_trough_252d_d2': {'inputs': ['insider_buy_value'], 'func': f27_istj_145_insider_buy_value_trough_252d_d2}, 'f27_istj_146_insider_buy_to_sell_regime_change_252d_d2': {'inputs': ['insider_buy_value', 'insider_sell_value'], 'func': f27_istj_146_insider_buy_to_sell_regime_change_252d_d2}, 'f27_istj_147_insider_sell_value_growth_step_252d_d2': {'inputs': ['insider_sell_value'], 'func': f27_istj_147_insider_sell_value_growth_step_252d_d2}, 'f27_istj_148_insider_sell_burst_persistence_252d_d2': {'inputs': ['insider_sell_value'], 'func': f27_istj_148_insider_sell_burst_persistence_252d_d2}, 'f27_istj_149_insider_sell_total_long_window_yoy_d2': {'inputs': ['insider_sell_value'], 'func': f27_istj_149_insider_sell_total_long_window_yoy_d2}, 'f27_istj_150_insider_total_owned_trend_slope_252d_d2': {'inputs': ['insider_total_shares_owned'], 'func': f27_istj_150_insider_total_owned_trend_slope_252d_d2}}