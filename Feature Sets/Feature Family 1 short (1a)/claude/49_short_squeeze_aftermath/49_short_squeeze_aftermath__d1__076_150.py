"""short_squeeze_aftermath d1 (first-diff) features 076-150 — Pipeline 1a-inverse short-side blowup family.

First-difference (.diff()) of each corresponding base feature — captures rate of change.
Inputs: NSIR (shortinterest, daystocover, shortpctfloat, shortpctshares,
shortinterestpriormonth) and SEP OHLCV (close, high, low, open, volume).
Detects POST-squeeze aftermath: covering exhausted, momentum fading, price
about to break down. Distinct from family #16 (snapshot SI structure) and
#25 (pre-peak SI buildup). PIT-clean: right-anchored rolling, explicit
min_periods, no centered windows, no .shift(-N). NSIR is sparse; pandas
rolling naturally skips NaN — no internal forward-fill.
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


def _safe_log_abs(s, eps=1e-12):
    if isinstance(s, pd.Series):
        a = s.abs()
        return np.log(a.where(a > eps, np.nan))
    a = np.abs(s)
    return np.log(np.where(a > eps, a, np.nan))


def _rolling_zscore(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    m = s.rolling(window, min_periods=min_periods).mean()
    sd = s.rolling(window, min_periods=min_periods).std()
    return (s - m) / sd.replace(0, np.nan)


def _ema(s, span, min_periods=None):
    if min_periods is None:
        min_periods = max(span // 3, 2)
    return s.ewm(span=span, adjust=False, min_periods=min_periods).mean()


def _rolling_max(s, w, mp=None):
    if mp is None:
        mp = max(w // 3, 2)
    return s.rolling(w, min_periods=mp).max()


def _rolling_min(s, w, mp=None):
    if mp is None:
        mp = max(w // 3, 2)
    return s.rolling(w, min_periods=mp).min()


def _pct_change(s, n):
    return _safe_div(s - s.shift(n), s.shift(n).abs())


# ============================================================
#                    FEATURES 076-150
# ============================================================


def f49_ssaf_076_double_top_gap_from_recent_high_d1(high):
    pk_old = _rolling_max(high, 252, mp=42).shift(21)
    pk_new = _rolling_max(high, 21, mp=5)
    return (_safe_div(pk_new - pk_old, pk_old)).diff()


def f49_ssaf_077_high_under_squeeze_peak_persistence_d1(high):
    pk = _rolling_max(high, 126, mp=21).shift(21)
    under = (high < pk).astype(float)
    return (under.rolling(63, min_periods=10).mean()).diff()


def f49_ssaf_078_rejection_at_prior_high_upper_wick_d1(high, close, open):
    pk = _rolling_max(high, 63, mp=10).shift(5)
    near = (_safe_div(high, pk) > 0.95).astype(float)
    wick = _safe_div(high - close.clip(lower=open).where(close >= open, open), close.replace(0, np.nan))
    return (near * wick).diff()


def f49_ssaf_079_consecutive_failed_breakout_count_63d_d1(high):
    pk21 = _rolling_max(high, 21, mp=5).shift(1)
    broke = (high > pk21).astype(float)
    back = broke.shift(1) * (high < pk21).astype(float)
    return (back.rolling(63, min_periods=10).sum()).diff()


def f49_ssaf_080_drop_from_failed_high_normalized_d1(high, close):
    pk = _rolling_max(high, 63, mp=10)
    atr_proxy = (high - close).rolling(21, min_periods=5).mean().replace(0, np.nan)
    return (_safe_div(pk - close, atr_proxy)).diff()


def f49_ssaf_081_close_below_squeeze_high_volume_rising_d1(close, high, volume):
    pk = _rolling_max(high, 63, mp=10).shift(5)
    under = (close < pk).astype(float)
    vchg = _pct_change(volume.rolling(5, min_periods=2).mean(), 21)
    return (under * vchg).diff()


def f49_ssaf_082_obv_divergence_below_peak_42d_d1(close, volume):
    d = np.sign(close.diff())
    obv = (d * volume).cumsum()
    obv_z = _rolling_zscore(obv, 63)
    px_z = _rolling_zscore(_safe_log(close), 63)
    return (px_z - obv_z).diff()


def f49_ssaf_083_distribution_days_count_21d_d1(close, volume):
    dn = (close.diff() < 0).astype(float)
    vup = (volume > volume.rolling(21, min_periods=5).mean()).astype(float)
    return ((dn * vup).rolling(21, min_periods=5).sum()).diff()


def f49_ssaf_084_close_in_low_third_of_day_streak_d1(close, high, low):
    pos = _safe_div(close - low, (high - low).replace(0, np.nan))
    low3 = (pos < 0.33).astype(float)
    grp = (low3 == 0).cumsum()
    return (low3.groupby(grp).cumsum()).diff()


def f49_ssaf_085_smart_money_signature_close_vs_open_21d_avg_d1(close, open):
    co = _safe_div(close - open, open)
    return (co.rolling(21, min_periods=5).mean()).diff()


def f49_ssaf_086_volume_weighted_close_vs_peak_42d_d1(close, volume, high):
    vwap = _safe_div((close * volume).rolling(42, min_periods=8).sum(), volume.rolling(42, min_periods=8).sum())
    pk = _rolling_max(high, 63, mp=10).shift(5)
    return (_safe_div(vwap, pk)).diff()


def f49_ssaf_087_ad_line_slope_negative_below_peak_d1(close, high, low, volume):
    clv = _safe_div((close - low) - (high - close), (high - low).replace(0, np.nan))
    ad = (clv * volume).cumsum()
    return (-_rolling_zscore(ad, 63)).diff()


def f49_ssaf_088_down_close_under_high_streak_d1(close, high):
    pk = _rolling_max(high, 63, mp=10).shift(5)
    down_under = ((close < pk) & (close.diff() < 0)).astype(float)
    grp = (down_under == 0).cumsum()
    return (down_under.groupby(grp).cumsum()).diff()


def f49_ssaf_089_squeeze_day_gap_unfilled_fraction_d1(open, low, close):
    gap = (open - close.shift(1)).clip(lower=0)
    gap_top = open
    gap_bot = close.shift(1)
    fill = ((low <= gap_bot) & (gap > 0)).astype(float)
    return ((1.0 - fill.rolling(21, min_periods=5).max()) * _safe_div(gap, close.shift(1))).diff()


def f49_ssaf_090_max_recent_gap_x_si_drop_d1(open, close, shortinterest):
    gap = _safe_div(open - close.shift(1), close.shift(1)).clip(lower=0)
    mg = gap.rolling(42, min_periods=8).max()
    si_drop = -_pct_change(shortinterest, 42)
    return (mg * si_drop).diff()


def f49_ssaf_091_fraction_gap_filled_21d_d1(open, low, close):
    gap = (open - close.shift(1)).clip(lower=0)
    filled_amt = (open - low).clip(lower=0).clip(upper=gap)
    return (_safe_div(filled_amt, gap).rolling(21, min_periods=5).mean()).diff()


def f49_ssaf_092_post_gap_pullback_depth_21d_d1(open, low):
    pivot = open.rolling(21, min_periods=5).max()
    return (_safe_div(pivot - low.rolling(5, min_periods=1).min(), pivot)).diff()


def f49_ssaf_093_gap_count_recent_21d_d1(open, close):
    g = (_safe_div(open - close.shift(1), close.shift(1)) > 0.02).astype(float)
    return (g.rolling(21, min_periods=5).sum()).diff()


def f49_ssaf_094_gap_fill_then_lower_low_proxy_d1(open, low, close):
    gap_top = open
    gap_bot = close.shift(1)
    filled = (low <= gap_bot).astype(float)
    newlow = (low < _rolling_min(low, 21, mp=5).shift(1)).astype(float)
    return ((filled * newlow).rolling(21, min_periods=5).sum()).diff()


def f49_ssaf_095_realized_vol_21d_drop_from_peak_d1(close):
    lr = _safe_log(close).diff()
    rv = lr.rolling(21, min_periods=5).std()
    pk = _rolling_max(rv, 63, mp=10)
    return (_safe_div(pk - rv, pk)).diff()


def f49_ssaf_096_vol_of_vol_collapse_63d_d1(close):
    lr = _safe_log(close).diff()
    rv = lr.rolling(21, min_periods=5).std()
    return (-_rolling_zscore(rv.rolling(21, min_periods=5).std(), 63)).diff()


def f49_ssaf_097_parkinson_vol_drop_42d_d1(high, low):
    pv = (_safe_log(high) - _safe_log(low)) ** 2
    p_est = (pv.rolling(21, min_periods=5).mean() / (4 * np.log(2))) ** 0.5
    pk = _rolling_max(p_est, 63, mp=10)
    return (_safe_div(pk - p_est, pk)).diff()


def f49_ssaf_098_garman_klass_vol_collapse_d1(open, high, low, close):
    term1 = 0.5 * (_safe_log(high) - _safe_log(low)) ** 2
    term2 = (2 * np.log(2) - 1) * (_safe_log(close) - _safe_log(open)) ** 2
    gk = (term1 - term2).rolling(21, min_periods=5).mean()
    pk = _rolling_max(gk, 63, mp=10)
    return (_safe_div(pk - gk, pk)).diff()


def f49_ssaf_099_vol_term_structure_inversion_21_vs_63_d1(close):
    lr = _safe_log(close).diff()
    v21 = lr.rolling(21, min_periods=5).std()
    v63 = lr.rolling(63, min_periods=10).std()
    return (_safe_div(v63 - v21, v63)).diff()


def f49_ssaf_100_realized_skew_proxy_drop_d1(close):
    lr = _safe_log(close).diff()
    mn = lr.rolling(63, min_periods=10).mean()
    sd = lr.rolling(63, min_periods=10).std()
    skew_proxy = ((lr - mn) ** 3).rolling(63, min_periods=10).mean() / (sd ** 3)
    return (-skew_proxy).diff()


def f49_ssaf_101_vol_collapse_x_si_drop_compound_d1(close, shortinterest):
    lr = _safe_log(close).diff()
    rv = lr.rolling(21, min_periods=5).std()
    vd = -_rolling_zscore(rv, 63)
    sd_si = -_rolling_zscore(shortinterest, 63)
    return (vd * sd_si).diff()


def f49_ssaf_102_high_low_atr_drop_signal_d1(high, low, close):
    pc = close.shift(1)
    tr = pd.concat([high - low, (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    a21 = tr.rolling(21, min_periods=5).mean()
    pk = _rolling_max(a21, 63, mp=10)
    return (_safe_div(pk - a21, pk)).diff()


def f49_ssaf_103_cum_volume_since_squeeze_peak_vs_si_d1(volume, shortinterest):
    cv = volume.rolling(42, min_periods=8).sum()
    return (_safe_div(cv, shortinterest)).diff()


def f49_ssaf_104_rotation_velocity_vs_priormonth_si_d1(volume, shortinterestpriormonth):
    cv = volume.rolling(21, min_periods=5).sum()
    return (_safe_div(cv, shortinterestpriormonth)).diff()


def f49_ssaf_105_spfloat_x_cumulative_turnover_decay_d1(volume, shortpctfloat):
    cv63 = volume.rolling(63, min_periods=10).sum()
    cv252 = volume.rolling(252, min_periods=42).sum()
    turnover_z = _safe_div(cv63, cv252)
    return (shortpctfloat * (1 - turnover_z)).diff()


def f49_ssaf_106_rotation_completed_indicator_d1(volume, shortinterest):
    cv = volume.rolling(63, min_periods=10).sum()
    ratio = _safe_div(cv, shortinterest)
    return ((ratio > 5).astype(float)).diff()


def f49_ssaf_107_dollar_rotation_to_si_value_d1(close, volume, shortinterest):
    dv = (close * volume).rolling(42, min_periods=8).sum()
    si_val = shortinterest * close
    return (_safe_div(dv, si_val)).diff()


def f49_ssaf_108_post_squeeze_cum_volume_z_normalized_d1(volume):
    return (_rolling_zscore(volume.rolling(42, min_periods=8).sum(), 252)).diff()


def f49_ssaf_109_si_vs_pre_squeeze_baseline_252d_mean_d1(shortinterest):
    base = shortinterest.shift(252).rolling(63, min_periods=10).mean()
    return (_safe_div(shortinterest - base, base)).diff()


def f49_ssaf_110_spfloat_vs_pre_squeeze_baseline_d1(shortpctfloat):
    base = shortpctfloat.shift(252).rolling(63, min_periods=10).mean()
    return (shortpctfloat - base).diff()


def f49_ssaf_111_si_distance_from_252d_min_normalized_d1(shortinterest):
    mn = _rolling_min(shortinterest, 252, mp=42)
    mx = _rolling_max(shortinterest, 252, mp=42)
    return (_safe_div(shortinterest - mn, (mx - mn).replace(0, np.nan))).diff()


def f49_ssaf_112_spshares_to_pre_squeeze_min_d1(shortpctshares):
    mn = _rolling_min(shortpctshares, 252, mp=42)
    return (_safe_div(shortpctshares - mn, mn.replace(0, np.nan))).diff()


def f49_ssaf_113_dtc_back_to_baseline_distance_d1(daystocover):
    base = daystocover.shift(252).rolling(63, min_periods=10).mean()
    return (_safe_div(daystocover - base, base)).diff()


def f49_ssaf_114_si_full_round_trip_proxy_d1(shortinterest):
    mx = _rolling_max(shortinterest, 252, mp=42)
    mn252 = _rolling_min(shortinterest, 252, mp=42)
    depth = _safe_div(mx - shortinterest, mx - mn252)
    return (depth).diff()


def f49_ssaf_115_log_si_minus_year_lag_log_si_d1(shortinterest):
    return (_safe_log(shortinterest) - _safe_log(shortinterest).shift(252)).diff()


def f49_ssaf_116_si_drop_streak_monthly_3consec_d1(shortinterest):
    m1 = shortinterest.shift(0) - shortinterest.shift(21)
    m2 = shortinterest.shift(21) - shortinterest.shift(42)
    m3 = shortinterest.shift(42) - shortinterest.shift(63)
    return (((m1 < 0).astype(float) + (m2 < 0).astype(float) + (m3 < 0).astype(float))).diff()


def f49_ssaf_117_si_seq_first_diff_negative_density_126d_d1(shortinterest):
    d = shortinterest.diff()
    return ((d < 0).astype(float).rolling(126, min_periods=21).mean()).diff()


def f49_ssaf_118_si_drop_magnitude_increasing_proxy_d1(shortinterest):
    d1 = shortinterest.diff(21)
    d2 = shortinterest.diff(21).shift(21)
    return (_safe_div(d1, d2)).diff()


def f49_ssaf_119_consecutive_lower_si_lows_count_d1(shortinterest):
    mn = _rolling_min(shortinterest, 21, mp=5)
    lower = (mn < mn.shift(21)).astype(float)
    grp = (lower == 0).cumsum()
    return (lower.groupby(grp).cumsum()).diff()


def f49_ssaf_120_si_drop_sequence_skew_proxy_d1(shortinterest):
    d = shortinterest.diff(21)
    mn = d.rolling(126, min_periods=21).mean()
    sd = d.rolling(126, min_periods=21).std()
    return (((d - mn) ** 3).rolling(126, min_periods=21).mean() / (sd ** 3)).diff()


def f49_ssaf_121_multi_horizon_si_drop_composite_d1(shortinterest):
    d21 = -_pct_change(shortinterest, 21)
    d63 = -_pct_change(shortinterest, 63)
    d126 = -_pct_change(shortinterest, 126)
    return ((d21 + d63 + d126) / 3.0).diff()


def f49_ssaf_122_fib_50_retrace_proxy_d1(close, high, low):
    pk = _rolling_max(high, 252, mp=42)
    tr = _rolling_min(low, 252, mp=42)
    half = (pk + tr) / 2.0
    return (_safe_div(half - close, pk - tr).clip(-2, 2)).diff()


def f49_ssaf_123_fib_618_retrace_breach_d1(close, high, low):
    pk = _rolling_max(high, 252, mp=42)
    tr = _rolling_min(low, 252, mp=42)
    fib = pk - 0.618 * (pk - tr)
    return ((close < fib).astype(float)).diff()


def f49_ssaf_124_retrace_depth_from_squeeze_peak_d1(close, high):
    pk = _rolling_max(high, 126, mp=21)
    return (_safe_div(pk - close, pk)).diff()


def f49_ssaf_125_speed_of_retrace_42d_d1(close, high):
    pk = _rolling_max(high, 126, mp=21)
    depth = _safe_div(pk - close, pk)
    return (depth - depth.shift(42)).diff()


def f49_ssaf_126_below_50pct_retrace_persistence_d1(close, high, low):
    pk = _rolling_max(high, 252, mp=42)
    tr = _rolling_min(low, 252, mp=42)
    half = (pk + tr) / 2.0
    return ((close < half).astype(float).rolling(63, min_periods=10).mean()).diff()


def f49_ssaf_127_retrace_completion_to_pre_squeeze_close_d1(close):
    pre = close.shift(126).rolling(21, min_periods=5).mean()
    return (_safe_div(close - pre, pre.abs())).diff()


def f49_ssaf_128_max_retrace_drawdown_63d_d1(close):
    mx = _rolling_max(close, 126, mp=21)
    dd = _safe_div(close - mx, mx)
    return (dd.rolling(63, min_periods=10).min()).diff()


def f49_ssaf_129_lower_low_after_squeeze_count_63d_d1(low):
    mn21 = _rolling_min(low, 21, mp=5)
    ll = (mn21 < mn21.shift(21)).astype(float)
    return (ll.rolling(63, min_periods=10).sum()).diff()


def f49_ssaf_130_higher_low_failure_indicator_d1(low):
    recent_mn = _rolling_min(low, 21, mp=5)
    older_mn = _rolling_min(low, 21, mp=5).shift(21)
    failure = (recent_mn < older_mn).astype(float)
    return (failure.rolling(42, min_periods=8).max()).diff()


def f49_ssaf_131_lower_high_sequence_signal_d1(high):
    mx21 = _rolling_max(high, 21, mp=5)
    lh = (mx21 < mx21.shift(21)).astype(float)
    return (lh.rolling(63, min_periods=10).sum()).diff()


def f49_ssaf_132_swing_high_lower_high_normalized_d1(high):
    mx_recent = _rolling_max(high, 21, mp=5)
    mx_prior = _rolling_max(high, 21, mp=5).shift(21)
    return (_safe_div(mx_recent - mx_prior, mx_prior)).diff()


def f49_ssaf_133_trend_break_below_42d_ema_after_peak_d1(close):
    ema = _ema(close, 42, min_periods=8)
    return ((close < ema).astype(float).rolling(63, min_periods=10).mean()).diff()


def f49_ssaf_134_down_swing_amplitude_vs_up_swing_d1(close):
    lr = _safe_log(close).diff()
    neg = lr.where(lr < 0, 0.0)
    pos = lr.where(lr > 0, 0.0)
    sum_neg = neg.rolling(63, min_periods=10).sum()
    sum_pos = pos.rolling(63, min_periods=10).sum()
    return (_safe_div(sum_neg.abs(), sum_pos)).diff()


def f49_ssaf_135_bars_since_252d_close_high_d1(close):
    def _bsm(w): return (len(w) - 1) - int(np.argmax(w))
    return (close.rolling(252, min_periods=42).apply(_bsm, raw=True)).diff()


def f49_ssaf_136_bars_since_max_si_x_si_drop_d1(shortinterest):
    def _bsm(w): return (len(w) - 1) - int(np.argmax(w))
    age = shortinterest.rolling(126, min_periods=21).apply(_bsm, raw=True)
    drop = -_pct_change(shortinterest, 21)
    return (age * drop).diff()


def f49_ssaf_137_bars_since_max_dtc_d1(daystocover):
    def _bsm(w): return (len(w) - 1) - int(np.argmax(w))
    return (daystocover.rolling(126, min_periods=21).apply(_bsm, raw=True)).diff()


def f49_ssaf_138_time_decay_log_age_close_below_peak_d1(close, high):
    def _bsm(w): return (len(w) - 1) - int(np.argmax(w))
    age = high.rolling(126, min_periods=21).apply(_bsm, raw=True)
    pk = _rolling_max(high, 126, mp=21)
    under = _safe_div(pk - close, pk)
    return (_safe_log(1 + age) * under).diff()


def f49_ssaf_139_weeks_since_volume_spike_x_si_drop_d1(volume, shortinterest):
    def _bsm(w): return (len(w) - 1) - int(np.argmax(w))
    age = volume.rolling(63, min_periods=10).apply(_bsm, raw=True)
    si_drop = -_pct_change(shortinterest, 63)
    return (age * si_drop).diff()


def f49_ssaf_140_compound_si_drop_x_price_elevated_d1(shortinterest, close):
    si_drop = -_pct_change(shortinterest, 63)
    px_z = _rolling_zscore(_safe_log(close), 252)
    return (si_drop * px_z).diff()


def f49_ssaf_141_compound_covering_vol_crush_x_distribution_d1(shortinterest, close, volume):
    si_drop = -_pct_change(shortinterest, 42)
    lr = _safe_log(close).diff()
    rv_drop = -_rolling_zscore(lr.rolling(21, min_periods=5).std(), 63)
    dn_v = (lr < 0).astype(float) * _safe_log(volume)
    dist = dn_v.rolling(21, min_periods=5).mean()
    return (si_drop * rv_drop * dist).diff()


def f49_ssaf_142_compound_dtc_collapse_x_range_compression_d1(daystocover, high, low, close):
    dtc_drop = -_pct_change(daystocover, 21)
    rng = _safe_div(high - low, close)
    rng_drop = -_rolling_zscore(rng, 63)
    return (dtc_drop * rng_drop).diff()


def f49_ssaf_143_compound_si_unwind_x_lower_high_d1(shortinterest, high):
    si_drop = -_pct_change(shortinterest, 42)
    mx_now = _rolling_max(high, 21, mp=5)
    mx_old = _rolling_max(high, 21, mp=5).shift(21)
    lh = _safe_div(mx_old - mx_now, mx_old)
    return (si_drop * lh).diff()


def f49_ssaf_144_compound_spfloat_drop_x_volume_thinning_d1(shortpctfloat, volume):
    spf_drop = -(shortpctfloat - shortpctfloat.shift(42))
    v_thin = -_rolling_zscore(volume, 63)
    return (spf_drop * v_thin).diff()


def f49_ssaf_145_triple_compound_aftermath_score_d1(shortinterest, close, high):
    si_drop = -_pct_change(shortinterest, 42)
    pk = _rolling_max(high, 126, mp=21)
    px_under = _safe_div(pk - close, pk)
    lr = _safe_log(close).diff()
    rv_drop = -_rolling_zscore(lr.rolling(21, min_periods=5).std(), 63)
    return (si_drop * px_under * rv_drop).diff()


def f49_ssaf_146_upper_wick_ratio_at_peak_63d_avg_d1(high, open, close):
    body_top = pd.concat([open, close], axis=1).max(axis=1)
    wick = (high - body_top).clip(lower=0)
    rng = (high - pd.concat([open, close], axis=1).min(axis=1)).replace(0, np.nan)
    ratio = _safe_div(wick, rng)
    return (ratio.rolling(63, min_periods=10).mean()).diff()


def f49_ssaf_147_close_minus_open_negative_streak_d1(close, open):
    neg = (close < open).astype(float)
    grp = (neg == 0).cumsum()
    return (neg.groupby(grp).cumsum()).diff()


def f49_ssaf_148_vwap_retracement_42d_d1(close, volume):
    vwap = _safe_div((close * volume).rolling(42, min_periods=8).sum(), volume.rolling(42, min_periods=8).sum())
    return (_safe_div(close - vwap, vwap)).diff()


def f49_ssaf_149_weekly_close_below_squeeze_peak_persistence_d1(close, high):
    wk_close = close.rolling(5, min_periods=1).mean()
    pk = _rolling_max(high, 126, mp=21).shift(5)
    return ((wk_close < pk).astype(float).rolling(63, min_periods=10).mean()).diff()


def f49_ssaf_150_post_squeeze_total_aftermath_index_d1(close, shortinterest, volume, high):
    pk_p = _rolling_max(high, 126, mp=21)
    dd = _safe_div(pk_p - close, pk_p)
    si_drop = -_pct_change(shortinterest, 63)
    v_thin = -_rolling_zscore(volume, 63)
    lr = _safe_log(close).diff()
    rv_drop = -_rolling_zscore(lr.rolling(21, min_periods=5).std(), 63)
    return ((dd + si_drop + v_thin + rv_drop) / 4.0).diff()


SHORT_SQUEEZE_AFTERMATH_D1_REGISTRY_076_150 = {
    "f49_ssaf_076_double_top_gap_from_recent_high_d1": {"inputs": ["high"], "func": f49_ssaf_076_double_top_gap_from_recent_high_d1},
    "f49_ssaf_077_high_under_squeeze_peak_persistence_d1": {"inputs": ["high"], "func": f49_ssaf_077_high_under_squeeze_peak_persistence_d1},
    "f49_ssaf_078_rejection_at_prior_high_upper_wick_d1": {"inputs": ["high", "close", "open"], "func": f49_ssaf_078_rejection_at_prior_high_upper_wick_d1},
    "f49_ssaf_079_consecutive_failed_breakout_count_63d_d1": {"inputs": ["high"], "func": f49_ssaf_079_consecutive_failed_breakout_count_63d_d1},
    "f49_ssaf_080_drop_from_failed_high_normalized_d1": {"inputs": ["high", "close"], "func": f49_ssaf_080_drop_from_failed_high_normalized_d1},
    "f49_ssaf_081_close_below_squeeze_high_volume_rising_d1": {"inputs": ["close", "high", "volume"], "func": f49_ssaf_081_close_below_squeeze_high_volume_rising_d1},
    "f49_ssaf_082_obv_divergence_below_peak_42d_d1": {"inputs": ["close", "volume"], "func": f49_ssaf_082_obv_divergence_below_peak_42d_d1},
    "f49_ssaf_083_distribution_days_count_21d_d1": {"inputs": ["close", "volume"], "func": f49_ssaf_083_distribution_days_count_21d_d1},
    "f49_ssaf_084_close_in_low_third_of_day_streak_d1": {"inputs": ["close", "high", "low"], "func": f49_ssaf_084_close_in_low_third_of_day_streak_d1},
    "f49_ssaf_085_smart_money_signature_close_vs_open_21d_avg_d1": {"inputs": ["close", "open"], "func": f49_ssaf_085_smart_money_signature_close_vs_open_21d_avg_d1},
    "f49_ssaf_086_volume_weighted_close_vs_peak_42d_d1": {"inputs": ["close", "volume", "high"], "func": f49_ssaf_086_volume_weighted_close_vs_peak_42d_d1},
    "f49_ssaf_087_ad_line_slope_negative_below_peak_d1": {"inputs": ["close", "high", "low", "volume"], "func": f49_ssaf_087_ad_line_slope_negative_below_peak_d1},
    "f49_ssaf_088_down_close_under_high_streak_d1": {"inputs": ["close", "high"], "func": f49_ssaf_088_down_close_under_high_streak_d1},
    "f49_ssaf_089_squeeze_day_gap_unfilled_fraction_d1": {"inputs": ["open", "low", "close"], "func": f49_ssaf_089_squeeze_day_gap_unfilled_fraction_d1},
    "f49_ssaf_090_max_recent_gap_x_si_drop_d1": {"inputs": ["open", "close", "shortinterest"], "func": f49_ssaf_090_max_recent_gap_x_si_drop_d1},
    "f49_ssaf_091_fraction_gap_filled_21d_d1": {"inputs": ["open", "low", "close"], "func": f49_ssaf_091_fraction_gap_filled_21d_d1},
    "f49_ssaf_092_post_gap_pullback_depth_21d_d1": {"inputs": ["open", "low"], "func": f49_ssaf_092_post_gap_pullback_depth_21d_d1},
    "f49_ssaf_093_gap_count_recent_21d_d1": {"inputs": ["open", "close"], "func": f49_ssaf_093_gap_count_recent_21d_d1},
    "f49_ssaf_094_gap_fill_then_lower_low_proxy_d1": {"inputs": ["open", "low", "close"], "func": f49_ssaf_094_gap_fill_then_lower_low_proxy_d1},
    "f49_ssaf_095_realized_vol_21d_drop_from_peak_d1": {"inputs": ["close"], "func": f49_ssaf_095_realized_vol_21d_drop_from_peak_d1},
    "f49_ssaf_096_vol_of_vol_collapse_63d_d1": {"inputs": ["close"], "func": f49_ssaf_096_vol_of_vol_collapse_63d_d1},
    "f49_ssaf_097_parkinson_vol_drop_42d_d1": {"inputs": ["high", "low"], "func": f49_ssaf_097_parkinson_vol_drop_42d_d1},
    "f49_ssaf_098_garman_klass_vol_collapse_d1": {"inputs": ["open", "high", "low", "close"], "func": f49_ssaf_098_garman_klass_vol_collapse_d1},
    "f49_ssaf_099_vol_term_structure_inversion_21_vs_63_d1": {"inputs": ["close"], "func": f49_ssaf_099_vol_term_structure_inversion_21_vs_63_d1},
    "f49_ssaf_100_realized_skew_proxy_drop_d1": {"inputs": ["close"], "func": f49_ssaf_100_realized_skew_proxy_drop_d1},
    "f49_ssaf_101_vol_collapse_x_si_drop_compound_d1": {"inputs": ["close", "shortinterest"], "func": f49_ssaf_101_vol_collapse_x_si_drop_compound_d1},
    "f49_ssaf_102_high_low_atr_drop_signal_d1": {"inputs": ["high", "low", "close"], "func": f49_ssaf_102_high_low_atr_drop_signal_d1},
    "f49_ssaf_103_cum_volume_since_squeeze_peak_vs_si_d1": {"inputs": ["volume", "shortinterest"], "func": f49_ssaf_103_cum_volume_since_squeeze_peak_vs_si_d1},
    "f49_ssaf_104_rotation_velocity_vs_priormonth_si_d1": {"inputs": ["volume", "shortinterestpriormonth"], "func": f49_ssaf_104_rotation_velocity_vs_priormonth_si_d1},
    "f49_ssaf_105_spfloat_x_cumulative_turnover_decay_d1": {"inputs": ["volume", "shortpctfloat"], "func": f49_ssaf_105_spfloat_x_cumulative_turnover_decay_d1},
    "f49_ssaf_106_rotation_completed_indicator_d1": {"inputs": ["volume", "shortinterest"], "func": f49_ssaf_106_rotation_completed_indicator_d1},
    "f49_ssaf_107_dollar_rotation_to_si_value_d1": {"inputs": ["close", "volume", "shortinterest"], "func": f49_ssaf_107_dollar_rotation_to_si_value_d1},
    "f49_ssaf_108_post_squeeze_cum_volume_z_normalized_d1": {"inputs": ["volume"], "func": f49_ssaf_108_post_squeeze_cum_volume_z_normalized_d1},
    "f49_ssaf_109_si_vs_pre_squeeze_baseline_252d_mean_d1": {"inputs": ["shortinterest"], "func": f49_ssaf_109_si_vs_pre_squeeze_baseline_252d_mean_d1},
    "f49_ssaf_110_spfloat_vs_pre_squeeze_baseline_d1": {"inputs": ["shortpctfloat"], "func": f49_ssaf_110_spfloat_vs_pre_squeeze_baseline_d1},
    "f49_ssaf_111_si_distance_from_252d_min_normalized_d1": {"inputs": ["shortinterest"], "func": f49_ssaf_111_si_distance_from_252d_min_normalized_d1},
    "f49_ssaf_112_spshares_to_pre_squeeze_min_d1": {"inputs": ["shortpctshares"], "func": f49_ssaf_112_spshares_to_pre_squeeze_min_d1},
    "f49_ssaf_113_dtc_back_to_baseline_distance_d1": {"inputs": ["daystocover"], "func": f49_ssaf_113_dtc_back_to_baseline_distance_d1},
    "f49_ssaf_114_si_full_round_trip_proxy_d1": {"inputs": ["shortinterest"], "func": f49_ssaf_114_si_full_round_trip_proxy_d1},
    "f49_ssaf_115_log_si_minus_year_lag_log_si_d1": {"inputs": ["shortinterest"], "func": f49_ssaf_115_log_si_minus_year_lag_log_si_d1},
    "f49_ssaf_116_si_drop_streak_monthly_3consec_d1": {"inputs": ["shortinterest"], "func": f49_ssaf_116_si_drop_streak_monthly_3consec_d1},
    "f49_ssaf_117_si_seq_first_diff_negative_density_126d_d1": {"inputs": ["shortinterest"], "func": f49_ssaf_117_si_seq_first_diff_negative_density_126d_d1},
    "f49_ssaf_118_si_drop_magnitude_increasing_proxy_d1": {"inputs": ["shortinterest"], "func": f49_ssaf_118_si_drop_magnitude_increasing_proxy_d1},
    "f49_ssaf_119_consecutive_lower_si_lows_count_d1": {"inputs": ["shortinterest"], "func": f49_ssaf_119_consecutive_lower_si_lows_count_d1},
    "f49_ssaf_120_si_drop_sequence_skew_proxy_d1": {"inputs": ["shortinterest"], "func": f49_ssaf_120_si_drop_sequence_skew_proxy_d1},
    "f49_ssaf_121_multi_horizon_si_drop_composite_d1": {"inputs": ["shortinterest"], "func": f49_ssaf_121_multi_horizon_si_drop_composite_d1},
    "f49_ssaf_122_fib_50_retrace_proxy_d1": {"inputs": ["close", "high", "low"], "func": f49_ssaf_122_fib_50_retrace_proxy_d1},
    "f49_ssaf_123_fib_618_retrace_breach_d1": {"inputs": ["close", "high", "low"], "func": f49_ssaf_123_fib_618_retrace_breach_d1},
    "f49_ssaf_124_retrace_depth_from_squeeze_peak_d1": {"inputs": ["close", "high"], "func": f49_ssaf_124_retrace_depth_from_squeeze_peak_d1},
    "f49_ssaf_125_speed_of_retrace_42d_d1": {"inputs": ["close", "high"], "func": f49_ssaf_125_speed_of_retrace_42d_d1},
    "f49_ssaf_126_below_50pct_retrace_persistence_d1": {"inputs": ["close", "high", "low"], "func": f49_ssaf_126_below_50pct_retrace_persistence_d1},
    "f49_ssaf_127_retrace_completion_to_pre_squeeze_close_d1": {"inputs": ["close"], "func": f49_ssaf_127_retrace_completion_to_pre_squeeze_close_d1},
    "f49_ssaf_128_max_retrace_drawdown_63d_d1": {"inputs": ["close"], "func": f49_ssaf_128_max_retrace_drawdown_63d_d1},
    "f49_ssaf_129_lower_low_after_squeeze_count_63d_d1": {"inputs": ["low"], "func": f49_ssaf_129_lower_low_after_squeeze_count_63d_d1},
    "f49_ssaf_130_higher_low_failure_indicator_d1": {"inputs": ["low"], "func": f49_ssaf_130_higher_low_failure_indicator_d1},
    "f49_ssaf_131_lower_high_sequence_signal_d1": {"inputs": ["high"], "func": f49_ssaf_131_lower_high_sequence_signal_d1},
    "f49_ssaf_132_swing_high_lower_high_normalized_d1": {"inputs": ["high"], "func": f49_ssaf_132_swing_high_lower_high_normalized_d1},
    "f49_ssaf_133_trend_break_below_42d_ema_after_peak_d1": {"inputs": ["close"], "func": f49_ssaf_133_trend_break_below_42d_ema_after_peak_d1},
    "f49_ssaf_134_down_swing_amplitude_vs_up_swing_d1": {"inputs": ["close"], "func": f49_ssaf_134_down_swing_amplitude_vs_up_swing_d1},
    "f49_ssaf_135_bars_since_252d_close_high_d1": {"inputs": ["close"], "func": f49_ssaf_135_bars_since_252d_close_high_d1},
    "f49_ssaf_136_bars_since_max_si_x_si_drop_d1": {"inputs": ["shortinterest"], "func": f49_ssaf_136_bars_since_max_si_x_si_drop_d1},
    "f49_ssaf_137_bars_since_max_dtc_d1": {"inputs": ["daystocover"], "func": f49_ssaf_137_bars_since_max_dtc_d1},
    "f49_ssaf_138_time_decay_log_age_close_below_peak_d1": {"inputs": ["close", "high"], "func": f49_ssaf_138_time_decay_log_age_close_below_peak_d1},
    "f49_ssaf_139_weeks_since_volume_spike_x_si_drop_d1": {"inputs": ["volume", "shortinterest"], "func": f49_ssaf_139_weeks_since_volume_spike_x_si_drop_d1},
    "f49_ssaf_140_compound_si_drop_x_price_elevated_d1": {"inputs": ["shortinterest", "close"], "func": f49_ssaf_140_compound_si_drop_x_price_elevated_d1},
    "f49_ssaf_141_compound_covering_vol_crush_x_distribution_d1": {"inputs": ["shortinterest", "close", "volume"], "func": f49_ssaf_141_compound_covering_vol_crush_x_distribution_d1},
    "f49_ssaf_142_compound_dtc_collapse_x_range_compression_d1": {"inputs": ["daystocover", "high", "low", "close"], "func": f49_ssaf_142_compound_dtc_collapse_x_range_compression_d1},
    "f49_ssaf_143_compound_si_unwind_x_lower_high_d1": {"inputs": ["shortinterest", "high"], "func": f49_ssaf_143_compound_si_unwind_x_lower_high_d1},
    "f49_ssaf_144_compound_spfloat_drop_x_volume_thinning_d1": {"inputs": ["shortpctfloat", "volume"], "func": f49_ssaf_144_compound_spfloat_drop_x_volume_thinning_d1},
    "f49_ssaf_145_triple_compound_aftermath_score_d1": {"inputs": ["shortinterest", "close", "high"], "func": f49_ssaf_145_triple_compound_aftermath_score_d1},
    "f49_ssaf_146_upper_wick_ratio_at_peak_63d_avg_d1": {"inputs": ["high", "open", "close"], "func": f49_ssaf_146_upper_wick_ratio_at_peak_63d_avg_d1},
    "f49_ssaf_147_close_minus_open_negative_streak_d1": {"inputs": ["close", "open"], "func": f49_ssaf_147_close_minus_open_negative_streak_d1},
    "f49_ssaf_148_vwap_retracement_42d_d1": {"inputs": ["close", "volume"], "func": f49_ssaf_148_vwap_retracement_42d_d1},
    "f49_ssaf_149_weekly_close_below_squeeze_peak_persistence_d1": {"inputs": ["close", "high"], "func": f49_ssaf_149_weekly_close_below_squeeze_peak_persistence_d1},
    "f49_ssaf_150_post_squeeze_total_aftermath_index_d1": {"inputs": ["close", "shortinterest", "volume", "high"], "func": f49_ssaf_150_post_squeeze_total_aftermath_index_d1},
}
