"""distribution_rolling_top_signature base features 076-150 — Pipeline 1a-inverse short-side blowup family.

Continuation of __base__001_075.py: effort/result divergence (cont.), classic top patterns,
pattern-completion / breakdown triggers, momentum decay at top, and composite scores.
Self-contained; helpers redefined locally per HANDOFF.
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


def _ema(s, span, min_periods=None):
    if min_periods is None:
        min_periods = max(span // 2, 2)
    return s.ewm(span=span, adjust=False, min_periods=min_periods).mean()


# ============================================================
#                    FEATURES 076-150
# ============================================================

# ---- Block D cont: effort-vs-result / volume divergence (076-080) ----

def f38_drts_076_churning_to_advance_ratio_42d(close, volume, high, low):
    rng = (high - low).replace(0, np.nan)
    churn = volume / rng
    adv = (close - close.shift(MDAYS)).abs()
    return _safe_div(churn.rolling(42, min_periods=10).mean(), adv)


def f38_drts_077_ease_of_movement_avg_21d(high, low, volume):
    mid = (high + low) / 2.0
    box = volume / (high - low).replace(0, np.nan)
    eom = mid.diff() / box
    return eom.rolling(MDAYS, min_periods=5).mean()


def f38_drts_078_force_index_zscore_21d(close, volume):
    fi = close.diff() * volume
    return _rolling_zscore(fi, MDAYS, 5)


def f38_drts_079_mfi_minus_price_zscore_42d(high, low, close, volume):
    tp = (high + low + close) / 3.0
    mf = tp * volume
    pos = mf.where(tp > tp.shift(1), 0.0).rolling(14, min_periods=5).sum()
    neg = mf.where(tp < tp.shift(1), 0.0).rolling(14, min_periods=5).sum()
    mfi = 100.0 - (100.0 / (1.0 + _safe_div(pos, neg)))
    return _rolling_zscore(mfi, 42, 10) - _rolling_zscore(close, 42, 10)


def f38_drts_080_volume_imbalance_at_top_42d(close, high, volume):
    rmax = high.rolling(QDAYS, min_periods=21).max()
    near_top = close / rmax >= 0.95
    upv = volume.where((close > close.shift(1)) & near_top, 0).rolling(42, min_periods=10).sum()
    dnv = volume.where((close < close.shift(1)) & near_top, 0).rolling(42, min_periods=10).sum()
    return _safe_div(upv - dnv, upv + dnv)


# ---- Block E: classic top patterns (081-100) ----

def f38_drts_081_double_top_proxy_63d(high):
    # two highs within 1% of each other, separated by at least 5 bars
    rmax = high.rolling(QDAYS, min_periods=21).max()
    near_max = (high / rmax >= 0.99).astype(int)
    spread = near_max.rolling(QDAYS, min_periods=21).sum()
    return (spread >= 2).astype(float) * spread


def f38_drts_082_triple_top_proxy_126d(high):
    rmax = high.rolling(126, min_periods=42).max()
    near_max = (high / rmax >= 0.99).astype(int)
    spread = near_max.rolling(126, min_periods=42).sum()
    return (spread >= 3).astype(float) * spread


def f38_drts_083_head_and_shoulders_proxy_126d(high, low):
    # crude: center bar is highest, left/right shoulders within 5% lower
    h_mid = high.rolling(WDAYS, min_periods=3).max()
    left = h_mid.shift(MDAYS)
    right = h_mid.shift(-MDAYS)  # PIT-violating; replace with anchored variant
    # PIT version: at bar t, check t-21 was a local high with shoulders at t-42 and t-0
    center = high.shift(MDAYS)
    ls = high.shift(2 * MDAYS)
    rs = high
    score = ((center > ls * 1.02) & (center > rs * 1.02) & (ls / rs).between(0.95, 1.05)).astype(float)
    return score.rolling(126, min_periods=42).sum()


def f38_drts_084_m_top_score_63d(high, close):
    # two peaks with a trough between them
    rmax = high.rolling(QDAYS, min_periods=21).max()
    p1 = high.shift(MDAYS) >= rmax.shift(MDAYS) * 0.99
    trough = close.shift(MDAYS // 2) < close.shift(MDAYS) * 0.97
    p2 = high >= rmax * 0.99
    return (p1.astype(float) + trough.astype(float) + p2.astype(float))


def f38_drts_085_rounded_top_curvature_126d(close):
    # second-difference average — positive curvature means concave-down (top-like)
    return -close.diff().diff().rolling(126, min_periods=30).mean()


def f38_drts_086_broadening_top_amplitude_42d(high, low):
    amp = high - low
    return amp.rolling(42, min_periods=10).mean() - amp.rolling(QDAYS, min_periods=21).mean()


def f38_drts_087_wedge_compression_index_63d(high, low):
    h_max = high.rolling(QDAYS, min_periods=21).max()
    l_min = low.rolling(QDAYS, min_periods=21).min()
    rng_now = high.rolling(MDAYS, min_periods=5).max() - low.rolling(MDAYS, min_periods=5).min()
    rng_full = h_max - l_min
    return _safe_div(rng_now, rng_full)


def f38_drts_088_flag_top_continuation_proxy_42d(close, high, low):
    # tight consolidation after a prior strong move
    atr21 = _atr(high, low, close, 21)
    atr5 = _atr(high, low, close, 5)
    prior_move = close.shift(MDAYS) / close.shift(2 * MDAYS) - 1.0
    tight = atr5 / atr21
    return prior_move * (1.0 / tight.clip(lower=1e-3))


def f38_drts_089_pennant_top_proxy_42d(high, low):
    h_slope = (high.rolling(MDAYS, min_periods=5).max() - high.rolling(MDAYS, min_periods=5).max().shift(MDAYS)) / MDAYS
    l_slope = (low.rolling(MDAYS, min_periods=5).min() - low.rolling(MDAYS, min_periods=5).min().shift(MDAYS)) / MDAYS
    # converging: h_slope<0 and l_slope>0
    return (h_slope.clip(upper=0) * l_slope.clip(lower=0)).abs()


def f38_drts_090_rising_wedge_top_score_63d(high, low):
    # both lines rising but high slope < low slope (converging up)
    h_slope = high.rolling(QDAYS, min_periods=21).apply(
        lambda w: np.polyfit(np.arange(len(w)), w, 1)[0] if np.isfinite(w).all() else np.nan, raw=True,
    )
    l_slope = low.rolling(QDAYS, min_periods=21).apply(
        lambda w: np.polyfit(np.arange(len(w)), w, 1)[0] if np.isfinite(w).all() else np.nan, raw=True,
    )
    return (l_slope - h_slope).clip(lower=0)


def f38_drts_091_island_reversal_top_count_63d(high, low, close):
    gap_up = low > high.shift(1) * 1.005
    gap_down = high < low.shift(1) * 0.995
    island = gap_up.shift(WDAYS) & gap_down  # gap up 5d ago, gap down today
    return island.astype(float).rolling(QDAYS, min_periods=21).sum()


def f38_drts_092_abandoned_baby_top_count_42d(open_, high, low, close):
    body = (close - open_).abs()
    rng = (high - low).replace(0, np.nan)
    doji = body / rng < 0.1
    gap_up = low > high.shift(1) * 1.005
    # PIT alternative: at bar t, look at bars t-2 and t-1: doji at t-1 with gap up before it, gap down today
    doji_prev = doji.shift(1)
    gap_up_prev = gap_up.shift(1)
    gap_down_today = high < low.shift(1) * 0.995
    pattern = (doji_prev & gap_up_prev & gap_down_today).astype(float)
    return pattern.rolling(42, min_periods=10).sum()


def f38_drts_093_three_drives_pattern_score_63d(high):
    # three successively higher highs with shrinking amplitude
    h1 = high.shift(2 * MDAYS)
    h2 = high.shift(MDAYS)
    h3 = high
    drive = ((h3 > h2) & (h2 > h1) & ((h3 - h2) < (h2 - h1))).astype(float)
    return drive.rolling(QDAYS, min_periods=21).sum()


def f38_drts_094_bump_and_run_top_score_126d(close, high):
    # acceleration ratio: latest 21d return vs prior 105d return
    r_recent = close / close.shift(MDAYS) - 1.0
    r_lead = close.shift(MDAYS) / close.shift(105) - 1.0
    return _safe_div(r_recent, r_lead.abs().clip(lower=1e-6))


def f38_drts_095_cup_and_handle_failure_proxy_126d(close, high, low):
    # cup base low vs cup rim, then handle pullback that fails
    rim = high.rolling(126, min_periods=42).max()
    base = low.rolling(126, min_periods=42).min()
    handle_low = low.rolling(MDAYS, min_periods=5).min()
    cup_depth = _safe_div(rim - base, rim.abs())
    handle_depth = _safe_div(rim - handle_low, rim.abs())
    return (cup_depth - handle_depth * 3.0).clip(upper=0).abs()


def f38_drts_096_v_top_sharpness_42d(close):
    # acceleration around the peak
    return -close.diff().diff().rolling(42, min_periods=10).max()


def f38_drts_097_spike_top_count_63d(high, low, close):
    atr21 = _atr(high, low, close, 21)
    spike = (high - high.shift(1) > 1.5 * atr21) & (close < high - atr21)
    return spike.astype(float).rolling(QDAYS, min_periods=21).sum()


def f38_drts_098_saucer_top_curvature_252d(close):
    return -close.diff().diff().rolling(YDAYS, min_periods=63).mean()


def f38_drts_099_ascending_triangle_failure_42d(high, low):
    h_max = high.rolling(42, min_periods=10).max()
    h_flat = (h_max - h_max.shift(MDAYS)).abs() < h_max * 0.01
    l_rising = low.rolling(42, min_periods=10).min() > low.rolling(42, min_periods=10).min().shift(MDAYS)
    failure = h_flat & l_rising & (low < low.shift(MDAYS))
    return failure.astype(float).rolling(42, min_periods=10).sum()


def f38_drts_100_descending_triangle_top_emergence_42d(high, low):
    l_min = low.rolling(42, min_periods=10).min()
    l_flat = (l_min - l_min.shift(MDAYS)).abs() < l_min * 0.01
    h_falling = high.rolling(42, min_periods=10).max() < high.rolling(42, min_periods=10).max().shift(MDAYS)
    pattern = l_flat & h_falling
    return pattern.astype(float).rolling(42, min_periods=10).sum()


# ---- Block F: pattern-completion / breakdown trigger (101-120) ----

def f38_drts_101_neckline_break_distance_to_peak_42d(close, high, low):
    rmax = high.rolling(42, min_periods=10).max()
    neckline = low.rolling(42, min_periods=10).min()
    return _safe_div(close - neckline, rmax - neckline)


def f38_drts_102_shoulder_symmetry_score_63d(high):
    ls = high.shift(2 * MDAYS).rolling(WDAYS, min_periods=2).max()
    rs = high.rolling(WDAYS, min_periods=2).max()
    return -_safe_div(ls - rs, (ls + rs).abs())


def f38_drts_103_left_minus_right_shoulder_amplitude_63d(high):
    ls = high.shift(2 * MDAYS)
    rs = high
    return ls - rs


def f38_drts_104_days_below_neckline_after_completion_21d(close, low):
    neckline = low.rolling(42, min_periods=10).min()
    below = (close < neckline).astype(int)
    return below.rolling(MDAYS, min_periods=5).sum()


def f38_drts_105_retest_strength_index_42d(close, high):
    rmax = high.rolling(42, min_periods=10).max()
    retest_dist = (rmax - close).abs() / rmax.replace(0, np.nan)
    return retest_dist.rolling(MDAYS, min_periods=5).min()


def f38_drts_106_breakdown_volume_signature_21d(close, low, volume):
    l21 = low.rolling(MDAYS, min_periods=5).min().shift(1)
    breakdown = close < l21
    v_avg = volume.rolling(MDAYS, min_periods=5).mean()
    return (breakdown.astype(float) * (volume / v_avg)).rolling(MDAYS, min_periods=5).mean()


def f38_drts_107_measured_move_target_to_current_42d(close, high, low):
    rmax = high.rolling(42, min_periods=10).max()
    rmin = low.rolling(42, min_periods=10).min()
    target = rmin - (rmax - rmin)
    return _safe_div(close - target, (rmax - rmin).abs())


def f38_drts_108_breakdown_amplitude_vs_pattern_height_63d(close, high, low):
    rmax = high.rolling(QDAYS, min_periods=21).max()
    rmin = low.rolling(QDAYS, min_periods=21).min()
    return _safe_div(rmax - close, rmax - rmin)


def f38_drts_109_followthrough_strength_after_breakdown_21d(close):
    return -close.diff(WDAYS).rolling(MDAYS, min_periods=5).mean()


def f38_drts_110_days_to_first_close_below_pattern_low_42d(close, low):
    l_min = low.rolling(42, min_periods=10).min()
    below = (close < l_min).astype(int)
    cum = below.cumsum()
    last_below = cum.where(below > 0).ffill()
    return cum - last_below


def f38_drts_111_lower_shadow_dominance_at_top_21d(open_, high, low, close):
    body_lo = pd.concat([open_, close], axis=1).min(axis=1)
    ls = body_lo - low
    rng = (high - low).replace(0, np.nan)
    return (ls / rng).rolling(MDAYS, min_periods=5).mean()


def f38_drts_112_upper_shadow_dominance_at_top_21d(open_, high, low, close):
    body_hi = pd.concat([open_, close], axis=1).max(axis=1)
    us = high - body_hi
    rng = (high - low).replace(0, np.nan)
    return (us / rng).rolling(MDAYS, min_periods=5).mean()


def f38_drts_113_wick_imbalance_at_swing_high_21d(open_, high, low, close):
    body_hi = pd.concat([open_, close], axis=1).max(axis=1)
    body_lo = pd.concat([open_, close], axis=1).min(axis=1)
    us = high - body_hi
    ls = body_lo - low
    return _safe_div(us - ls, us + ls)


def f38_drts_114_tail_pattern_at_top_score_21d(open_, high, low, close):
    body = (close - open_).abs()
    rng = (high - low).replace(0, np.nan)
    body_hi = pd.concat([open_, close], axis=1).max(axis=1)
    us = high - body_hi
    tail_dominant = ((us / rng) > 0.6) & (body / rng < 0.25)
    return tail_dominant.astype(float).rolling(MDAYS, min_periods=5).sum()


def f38_drts_115_exhaustion_gap_count_42d(high, low, volume):
    gap_up = low > high.shift(1) * 1.005
    v_avg = volume.rolling(MDAYS, min_periods=5).mean()
    big_vol = volume > 2.0 * v_avg
    return (gap_up & big_vol).astype(float).rolling(42, min_periods=10).sum()


def f38_drts_116_breakaway_gap_count_42d(high, low):
    gap_dn = high < low.shift(1) * 0.995
    return gap_dn.astype(float).rolling(42, min_periods=10).sum()


def f38_drts_117_gap_fill_failure_count_42d(high, low, close):
    gap_dn = high < low.shift(1) * 0.995
    # 5 bars later, close still below gap level
    failed = gap_dn.shift(WDAYS) & (close < low.shift(WDAYS + 1))
    return failed.astype(float).rolling(42, min_periods=10).sum()


def f38_drts_118_closing_position_in_range_avg_21d(high, low, close):
    rng = (high - low).replace(0, np.nan)
    return ((close - low) / rng).rolling(MDAYS, min_periods=5).mean()


def f38_drts_119_opening_gap_down_count_21d(open_, close):
    return (open_ < close.shift(1) * 0.995).astype(float).rolling(MDAYS, min_periods=5).sum()


def f38_drts_120_closing_gap_minus_opening_gap_diff_21d(open_, close):
    closing_gap = close - close.shift(1)
    opening_gap = open_ - close.shift(1)
    return (closing_gap - opening_gap).rolling(MDAYS, min_periods=5).mean()


# ---- Block G: momentum decay at top (121-135) ----

def f38_drts_121_momentum_minus_price_divergence_zscore_42d(close):
    mom = close - close.shift(MDAYS)
    return _rolling_zscore(mom, 42, 10) - _rolling_zscore(close, 42, 10)


def f38_drts_122_rsi_at_top_negative_divergence_42d(close):
    delta = close.diff()
    up = delta.clip(lower=0).rolling(14, min_periods=5).mean()
    dn = (-delta.clip(upper=0)).rolling(14, min_periods=5).mean()
    rsi = 100.0 - (100.0 / (1.0 + _safe_div(up, dn)))
    return _rolling_zscore(rsi, 42, 10) - _rolling_zscore(close, 42, 10)


def f38_drts_123_macd_histogram_divergence_at_top_42d(close):
    macd = _ema(close, 12) - _ema(close, 26)
    sig = _ema(macd, 9)
    hist = macd - sig
    return _rolling_zscore(hist, 42, 10) - _rolling_zscore(close, 42, 10)


def f38_drts_124_trix_negative_divergence_42d(close):
    e1 = _ema(_safe_log(close), 15)
    e2 = _ema(e1, 15)
    e3 = _ema(e2, 15)
    trix = e3.diff()
    return _rolling_zscore(trix, 42, 10) - _rolling_zscore(close, 42, 10)


def f38_drts_125_cmo_negative_divergence_42d(close):
    delta = close.diff()
    up = delta.clip(lower=0).rolling(14, min_periods=5).sum()
    dn = (-delta.clip(upper=0)).rolling(14, min_periods=5).sum()
    cmo = 100.0 * _safe_div(up - dn, up + dn)
    return _rolling_zscore(cmo, 42, 10) - _rolling_zscore(close, 42, 10)


def f38_drts_126_stochastic_overbought_exit_count_42d(high, low, close):
    ll = low.rolling(14, min_periods=5).min()
    hh = high.rolling(14, min_periods=5).max()
    k = 100.0 * _safe_div(close - ll, hh - ll)
    exit_ob = ((k.shift(1) > 80) & (k < 80)).astype(float)
    return exit_ob.rolling(42, min_periods=10).sum()


def f38_drts_127_williams_r_overbought_exit_count_42d(high, low, close):
    hh = high.rolling(14, min_periods=5).max()
    ll = low.rolling(14, min_periods=5).min()
    wr = -100.0 * _safe_div(hh - close, hh - ll)
    exit_ob = ((wr.shift(1) > -20) & (wr < -20)).astype(float)
    return exit_ob.rolling(42, min_periods=10).sum()


def f38_drts_128_roc_decay_at_top_21d_minus_42d(close):
    roc21 = close / close.shift(MDAYS) - 1.0
    roc42 = close / close.shift(42) - 1.0
    return roc21 - roc42


def f38_drts_129_price_displacement_decay_to_high_amplitude_42d(close, high):
    rmax = high.rolling(QDAYS, min_periods=21).max()
    dist = _safe_div(close - rmax, rmax.abs())
    return -dist.rolling(42, min_periods=10).mean()


def f38_drts_130_momentum_collapse_after_high_21d(close, high):
    rmax = high.rolling(QDAYS, min_periods=21).max()
    days_since = (high < rmax).astype(int).cumsum()
    last_high = days_since.where(high >= rmax).ffill()
    age = days_since - last_high
    # at days when age <= 21, measure return drawdown since high
    return _safe_div(close - rmax, rmax.abs()).where(age <= MDAYS)


def f38_drts_131_acceleration_to_deceleration_pivot_distance_42d(close):
    a = close.diff().diff()
    flip = (a.shift(1) > 0) & (a < 0)
    age = flip.astype(int).cumsum()
    last_flip = age.where(flip).ffill()
    return age - last_flip


def f38_drts_132_peak_strength_index_decay_21d(close, high, low):
    atr21 = _atr(high, low, close, 21)
    psi = _safe_div(close - low.rolling(MDAYS, min_periods=5).min(), atr21)
    return psi - psi.shift(MDAYS)


def f38_drts_133_trend_strength_decay_aroon_42d(high, low):
    n = 25
    aup = high.rolling(n + 1, min_periods=n // 2).apply(lambda w: 100.0 * (n - (n - w.argmax())) / n, raw=True)
    adn = low.rolling(n + 1, min_periods=n // 2).apply(lambda w: 100.0 * (n - (n - w.argmin())) / n, raw=True)
    osc = aup - adn
    return osc - osc.shift(42)


def f38_drts_134_dmi_di_minus_dominance_at_top_21d(high, low, close):
    up = high.diff()
    dn = -low.diff()
    plus_dm = up.where((up > dn) & (up > 0), 0.0)
    minus_dm = dn.where((dn > up) & (dn > 0), 0.0)
    tr = _atr(high, low, close, 14) * 14
    plus_di = 100.0 * plus_dm.rolling(14, min_periods=5).sum() / tr.replace(0, np.nan)
    minus_di = 100.0 * minus_dm.rolling(14, min_periods=5).sum() / tr.replace(0, np.nan)
    return (minus_di - plus_di).rolling(MDAYS, min_periods=5).mean()


def f38_drts_135_adx_decline_after_peak_21d(high, low, close):
    up = high.diff()
    dn = -low.diff()
    plus_dm = up.where((up > dn) & (up > 0), 0.0)
    minus_dm = dn.where((dn > up) & (dn > 0), 0.0)
    tr = _atr(high, low, close, 14) * 14
    plus_di = 100.0 * plus_dm.rolling(14, min_periods=5).sum() / tr.replace(0, np.nan)
    minus_di = 100.0 * minus_dm.rolling(14, min_periods=5).sum() / tr.replace(0, np.nan)
    dx = 100.0 * (plus_di - minus_di).abs() / (plus_di + minus_di).replace(0, np.nan)
    adx = dx.rolling(14, min_periods=5).mean()
    return adx.shift(MDAYS) - adx


# ---- Block H: top-composite scores (136-150) ----

def f38_drts_136_distribution_top_composite_score(close, high, low, volume):
    rmax = high.rolling(QDAYS, min_periods=21).max()
    near_top = (close / rmax >= 0.95).astype(float)
    v_avg = volume.rolling(MDAYS, min_periods=5).mean()
    rng = (high - low).replace(0, np.nan)
    pos = (close - low) / rng
    dist = ((pos < 1.0 / 3.0) & (volume > v_avg) & (close < close.shift(1))).astype(float)
    return (near_top * dist).rolling(QDAYS, min_periods=21).sum()


def f38_drts_137_rolling_top_strength_zscore_8w(close, high):
    rmax = high.rolling(QDAYS, min_periods=21).max()
    dwell = (close / rmax >= 0.97).astype(float).rolling(QDAYS, min_periods=21).sum()
    return _rolling_zscore(dwell, 40, 10)


def f38_drts_138_top_signature_pattern_score_63d(high, close):
    h21 = high.rolling(MDAYS, min_periods=5).max().shift(1)
    failed = ((high > h21) & (close < h21)).astype(float)
    lh = (high < high.shift(1)).astype(float)
    return failed.rolling(QDAYS, min_periods=21).sum() + lh.rolling(QDAYS, min_periods=21).sum() / 4.0


def f38_drts_139_heavy_distribution_index_42d(close, high, low, volume):
    rng = (high - low).replace(0, np.nan)
    pos = (close - low) / rng
    weighted = (1.0 - pos) * volume
    return weighted.rolling(42, min_periods=10).sum() / volume.rolling(42, min_periods=10).sum().replace(0, np.nan)


def f38_drts_140_distribution_persistence_score_63d(close, high, low, volume):
    rng = (high - low).replace(0, np.nan)
    pos = (close - low) / rng
    v_avg = volume.rolling(MDAYS, min_periods=5).mean()
    dist = ((pos < 1.0 / 3.0) & (volume > v_avg) & (close < close.shift(1))).astype(int)
    return _streak_last_down(dist, QDAYS)


def f38_drts_141_failed_top_breakout_intensity_63d(high, close, volume):
    h21 = high.rolling(MDAYS, min_periods=5).max().shift(1)
    failed = ((high > h21) & (close < h21)).astype(float)
    v_avg = volume.rolling(MDAYS, min_periods=5).mean()
    return (failed * (volume / v_avg.replace(0, np.nan))).rolling(QDAYS, min_periods=21).mean()


def f38_drts_142_top_dwell_with_distribution_composite_63d(close, high, low, volume):
    rmax = high.rolling(QDAYS, min_periods=21).max()
    dwell = (close / rmax >= 0.97).astype(float).rolling(QDAYS, min_periods=21).sum()
    v_avg = volume.rolling(MDAYS, min_periods=5).mean()
    dn_vol = (close < close.shift(1)).astype(float) * volume / v_avg.replace(0, np.nan)
    return dwell * dn_vol.rolling(QDAYS, min_periods=21).mean()


def f38_drts_143_multi_pattern_top_count_63d(high, close, low, open_):
    rmax = high.rolling(QDAYS, min_periods=21).max()
    bear_eng = (close < open_) & (close.shift(1) > open_.shift(1)) & (close < open_.shift(1)) & (open_ > close.shift(1))
    body = (close - open_).abs()
    rng = (high - low).replace(0, np.nan)
    body_hi = pd.concat([open_, close], axis=1).max(axis=1)
    shooting_star = ((high - body_hi) / rng > 0.6) & (body / rng < 0.3)
    near_top = high / rmax >= 0.98
    multi = (bear_eng.fillna(False).astype(int) + shooting_star.fillna(False).astype(int)) * near_top.astype(int)
    return multi.rolling(QDAYS, min_periods=21).sum()


def f38_drts_144_churning_distribution_composite_63d(high, low, close, volume):
    rng = (high - low).replace(0, np.nan)
    churn = volume / rng
    pos = (close - low) / rng
    return (churn * (1.0 - pos)).rolling(QDAYS, min_periods=21).mean()


def f38_drts_145_weakness_signature_index_63d(close, high):
    rmax = high.rolling(QDAYS, min_periods=21).max()
    dist = _safe_div(close - rmax, rmax.abs())
    return -dist.rolling(QDAYS, min_periods=21).mean()


def f38_drts_146_lower_highs_with_volume_composite_63d(high, volume):
    lh = (high < high.shift(1)).astype(float)
    v_avg = volume.rolling(MDAYS, min_periods=5).mean()
    return (lh * volume / v_avg.replace(0, np.nan)).rolling(QDAYS, min_periods=21).mean()


def f38_drts_147_supply_dominance_zscore_63d(close, high, low, volume):
    rng = (high - low).replace(0, np.nan)
    pos = (close - low) / rng
    supply = (1.0 - pos) * volume
    return _rolling_zscore(supply, QDAYS, 21)


def f38_drts_148_dollar_volume_distribution_zscore_42d(close, low, high, volume):
    dv = close * volume
    rng = (high - low).replace(0, np.nan)
    pos = (close - low) / rng
    weighted = (1.0 - pos) * dv
    return _rolling_zscore(weighted, 42, 10)


def f38_drts_149_top_breakdown_lead_score_63d(close, high, low):
    rmax = high.rolling(QDAYS, min_periods=21).max()
    rmin = low.rolling(QDAYS, min_periods=21).min()
    rng = (rmax - rmin).replace(0, np.nan)
    pos_in_range = (close - rmin) / rng
    return pos_in_range.shift(MDAYS) - pos_in_range  # decline in range position over 21d


def f38_drts_150_distribution_top_aggregate_zscore_63d(close, high, low, volume):
    rng = (high - low).replace(0, np.nan)
    pos = (close - low) / rng
    v_avg = volume.rolling(MDAYS, min_periods=5).mean()
    dist = ((pos < 1.0 / 3.0) & (volume > v_avg) & (close < close.shift(1))).astype(float)
    rmax = high.rolling(QDAYS, min_periods=21).max()
    dwell = (close / rmax >= 0.97).astype(float)
    z_dist = _rolling_zscore(dist.rolling(QDAYS, min_periods=21).sum(), 126, 30)
    z_dwell = _rolling_zscore(dwell.rolling(QDAYS, min_periods=21).sum(), 126, 30)
    return z_dist + z_dwell


# ============================================================
#                        REGISTRY
# ============================================================

DISTRIBUTION_ROLLING_TOP_SIGNATURE_BASE_REGISTRY_076_150 = {
    "f38_drts_076_churning_to_advance_ratio_42d": {"inputs": ["close", "volume", "high", "low"], "func": f38_drts_076_churning_to_advance_ratio_42d},
    "f38_drts_077_ease_of_movement_avg_21d": {"inputs": ["high", "low", "volume"], "func": f38_drts_077_ease_of_movement_avg_21d},
    "f38_drts_078_force_index_zscore_21d": {"inputs": ["close", "volume"], "func": f38_drts_078_force_index_zscore_21d},
    "f38_drts_079_mfi_minus_price_zscore_42d": {"inputs": ["high", "low", "close", "volume"], "func": f38_drts_079_mfi_minus_price_zscore_42d},
    "f38_drts_080_volume_imbalance_at_top_42d": {"inputs": ["close", "high", "volume"], "func": f38_drts_080_volume_imbalance_at_top_42d},
    "f38_drts_081_double_top_proxy_63d": {"inputs": ["high"], "func": f38_drts_081_double_top_proxy_63d},
    "f38_drts_082_triple_top_proxy_126d": {"inputs": ["high"], "func": f38_drts_082_triple_top_proxy_126d},
    "f38_drts_083_head_and_shoulders_proxy_126d": {"inputs": ["high", "low"], "func": f38_drts_083_head_and_shoulders_proxy_126d},
    "f38_drts_084_m_top_score_63d": {"inputs": ["high", "close"], "func": f38_drts_084_m_top_score_63d},
    "f38_drts_085_rounded_top_curvature_126d": {"inputs": ["close"], "func": f38_drts_085_rounded_top_curvature_126d},
    "f38_drts_086_broadening_top_amplitude_42d": {"inputs": ["high", "low"], "func": f38_drts_086_broadening_top_amplitude_42d},
    "f38_drts_087_wedge_compression_index_63d": {"inputs": ["high", "low"], "func": f38_drts_087_wedge_compression_index_63d},
    "f38_drts_088_flag_top_continuation_proxy_42d": {"inputs": ["close", "high", "low"], "func": f38_drts_088_flag_top_continuation_proxy_42d},
    "f38_drts_089_pennant_top_proxy_42d": {"inputs": ["high", "low"], "func": f38_drts_089_pennant_top_proxy_42d},
    "f38_drts_090_rising_wedge_top_score_63d": {"inputs": ["high", "low"], "func": f38_drts_090_rising_wedge_top_score_63d},
    "f38_drts_091_island_reversal_top_count_63d": {"inputs": ["high", "low", "close"], "func": f38_drts_091_island_reversal_top_count_63d},
    "f38_drts_092_abandoned_baby_top_count_42d": {"inputs": ["open", "high", "low", "close"], "func": f38_drts_092_abandoned_baby_top_count_42d},
    "f38_drts_093_three_drives_pattern_score_63d": {"inputs": ["high"], "func": f38_drts_093_three_drives_pattern_score_63d},
    "f38_drts_094_bump_and_run_top_score_126d": {"inputs": ["close", "high"], "func": f38_drts_094_bump_and_run_top_score_126d},
    "f38_drts_095_cup_and_handle_failure_proxy_126d": {"inputs": ["close", "high", "low"], "func": f38_drts_095_cup_and_handle_failure_proxy_126d},
    "f38_drts_096_v_top_sharpness_42d": {"inputs": ["close"], "func": f38_drts_096_v_top_sharpness_42d},
    "f38_drts_097_spike_top_count_63d": {"inputs": ["high", "low", "close"], "func": f38_drts_097_spike_top_count_63d},
    "f38_drts_098_saucer_top_curvature_252d": {"inputs": ["close"], "func": f38_drts_098_saucer_top_curvature_252d},
    "f38_drts_099_ascending_triangle_failure_42d": {"inputs": ["high", "low"], "func": f38_drts_099_ascending_triangle_failure_42d},
    "f38_drts_100_descending_triangle_top_emergence_42d": {"inputs": ["high", "low"], "func": f38_drts_100_descending_triangle_top_emergence_42d},
    "f38_drts_101_neckline_break_distance_to_peak_42d": {"inputs": ["close", "high", "low"], "func": f38_drts_101_neckline_break_distance_to_peak_42d},
    "f38_drts_102_shoulder_symmetry_score_63d": {"inputs": ["high"], "func": f38_drts_102_shoulder_symmetry_score_63d},
    "f38_drts_103_left_minus_right_shoulder_amplitude_63d": {"inputs": ["high"], "func": f38_drts_103_left_minus_right_shoulder_amplitude_63d},
    "f38_drts_104_days_below_neckline_after_completion_21d": {"inputs": ["close", "low"], "func": f38_drts_104_days_below_neckline_after_completion_21d},
    "f38_drts_105_retest_strength_index_42d": {"inputs": ["close", "high"], "func": f38_drts_105_retest_strength_index_42d},
    "f38_drts_106_breakdown_volume_signature_21d": {"inputs": ["close", "low", "volume"], "func": f38_drts_106_breakdown_volume_signature_21d},
    "f38_drts_107_measured_move_target_to_current_42d": {"inputs": ["close", "high", "low"], "func": f38_drts_107_measured_move_target_to_current_42d},
    "f38_drts_108_breakdown_amplitude_vs_pattern_height_63d": {"inputs": ["close", "high", "low"], "func": f38_drts_108_breakdown_amplitude_vs_pattern_height_63d},
    "f38_drts_109_followthrough_strength_after_breakdown_21d": {"inputs": ["close"], "func": f38_drts_109_followthrough_strength_after_breakdown_21d},
    "f38_drts_110_days_to_first_close_below_pattern_low_42d": {"inputs": ["close", "low"], "func": f38_drts_110_days_to_first_close_below_pattern_low_42d},
    "f38_drts_111_lower_shadow_dominance_at_top_21d": {"inputs": ["open", "high", "low", "close"], "func": f38_drts_111_lower_shadow_dominance_at_top_21d},
    "f38_drts_112_upper_shadow_dominance_at_top_21d": {"inputs": ["open", "high", "low", "close"], "func": f38_drts_112_upper_shadow_dominance_at_top_21d},
    "f38_drts_113_wick_imbalance_at_swing_high_21d": {"inputs": ["open", "high", "low", "close"], "func": f38_drts_113_wick_imbalance_at_swing_high_21d},
    "f38_drts_114_tail_pattern_at_top_score_21d": {"inputs": ["open", "high", "low", "close"], "func": f38_drts_114_tail_pattern_at_top_score_21d},
    "f38_drts_115_exhaustion_gap_count_42d": {"inputs": ["high", "low", "volume"], "func": f38_drts_115_exhaustion_gap_count_42d},
    "f38_drts_116_breakaway_gap_count_42d": {"inputs": ["high", "low"], "func": f38_drts_116_breakaway_gap_count_42d},
    "f38_drts_117_gap_fill_failure_count_42d": {"inputs": ["high", "low", "close"], "func": f38_drts_117_gap_fill_failure_count_42d},
    "f38_drts_118_closing_position_in_range_avg_21d": {"inputs": ["high", "low", "close"], "func": f38_drts_118_closing_position_in_range_avg_21d},
    "f38_drts_119_opening_gap_down_count_21d": {"inputs": ["open", "close"], "func": f38_drts_119_opening_gap_down_count_21d},
    "f38_drts_120_closing_gap_minus_opening_gap_diff_21d": {"inputs": ["open", "close"], "func": f38_drts_120_closing_gap_minus_opening_gap_diff_21d},
    "f38_drts_121_momentum_minus_price_divergence_zscore_42d": {"inputs": ["close"], "func": f38_drts_121_momentum_minus_price_divergence_zscore_42d},
    "f38_drts_122_rsi_at_top_negative_divergence_42d": {"inputs": ["close"], "func": f38_drts_122_rsi_at_top_negative_divergence_42d},
    "f38_drts_123_macd_histogram_divergence_at_top_42d": {"inputs": ["close"], "func": f38_drts_123_macd_histogram_divergence_at_top_42d},
    "f38_drts_124_trix_negative_divergence_42d": {"inputs": ["close"], "func": f38_drts_124_trix_negative_divergence_42d},
    "f38_drts_125_cmo_negative_divergence_42d": {"inputs": ["close"], "func": f38_drts_125_cmo_negative_divergence_42d},
    "f38_drts_126_stochastic_overbought_exit_count_42d": {"inputs": ["high", "low", "close"], "func": f38_drts_126_stochastic_overbought_exit_count_42d},
    "f38_drts_127_williams_r_overbought_exit_count_42d": {"inputs": ["high", "low", "close"], "func": f38_drts_127_williams_r_overbought_exit_count_42d},
    "f38_drts_128_roc_decay_at_top_21d_minus_42d": {"inputs": ["close"], "func": f38_drts_128_roc_decay_at_top_21d_minus_42d},
    "f38_drts_129_price_displacement_decay_to_high_amplitude_42d": {"inputs": ["close", "high"], "func": f38_drts_129_price_displacement_decay_to_high_amplitude_42d},
    "f38_drts_130_momentum_collapse_after_high_21d": {"inputs": ["close", "high"], "func": f38_drts_130_momentum_collapse_after_high_21d},
    "f38_drts_131_acceleration_to_deceleration_pivot_distance_42d": {"inputs": ["close"], "func": f38_drts_131_acceleration_to_deceleration_pivot_distance_42d},
    "f38_drts_132_peak_strength_index_decay_21d": {"inputs": ["close", "high", "low"], "func": f38_drts_132_peak_strength_index_decay_21d},
    "f38_drts_133_trend_strength_decay_aroon_42d": {"inputs": ["high", "low"], "func": f38_drts_133_trend_strength_decay_aroon_42d},
    "f38_drts_134_dmi_di_minus_dominance_at_top_21d": {"inputs": ["high", "low", "close"], "func": f38_drts_134_dmi_di_minus_dominance_at_top_21d},
    "f38_drts_135_adx_decline_after_peak_21d": {"inputs": ["high", "low", "close"], "func": f38_drts_135_adx_decline_after_peak_21d},
    "f38_drts_136_distribution_top_composite_score": {"inputs": ["close", "high", "low", "volume"], "func": f38_drts_136_distribution_top_composite_score},
    "f38_drts_137_rolling_top_strength_zscore_8w": {"inputs": ["close", "high"], "func": f38_drts_137_rolling_top_strength_zscore_8w},
    "f38_drts_138_top_signature_pattern_score_63d": {"inputs": ["high", "close"], "func": f38_drts_138_top_signature_pattern_score_63d},
    "f38_drts_139_heavy_distribution_index_42d": {"inputs": ["close", "high", "low", "volume"], "func": f38_drts_139_heavy_distribution_index_42d},
    "f38_drts_140_distribution_persistence_score_63d": {"inputs": ["close", "high", "low", "volume"], "func": f38_drts_140_distribution_persistence_score_63d},
    "f38_drts_141_failed_top_breakout_intensity_63d": {"inputs": ["high", "close", "volume"], "func": f38_drts_141_failed_top_breakout_intensity_63d},
    "f38_drts_142_top_dwell_with_distribution_composite_63d": {"inputs": ["close", "high", "low", "volume"], "func": f38_drts_142_top_dwell_with_distribution_composite_63d},
    "f38_drts_143_multi_pattern_top_count_63d": {"inputs": ["high", "close", "low", "open"], "func": f38_drts_143_multi_pattern_top_count_63d},
    "f38_drts_144_churning_distribution_composite_63d": {"inputs": ["high", "low", "close", "volume"], "func": f38_drts_144_churning_distribution_composite_63d},
    "f38_drts_145_weakness_signature_index_63d": {"inputs": ["close", "high"], "func": f38_drts_145_weakness_signature_index_63d},
    "f38_drts_146_lower_highs_with_volume_composite_63d": {"inputs": ["high", "volume"], "func": f38_drts_146_lower_highs_with_volume_composite_63d},
    "f38_drts_147_supply_dominance_zscore_63d": {"inputs": ["close", "high", "low", "volume"], "func": f38_drts_147_supply_dominance_zscore_63d},
    "f38_drts_148_dollar_volume_distribution_zscore_42d": {"inputs": ["close", "low", "high", "volume"], "func": f38_drts_148_dollar_volume_distribution_zscore_42d},
    "f38_drts_149_top_breakdown_lead_score_63d": {"inputs": ["close", "high", "low"], "func": f38_drts_149_top_breakdown_lead_score_63d},
    "f38_drts_150_distribution_top_aggregate_zscore_63d": {"inputs": ["close", "high", "low", "volume"], "func": f38_drts_150_distribution_top_aggregate_zscore_63d},
}
