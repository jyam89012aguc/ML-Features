"""revenue_deceleration_acceleration d2 features 076_150 — Pipeline 1a-inverse short-side blowup family.

Pattern-detection hypotheses on revenue acceleration dynamics (yoy% growth's quarter-over-quarter
change). Distinct from family 21 (rgdc) which owns levels/slopes/trends. Per HANDOFF §6
families 29-36 special rule: base = pattern features on acceleration, NOT raw 2nd derivatives.
Self-contained: helpers at top of each file. PIT-clean: right-anchored rolling, explicit
min_periods, no centered windows, no .shift(-N). SF1 quarterly cadence (lags 1, 4, 8, 12, 16, 20).
"""
import numpy as np
import pandas as pd


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


def _ttm(s):
    return s.rolling(4, min_periods=1).sum()


def _avg4(s):
    return s.rolling(4, min_periods=1).mean()


def _yoy(s):
    return s - s.shift(4)


def _yoy_pct(s):
    return _safe_div(s - s.shift(4), s.shift(4).abs())


def _qoq(s):
    return s.diff()


def _qoq_pct(s):
    return _safe_div(s.diff(), s.shift(1).abs())


def _accel(s):
    return _yoy_pct(s).diff()


def _qaccel(s):
    return _qoq_pct(s).diff()


def _ttm_accel(s):
    return _yoy_pct(_ttm(s)).diff()


def _ema(s, span):
    return s.ewm(span=span, adjust=False, min_periods=max(span // 3, 2)).mean()


def _rolling_mad(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    med = s.rolling(window, min_periods=min_periods).median()
    return (s - med).abs().rolling(window, min_periods=min_periods).median()


def _rolling_quantile(s, window, q, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    return s.rolling(window, min_periods=min_periods).quantile(q)


def _rolling_rank_pct(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    return s.rolling(window, min_periods=min_periods).rank(pct=True)


def _consec_true_streak(b):
    b = b.fillna(False).astype(bool)
    grp = (~b).cumsum()
    return b.astype(int).groupby(grp).cumsum()


def _max_consec_true(b, window):
    streak = _consec_true_streak(b)
    return streak.rolling(window, min_periods=1).max()


def _rolling_count(b, window):
    return b.fillna(False).astype(float).rolling(window, min_periods=1).sum()


def _rolling_frac(b, window):
    return b.fillna(False).astype(float).rolling(window, min_periods=1).mean()


def _sign_safe(s):
    return np.sign(s).where(s.notna(), np.nan)


def _winsorize(s, lo=0.1, hi=0.9, window=8, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    qlo = s.rolling(window, min_periods=min_periods).quantile(lo)
    qhi = s.rolling(window, min_periods=min_periods).quantile(hi)
    return s.clip(lower=qlo, upper=qhi)


def f29_rdac_076_sign_agreement_count_rev_gp_cogs_netinc_accel_d2(revenue, gp, cogs, netinc):
    s = (_accel(revenue) < 0).astype(float) + (_accel(gp) < 0).astype(float) + (_accel(cogs) < 0).astype(float) + (_accel(netinc) < 0).astype(float)
    result = s.where(_accel(revenue).notna(), np.nan)
    return result.diff().diff()


def f29_rdac_077_sign_agreement_count_sum_4q_d2(revenue, gp, cogs, netinc):
    s = (_accel(revenue) < 0).astype(float) + (_accel(gp) < 0).astype(float) + (_accel(cogs) < 0).astype(float) + (_accel(netinc) < 0).astype(float)
    result = s.rolling(4, min_periods=2).sum()
    return result.diff().diff()


def f29_rdac_078_cross_metric_corr_rev_netinc_accel_8q_d2(revenue, netinc):
    result = _accel(revenue).rolling(8, min_periods=4).corr(_accel(netinc))
    return result.diff().diff()


def f29_rdac_079_worst_horizon_accel_z_signed_d2(revenue):
    zy = _rolling_zscore(_accel(revenue), 8); zq = _rolling_zscore(_qaccel(revenue), 8); zt = _rolling_zscore(_ttm_accel(revenue), 8)
    result = pd.concat([zy, zq, zt], axis=1).min(axis=1)
    return result.diff().diff()


def f29_rdac_080_smoothed_raw_accel_sign_disagree_d2(revenue):
    a = _accel(revenue); em = _ema(a, 4)
    result = (_sign_safe(em) != _sign_safe(a)).astype(float).where(a.notna() & em.notna(), np.nan)
    return result.diff().diff()


def f29_rdac_081_ema4_accel_just_flipped_pos_to_neg_d2(revenue):
    em = _ema(_accel(revenue), 4)
    result = ((em < 0) & (em.shift(1) >= 0)).astype(float).where(em.notna() & em.shift(1).notna(), np.nan)
    return result.diff().diff()


def f29_rdac_082_raw_pos_ema_neg_catchup_warning_d2(revenue):
    a = _accel(revenue); em = _ema(a, 4)
    result = ((a > 0) & (em < 0)).astype(float).where(a.notna() & em.notna(), np.nan)
    return result.diff().diff()


def f29_rdac_083_raw_neg_ema_pos_false_alarm_filter_d2(revenue):
    a = _accel(revenue); em = _ema(a, 4)
    result = ((a < 0) & (em > 0)).astype(float).where(a.notna() & em.notna(), np.nan)
    return result.diff().diff()


def f29_rdac_084_accel_residuals_skew_8q_d2(revenue):
    a = _accel(revenue); m = a.rolling(8, min_periods=4).mean()
    result = (a - m).rolling(8, min_periods=4).skew()
    return result.diff().diff()


def f29_rdac_085_accel_residuals_kurt_8q_d2(revenue):
    a = _accel(revenue); m = a.rolling(8, min_periods=4).mean()
    result = (a - m).rolling(8, min_periods=4).kurt()
    return result.diff().diff()


def f29_rdac_086_accel_ema_long_short_cross_sign_disagree_d2(revenue):
    a = _accel(revenue); e4 = _ema(a, 4); e12 = _ema(a, 12)
    result = (_sign_safe(e4) != _sign_safe(e12)).astype(float).where(e4.notna() & e12.notna(), np.nan)
    return result.diff().diff()


def f29_rdac_087_accel_ema4_below_ema12_persistent_3q_d2(revenue):
    a = _accel(revenue); e4 = _ema(a, 4); e12 = _ema(a, 12)
    result = _max_consec_true(e4 < e12, 8).astype(float)
    return result.diff().diff()


def f29_rdac_088_accel_2nd_diff_current_d2(revenue):
    result = _accel(revenue).diff().diff()
    return result.diff().diff()


def f29_rdac_089_accel_2nd_diff_zscore_8q_d2(revenue):
    c = _accel(revenue).diff().diff()
    result = _rolling_zscore(c, 8)
    return result.diff().diff()


def f29_rdac_090_accel_2nd_diff_flip_pos_to_neg_d2(revenue):
    c = _accel(revenue).diff().diff()
    result = ((c < 0) & (c.shift(1) >= 0)).astype(float).where(c.notna() & c.shift(1).notna(), np.nan)
    return result.diff().diff()


def f29_rdac_091_accel_slope_sign_flip_pos_to_neg_d2(revenue):
    sl = _rolling_slope(_accel(revenue), 4)
    result = ((sl < 0) & (sl.shift(1) >= 0)).astype(float).where(sl.notna() & sl.shift(1).notna(), np.nan)
    return result.diff().diff()


def f29_rdac_092_accel_slope_4q_d2(revenue):
    result = _rolling_slope(_accel(revenue), 4)
    return result.diff().diff()


def f29_rdac_093_accel_slope_8q_minus_4q_d2(revenue):
    result = _rolling_slope(_accel(revenue), 8) - _rolling_slope(_accel(revenue), 4)
    return result.diff().diff()


def f29_rdac_094_accel_dev_from_8q_median_d2(revenue):
    a = _accel(revenue)
    result = a - a.rolling(8, min_periods=3).median()
    return result.diff().diff()


def f29_rdac_095_accel_hampel_outlier_3mad_12q_d2(revenue):
    a = _accel(revenue); med = a.rolling(12, min_periods=4).median(); mad = _rolling_mad(a, 12)
    result = ((a - med).abs() > 3.0 * mad).astype(float).where(a.notna() & mad.notna(), np.nan)
    return result.diff().diff()


def f29_rdac_096_accel_hampel_positive_outlier_12q_d2(revenue):
    a = _accel(revenue); med = a.rolling(12, min_periods=4).median(); mad = _rolling_mad(a, 12)
    result = ((a - med) > 3.0 * mad).astype(float).where(a.notna() & mad.notna(), np.nan)
    return result.diff().diff()


def f29_rdac_097_accel_hampel_negative_outlier_12q_d2(revenue):
    a = _accel(revenue); med = a.rolling(12, min_periods=4).median(); mad = _rolling_mad(a, 12)
    result = ((med - a) > 3.0 * mad).astype(float).where(a.notna() & mad.notna(), np.nan)
    return result.diff().diff()


def f29_rdac_098_accel_rolling_rank_pct_16q_d2(revenue):
    result = _rolling_rank_pct(_accel(revenue), 16)
    return result.diff().diff()


def f29_rdac_099_accel_rolling_decile_20q_d2(revenue):
    result = (_rolling_rank_pct(_accel(revenue), 20) * 10.0).round()
    return result.diff().diff()


def f29_rdac_100_accel_extreme_recency_12q_d2(revenue):
    z = _rolling_zscore(_accel(revenue), 12).abs()
    hit = (z > 2.0).astype(float)
    idx_arr = np.arange(len(z), dtype=float)
    last_hit = pd.Series(np.where(hit > 0, idx_arr, np.nan), index=z.index).ffill()
    result = (pd.Series(idx_arr, index=z.index) - last_hit).where(last_hit.notna(), np.nan)
    return result.diff().diff()


def f29_rdac_101_yoy_pct_drawdown_from_8q_max_d2(revenue):
    y = _yoy_pct(revenue)
    result = y.rolling(8, min_periods=3).max() - y
    return result.diff().diff()


def f29_rdac_102_yoy_pct_drawdown_from_12q_max_d2(revenue):
    y = _yoy_pct(revenue)
    result = y.rolling(12, min_periods=4).max() - y
    return result.diff().diff()


def f29_rdac_103_yoy_pct_q_since_12q_max_d2(revenue):
    y = _yoy_pct(revenue)
    result = y.rolling(12, min_periods=4).apply(lambda w: float(len(w) - 1 - int(np.nanargmax(w))) if not np.isnan(w).all() else np.nan, raw=True)
    return result.diff().diff()


def f29_rdac_104_ttm_yoy_drawdown_from_8q_max_d2(revenue):
    y = _yoy_pct(_ttm(revenue))
    result = y.rolling(8, min_periods=3).max() - y
    return result.diff().diff()


def f29_rdac_105_yoy_drawdown_velocity_depth_per_duration_d2(revenue):
    y = _yoy_pct(revenue); depth = y.rolling(12, min_periods=4).max() - y
    dur = y.rolling(12, min_periods=4).apply(lambda w: float(len(w) - 1 - int(np.nanargmax(w))) if not np.isnan(w).all() else np.nan, raw=True)
    result = _safe_div(depth, dur.replace(0, np.nan))
    return result.diff().diff()


def f29_rdac_106_yoy_recovery_rate_from_8q_min_d2(revenue):
    y = _yoy_pct(revenue); mn = y.rolling(8, min_periods=3).min(); mx = y.rolling(8, min_periods=3).max()
    result = _safe_div(y - mn, mx - mn)
    return result.diff().diff()


def f29_rdac_107_accel_diff_neg_over_pos_mean_mag_8q_d2(revenue):
    d = _accel(revenue).diff()
    neg = d.where(d < 0).abs().rolling(8, min_periods=2).mean()
    pos = d.where(d > 0).rolling(8, min_periods=2).mean()
    result = _safe_div(neg, pos)
    return result.diff().diff()


def f29_rdac_108_accel_pain_ratio_neg_sum_over_total_8q_d2(revenue):
    d = _accel(revenue).diff()
    neg = d.where(d < 0).abs().rolling(8, min_periods=2).sum()
    tot = d.abs().rolling(8, min_periods=2).sum()
    result = _safe_div(neg, tot)
    return result.diff().diff()


def f29_rdac_109_yoy_pct_max_drawdown_16q_d2(revenue):
    y = _yoy_pct(revenue)
    result = (y.rolling(16, min_periods=5).max() - y.rolling(16, min_periods=5).min())
    return result.diff().diff()


def f29_rdac_110_yoy_pct_q_since_16q_max_d2(revenue):
    y = _yoy_pct(revenue)
    result = y.rolling(16, min_periods=5).apply(lambda w: float(len(w) - 1 - int(np.nanargmax(w))) if not np.isnan(w).all() else np.nan, raw=True)
    return result.diff().diff()


def f29_rdac_111_accel_curve_signed_area_8q_d2(revenue):
    result = _accel(revenue).rolling(8, min_periods=3).sum()
    return result.diff().diff()


def f29_rdac_112_accel_ulcer_index_negative_dd_rms_8q_d2(revenue):
    a = _accel(revenue); dd = (a.rolling(8, min_periods=3).max() - a).clip(lower=0)
    result = (dd ** 2).rolling(8, min_periods=3).mean().pow(0.5)
    return result.diff().diff()


def f29_rdac_113_accel_calmar_proxy_4q_mean_over_8q_dd_d2(revenue):
    a = _accel(revenue); m4 = a.rolling(4, min_periods=2).mean(); dd = a.rolling(8, min_periods=3).max() - a.rolling(8, min_periods=3).min()
    result = _safe_div(m4, dd.replace(0, np.nan))
    return result.diff().diff()


def f29_rdac_114_yoy_drawdown_event_count_5pct_12q_d2(revenue):
    y = _yoy_pct(revenue); dd = y.rolling(12, min_periods=4).max() - y
    result = _rolling_count(dd > 0.05, 12)
    return result.diff().diff()


def f29_rdac_115_yoy_recovery_failure_after_min_8q_d2(revenue):
    y = _yoy_pct(revenue); mn8 = y.rolling(8, min_periods=3).min(); rng16 = y.rolling(16, min_periods=5).max() - y.rolling(16, min_periods=5).min()
    pos = _safe_div(y - y.rolling(16, min_periods=5).min(), rng16)
    result = ((y.shift(8) == mn8.shift(8)) & (pos < 0.5)).astype(float).where(y.notna() & pos.notna(), np.nan)
    return result.diff().diff()


def f29_rdac_116_yoy_stairstep_down_new_min_count_8q_d2(revenue):
    y = _yoy_pct(revenue)
    nl = (y == y.rolling(12, min_periods=4).min()).astype(float)
    result = nl.rolling(8, min_periods=2).sum()
    return result.diff().diff()


def f29_rdac_117_accel_convex_chord_deviation_8q_d2(revenue):
    a = _accel(revenue)
    chord = (a + a.shift(7)) / 2.0
    result = a.rolling(8, min_periods=3).mean() - chord
    return result.diff().diff()


def f29_rdac_118_yoy_consecutive_decline_streak_d2(revenue):
    y = _yoy_pct(revenue)
    result = _consec_true_streak(y < y.shift(1)).astype(float)
    return result.diff().diff()


def f29_rdac_119_composite_broken_down_score_8q_d2(revenue):
    a = _accel(revenue); d = a.diff()
    cliff = (d < -0.05).astype(float).rolling(8, min_periods=2).sum()
    nl = (a == a.rolling(12, min_periods=4).min()).astype(float).rolling(8, min_periods=2).sum()
    streak = _consec_true_streak(a < 0).astype(float)
    result = cliff.fillna(0) + nl.fillna(0) + streak.fillna(0).clip(upper=8)
    return result.diff().diff()


def f29_rdac_120_yoy_drawdown_acceleration_4q_d2(revenue):
    y = _yoy_pct(revenue); dd = y.rolling(12, min_periods=4).max() - y
    result = dd - dd.shift(4)
    return result.diff().diff()


def f29_rdac_121_accel_skew_8q_d2(revenue):
    result = _accel(revenue).rolling(8, min_periods=4).skew()
    return result.diff().diff()


def f29_rdac_122_accel_skew_12q_d2(revenue):
    result = _accel(revenue).rolling(12, min_periods=5).skew()
    return result.diff().diff()


def f29_rdac_123_accel_kurt_8q_d2(revenue):
    result = _accel(revenue).rolling(8, min_periods=4).kurt()
    return result.diff().diff()


def f29_rdac_124_accel_kurt_12q_d2(revenue):
    result = _accel(revenue).rolling(12, min_periods=5).kurt()
    return result.diff().diff()


def f29_rdac_125_accel_skew_change_8q_vs_12q_d2(revenue):
    a = _accel(revenue)
    result = a.rolling(8, min_periods=4).skew() - a.rolling(12, min_periods=5).skew()
    return result.diff().diff()


def f29_rdac_126_accel_kurt_change_8q_vs_12q_d2(revenue):
    a = _accel(revenue)
    result = a.rolling(8, min_periods=4).kurt() - a.rolling(12, min_periods=5).kurt()
    return result.diff().diff()


def f29_rdac_127_accel_cv_8q_d2(revenue):
    a = _accel(revenue)
    result = _safe_div(a.rolling(8, min_periods=3).std(), a.rolling(8, min_periods=3).mean().abs())
    return result.diff().diff()


def f29_rdac_128_accel_cv_change_8q_vs_16q_d2(revenue):
    a = _accel(revenue)
    cv8 = _safe_div(a.rolling(8, min_periods=3).std(), a.rolling(8, min_periods=3).mean().abs())
    cv16 = _safe_div(a.rolling(16, min_periods=5).std(), a.rolling(16, min_periods=5).mean().abs())
    result = cv8 - cv16
    return result.diff().diff()


def f29_rdac_129_accel_quantile_dispersion_q90_q10_12q_d2(revenue):
    a = _accel(revenue)
    result = a.rolling(12, min_periods=4).quantile(0.9) - a.rolling(12, min_periods=4).quantile(0.1)
    return result.diff().diff()


def f29_rdac_130_accel_neg_tail_4q_in_16q_q25_d2(revenue):
    a = _accel(revenue); q25 = a.rolling(16, min_periods=5).quantile(0.25)
    result = _rolling_count(a < q25, 4)
    return result.diff().diff()


def f29_rdac_131_accel_right_tail_collapse_q90_neg_8q_d2(revenue):
    a = _accel(revenue); q90 = a.rolling(8, min_periods=3).quantile(0.9)
    result = (q90 < 0).astype(float).where(q90.notna(), np.nan)
    return result.diff().diff()


def f29_rdac_132_accel_median_z_signed_8q_d2(revenue):
    a = _accel(revenue)
    result = _safe_div(a.rolling(8, min_periods=3).median(), a.rolling(8, min_periods=3).std())
    return result.diff().diff()


def f29_rdac_133_accel_mean_minus_median_8q_d2(revenue):
    a = _accel(revenue)
    result = a.rolling(8, min_periods=3).mean() - a.rolling(8, min_periods=3).median()
    return result.diff().diff()


def f29_rdac_134_accel_trimmed_mean_8q_d2(revenue):
    a = _accel(revenue)
    result = a.rolling(8, min_periods=4).apply(lambda w: np.nanmean(np.sort(w[~np.isnan(w)])[1:-1]) if (~np.isnan(w)).sum() >= 4 else np.nan, raw=True)
    return result.diff().diff()


def f29_rdac_135_accel_winsorized_z_10pct_8q_d2(revenue):
    a = _accel(revenue); w = _winsorize(a, 0.1, 0.9, 8)
    result = _rolling_zscore(w, 8)
    return result.diff().diff()


def f29_rdac_136_accel_range_over_abs_median_8q_d2(revenue):
    a = _accel(revenue)
    result = _safe_div(a.rolling(8, min_periods=3).max() - a.rolling(8, min_periods=3).min(), a.rolling(8, min_periods=3).median().abs())
    return result.diff().diff()


def f29_rdac_137_accel_iqr_over_abs_median_8q_d2(revenue):
    a = _accel(revenue)
    iqr = a.rolling(8, min_periods=3).quantile(0.75) - a.rolling(8, min_periods=3).quantile(0.25)
    result = _safe_div(iqr, a.rolling(8, min_periods=3).median().abs())
    return result.diff().diff()


def f29_rdac_138_accel_sign_runlength_var_8q_d2(revenue):
    a = _accel(revenue); sg = _sign_safe(a)
    flip = (sg != sg.shift(1)).astype(float)
    result = flip.rolling(8, min_periods=3).sum()
    return result.diff().diff()


def f29_rdac_139_accel_sign_entropy_proxy_5q_d2(revenue):
    a = _accel(revenue); p = (a > 0).astype(float).rolling(5, min_periods=2).mean()
    result = -(p * np.log(p.where(p > 0, np.nan)) + (1 - p) * np.log((1 - p).where(p < 1, np.nan))).fillna(0)
    return result.diff().diff()


def f29_rdac_140_accel_persistence_index_lag1_8q_d2(revenue):
    a = _accel(revenue)
    result = _safe_div((a * a.shift(1)).rolling(8, min_periods=3).sum(), (a ** 2).rolling(8, min_periods=3).sum())
    return result.diff().diff()


def f29_rdac_141_composite_crash_5_binaries_8q_d2(revenue):
    a = _accel(revenue); d = a.diff()
    b1 = _rolling_count(d < -0.05, 8); b2 = _rolling_count(a < -0.10, 8); b3 = _rolling_count(_rolling_zscore(a, 12) < -2, 8); b4 = _rolling_count(a == a.rolling(12, min_periods=4).min(), 8); b5 = _consec_true_streak(a < 0).astype(float).rolling(8, min_periods=2).max()
    result = b1.fillna(0) + b2.fillna(0) + b3.fillna(0) + b4.fillna(0) + b5.fillna(0)
    return result.diff().diff()


def f29_rdac_142_weighted_crash_score_z_clip_m3_8q_d2(revenue):
    z = _rolling_zscore(_accel(revenue), 8).clip(lower=-3.0, upper=0)
    result = -z.rolling(8, min_periods=3).sum()
    return result.diff().diff()


def f29_rdac_143_multi_horizon_crash_score_4_8_12_clip_m3_d2(revenue):
    a = _accel(revenue)
    z4 = _rolling_zscore(a, 4).clip(lower=-3, upper=0); z8 = _rolling_zscore(a, 8).clip(lower=-3, upper=0); z12 = _rolling_zscore(a, 12).clip(lower=-3, upper=0)
    result = -(z4 + z8 + z12)
    return result.diff().diff()


def f29_rdac_144_ewm_decay_crash_score_8q_neg_only_d2(revenue):
    a = _accel(revenue).clip(upper=0)
    result = -a.ewm(span=8, adjust=False, min_periods=3).mean()
    return result.diff().diff()


def f29_rdac_145_logit_crash_probability_proxy_d2(revenue):
    z = _rolling_zscore(_accel(revenue), 12)
    result = 1.0 / (1.0 + np.exp(z.clip(lower=-10, upper=10)))
    return result.diff().diff()


def f29_rdac_146_mahalanobis_distance_accel_slope_8q_d2(revenue):
    a = _accel(revenue); s = _rolling_slope(a, 8)
    za = _rolling_zscore(a, 12); zs = _rolling_zscore(s, 12)
    result = (za ** 2 + zs ** 2).pow(0.5)
    return result.diff().diff()


def f29_rdac_147_hotelling_t_accel_vol_8q_d2(revenue):
    a = _accel(revenue); v = a.rolling(4, min_periods=2).std()
    za = _rolling_zscore(a, 12); zv = _rolling_zscore(v, 12)
    result = za.abs() + zv.abs()
    return result.diff().diff()


def f29_rdac_148_yoy_terminal_distance_5y_proxy_d2(revenue):
    y = _yoy_pct(revenue); mn = y.rolling(20, min_periods=6).min(); mx = y.rolling(20, min_periods=6).max()
    result = _safe_div(y - mn, mx.abs())
    return result.diff().diff()


def f29_rdac_149_trend_velocity_collapse_4q_over_12q_d2(revenue):
    a = _accel(revenue); s4 = _rolling_slope(a, 4); s12 = _rolling_slope(a, 12)
    result = _safe_div(s4, s12.abs())
    return result.diff().diff()


def f29_rdac_150_all_cylinders_down_composite_8q_d2(revenue):
    a = _accel(revenue); d = a.diff()
    cliff = _rolling_count(d < -0.05, 8); nl = _rolling_count(a == a.rolling(12, min_periods=4).min(), 8); ns = _consec_true_streak(a < 0).astype(float).rolling(8, min_periods=2).max(); dd = (a.rolling(8, min_periods=3).max() - a)
    result = (cliff.fillna(0) / 4.0 + nl.fillna(0) / 4.0 + ns.fillna(0) / 4.0 + dd.fillna(0) / 0.10).where(a.notna(), np.nan)
    return result.diff().diff()


REVENUE_DECELERATION_ACCELERATION_D2_REGISTRY_076_150 = {
    "f29_rdac_076_sign_agreement_count_rev_gp_cogs_netinc_accel_d2": {"inputs": ["revenue", "gp", "cogs", "netinc"], "func": f29_rdac_076_sign_agreement_count_rev_gp_cogs_netinc_accel_d2},
    "f29_rdac_077_sign_agreement_count_sum_4q_d2": {"inputs": ["revenue", "gp", "cogs", "netinc"], "func": f29_rdac_077_sign_agreement_count_sum_4q_d2},
    "f29_rdac_078_cross_metric_corr_rev_netinc_accel_8q_d2": {"inputs": ["revenue", "netinc"], "func": f29_rdac_078_cross_metric_corr_rev_netinc_accel_8q_d2},
    "f29_rdac_079_worst_horizon_accel_z_signed_d2": {"inputs": ["revenue"], "func": f29_rdac_079_worst_horizon_accel_z_signed_d2},
    "f29_rdac_080_smoothed_raw_accel_sign_disagree_d2": {"inputs": ["revenue"], "func": f29_rdac_080_smoothed_raw_accel_sign_disagree_d2},
    "f29_rdac_081_ema4_accel_just_flipped_pos_to_neg_d2": {"inputs": ["revenue"], "func": f29_rdac_081_ema4_accel_just_flipped_pos_to_neg_d2},
    "f29_rdac_082_raw_pos_ema_neg_catchup_warning_d2": {"inputs": ["revenue"], "func": f29_rdac_082_raw_pos_ema_neg_catchup_warning_d2},
    "f29_rdac_083_raw_neg_ema_pos_false_alarm_filter_d2": {"inputs": ["revenue"], "func": f29_rdac_083_raw_neg_ema_pos_false_alarm_filter_d2},
    "f29_rdac_084_accel_residuals_skew_8q_d2": {"inputs": ["revenue"], "func": f29_rdac_084_accel_residuals_skew_8q_d2},
    "f29_rdac_085_accel_residuals_kurt_8q_d2": {"inputs": ["revenue"], "func": f29_rdac_085_accel_residuals_kurt_8q_d2},
    "f29_rdac_086_accel_ema_long_short_cross_sign_disagree_d2": {"inputs": ["revenue"], "func": f29_rdac_086_accel_ema_long_short_cross_sign_disagree_d2},
    "f29_rdac_087_accel_ema4_below_ema12_persistent_3q_d2": {"inputs": ["revenue"], "func": f29_rdac_087_accel_ema4_below_ema12_persistent_3q_d2},
    "f29_rdac_088_accel_2nd_diff_current_d2": {"inputs": ["revenue"], "func": f29_rdac_088_accel_2nd_diff_current_d2},
    "f29_rdac_089_accel_2nd_diff_zscore_8q_d2": {"inputs": ["revenue"], "func": f29_rdac_089_accel_2nd_diff_zscore_8q_d2},
    "f29_rdac_090_accel_2nd_diff_flip_pos_to_neg_d2": {"inputs": ["revenue"], "func": f29_rdac_090_accel_2nd_diff_flip_pos_to_neg_d2},
    "f29_rdac_091_accel_slope_sign_flip_pos_to_neg_d2": {"inputs": ["revenue"], "func": f29_rdac_091_accel_slope_sign_flip_pos_to_neg_d2},
    "f29_rdac_092_accel_slope_4q_d2": {"inputs": ["revenue"], "func": f29_rdac_092_accel_slope_4q_d2},
    "f29_rdac_093_accel_slope_8q_minus_4q_d2": {"inputs": ["revenue"], "func": f29_rdac_093_accel_slope_8q_minus_4q_d2},
    "f29_rdac_094_accel_dev_from_8q_median_d2": {"inputs": ["revenue"], "func": f29_rdac_094_accel_dev_from_8q_median_d2},
    "f29_rdac_095_accel_hampel_outlier_3mad_12q_d2": {"inputs": ["revenue"], "func": f29_rdac_095_accel_hampel_outlier_3mad_12q_d2},
    "f29_rdac_096_accel_hampel_positive_outlier_12q_d2": {"inputs": ["revenue"], "func": f29_rdac_096_accel_hampel_positive_outlier_12q_d2},
    "f29_rdac_097_accel_hampel_negative_outlier_12q_d2": {"inputs": ["revenue"], "func": f29_rdac_097_accel_hampel_negative_outlier_12q_d2},
    "f29_rdac_098_accel_rolling_rank_pct_16q_d2": {"inputs": ["revenue"], "func": f29_rdac_098_accel_rolling_rank_pct_16q_d2},
    "f29_rdac_099_accel_rolling_decile_20q_d2": {"inputs": ["revenue"], "func": f29_rdac_099_accel_rolling_decile_20q_d2},
    "f29_rdac_100_accel_extreme_recency_12q_d2": {"inputs": ["revenue"], "func": f29_rdac_100_accel_extreme_recency_12q_d2},
    "f29_rdac_101_yoy_pct_drawdown_from_8q_max_d2": {"inputs": ["revenue"], "func": f29_rdac_101_yoy_pct_drawdown_from_8q_max_d2},
    "f29_rdac_102_yoy_pct_drawdown_from_12q_max_d2": {"inputs": ["revenue"], "func": f29_rdac_102_yoy_pct_drawdown_from_12q_max_d2},
    "f29_rdac_103_yoy_pct_q_since_12q_max_d2": {"inputs": ["revenue"], "func": f29_rdac_103_yoy_pct_q_since_12q_max_d2},
    "f29_rdac_104_ttm_yoy_drawdown_from_8q_max_d2": {"inputs": ["revenue"], "func": f29_rdac_104_ttm_yoy_drawdown_from_8q_max_d2},
    "f29_rdac_105_yoy_drawdown_velocity_depth_per_duration_d2": {"inputs": ["revenue"], "func": f29_rdac_105_yoy_drawdown_velocity_depth_per_duration_d2},
    "f29_rdac_106_yoy_recovery_rate_from_8q_min_d2": {"inputs": ["revenue"], "func": f29_rdac_106_yoy_recovery_rate_from_8q_min_d2},
    "f29_rdac_107_accel_diff_neg_over_pos_mean_mag_8q_d2": {"inputs": ["revenue"], "func": f29_rdac_107_accel_diff_neg_over_pos_mean_mag_8q_d2},
    "f29_rdac_108_accel_pain_ratio_neg_sum_over_total_8q_d2": {"inputs": ["revenue"], "func": f29_rdac_108_accel_pain_ratio_neg_sum_over_total_8q_d2},
    "f29_rdac_109_yoy_pct_max_drawdown_16q_d2": {"inputs": ["revenue"], "func": f29_rdac_109_yoy_pct_max_drawdown_16q_d2},
    "f29_rdac_110_yoy_pct_q_since_16q_max_d2": {"inputs": ["revenue"], "func": f29_rdac_110_yoy_pct_q_since_16q_max_d2},
    "f29_rdac_111_accel_curve_signed_area_8q_d2": {"inputs": ["revenue"], "func": f29_rdac_111_accel_curve_signed_area_8q_d2},
    "f29_rdac_112_accel_ulcer_index_negative_dd_rms_8q_d2": {"inputs": ["revenue"], "func": f29_rdac_112_accel_ulcer_index_negative_dd_rms_8q_d2},
    "f29_rdac_113_accel_calmar_proxy_4q_mean_over_8q_dd_d2": {"inputs": ["revenue"], "func": f29_rdac_113_accel_calmar_proxy_4q_mean_over_8q_dd_d2},
    "f29_rdac_114_yoy_drawdown_event_count_5pct_12q_d2": {"inputs": ["revenue"], "func": f29_rdac_114_yoy_drawdown_event_count_5pct_12q_d2},
    "f29_rdac_115_yoy_recovery_failure_after_min_8q_d2": {"inputs": ["revenue"], "func": f29_rdac_115_yoy_recovery_failure_after_min_8q_d2},
    "f29_rdac_116_yoy_stairstep_down_new_min_count_8q_d2": {"inputs": ["revenue"], "func": f29_rdac_116_yoy_stairstep_down_new_min_count_8q_d2},
    "f29_rdac_117_accel_convex_chord_deviation_8q_d2": {"inputs": ["revenue"], "func": f29_rdac_117_accel_convex_chord_deviation_8q_d2},
    "f29_rdac_118_yoy_consecutive_decline_streak_d2": {"inputs": ["revenue"], "func": f29_rdac_118_yoy_consecutive_decline_streak_d2},
    "f29_rdac_119_composite_broken_down_score_8q_d2": {"inputs": ["revenue"], "func": f29_rdac_119_composite_broken_down_score_8q_d2},
    "f29_rdac_120_yoy_drawdown_acceleration_4q_d2": {"inputs": ["revenue"], "func": f29_rdac_120_yoy_drawdown_acceleration_4q_d2},
    "f29_rdac_121_accel_skew_8q_d2": {"inputs": ["revenue"], "func": f29_rdac_121_accel_skew_8q_d2},
    "f29_rdac_122_accel_skew_12q_d2": {"inputs": ["revenue"], "func": f29_rdac_122_accel_skew_12q_d2},
    "f29_rdac_123_accel_kurt_8q_d2": {"inputs": ["revenue"], "func": f29_rdac_123_accel_kurt_8q_d2},
    "f29_rdac_124_accel_kurt_12q_d2": {"inputs": ["revenue"], "func": f29_rdac_124_accel_kurt_12q_d2},
    "f29_rdac_125_accel_skew_change_8q_vs_12q_d2": {"inputs": ["revenue"], "func": f29_rdac_125_accel_skew_change_8q_vs_12q_d2},
    "f29_rdac_126_accel_kurt_change_8q_vs_12q_d2": {"inputs": ["revenue"], "func": f29_rdac_126_accel_kurt_change_8q_vs_12q_d2},
    "f29_rdac_127_accel_cv_8q_d2": {"inputs": ["revenue"], "func": f29_rdac_127_accel_cv_8q_d2},
    "f29_rdac_128_accel_cv_change_8q_vs_16q_d2": {"inputs": ["revenue"], "func": f29_rdac_128_accel_cv_change_8q_vs_16q_d2},
    "f29_rdac_129_accel_quantile_dispersion_q90_q10_12q_d2": {"inputs": ["revenue"], "func": f29_rdac_129_accel_quantile_dispersion_q90_q10_12q_d2},
    "f29_rdac_130_accel_neg_tail_4q_in_16q_q25_d2": {"inputs": ["revenue"], "func": f29_rdac_130_accel_neg_tail_4q_in_16q_q25_d2},
    "f29_rdac_131_accel_right_tail_collapse_q90_neg_8q_d2": {"inputs": ["revenue"], "func": f29_rdac_131_accel_right_tail_collapse_q90_neg_8q_d2},
    "f29_rdac_132_accel_median_z_signed_8q_d2": {"inputs": ["revenue"], "func": f29_rdac_132_accel_median_z_signed_8q_d2},
    "f29_rdac_133_accel_mean_minus_median_8q_d2": {"inputs": ["revenue"], "func": f29_rdac_133_accel_mean_minus_median_8q_d2},
    "f29_rdac_134_accel_trimmed_mean_8q_d2": {"inputs": ["revenue"], "func": f29_rdac_134_accel_trimmed_mean_8q_d2},
    "f29_rdac_135_accel_winsorized_z_10pct_8q_d2": {"inputs": ["revenue"], "func": f29_rdac_135_accel_winsorized_z_10pct_8q_d2},
    "f29_rdac_136_accel_range_over_abs_median_8q_d2": {"inputs": ["revenue"], "func": f29_rdac_136_accel_range_over_abs_median_8q_d2},
    "f29_rdac_137_accel_iqr_over_abs_median_8q_d2": {"inputs": ["revenue"], "func": f29_rdac_137_accel_iqr_over_abs_median_8q_d2},
    "f29_rdac_138_accel_sign_runlength_var_8q_d2": {"inputs": ["revenue"], "func": f29_rdac_138_accel_sign_runlength_var_8q_d2},
    "f29_rdac_139_accel_sign_entropy_proxy_5q_d2": {"inputs": ["revenue"], "func": f29_rdac_139_accel_sign_entropy_proxy_5q_d2},
    "f29_rdac_140_accel_persistence_index_lag1_8q_d2": {"inputs": ["revenue"], "func": f29_rdac_140_accel_persistence_index_lag1_8q_d2},
    "f29_rdac_141_composite_crash_5_binaries_8q_d2": {"inputs": ["revenue"], "func": f29_rdac_141_composite_crash_5_binaries_8q_d2},
    "f29_rdac_142_weighted_crash_score_z_clip_m3_8q_d2": {"inputs": ["revenue"], "func": f29_rdac_142_weighted_crash_score_z_clip_m3_8q_d2},
    "f29_rdac_143_multi_horizon_crash_score_4_8_12_clip_m3_d2": {"inputs": ["revenue"], "func": f29_rdac_143_multi_horizon_crash_score_4_8_12_clip_m3_d2},
    "f29_rdac_144_ewm_decay_crash_score_8q_neg_only_d2": {"inputs": ["revenue"], "func": f29_rdac_144_ewm_decay_crash_score_8q_neg_only_d2},
    "f29_rdac_145_logit_crash_probability_proxy_d2": {"inputs": ["revenue"], "func": f29_rdac_145_logit_crash_probability_proxy_d2},
    "f29_rdac_146_mahalanobis_distance_accel_slope_8q_d2": {"inputs": ["revenue"], "func": f29_rdac_146_mahalanobis_distance_accel_slope_8q_d2},
    "f29_rdac_147_hotelling_t_accel_vol_8q_d2": {"inputs": ["revenue"], "func": f29_rdac_147_hotelling_t_accel_vol_8q_d2},
    "f29_rdac_148_yoy_terminal_distance_5y_proxy_d2": {"inputs": ["revenue"], "func": f29_rdac_148_yoy_terminal_distance_5y_proxy_d2},
    "f29_rdac_149_trend_velocity_collapse_4q_over_12q_d2": {"inputs": ["revenue"], "func": f29_rdac_149_trend_velocity_collapse_4q_over_12q_d2},
    "f29_rdac_150_all_cylinders_down_composite_8q_d2": {"inputs": ["revenue"], "func": f29_rdac_150_all_cylinders_down_composite_8q_d2},
}
