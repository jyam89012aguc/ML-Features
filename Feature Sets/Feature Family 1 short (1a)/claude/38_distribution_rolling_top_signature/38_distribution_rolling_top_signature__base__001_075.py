"""distribution_rolling_top_signature base features 001-075 — Pipeline 1a-inverse short-side blowup family.

75 distinct hypotheses about rolling-top distribution patterns near peak (continued in
__base__076_150.py). Inputs: SEP OHLCV. PIT-clean: right-anchored rolling, explicit
min_periods, no centered windows, no .shift(-N).
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


def _true_range(high, low, close):
    pc = close.shift(1)
    return pd.concat([high - low, (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)


def _atr(high, low, close, n=21):
    return _true_range(high, low, close).rolling(n, min_periods=max(n // 3, 2)).mean()


def _streak_last_down(s, window):
    return s.rolling(window, min_periods=3).apply(
        lambda w: int(w[::-1].cumprod().sum()) if w.size else np.nan, raw=True,
    )


# ============================================================
#                    FEATURES 001-075
# ============================================================

# ---- Block A: rolling-top range & duration (001-020) ----

def f38_drts_001_days_within_top_decile_252d_in_63d(high, close):
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = high.rolling(YDAYS, min_periods=QDAYS).min()
    rng = (rmax - rmin).replace(0, np.nan)
    in_top = ((close - rmin) / rng) >= 0.90
    return in_top.rolling(QDAYS, min_periods=21).sum()


def f38_drts_002_range_compression_at_top_21d(high, low, close):
    atr21 = _atr(high, low, close, 21)
    atr63 = _atr(high, low, close, 63)
    return _safe_div(atr21, atr63)


def f38_drts_003_close_within_5pct_of_252d_max_count_63d(close, high):
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    within = close / rmax >= 0.95
    return within.rolling(QDAYS, min_periods=21).sum()


def f38_drts_004_consec_close_within_5pct_252d_max_streak_63d(close, high):
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    within = (close / rmax >= 0.95).astype(int)
    return _streak_last_down(within, QDAYS)


def f38_drts_005_new_21d_high_count_63d(high):
    nh = (high >= high.rolling(MDAYS, min_periods=5).max().shift(1)).astype(float)
    return nh.rolling(QDAYS, min_periods=21).sum()


def f38_drts_006_failed_21d_high_count_63d(high, close):
    h21 = high.rolling(MDAYS, min_periods=5).max().shift(1)
    failed = ((high > h21) & (close < h21)).astype(float)
    return failed.rolling(QDAYS, min_periods=21).sum()


def f38_drts_007_failed_21d_breakout_followthrough_count_63d(high, close):
    h21 = high.rolling(MDAYS, min_periods=5).max().shift(1)
    # PIT: at bar t, look at what happened 5 bars ago — was there a breakout that has since failed?
    broke_then_back = ((close.shift(WDAYS) > h21.shift(WDAYS)) & (close < h21.shift(WDAYS))).astype(float)
    return broke_then_back.rolling(QDAYS, min_periods=21).sum()


def f38_drts_008_pct_time_within_2pct_of_63d_max_63d(close, high):
    rmax = high.rolling(QDAYS, min_periods=21).max()
    within = (close / rmax >= 0.98).astype(float)
    return within.rolling(QDAYS, min_periods=21).mean()


def f38_drts_009_range_contraction_index_21d_vs_63d(high, low):
    r21 = (high.rolling(MDAYS, min_periods=5).max() - low.rolling(MDAYS, min_periods=5).min())
    r63 = (high.rolling(QDAYS, min_periods=21).max() - low.rolling(QDAYS, min_periods=21).min())
    return _safe_div(r21, r63)


def f38_drts_010_close_in_top_third_of_day_range_count_21d(open_, high, low, close):
    rng = (high - low).replace(0, np.nan)
    pos = (close - low) / rng
    return (pos >= 2.0 / 3.0).astype(float).rolling(MDAYS, min_periods=5).sum()


def f38_drts_011_equal_close_count_21d(close):
    eq = (close.diff().abs() < (close.abs() * 0.0005)).astype(float)
    return eq.rolling(MDAYS, min_periods=5).sum()


def f38_drts_012_inside_day_count_63d(high, low):
    inside = ((high < high.shift(1)) & (low > low.shift(1))).astype(float)
    return inside.rolling(QDAYS, min_periods=21).sum()


def f38_drts_013_narrow_range_4_count_21d(high, low):
    rng = high - low
    nr4 = (rng < rng.rolling(4, min_periods=4).min().shift(1)).astype(float)
    return nr4.rolling(MDAYS, min_periods=5).sum()


def f38_drts_014_churn_index_63d(high, low, close, volume):
    rng = (high - low).replace(0, np.nan)
    dv = volume * close
    return _safe_div(dv, rng).rolling(QDAYS, min_periods=21).mean()


def f38_drts_015_top_dwell_to_peak_amplitude_ratio_63d(close, high, low):
    rmax = high.rolling(QDAYS, min_periods=21).max()
    rmin = low.rolling(QDAYS, min_periods=21).min()
    dwell = (close / rmax >= 0.97).astype(float).rolling(QDAYS, min_periods=21).sum()
    amp = _safe_div(rmax - rmin, rmin.abs())
    return _safe_div(dwell, amp)


def f38_drts_016_days_within_atr_of_252d_high_in_63d(close, high, low):
    atr21 = _atr(high, low, close, 21)
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    within = ((rmax - close).abs() <= atr21).astype(float)
    return within.rolling(QDAYS, min_periods=21).sum()


def f38_drts_017_consecutive_higher_highs_streak_max_63d(high):
    hh = (high > high.shift(1)).astype(int)
    return _streak_last_down(hh, QDAYS)


def f38_drts_018_higher_highs_minus_higher_lows_count_63d(high, low):
    hh = (high > high.shift(1)).astype(float)
    hl = (low > low.shift(1)).astype(float)
    return (hh - hl).rolling(QDAYS, min_periods=21).sum()


def f38_drts_019_top_pattern_width_proxy_63d(close, high, low):
    rmax = high.rolling(QDAYS, min_periods=21).max()
    rmin = low.rolling(QDAYS, min_periods=21).min()
    rng = (rmax - rmin).replace(0, np.nan)
    in_top = (close - rmin) / rng >= 0.85
    return in_top.rolling(QDAYS, min_periods=21).sum()


def f38_drts_020_top_dwell_zscore_252d(close, high):
    rmax = high.rolling(QDAYS, min_periods=21).max()
    dwell = (close / rmax >= 0.97).astype(float).rolling(QDAYS, min_periods=21).sum()
    return _rolling_zscore(dwell, YDAYS, min_periods=63)


# ---- Block B: failed-breakout / supply zones (021-040) ----

def f38_drts_021_weekly_high_break_failures_8w(high, close):
    h5 = high.rolling(WDAYS, min_periods=3).max().shift(1)
    failed = ((high > h5) & (close < h5)).astype(float)
    return failed.rolling(40, min_periods=10).sum()


def f38_drts_022_monthly_high_break_failures_6m(high, close):
    h21 = high.rolling(MDAYS, min_periods=10).max().shift(1)
    failed = ((high > h21) & (close < h21)).astype(float)
    return failed.rolling(126, min_periods=40).sum()


def f38_drts_023_failed_252d_high_breakout_count(high, close):
    h252 = high.rolling(YDAYS, min_periods=QDAYS).max().shift(1)
    failed = ((high > h252) & (close < h252)).astype(float)
    return failed.rolling(YDAYS, min_periods=QDAYS).sum()


def f38_drts_024_bull_trap_count_63d(high, close):
    h21 = high.rolling(MDAYS, min_periods=5).max().shift(1)
    # PIT: at bar t, detect that 5 bars ago there was a breakout above h21 that has since reversed -3%+
    trapped = ((close.shift(WDAYS) > h21.shift(WDAYS)) & ((close / close.shift(WDAYS) - 1.0) < -0.03)).astype(float)
    return trapped.rolling(QDAYS, min_periods=21).sum()


def f38_drts_025_supply_zone_cluster_count_63d(close, high, volume):
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    v_avg = volume.rolling(MDAYS, min_periods=5).mean()
    cluster = ((close / rmax >= 0.95) & (volume > 1.5 * v_avg)).astype(float)
    return cluster.rolling(QDAYS, min_periods=21).sum()


def f38_drts_026_retest_failure_count_42d(high, close):
    h21 = high.rolling(MDAYS, min_periods=5).max().shift(1)
    test = (high >= h21 * 0.99).astype(float)
    fail = (close < high.rolling(WDAYS, min_periods=2).mean()).astype(float)
    return (test * fail).rolling(42, min_periods=10).sum()


def f38_drts_027_resistance_touch_count_63d(high, close):
    rmax = high.rolling(QDAYS, min_periods=21).max()
    touch = ((high >= rmax * 0.98) & (close < rmax * 0.98)).astype(float)
    return touch.rolling(QDAYS, min_periods=21).sum()


def f38_drts_028_days_since_first_failed_breakout_from_252d_high(high, close):
    h252 = high.rolling(YDAYS, min_periods=QDAYS).max().shift(1)
    failed_today = ((high > h252) & (close < h252)).astype(float)
    cum = failed_today.cumsum()
    last_fail = cum.where(failed_today > 0).ffill()
    age = cum - last_fail
    return age.fillna(np.nan)


def f38_drts_029_peak_breakdown_sharpness_21d(high, close):
    rmax = high.rolling(QDAYS, min_periods=21).max()
    return _safe_div(close - rmax, rmax.abs())


def f38_drts_030_lower_high_count_63d(high):
    lh = (high < high.shift(1)).astype(float)
    return lh.rolling(QDAYS, min_periods=21).sum()


def f38_drts_031_lower_high_to_higher_high_ratio_63d(high):
    hh = (high > high.shift(1)).astype(float).rolling(QDAYS, min_periods=21).sum()
    lh = (high < high.shift(1)).astype(float).rolling(QDAYS, min_periods=21).sum()
    return _safe_div(lh, hh + 1.0)


def f38_drts_032_distribution_day_count_25d(close, high, low, volume):
    rng = (high - low).replace(0, np.nan)
    pos = (close - low) / rng
    v_avg = volume.rolling(MDAYS, min_periods=5).mean()
    dist = ((pos < 1.0 / 3.0) & (close < close.shift(1)) & (volume > v_avg)).astype(float)
    return dist.rolling(25, min_periods=8).sum()


def f38_drts_033_distribution_day_share_of_decline_63d(close, high, low, volume):
    rng = (high - low).replace(0, np.nan)
    pos = (close - low) / rng
    v_avg = volume.rolling(MDAYS, min_periods=5).mean()
    dist = ((pos < 1.0 / 3.0) & (close < close.shift(1)) & (volume > v_avg)).astype(float)
    decl = (close < close.shift(1)).astype(float)
    return _safe_div(dist.rolling(QDAYS, min_periods=21).sum(),
                      decl.rolling(QDAYS, min_periods=21).sum())


def f38_drts_034_close_below_open_count_21d(open_, close):
    return (close < open_).astype(float).rolling(MDAYS, min_periods=5).sum()


def f38_drts_035_close_below_open_share_63d(open_, close):
    return (close < open_).astype(float).rolling(QDAYS, min_periods=21).mean()


def f38_drts_036_negative_outside_day_count_63d(high, low, close):
    outside = (high > high.shift(1)) & (low < low.shift(1))
    bearish = close < close.shift(1)
    return (outside & bearish).astype(float).rolling(QDAYS, min_periods=21).sum()


def f38_drts_037_outside_day_bearish_count_42d(high, low, close, open_):
    outside = (high > high.shift(1)) & (low < low.shift(1))
    bearish = close < open_
    return (outside & bearish).astype(float).rolling(42, min_periods=10).sum()


def f38_drts_038_high_test_failure_volume_avg_21d(high, close, volume):
    h21 = high.rolling(MDAYS, min_periods=5).max().shift(1)
    failed = (high > h21) & (close < h21)
    masked_vol = volume.where(failed, np.nan)
    return masked_vol.rolling(MDAYS, min_periods=2).mean()


def f38_drts_039_low_test_holds_count_21d(low, close):
    l21 = low.rolling(MDAYS, min_periods=5).min().shift(1)
    held = ((low <= l21) & (close > l21)).astype(float)
    return held.rolling(MDAYS, min_periods=5).sum()


def f38_drts_040_churning_index_63d(high, low, volume):
    rng = (high - low).replace(0, np.nan)
    return _safe_div(volume, rng).rolling(QDAYS, min_periods=21).mean()


# ---- Block C: stair-step distribution / sequential weakness (041-060) ----

def f38_drts_041_stair_step_lower_high_sequence_63d(high):
    hh = high.rolling(5, min_periods=3).max()
    seq = (hh < hh.shift(5)).astype(float)
    return seq.rolling(QDAYS, min_periods=21).sum()


def f38_drts_042_swing_high_height_decay_63d(high):
    hh = high.rolling(5, min_periods=3).max()
    return hh - hh.shift(QDAYS)


def f38_drts_043_swing_low_height_decay_63d(low):
    ll = low.rolling(5, min_periods=3).min()
    return ll.shift(QDAYS) - ll


def f38_drts_044_zigzag_top_amplitude_decay_63d(high, low):
    amp = (high.rolling(MDAYS, min_periods=5).max() - low.rolling(MDAYS, min_periods=5).min())
    return amp - amp.shift(QDAYS)


def f38_drts_045_consecutive_lower_highs_streak_max_63d(high):
    lh = (high < high.shift(1)).astype(int)
    return _streak_last_down(lh, QDAYS)


def f38_drts_046_consecutive_lower_closes_streak_max_21d(close):
    lc = (close < close.shift(1)).astype(int)
    return _streak_last_down(lc, MDAYS)


def f38_drts_047_close_below_5d_high_count_21d(high, close):
    h5 = high.rolling(WDAYS, min_periods=3).max().shift(1)
    return (close < h5).astype(float).rolling(MDAYS, min_periods=5).sum()


def f38_drts_048_close_below_21d_high_count_63d(high, close):
    h21 = high.rolling(MDAYS, min_periods=5).max().shift(1)
    return (close < h21).astype(float).rolling(QDAYS, min_periods=21).sum()


def f38_drts_049_negative_5d_close_count_63d(close):
    ret5 = close / close.shift(WDAYS) - 1.0
    return (ret5 < 0).astype(float).rolling(QDAYS, min_periods=21).sum()


def f38_drts_050_close_below_sma21_count_63d(close):
    sma = close.rolling(MDAYS, min_periods=5).mean()
    return (close < sma).astype(float).rolling(QDAYS, min_periods=21).sum()


def f38_drts_051_up_bars_share_decline_63d_vs_21d(close):
    up63 = (close > close.shift(1)).astype(float).rolling(QDAYS, min_periods=21).mean()
    up21 = (close > close.shift(1)).astype(float).rolling(MDAYS, min_periods=5).mean()
    return up21 - up63


def f38_drts_052_down_close_streak_max_42d(close):
    dc = (close < close.shift(1)).astype(int)
    return _streak_last_down(dc, 42)


def f38_drts_053_roll_off_top_velocity_21d(high, close):
    rmax = high.rolling(QDAYS, min_periods=21).max()
    return _safe_div(close - rmax, rmax.abs()).diff().rolling(MDAYS, min_periods=5).mean()


def f38_drts_054_peak_to_current_amplitude_share_63d(close, high, low):
    rmax = high.rolling(QDAYS, min_periods=21).max()
    rmin = low.rolling(QDAYS, min_periods=21).min()
    rng = (rmax - rmin).replace(0, np.nan)
    return _safe_div(close - rmin, rng)


def f38_drts_055_fading_high_strength_index_63d(high, low, close):
    atr21 = _atr(high, low, close, 21)
    atr63 = _atr(high, low, close, 63)
    return atr21 - atr63


def f38_drts_056_high_age_in_days_63d(high):
    rmax = high.rolling(QDAYS, min_periods=21).max()
    age = (high < rmax).astype(int).rolling(QDAYS, min_periods=21).apply(
        lambda w: int(w[::-1].cumprod().sum()), raw=True,
    )
    return age


def f38_drts_057_high_age_to_avg_age_ratio_63d(high):
    rmax = high.rolling(QDAYS, min_periods=21).max()
    age = (high < rmax).astype(int).rolling(QDAYS, min_periods=21).apply(
        lambda w: int(w[::-1].cumprod().sum()), raw=True,
    )
    return _safe_div(age, age.rolling(YDAYS, min_periods=QDAYS).mean())


def f38_drts_058_days_since_252d_high(high):
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    age = (high < rmax).astype(int).rolling(YDAYS, min_periods=QDAYS).apply(
        lambda w: int(w[::-1].cumprod().sum()), raw=True,
    )
    return age


def f38_drts_059_session_close_below_open_share_21d(open_, close):
    return (close < open_).astype(float).rolling(MDAYS, min_periods=5).mean()


def f38_drts_060_closing_strength_decay_index_21d(high, low, close):
    rng = (high - low).replace(0, np.nan)
    cs = (close - low) / rng
    return cs.rolling(WDAYS, min_periods=2).mean() - cs.rolling(MDAYS, min_periods=5).mean()


# ---- Block D start: effort-vs-result / volume divergence (061-075) ----

def f38_drts_061_range_per_dollar_volume_avg_21d(high, low, close, volume):
    rng = (high - low)
    return _safe_div(rng, volume * close).rolling(MDAYS, min_periods=5).mean()


def f38_drts_062_up_day_volume_share_decline_63d(close, volume):
    up = close > close.shift(1)
    upv = volume.where(up, 0).rolling(QDAYS, min_periods=21).sum()
    total = volume.rolling(QDAYS, min_periods=21).sum()
    share = _safe_div(upv, total)
    return share - share.shift(QDAYS)


def f38_drts_063_effort_result_divergence_21d(high, low, volume):
    rng = (high - low)
    z_rng = _rolling_zscore(rng, MDAYS, 5)
    z_vol = _rolling_zscore(volume, MDAYS, 5)
    return z_vol - z_rng


def f38_drts_064_volume_climax_at_top_coincidence_21d(high, volume):
    rmax = high.rolling(MDAYS, min_periods=5).max()
    at_top = (high >= rmax).astype(float)
    v_avg = volume.rolling(MDAYS, min_periods=5).mean()
    climax = ((volume > 2.0 * v_avg) & (at_top > 0)).astype(float)
    return climax.rolling(MDAYS, min_periods=5).sum()


def f38_drts_065_distribution_efficiency_index_63d(close, high, low, volume):
    rng = (high - low).replace(0, np.nan)
    pos = (close - low) / rng
    weighted = (1.0 - pos) * volume
    return weighted.rolling(QDAYS, min_periods=21).sum() / volume.rolling(QDAYS, min_periods=21).sum().replace(0, np.nan)


def f38_drts_066_price_volume_divergence_zscore_42d(close, volume):
    z_p = _rolling_zscore(close, 42, 10)
    z_v = _rolling_zscore(volume, 42, 10)
    return z_p - z_v


def f38_drts_067_obv_minus_price_slope_42d(close, volume):
    sign = np.sign(close.diff().fillna(0))
    obv = (sign * volume).cumsum()
    obv_slope = obv.diff(42)
    price_slope = close.diff(42)
    return _safe_div(price_slope, close.abs()) - _safe_div(obv_slope, obv.abs())


def f38_drts_068_ad_line_slope_21d(high, low, close, volume):
    rng = (high - low).replace(0, np.nan)
    mfm = ((close - low) - (high - close)) / rng
    mfv = mfm * volume
    ad = mfv.cumsum()
    return ad.diff(MDAYS)


def f38_drts_069_up_volume_minus_down_volume_share_42d(close, volume):
    up = close > close.shift(1)
    upv = volume.where(up, 0).rolling(42, min_periods=10).sum()
    dnv = volume.where(~up, 0).rolling(42, min_periods=10).sum()
    total = volume.rolling(42, min_periods=10).sum().replace(0, np.nan)
    return (upv - dnv) / total


def f38_drts_070_chaikin_money_flow_21d(high, low, close, volume):
    rng = (high - low).replace(0, np.nan)
    mfm = ((close - low) - (high - close)) / rng
    mfv = mfm * volume
    return mfv.rolling(MDAYS, min_periods=5).sum() / volume.rolling(MDAYS, min_periods=5).sum().replace(0, np.nan)


def f38_drts_071_chaikin_oscillator_21d(high, low, close, volume):
    rng = (high - low).replace(0, np.nan)
    mfm = ((close - low) - (high - close)) / rng
    mfv = mfm * volume
    ad = mfv.cumsum()
    return ad.ewm(span=3, adjust=False, min_periods=3).mean() - ad.ewm(span=10, adjust=False, min_periods=5).mean()


def f38_drts_072_ad_line_minus_price_zscore_42d(high, low, close, volume):
    rng = (high - low).replace(0, np.nan)
    mfm = ((close - low) - (high - close)) / rng
    ad = (mfm * volume).cumsum()
    return _rolling_zscore(ad, 42, 10) - _rolling_zscore(close, 42, 10)


def f38_drts_073_wyckoff_distribution_proxy_63d(close, high, low, volume):
    # near top with rising volume but stagnant close = test of supply
    rmax = high.rolling(QDAYS, min_periods=21).max()
    near_top = close / rmax >= 0.95
    flat = close.diff().abs() < (_atr(high, low, close, 21) * 0.25)
    vol_z = _rolling_zscore(volume, MDAYS, 5)
    sig = (near_top & flat & (vol_z > 1.0)).astype(float)
    return sig.rolling(QDAYS, min_periods=21).sum()


def f38_drts_074_high_volume_down_bar_count_42d(close, volume):
    v_avg = volume.rolling(MDAYS, min_periods=5).mean()
    hv_down = ((close < close.shift(1)) & (volume > 1.5 * v_avg)).astype(float)
    return hv_down.rolling(42, min_periods=10).sum()


def f38_drts_075_low_volume_up_bar_count_42d(close, volume):
    v_avg = volume.rolling(MDAYS, min_periods=5).mean()
    lv_up = ((close > close.shift(1)) & (volume < 0.7 * v_avg)).astype(float)
    return lv_up.rolling(42, min_periods=10).sum()


# ============================================================
#                        REGISTRY
# ============================================================

DISTRIBUTION_ROLLING_TOP_SIGNATURE_BASE_REGISTRY_001_075 = {
    "f38_drts_001_days_within_top_decile_252d_in_63d": {"inputs": ["high", "close"], "func": f38_drts_001_days_within_top_decile_252d_in_63d},
    "f38_drts_002_range_compression_at_top_21d": {"inputs": ["high", "low", "close"], "func": f38_drts_002_range_compression_at_top_21d},
    "f38_drts_003_close_within_5pct_of_252d_max_count_63d": {"inputs": ["close", "high"], "func": f38_drts_003_close_within_5pct_of_252d_max_count_63d},
    "f38_drts_004_consec_close_within_5pct_252d_max_streak_63d": {"inputs": ["close", "high"], "func": f38_drts_004_consec_close_within_5pct_252d_max_streak_63d},
    "f38_drts_005_new_21d_high_count_63d": {"inputs": ["high"], "func": f38_drts_005_new_21d_high_count_63d},
    "f38_drts_006_failed_21d_high_count_63d": {"inputs": ["high", "close"], "func": f38_drts_006_failed_21d_high_count_63d},
    "f38_drts_007_failed_21d_breakout_followthrough_count_63d": {"inputs": ["high", "close"], "func": f38_drts_007_failed_21d_breakout_followthrough_count_63d},
    "f38_drts_008_pct_time_within_2pct_of_63d_max_63d": {"inputs": ["close", "high"], "func": f38_drts_008_pct_time_within_2pct_of_63d_max_63d},
    "f38_drts_009_range_contraction_index_21d_vs_63d": {"inputs": ["high", "low"], "func": f38_drts_009_range_contraction_index_21d_vs_63d},
    "f38_drts_010_close_in_top_third_of_day_range_count_21d": {"inputs": ["open", "high", "low", "close"], "func": f38_drts_010_close_in_top_third_of_day_range_count_21d},
    "f38_drts_011_equal_close_count_21d": {"inputs": ["close"], "func": f38_drts_011_equal_close_count_21d},
    "f38_drts_012_inside_day_count_63d": {"inputs": ["high", "low"], "func": f38_drts_012_inside_day_count_63d},
    "f38_drts_013_narrow_range_4_count_21d": {"inputs": ["high", "low"], "func": f38_drts_013_narrow_range_4_count_21d},
    "f38_drts_014_churn_index_63d": {"inputs": ["high", "low", "close", "volume"], "func": f38_drts_014_churn_index_63d},
    "f38_drts_015_top_dwell_to_peak_amplitude_ratio_63d": {"inputs": ["close", "high", "low"], "func": f38_drts_015_top_dwell_to_peak_amplitude_ratio_63d},
    "f38_drts_016_days_within_atr_of_252d_high_in_63d": {"inputs": ["close", "high", "low"], "func": f38_drts_016_days_within_atr_of_252d_high_in_63d},
    "f38_drts_017_consecutive_higher_highs_streak_max_63d": {"inputs": ["high"], "func": f38_drts_017_consecutive_higher_highs_streak_max_63d},
    "f38_drts_018_higher_highs_minus_higher_lows_count_63d": {"inputs": ["high", "low"], "func": f38_drts_018_higher_highs_minus_higher_lows_count_63d},
    "f38_drts_019_top_pattern_width_proxy_63d": {"inputs": ["close", "high", "low"], "func": f38_drts_019_top_pattern_width_proxy_63d},
    "f38_drts_020_top_dwell_zscore_252d": {"inputs": ["close", "high"], "func": f38_drts_020_top_dwell_zscore_252d},
    "f38_drts_021_weekly_high_break_failures_8w": {"inputs": ["high", "close"], "func": f38_drts_021_weekly_high_break_failures_8w},
    "f38_drts_022_monthly_high_break_failures_6m": {"inputs": ["high", "close"], "func": f38_drts_022_monthly_high_break_failures_6m},
    "f38_drts_023_failed_252d_high_breakout_count": {"inputs": ["high", "close"], "func": f38_drts_023_failed_252d_high_breakout_count},
    "f38_drts_024_bull_trap_count_63d": {"inputs": ["high", "close"], "func": f38_drts_024_bull_trap_count_63d},
    "f38_drts_025_supply_zone_cluster_count_63d": {"inputs": ["close", "high", "volume"], "func": f38_drts_025_supply_zone_cluster_count_63d},
    "f38_drts_026_retest_failure_count_42d": {"inputs": ["high", "close"], "func": f38_drts_026_retest_failure_count_42d},
    "f38_drts_027_resistance_touch_count_63d": {"inputs": ["high", "close"], "func": f38_drts_027_resistance_touch_count_63d},
    "f38_drts_028_days_since_first_failed_breakout_from_252d_high": {"inputs": ["high", "close"], "func": f38_drts_028_days_since_first_failed_breakout_from_252d_high},
    "f38_drts_029_peak_breakdown_sharpness_21d": {"inputs": ["high", "close"], "func": f38_drts_029_peak_breakdown_sharpness_21d},
    "f38_drts_030_lower_high_count_63d": {"inputs": ["high"], "func": f38_drts_030_lower_high_count_63d},
    "f38_drts_031_lower_high_to_higher_high_ratio_63d": {"inputs": ["high"], "func": f38_drts_031_lower_high_to_higher_high_ratio_63d},
    "f38_drts_032_distribution_day_count_25d": {"inputs": ["close", "high", "low", "volume"], "func": f38_drts_032_distribution_day_count_25d},
    "f38_drts_033_distribution_day_share_of_decline_63d": {"inputs": ["close", "high", "low", "volume"], "func": f38_drts_033_distribution_day_share_of_decline_63d},
    "f38_drts_034_close_below_open_count_21d": {"inputs": ["open", "close"], "func": f38_drts_034_close_below_open_count_21d},
    "f38_drts_035_close_below_open_share_63d": {"inputs": ["open", "close"], "func": f38_drts_035_close_below_open_share_63d},
    "f38_drts_036_negative_outside_day_count_63d": {"inputs": ["high", "low", "close"], "func": f38_drts_036_negative_outside_day_count_63d},
    "f38_drts_037_outside_day_bearish_count_42d": {"inputs": ["high", "low", "close", "open"], "func": f38_drts_037_outside_day_bearish_count_42d},
    "f38_drts_038_high_test_failure_volume_avg_21d": {"inputs": ["high", "close", "volume"], "func": f38_drts_038_high_test_failure_volume_avg_21d},
    "f38_drts_039_low_test_holds_count_21d": {"inputs": ["low", "close"], "func": f38_drts_039_low_test_holds_count_21d},
    "f38_drts_040_churning_index_63d": {"inputs": ["high", "low", "volume"], "func": f38_drts_040_churning_index_63d},
    "f38_drts_041_stair_step_lower_high_sequence_63d": {"inputs": ["high"], "func": f38_drts_041_stair_step_lower_high_sequence_63d},
    "f38_drts_042_swing_high_height_decay_63d": {"inputs": ["high"], "func": f38_drts_042_swing_high_height_decay_63d},
    "f38_drts_043_swing_low_height_decay_63d": {"inputs": ["low"], "func": f38_drts_043_swing_low_height_decay_63d},
    "f38_drts_044_zigzag_top_amplitude_decay_63d": {"inputs": ["high", "low"], "func": f38_drts_044_zigzag_top_amplitude_decay_63d},
    "f38_drts_045_consecutive_lower_highs_streak_max_63d": {"inputs": ["high"], "func": f38_drts_045_consecutive_lower_highs_streak_max_63d},
    "f38_drts_046_consecutive_lower_closes_streak_max_21d": {"inputs": ["close"], "func": f38_drts_046_consecutive_lower_closes_streak_max_21d},
    "f38_drts_047_close_below_5d_high_count_21d": {"inputs": ["high", "close"], "func": f38_drts_047_close_below_5d_high_count_21d},
    "f38_drts_048_close_below_21d_high_count_63d": {"inputs": ["high", "close"], "func": f38_drts_048_close_below_21d_high_count_63d},
    "f38_drts_049_negative_5d_close_count_63d": {"inputs": ["close"], "func": f38_drts_049_negative_5d_close_count_63d},
    "f38_drts_050_close_below_sma21_count_63d": {"inputs": ["close"], "func": f38_drts_050_close_below_sma21_count_63d},
    "f38_drts_051_up_bars_share_decline_63d_vs_21d": {"inputs": ["close"], "func": f38_drts_051_up_bars_share_decline_63d_vs_21d},
    "f38_drts_052_down_close_streak_max_42d": {"inputs": ["close"], "func": f38_drts_052_down_close_streak_max_42d},
    "f38_drts_053_roll_off_top_velocity_21d": {"inputs": ["high", "close"], "func": f38_drts_053_roll_off_top_velocity_21d},
    "f38_drts_054_peak_to_current_amplitude_share_63d": {"inputs": ["close", "high", "low"], "func": f38_drts_054_peak_to_current_amplitude_share_63d},
    "f38_drts_055_fading_high_strength_index_63d": {"inputs": ["high", "low", "close"], "func": f38_drts_055_fading_high_strength_index_63d},
    "f38_drts_056_high_age_in_days_63d": {"inputs": ["high"], "func": f38_drts_056_high_age_in_days_63d},
    "f38_drts_057_high_age_to_avg_age_ratio_63d": {"inputs": ["high"], "func": f38_drts_057_high_age_to_avg_age_ratio_63d},
    "f38_drts_058_days_since_252d_high": {"inputs": ["high"], "func": f38_drts_058_days_since_252d_high},
    "f38_drts_059_session_close_below_open_share_21d": {"inputs": ["open", "close"], "func": f38_drts_059_session_close_below_open_share_21d},
    "f38_drts_060_closing_strength_decay_index_21d": {"inputs": ["high", "low", "close"], "func": f38_drts_060_closing_strength_decay_index_21d},
    "f38_drts_061_range_per_dollar_volume_avg_21d": {"inputs": ["high", "low", "close", "volume"], "func": f38_drts_061_range_per_dollar_volume_avg_21d},
    "f38_drts_062_up_day_volume_share_decline_63d": {"inputs": ["close", "volume"], "func": f38_drts_062_up_day_volume_share_decline_63d},
    "f38_drts_063_effort_result_divergence_21d": {"inputs": ["high", "low", "volume"], "func": f38_drts_063_effort_result_divergence_21d},
    "f38_drts_064_volume_climax_at_top_coincidence_21d": {"inputs": ["high", "volume"], "func": f38_drts_064_volume_climax_at_top_coincidence_21d},
    "f38_drts_065_distribution_efficiency_index_63d": {"inputs": ["close", "high", "low", "volume"], "func": f38_drts_065_distribution_efficiency_index_63d},
    "f38_drts_066_price_volume_divergence_zscore_42d": {"inputs": ["close", "volume"], "func": f38_drts_066_price_volume_divergence_zscore_42d},
    "f38_drts_067_obv_minus_price_slope_42d": {"inputs": ["close", "volume"], "func": f38_drts_067_obv_minus_price_slope_42d},
    "f38_drts_068_ad_line_slope_21d": {"inputs": ["high", "low", "close", "volume"], "func": f38_drts_068_ad_line_slope_21d},
    "f38_drts_069_up_volume_minus_down_volume_share_42d": {"inputs": ["close", "volume"], "func": f38_drts_069_up_volume_minus_down_volume_share_42d},
    "f38_drts_070_chaikin_money_flow_21d": {"inputs": ["high", "low", "close", "volume"], "func": f38_drts_070_chaikin_money_flow_21d},
    "f38_drts_071_chaikin_oscillator_21d": {"inputs": ["high", "low", "close", "volume"], "func": f38_drts_071_chaikin_oscillator_21d},
    "f38_drts_072_ad_line_minus_price_zscore_42d": {"inputs": ["high", "low", "close", "volume"], "func": f38_drts_072_ad_line_minus_price_zscore_42d},
    "f38_drts_073_wyckoff_distribution_proxy_63d": {"inputs": ["close", "high", "low", "volume"], "func": f38_drts_073_wyckoff_distribution_proxy_63d},
    "f38_drts_074_high_volume_down_bar_count_42d": {"inputs": ["close", "volume"], "func": f38_drts_074_high_volume_down_bar_count_42d},
    "f38_drts_075_low_volume_up_bar_count_42d": {"inputs": ["close", "volume"], "func": f38_drts_075_low_volume_up_bar_count_42d},
}
