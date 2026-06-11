"""distribution_rolling_top_signature d1 features 001-075 — order-1 difference of corresponding base features.

Each function inlines the base body and wraps the return value with .diff(). Self-contained; helpers redefined locally per HANDOFF."""
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

def _true_range(high, low, close):
    pc = close.shift(1)
    return pd.concat([high - low, (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)

def _atr(high, low, close, n=21):
    return _true_range(high, low, close).rolling(n, min_periods=max(n // 3, 2)).mean()

def _streak_last_down(s, window):
    return s.rolling(window, min_periods=3).apply(lambda w: int(w[::-1].cumprod().sum()) if w.size else np.nan, raw=True)

def f38_drts_001_days_within_top_decile_252d_in_63d_d1(high, close):
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = high.rolling(YDAYS, min_periods=QDAYS).min()
    rng = (rmax - rmin).replace(0, np.nan)
    in_top = (close - rmin) / rng >= 0.9
    return in_top.rolling(QDAYS, min_periods=21).sum().diff()

def f38_drts_002_range_compression_at_top_21d_d1(high, low, close):
    atr21 = _atr(high, low, close, 21)
    atr63 = _atr(high, low, close, 63)
    return _safe_div(atr21, atr63).diff()

def f38_drts_003_close_within_5pct_of_252d_max_count_63d_d1(close, high):
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    within = close / rmax >= 0.95
    return within.rolling(QDAYS, min_periods=21).sum().diff()

def f38_drts_004_consec_close_within_5pct_252d_max_streak_63d_d1(close, high):
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    within = (close / rmax >= 0.95).astype(int)
    return _streak_last_down(within, QDAYS).diff()

def f38_drts_005_new_21d_high_count_63d_d1(high):
    nh = (high >= high.rolling(MDAYS, min_periods=5).max().shift(1)).astype(float)
    return nh.rolling(QDAYS, min_periods=21).sum().diff()

def f38_drts_006_failed_21d_high_count_63d_d1(high, close):
    h21 = high.rolling(MDAYS, min_periods=5).max().shift(1)
    failed = ((high > h21) & (close < h21)).astype(float)
    return failed.rolling(QDAYS, min_periods=21).sum().diff()

def f38_drts_007_failed_21d_breakout_followthrough_count_63d_d1(high, close):
    h21 = high.rolling(MDAYS, min_periods=5).max().shift(1)
    broke_then_back = ((close.shift(WDAYS) > h21.shift(WDAYS)) & (close < h21.shift(WDAYS))).astype(float)
    return broke_then_back.rolling(QDAYS, min_periods=21).sum().diff()

def f38_drts_008_pct_time_within_2pct_of_63d_max_63d_d1(close, high):
    rmax = high.rolling(QDAYS, min_periods=21).max()
    within = (close / rmax >= 0.98).astype(float)
    return within.rolling(QDAYS, min_periods=21).mean().diff()

def f38_drts_009_range_contraction_index_21d_vs_63d_d1(high, low):
    r21 = high.rolling(MDAYS, min_periods=5).max() - low.rolling(MDAYS, min_periods=5).min()
    r63 = high.rolling(QDAYS, min_periods=21).max() - low.rolling(QDAYS, min_periods=21).min()
    return _safe_div(r21, r63).diff()

def f38_drts_010_close_in_top_third_of_day_range_count_21d_d1(open_, high, low, close):
    rng = (high - low).replace(0, np.nan)
    pos = (close - low) / rng
    return (pos >= 2.0 / 3.0).astype(float).rolling(MDAYS, min_periods=5).sum().diff()

def f38_drts_011_equal_close_count_21d_d1(close):
    eq = (close.diff().abs() < close.abs() * 0.0005).astype(float)
    return eq.rolling(MDAYS, min_periods=5).sum().diff()

def f38_drts_012_inside_day_count_63d_d1(high, low):
    inside = ((high < high.shift(1)) & (low > low.shift(1))).astype(float)
    return inside.rolling(QDAYS, min_periods=21).sum().diff()

def f38_drts_013_narrow_range_4_count_21d_d1(high, low):
    rng = high - low
    nr4 = (rng < rng.rolling(4, min_periods=4).min().shift(1)).astype(float)
    return nr4.rolling(MDAYS, min_periods=5).sum().diff()

def f38_drts_014_churn_index_63d_d1(high, low, close, volume):
    rng = (high - low).replace(0, np.nan)
    dv = volume * close
    return _safe_div(dv, rng).rolling(QDAYS, min_periods=21).mean().diff()

def f38_drts_015_top_dwell_to_peak_amplitude_ratio_63d_d1(close, high, low):
    rmax = high.rolling(QDAYS, min_periods=21).max()
    rmin = low.rolling(QDAYS, min_periods=21).min()
    dwell = (close / rmax >= 0.97).astype(float).rolling(QDAYS, min_periods=21).sum()
    amp = _safe_div(rmax - rmin, rmin.abs())
    return _safe_div(dwell, amp).diff()

def f38_drts_016_days_within_atr_of_252d_high_in_63d_d1(close, high, low):
    atr21 = _atr(high, low, close, 21)
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    within = ((rmax - close).abs() <= atr21).astype(float)
    return within.rolling(QDAYS, min_periods=21).sum().diff()

def f38_drts_017_consecutive_higher_highs_streak_max_63d_d1(high):
    hh = (high > high.shift(1)).astype(int)
    return _streak_last_down(hh, QDAYS).diff()

def f38_drts_018_higher_highs_minus_higher_lows_count_63d_d1(high, low):
    hh = (high > high.shift(1)).astype(float)
    hl = (low > low.shift(1)).astype(float)
    return (hh - hl).rolling(QDAYS, min_periods=21).sum().diff()

def f38_drts_019_top_pattern_width_proxy_63d_d1(close, high, low):
    rmax = high.rolling(QDAYS, min_periods=21).max()
    rmin = low.rolling(QDAYS, min_periods=21).min()
    rng = (rmax - rmin).replace(0, np.nan)
    in_top = (close - rmin) / rng >= 0.85
    return in_top.rolling(QDAYS, min_periods=21).sum().diff()

def f38_drts_020_top_dwell_zscore_252d_d1(close, high):
    rmax = high.rolling(QDAYS, min_periods=21).max()
    dwell = (close / rmax >= 0.97).astype(float).rolling(QDAYS, min_periods=21).sum()
    return _rolling_zscore(dwell, YDAYS, min_periods=63).diff()

def f38_drts_021_weekly_high_break_failures_8w_d1(high, close):
    h5 = high.rolling(WDAYS, min_periods=3).max().shift(1)
    failed = ((high > h5) & (close < h5)).astype(float)
    return failed.rolling(40, min_periods=10).sum().diff()

def f38_drts_022_monthly_high_break_failures_6m_d1(high, close):
    h21 = high.rolling(MDAYS, min_periods=10).max().shift(1)
    failed = ((high > h21) & (close < h21)).astype(float)
    return failed.rolling(126, min_periods=40).sum().diff()

def f38_drts_023_failed_252d_high_breakout_count_d1(high, close):
    h252 = high.rolling(YDAYS, min_periods=QDAYS).max().shift(1)
    failed = ((high > h252) & (close < h252)).astype(float)
    return failed.rolling(YDAYS, min_periods=QDAYS).sum().diff()

def f38_drts_024_bull_trap_count_63d_d1(high, close):
    h21 = high.rolling(MDAYS, min_periods=5).max().shift(1)
    trapped = ((close.shift(WDAYS) > h21.shift(WDAYS)) & (close / close.shift(WDAYS) - 1.0 < -0.03)).astype(float)
    return trapped.rolling(QDAYS, min_periods=21).sum().diff()

def f38_drts_025_supply_zone_cluster_count_63d_d1(close, high, volume):
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    v_avg = volume.rolling(MDAYS, min_periods=5).mean()
    cluster = ((close / rmax >= 0.95) & (volume > 1.5 * v_avg)).astype(float)
    return cluster.rolling(QDAYS, min_periods=21).sum().diff()

def f38_drts_026_retest_failure_count_42d_d1(high, close):
    h21 = high.rolling(MDAYS, min_periods=5).max().shift(1)
    test = (high >= h21 * 0.99).astype(float)
    fail = (close < high.rolling(WDAYS, min_periods=2).mean()).astype(float)
    return (test * fail).rolling(42, min_periods=10).sum().diff()

def f38_drts_027_resistance_touch_count_63d_d1(high, close):
    rmax = high.rolling(QDAYS, min_periods=21).max()
    touch = ((high >= rmax * 0.98) & (close < rmax * 0.98)).astype(float)
    return touch.rolling(QDAYS, min_periods=21).sum().diff()

def f38_drts_028_days_since_first_failed_breakout_from_252d_high_d1(high, close):
    h252 = high.rolling(YDAYS, min_periods=QDAYS).max().shift(1)
    failed_today = ((high > h252) & (close < h252)).astype(float)
    cum = failed_today.cumsum()
    last_fail = cum.where(failed_today > 0).ffill()
    age = cum - last_fail
    return age.fillna(np.nan).diff()

def f38_drts_029_peak_breakdown_sharpness_21d_d1(high, close):
    rmax = high.rolling(QDAYS, min_periods=21).max()
    return _safe_div(close - rmax, rmax.abs()).diff()

def f38_drts_030_lower_high_count_63d_d1(high):
    lh = (high < high.shift(1)).astype(float)
    return lh.rolling(QDAYS, min_periods=21).sum().diff()

def f38_drts_031_lower_high_to_higher_high_ratio_63d_d1(high):
    hh = (high > high.shift(1)).astype(float).rolling(QDAYS, min_periods=21).sum()
    lh = (high < high.shift(1)).astype(float).rolling(QDAYS, min_periods=21).sum()
    return _safe_div(lh, hh + 1.0).diff()

def f38_drts_032_distribution_day_count_25d_d1(close, high, low, volume):
    rng = (high - low).replace(0, np.nan)
    pos = (close - low) / rng
    v_avg = volume.rolling(MDAYS, min_periods=5).mean()
    dist = ((pos < 1.0 / 3.0) & (close < close.shift(1)) & (volume > v_avg)).astype(float)
    return dist.rolling(25, min_periods=8).sum().diff()

def f38_drts_033_distribution_day_share_of_decline_63d_d1(close, high, low, volume):
    rng = (high - low).replace(0, np.nan)
    pos = (close - low) / rng
    v_avg = volume.rolling(MDAYS, min_periods=5).mean()
    dist = ((pos < 1.0 / 3.0) & (close < close.shift(1)) & (volume > v_avg)).astype(float)
    decl = (close < close.shift(1)).astype(float)
    return _safe_div(dist.rolling(QDAYS, min_periods=21).sum(), decl.rolling(QDAYS, min_periods=21).sum()).diff()

def f38_drts_034_close_below_open_count_21d_d1(open_, close):
    return (close < open_).astype(float).rolling(MDAYS, min_periods=5).sum().diff()

def f38_drts_035_close_below_open_share_63d_d1(open_, close):
    return (close < open_).astype(float).rolling(QDAYS, min_periods=21).mean().diff()

def f38_drts_036_negative_outside_day_count_63d_d1(high, low, close):
    outside = (high > high.shift(1)) & (low < low.shift(1))
    bearish = close < close.shift(1)
    return (outside & bearish).astype(float).rolling(QDAYS, min_periods=21).sum().diff()

def f38_drts_037_outside_day_bearish_count_42d_d1(high, low, close, open_):
    outside = (high > high.shift(1)) & (low < low.shift(1))
    bearish = close < open_
    return (outside & bearish).astype(float).rolling(42, min_periods=10).sum().diff()

def f38_drts_038_high_test_failure_volume_avg_21d_d1(high, close, volume):
    h21 = high.rolling(MDAYS, min_periods=5).max().shift(1)
    failed = (high > h21) & (close < h21)
    masked_vol = volume.where(failed, np.nan)
    return masked_vol.rolling(MDAYS, min_periods=2).mean().diff()

def f38_drts_039_low_test_holds_count_21d_d1(low, close):
    l21 = low.rolling(MDAYS, min_periods=5).min().shift(1)
    held = ((low <= l21) & (close > l21)).astype(float)
    return held.rolling(MDAYS, min_periods=5).sum().diff()

def f38_drts_040_churning_index_63d_d1(high, low, volume):
    rng = (high - low).replace(0, np.nan)
    return _safe_div(volume, rng).rolling(QDAYS, min_periods=21).mean().diff()

def f38_drts_041_stair_step_lower_high_sequence_63d_d1(high):
    hh = high.rolling(5, min_periods=3).max()
    seq = (hh < hh.shift(5)).astype(float)
    return seq.rolling(QDAYS, min_periods=21).sum().diff()

def f38_drts_042_swing_high_height_decay_63d_d1(high):
    hh = high.rolling(5, min_periods=3).max()
    return (hh - hh.shift(QDAYS)).diff()

def f38_drts_043_swing_low_height_decay_63d_d1(low):
    ll = low.rolling(5, min_periods=3).min()
    return (ll.shift(QDAYS) - ll).diff()

def f38_drts_044_zigzag_top_amplitude_decay_63d_d1(high, low):
    amp = high.rolling(MDAYS, min_periods=5).max() - low.rolling(MDAYS, min_periods=5).min()
    return (amp - amp.shift(QDAYS)).diff()

def f38_drts_045_consecutive_lower_highs_streak_max_63d_d1(high):
    lh = (high < high.shift(1)).astype(int)
    return _streak_last_down(lh, QDAYS).diff()

def f38_drts_046_consecutive_lower_closes_streak_max_21d_d1(close):
    lc = (close < close.shift(1)).astype(int)
    return _streak_last_down(lc, MDAYS).diff()

def f38_drts_047_close_below_5d_high_count_21d_d1(high, close):
    h5 = high.rolling(WDAYS, min_periods=3).max().shift(1)
    return (close < h5).astype(float).rolling(MDAYS, min_periods=5).sum().diff()

def f38_drts_048_close_below_21d_high_count_63d_d1(high, close):
    h21 = high.rolling(MDAYS, min_periods=5).max().shift(1)
    return (close < h21).astype(float).rolling(QDAYS, min_periods=21).sum().diff()

def f38_drts_049_negative_5d_close_count_63d_d1(close):
    ret5 = close / close.shift(WDAYS) - 1.0
    return (ret5 < 0).astype(float).rolling(QDAYS, min_periods=21).sum().diff()

def f38_drts_050_close_below_sma21_count_63d_d1(close):
    sma = close.rolling(MDAYS, min_periods=5).mean()
    return (close < sma).astype(float).rolling(QDAYS, min_periods=21).sum().diff()

def f38_drts_051_up_bars_share_decline_63d_vs_21d_d1(close):
    up63 = (close > close.shift(1)).astype(float).rolling(QDAYS, min_periods=21).mean()
    up21 = (close > close.shift(1)).astype(float).rolling(MDAYS, min_periods=5).mean()
    return (up21 - up63).diff()

def f38_drts_052_down_close_streak_max_42d_d1(close):
    dc = (close < close.shift(1)).astype(int)
    return _streak_last_down(dc, 42).diff()

def f38_drts_053_roll_off_top_velocity_21d_d1(high, close):
    rmax = high.rolling(QDAYS, min_periods=21).max()
    return _safe_div(close - rmax, rmax.abs()).diff().rolling(MDAYS, min_periods=5).mean().diff()

def f38_drts_054_peak_to_current_amplitude_share_63d_d1(close, high, low):
    rmax = high.rolling(QDAYS, min_periods=21).max()
    rmin = low.rolling(QDAYS, min_periods=21).min()
    rng = (rmax - rmin).replace(0, np.nan)
    return _safe_div(close - rmin, rng).diff()

def f38_drts_055_fading_high_strength_index_63d_d1(high, low, close):
    atr21 = _atr(high, low, close, 21)
    atr63 = _atr(high, low, close, 63)
    return (atr21 - atr63).diff()

def f38_drts_056_high_age_in_days_63d_d1(high):
    rmax = high.rolling(QDAYS, min_periods=21).max()
    age = (high < rmax).astype(int).rolling(QDAYS, min_periods=21).apply(lambda w: int(w[::-1].cumprod().sum()), raw=True)
    return age.diff()

def f38_drts_057_high_age_to_avg_age_ratio_63d_d1(high):
    rmax = high.rolling(QDAYS, min_periods=21).max()
    age = (high < rmax).astype(int).rolling(QDAYS, min_periods=21).apply(lambda w: int(w[::-1].cumprod().sum()), raw=True)
    return _safe_div(age, age.rolling(YDAYS, min_periods=QDAYS).mean()).diff()

def f38_drts_058_days_since_252d_high_d1(high):
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    age = (high < rmax).astype(int).rolling(YDAYS, min_periods=QDAYS).apply(lambda w: int(w[::-1].cumprod().sum()), raw=True)
    return age.diff()

def f38_drts_059_session_close_below_open_share_21d_d1(open_, close):
    return (close < open_).astype(float).rolling(MDAYS, min_periods=5).mean().diff()

def f38_drts_060_closing_strength_decay_index_21d_d1(high, low, close):
    rng = (high - low).replace(0, np.nan)
    cs = (close - low) / rng
    return (cs.rolling(WDAYS, min_periods=2).mean() - cs.rolling(MDAYS, min_periods=5).mean()).diff()

def f38_drts_061_range_per_dollar_volume_avg_21d_d1(high, low, close, volume):
    rng = high - low
    return _safe_div(rng, volume * close).rolling(MDAYS, min_periods=5).mean().diff()

def f38_drts_062_up_day_volume_share_decline_63d_d1(close, volume):
    up = close > close.shift(1)
    upv = volume.where(up, 0).rolling(QDAYS, min_periods=21).sum()
    total = volume.rolling(QDAYS, min_periods=21).sum()
    share = _safe_div(upv, total)
    return (share - share.shift(QDAYS)).diff()

def f38_drts_063_effort_result_divergence_21d_d1(high, low, volume):
    rng = high - low
    z_rng = _rolling_zscore(rng, MDAYS, 5)
    z_vol = _rolling_zscore(volume, MDAYS, 5)
    return (z_vol - z_rng).diff()

def f38_drts_064_volume_climax_at_top_coincidence_21d_d1(high, volume):
    rmax = high.rolling(MDAYS, min_periods=5).max()
    at_top = (high >= rmax).astype(float)
    v_avg = volume.rolling(MDAYS, min_periods=5).mean()
    climax = ((volume > 2.0 * v_avg) & (at_top > 0)).astype(float)
    return climax.rolling(MDAYS, min_periods=5).sum().diff()

def f38_drts_065_distribution_efficiency_index_63d_d1(close, high, low, volume):
    rng = (high - low).replace(0, np.nan)
    pos = (close - low) / rng
    weighted = (1.0 - pos) * volume
    return (weighted.rolling(QDAYS, min_periods=21).sum() / volume.rolling(QDAYS, min_periods=21).sum().replace(0, np.nan)).diff()

def f38_drts_066_price_volume_divergence_zscore_42d_d1(close, volume):
    z_p = _rolling_zscore(close, 42, 10)
    z_v = _rolling_zscore(volume, 42, 10)
    return (z_p - z_v).diff()

def f38_drts_067_obv_minus_price_slope_42d_d1(close, volume):
    sign = np.sign(close.diff().fillna(0))
    obv = (sign * volume).cumsum()
    obv_slope = obv.diff(42)
    price_slope = close.diff(42)
    return (_safe_div(price_slope, close.abs()) - _safe_div(obv_slope, obv.abs())).diff()

def f38_drts_068_ad_line_slope_21d_d1(high, low, close, volume):
    rng = (high - low).replace(0, np.nan)
    mfm = (close - low - (high - close)) / rng
    mfv = mfm * volume
    ad = mfv.cumsum()
    return ad.diff(MDAYS).diff()

def f38_drts_069_up_volume_minus_down_volume_share_42d_d1(close, volume):
    up = close > close.shift(1)
    upv = volume.where(up, 0).rolling(42, min_periods=10).sum()
    dnv = volume.where(~up, 0).rolling(42, min_periods=10).sum()
    total = volume.rolling(42, min_periods=10).sum().replace(0, np.nan)
    return ((upv - dnv) / total).diff()

def f38_drts_070_chaikin_money_flow_21d_d1(high, low, close, volume):
    rng = (high - low).replace(0, np.nan)
    mfm = (close - low - (high - close)) / rng
    mfv = mfm * volume
    return (mfv.rolling(MDAYS, min_periods=5).sum() / volume.rolling(MDAYS, min_periods=5).sum().replace(0, np.nan)).diff()

def f38_drts_071_chaikin_oscillator_21d_d1(high, low, close, volume):
    rng = (high - low).replace(0, np.nan)
    mfm = (close - low - (high - close)) / rng
    mfv = mfm * volume
    ad = mfv.cumsum()
    return (ad.ewm(span=3, adjust=False, min_periods=3).mean() - ad.ewm(span=10, adjust=False, min_periods=5).mean()).diff()

def f38_drts_072_ad_line_minus_price_zscore_42d_d1(high, low, close, volume):
    rng = (high - low).replace(0, np.nan)
    mfm = (close - low - (high - close)) / rng
    ad = (mfm * volume).cumsum()
    return (_rolling_zscore(ad, 42, 10) - _rolling_zscore(close, 42, 10)).diff()

def f38_drts_073_wyckoff_distribution_proxy_63d_d1(close, high, low, volume):
    rmax = high.rolling(QDAYS, min_periods=21).max()
    near_top = close / rmax >= 0.95
    flat = close.diff().abs() < _atr(high, low, close, 21) * 0.25
    vol_z = _rolling_zscore(volume, MDAYS, 5)
    sig = (near_top & flat & (vol_z > 1.0)).astype(float)
    return sig.rolling(QDAYS, min_periods=21).sum().diff()

def f38_drts_074_high_volume_down_bar_count_42d_d1(close, volume):
    v_avg = volume.rolling(MDAYS, min_periods=5).mean()
    hv_down = ((close < close.shift(1)) & (volume > 1.5 * v_avg)).astype(float)
    return hv_down.rolling(42, min_periods=10).sum().diff()

def f38_drts_075_low_volume_up_bar_count_42d_d1(close, volume):
    v_avg = volume.rolling(MDAYS, min_periods=5).mean()
    lv_up = ((close > close.shift(1)) & (volume < 0.7 * v_avg)).astype(float)
    return lv_up.rolling(42, min_periods=10).sum().diff()
DISTRIBUTION_ROLLING_TOP_SIGNATURE_D1_REGISTRY_001_075 = {'f38_drts_001_days_within_top_decile_252d_in_63d_d1': {'inputs': ['high', 'close'], 'func': f38_drts_001_days_within_top_decile_252d_in_63d_d1}, 'f38_drts_002_range_compression_at_top_21d_d1': {'inputs': ['high', 'low', 'close'], 'func': f38_drts_002_range_compression_at_top_21d_d1}, 'f38_drts_003_close_within_5pct_of_252d_max_count_63d_d1': {'inputs': ['close', 'high'], 'func': f38_drts_003_close_within_5pct_of_252d_max_count_63d_d1}, 'f38_drts_004_consec_close_within_5pct_252d_max_streak_63d_d1': {'inputs': ['close', 'high'], 'func': f38_drts_004_consec_close_within_5pct_252d_max_streak_63d_d1}, 'f38_drts_005_new_21d_high_count_63d_d1': {'inputs': ['high'], 'func': f38_drts_005_new_21d_high_count_63d_d1}, 'f38_drts_006_failed_21d_high_count_63d_d1': {'inputs': ['high', 'close'], 'func': f38_drts_006_failed_21d_high_count_63d_d1}, 'f38_drts_007_failed_21d_breakout_followthrough_count_63d_d1': {'inputs': ['high', 'close'], 'func': f38_drts_007_failed_21d_breakout_followthrough_count_63d_d1}, 'f38_drts_008_pct_time_within_2pct_of_63d_max_63d_d1': {'inputs': ['close', 'high'], 'func': f38_drts_008_pct_time_within_2pct_of_63d_max_63d_d1}, 'f38_drts_009_range_contraction_index_21d_vs_63d_d1': {'inputs': ['high', 'low'], 'func': f38_drts_009_range_contraction_index_21d_vs_63d_d1}, 'f38_drts_010_close_in_top_third_of_day_range_count_21d_d1': {'inputs': ['open', 'high', 'low', 'close'], 'func': f38_drts_010_close_in_top_third_of_day_range_count_21d_d1}, 'f38_drts_011_equal_close_count_21d_d1': {'inputs': ['close'], 'func': f38_drts_011_equal_close_count_21d_d1}, 'f38_drts_012_inside_day_count_63d_d1': {'inputs': ['high', 'low'], 'func': f38_drts_012_inside_day_count_63d_d1}, 'f38_drts_013_narrow_range_4_count_21d_d1': {'inputs': ['high', 'low'], 'func': f38_drts_013_narrow_range_4_count_21d_d1}, 'f38_drts_014_churn_index_63d_d1': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f38_drts_014_churn_index_63d_d1}, 'f38_drts_015_top_dwell_to_peak_amplitude_ratio_63d_d1': {'inputs': ['close', 'high', 'low'], 'func': f38_drts_015_top_dwell_to_peak_amplitude_ratio_63d_d1}, 'f38_drts_016_days_within_atr_of_252d_high_in_63d_d1': {'inputs': ['close', 'high', 'low'], 'func': f38_drts_016_days_within_atr_of_252d_high_in_63d_d1}, 'f38_drts_017_consecutive_higher_highs_streak_max_63d_d1': {'inputs': ['high'], 'func': f38_drts_017_consecutive_higher_highs_streak_max_63d_d1}, 'f38_drts_018_higher_highs_minus_higher_lows_count_63d_d1': {'inputs': ['high', 'low'], 'func': f38_drts_018_higher_highs_minus_higher_lows_count_63d_d1}, 'f38_drts_019_top_pattern_width_proxy_63d_d1': {'inputs': ['close', 'high', 'low'], 'func': f38_drts_019_top_pattern_width_proxy_63d_d1}, 'f38_drts_020_top_dwell_zscore_252d_d1': {'inputs': ['close', 'high'], 'func': f38_drts_020_top_dwell_zscore_252d_d1}, 'f38_drts_021_weekly_high_break_failures_8w_d1': {'inputs': ['high', 'close'], 'func': f38_drts_021_weekly_high_break_failures_8w_d1}, 'f38_drts_022_monthly_high_break_failures_6m_d1': {'inputs': ['high', 'close'], 'func': f38_drts_022_monthly_high_break_failures_6m_d1}, 'f38_drts_023_failed_252d_high_breakout_count_d1': {'inputs': ['high', 'close'], 'func': f38_drts_023_failed_252d_high_breakout_count_d1}, 'f38_drts_024_bull_trap_count_63d_d1': {'inputs': ['high', 'close'], 'func': f38_drts_024_bull_trap_count_63d_d1}, 'f38_drts_025_supply_zone_cluster_count_63d_d1': {'inputs': ['close', 'high', 'volume'], 'func': f38_drts_025_supply_zone_cluster_count_63d_d1}, 'f38_drts_026_retest_failure_count_42d_d1': {'inputs': ['high', 'close'], 'func': f38_drts_026_retest_failure_count_42d_d1}, 'f38_drts_027_resistance_touch_count_63d_d1': {'inputs': ['high', 'close'], 'func': f38_drts_027_resistance_touch_count_63d_d1}, 'f38_drts_028_days_since_first_failed_breakout_from_252d_high_d1': {'inputs': ['high', 'close'], 'func': f38_drts_028_days_since_first_failed_breakout_from_252d_high_d1}, 'f38_drts_029_peak_breakdown_sharpness_21d_d1': {'inputs': ['high', 'close'], 'func': f38_drts_029_peak_breakdown_sharpness_21d_d1}, 'f38_drts_030_lower_high_count_63d_d1': {'inputs': ['high'], 'func': f38_drts_030_lower_high_count_63d_d1}, 'f38_drts_031_lower_high_to_higher_high_ratio_63d_d1': {'inputs': ['high'], 'func': f38_drts_031_lower_high_to_higher_high_ratio_63d_d1}, 'f38_drts_032_distribution_day_count_25d_d1': {'inputs': ['close', 'high', 'low', 'volume'], 'func': f38_drts_032_distribution_day_count_25d_d1}, 'f38_drts_033_distribution_day_share_of_decline_63d_d1': {'inputs': ['close', 'high', 'low', 'volume'], 'func': f38_drts_033_distribution_day_share_of_decline_63d_d1}, 'f38_drts_034_close_below_open_count_21d_d1': {'inputs': ['open', 'close'], 'func': f38_drts_034_close_below_open_count_21d_d1}, 'f38_drts_035_close_below_open_share_63d_d1': {'inputs': ['open', 'close'], 'func': f38_drts_035_close_below_open_share_63d_d1}, 'f38_drts_036_negative_outside_day_count_63d_d1': {'inputs': ['high', 'low', 'close'], 'func': f38_drts_036_negative_outside_day_count_63d_d1}, 'f38_drts_037_outside_day_bearish_count_42d_d1': {'inputs': ['high', 'low', 'close', 'open'], 'func': f38_drts_037_outside_day_bearish_count_42d_d1}, 'f38_drts_038_high_test_failure_volume_avg_21d_d1': {'inputs': ['high', 'close', 'volume'], 'func': f38_drts_038_high_test_failure_volume_avg_21d_d1}, 'f38_drts_039_low_test_holds_count_21d_d1': {'inputs': ['low', 'close'], 'func': f38_drts_039_low_test_holds_count_21d_d1}, 'f38_drts_040_churning_index_63d_d1': {'inputs': ['high', 'low', 'volume'], 'func': f38_drts_040_churning_index_63d_d1}, 'f38_drts_041_stair_step_lower_high_sequence_63d_d1': {'inputs': ['high'], 'func': f38_drts_041_stair_step_lower_high_sequence_63d_d1}, 'f38_drts_042_swing_high_height_decay_63d_d1': {'inputs': ['high'], 'func': f38_drts_042_swing_high_height_decay_63d_d1}, 'f38_drts_043_swing_low_height_decay_63d_d1': {'inputs': ['low'], 'func': f38_drts_043_swing_low_height_decay_63d_d1}, 'f38_drts_044_zigzag_top_amplitude_decay_63d_d1': {'inputs': ['high', 'low'], 'func': f38_drts_044_zigzag_top_amplitude_decay_63d_d1}, 'f38_drts_045_consecutive_lower_highs_streak_max_63d_d1': {'inputs': ['high'], 'func': f38_drts_045_consecutive_lower_highs_streak_max_63d_d1}, 'f38_drts_046_consecutive_lower_closes_streak_max_21d_d1': {'inputs': ['close'], 'func': f38_drts_046_consecutive_lower_closes_streak_max_21d_d1}, 'f38_drts_047_close_below_5d_high_count_21d_d1': {'inputs': ['high', 'close'], 'func': f38_drts_047_close_below_5d_high_count_21d_d1}, 'f38_drts_048_close_below_21d_high_count_63d_d1': {'inputs': ['high', 'close'], 'func': f38_drts_048_close_below_21d_high_count_63d_d1}, 'f38_drts_049_negative_5d_close_count_63d_d1': {'inputs': ['close'], 'func': f38_drts_049_negative_5d_close_count_63d_d1}, 'f38_drts_050_close_below_sma21_count_63d_d1': {'inputs': ['close'], 'func': f38_drts_050_close_below_sma21_count_63d_d1}, 'f38_drts_051_up_bars_share_decline_63d_vs_21d_d1': {'inputs': ['close'], 'func': f38_drts_051_up_bars_share_decline_63d_vs_21d_d1}, 'f38_drts_052_down_close_streak_max_42d_d1': {'inputs': ['close'], 'func': f38_drts_052_down_close_streak_max_42d_d1}, 'f38_drts_053_roll_off_top_velocity_21d_d1': {'inputs': ['high', 'close'], 'func': f38_drts_053_roll_off_top_velocity_21d_d1}, 'f38_drts_054_peak_to_current_amplitude_share_63d_d1': {'inputs': ['close', 'high', 'low'], 'func': f38_drts_054_peak_to_current_amplitude_share_63d_d1}, 'f38_drts_055_fading_high_strength_index_63d_d1': {'inputs': ['high', 'low', 'close'], 'func': f38_drts_055_fading_high_strength_index_63d_d1}, 'f38_drts_056_high_age_in_days_63d_d1': {'inputs': ['high'], 'func': f38_drts_056_high_age_in_days_63d_d1}, 'f38_drts_057_high_age_to_avg_age_ratio_63d_d1': {'inputs': ['high'], 'func': f38_drts_057_high_age_to_avg_age_ratio_63d_d1}, 'f38_drts_058_days_since_252d_high_d1': {'inputs': ['high'], 'func': f38_drts_058_days_since_252d_high_d1}, 'f38_drts_059_session_close_below_open_share_21d_d1': {'inputs': ['open', 'close'], 'func': f38_drts_059_session_close_below_open_share_21d_d1}, 'f38_drts_060_closing_strength_decay_index_21d_d1': {'inputs': ['high', 'low', 'close'], 'func': f38_drts_060_closing_strength_decay_index_21d_d1}, 'f38_drts_061_range_per_dollar_volume_avg_21d_d1': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f38_drts_061_range_per_dollar_volume_avg_21d_d1}, 'f38_drts_062_up_day_volume_share_decline_63d_d1': {'inputs': ['close', 'volume'], 'func': f38_drts_062_up_day_volume_share_decline_63d_d1}, 'f38_drts_063_effort_result_divergence_21d_d1': {'inputs': ['high', 'low', 'volume'], 'func': f38_drts_063_effort_result_divergence_21d_d1}, 'f38_drts_064_volume_climax_at_top_coincidence_21d_d1': {'inputs': ['high', 'volume'], 'func': f38_drts_064_volume_climax_at_top_coincidence_21d_d1}, 'f38_drts_065_distribution_efficiency_index_63d_d1': {'inputs': ['close', 'high', 'low', 'volume'], 'func': f38_drts_065_distribution_efficiency_index_63d_d1}, 'f38_drts_066_price_volume_divergence_zscore_42d_d1': {'inputs': ['close', 'volume'], 'func': f38_drts_066_price_volume_divergence_zscore_42d_d1}, 'f38_drts_067_obv_minus_price_slope_42d_d1': {'inputs': ['close', 'volume'], 'func': f38_drts_067_obv_minus_price_slope_42d_d1}, 'f38_drts_068_ad_line_slope_21d_d1': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f38_drts_068_ad_line_slope_21d_d1}, 'f38_drts_069_up_volume_minus_down_volume_share_42d_d1': {'inputs': ['close', 'volume'], 'func': f38_drts_069_up_volume_minus_down_volume_share_42d_d1}, 'f38_drts_070_chaikin_money_flow_21d_d1': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f38_drts_070_chaikin_money_flow_21d_d1}, 'f38_drts_071_chaikin_oscillator_21d_d1': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f38_drts_071_chaikin_oscillator_21d_d1}, 'f38_drts_072_ad_line_minus_price_zscore_42d_d1': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f38_drts_072_ad_line_minus_price_zscore_42d_d1}, 'f38_drts_073_wyckoff_distribution_proxy_63d_d1': {'inputs': ['close', 'high', 'low', 'volume'], 'func': f38_drts_073_wyckoff_distribution_proxy_63d_d1}, 'f38_drts_074_high_volume_down_bar_count_42d_d1': {'inputs': ['close', 'volume'], 'func': f38_drts_074_high_volume_down_bar_count_42d_d1}, 'f38_drts_075_low_volume_up_bar_count_42d_d1': {'inputs': ['close', 'volume'], 'func': f38_drts_075_low_volume_up_bar_count_42d_d1}}