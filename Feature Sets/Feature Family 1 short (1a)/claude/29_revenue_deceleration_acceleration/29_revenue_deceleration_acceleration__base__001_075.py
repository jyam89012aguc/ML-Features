"""revenue_deceleration_acceleration base features 001_075 — Pipeline 1a-inverse short-side blowup family.

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


def f29_rdac_001_yoy_accel_zscore_8q(revenue):
    result = _rolling_zscore(_accel(revenue), 8)
    return result


def f29_rdac_002_yoy_accel_zscore_12q(revenue):
    result = _rolling_zscore(_accel(revenue), 12)
    return result


def f29_rdac_003_ttm_yoy_accel_zscore_12q(revenue):
    result = _rolling_zscore(_ttm_accel(revenue), 12)
    return result


def f29_rdac_004_qoq_accel_zscore_8q(revenue):
    result = _rolling_zscore(_qaccel(revenue), 8)
    return result


def f29_rdac_005_yoy_accel_below_minus_2sd_8q(revenue):
    z = _rolling_zscore(_accel(revenue), 8)
    result = (z < -2.0).astype(float).where(z.notna(), np.nan)
    return result


def f29_rdac_006_yoy_accel_jump_magnitude_vs_8q_mad(revenue):
    a = _accel(revenue)
    mad = _rolling_mad(a, 8)
    result = _safe_div(a.abs(), mad)
    return result


def f29_rdac_007_yoy_accel_drop_from_8q_max(revenue):
    a = _accel(revenue)
    result = a - a.rolling(8, min_periods=3).max()
    return result


def f29_rdac_008_qoq_accel_drop_from_8q_max(revenue):
    a = _qaccel(revenue)
    result = a - a.rolling(8, min_periods=3).max()
    return result


def f29_rdac_009_yoy_accel_in_worst_quartile_12q(revenue):
    a = _accel(revenue)
    q25 = _rolling_quantile(a, 12, 0.25)
    result = (a <= q25).astype(float).where(a.notna(), np.nan)
    return result


def f29_rdac_010_yoy_accel_range_position_8q(revenue):
    a = _accel(revenue)
    mn = a.rolling(8, min_periods=3).min(); mx = a.rolling(8, min_periods=3).max()
    result = _safe_div(a - mn, mx - mn)
    return result


def f29_rdac_011_yoy_accel_sudden_drop_vs_8q_mad(revenue):
    a = _accel(revenue); d = a.diff()
    mad = _rolling_mad(d, 8)
    result = (d < -1.5 * mad).astype(float).where(d.notna() & mad.notna(), np.nan)
    return result


def f29_rdac_012_yoy_accel_one_q_cliff_10pp(revenue):
    d = _accel(revenue).diff()
    result = (d < -0.10).astype(float).where(d.notna(), np.nan)
    return result


def f29_rdac_013_qoq_accel_one_q_cliff_5pp(revenue):
    d = _qaccel(revenue).diff()
    result = (d < -0.05).astype(float).where(d.notna(), np.nan)
    return result


def f29_rdac_014_yoy_accel_cliff_count_4q(revenue):
    d = _accel(revenue).diff()
    result = _rolling_count(d < -0.05, 4)
    return result


def f29_rdac_015_yoy_accel_cliff_count_8q(revenue):
    d = _accel(revenue).diff()
    result = _rolling_count(d < -0.05, 8)
    return result


def f29_rdac_016_yoy_accel_cliff_streak(revenue):
    a = _accel(revenue)
    result = _consec_true_streak(a < -0.05).astype(float)
    return result


def f29_rdac_017_yoy_accel_down_up_asymmetry_8q(revenue):
    d = _accel(revenue).diff()
    neg = d.where(d < 0).rolling(8, min_periods=2).mean()
    pos = d.where(d > 0).rolling(8, min_periods=2).mean()
    result = _safe_div(neg.abs(), pos.abs())
    return result


def f29_rdac_018_yoy_accel_hard_floor_breach_m25pp_8q(revenue):
    a = _accel(revenue)
    result = _rolling_count(a < -0.25, 8)
    return result


def f29_rdac_019_yoy_accel_hard_floor_breach_m15pp_8q(revenue):
    a = _accel(revenue)
    result = _rolling_count(a < -0.15, 8)
    return result


def f29_rdac_020_yoy_accel_strictly_decreasing_streak(revenue):
    a = _accel(revenue)
    b = (a < a.shift(1)) & (a.shift(1) < a.shift(2))
    result = _consec_true_streak(b).astype(float)
    return result


def f29_rdac_021_yoy_accel_slope_4q_sign_flip(revenue):
    sl = _rolling_slope(_accel(revenue), 4)
    result = (_sign_safe(sl) != _sign_safe(sl.shift(1))).astype(float).where(sl.notna() & sl.shift(1).notna(), np.nan)
    return result


def f29_rdac_022_yoy_accel_ema4_sign_flip_pos_to_neg(revenue):
    em = _ema(_accel(revenue), 4)
    result = ((em < 0) & (em.shift(1) >= 0)).astype(float).where(em.notna() & em.shift(1).notna(), np.nan)
    return result


def f29_rdac_023_yoy_accel_inflection_magnitude_8q(revenue):
    a = _accel(revenue)
    sd = a.rolling(12, min_periods=4).std()
    result = _safe_div((a - a.shift(8)).abs(), sd)
    return result


def f29_rdac_024_yoy_accel_mean_shift_z_4v12(revenue):
    a = _accel(revenue)
    m4 = a.rolling(4, min_periods=2).mean(); m12 = a.rolling(12, min_periods=4).mean(); s12 = a.rolling(12, min_periods=4).std()
    result = _safe_div(m4 - m12, s12)
    return result


def f29_rdac_025_yoy_accel_mean_shift_down_indicator(revenue):
    a = _accel(revenue)
    m4 = a.rolling(4, min_periods=2).mean(); m12 = a.rolling(12, min_periods=4).mean(); s12 = a.rolling(12, min_periods=4).std()
    z = _safe_div(m4 - m12, s12)
    result = (z < -1.0).astype(float).where(z.notna(), np.nan)
    return result


def f29_rdac_026_yoy_accel_variance_ratio_4q_12q(revenue):
    a = _accel(revenue)
    v4 = a.rolling(4, min_periods=2).var(); v12 = a.rolling(12, min_periods=4).var()
    result = _safe_div(v4, v12)
    return result


def f29_rdac_027_yoy_accel_variance_ratio_zscore_16q(revenue):
    a = _accel(revenue)
    vr = _safe_div(a.rolling(4, min_periods=2).var(), a.rolling(12, min_periods=4).var())
    result = _rolling_zscore(vr, 16)
    return result


def f29_rdac_028_yoy_accel_var_shift_up_indicator(revenue):
    a = _accel(revenue)
    vr = _safe_div(a.rolling(4, min_periods=2).var(), a.rolling(12, min_periods=4).var())
    result = (vr > 2.0).astype(float).where(vr.notna(), np.nan)
    return result


def f29_rdac_029_yoy_accel_max_mean_shift_recency_12q(revenue):
    a = _accel(revenue)
    diffs = pd.concat([(a.rolling(k, min_periods=2).mean() - a.rolling(12 - k, min_periods=2).mean().shift(k)).rename(k) for k in range(2, 11)], axis=1)
    result = diffs.abs().idxmax(axis=1).where(a.notna(), np.nan).astype(float)
    return result


def f29_rdac_030_yoy_accel_regime_stickiness_bad_quartile_4q_in_20q(revenue):
    a = _accel(revenue)
    q25 = _rolling_quantile(a, 20, 0.25)
    result = _rolling_frac(a <= q25, 4)
    return result


def f29_rdac_031_yoy_accel_new_low_12q_indicator(revenue):
    a = _accel(revenue)
    result = (a == a.rolling(12, min_periods=4).min()).astype(float).where(a.notna(), np.nan)
    return result


def f29_rdac_032_yoy_accel_and_yoy_compound_new_low_12q(revenue):
    a = _accel(revenue); y = _yoy_pct(revenue)
    al = (a == a.rolling(12, min_periods=4).min()); yl = (y == y.rolling(12, min_periods=4).min())
    result = (al & yl).astype(float).where(a.notna() & y.notna(), np.nan)
    return result


def f29_rdac_033_yoy_accel_chow_like_fstat_mid_12q(revenue):
    a = _accel(revenue)
    m1 = a.rolling(6, min_periods=3).mean().shift(6); m2 = a.rolling(6, min_periods=3).mean()
    s12 = a.rolling(12, min_periods=4).std()
    result = _safe_div((m1 - m2).abs(), s12)
    return result


def f29_rdac_034_yoy_accel_max_split_diff_recency_12q(revenue):
    a = _accel(revenue)
    diffs = pd.concat([(a.rolling(k, min_periods=2).mean().shift(12 - k) - a.rolling(12 - k, min_periods=2).mean()).abs().rename(k) for k in range(3, 10)], axis=1)
    result = diffs.idxmax(axis=1).where(a.notna(), np.nan).astype(float)
    return result


def f29_rdac_035_yoy_accel_local_concavity_sign(revenue):
    a = _accel(revenue)
    result = _sign_safe(a.diff().diff())
    return result


def f29_rdac_036_yoy_accel_convexity_flip_pos_to_neg(revenue):
    c = _accel(revenue).diff().diff()
    result = ((c < 0) & (c.shift(1) >= 0)).astype(float).where(c.notna() & c.shift(1).notna(), np.nan)
    return result


def f29_rdac_037_yoy_accel_convexity_flip_neg_to_pos(revenue):
    c = _accel(revenue).diff().diff()
    result = ((c > 0) & (c.shift(1) <= 0)).astype(float).where(c.notna() & c.shift(1).notna(), np.nan)
    return result


def f29_rdac_038_yoy_accel_phase_shift_4q_vs_12q_norm(revenue):
    a = _accel(revenue)
    m4 = a.rolling(4, min_periods=2).mean(); m12 = a.rolling(12, min_periods=4).mean()
    result = _safe_div(m4 - m12, m12.abs())
    return result


def f29_rdac_039_yoy_accel_ar1_persistence_8q(revenue):
    a = _accel(revenue)
    result = a.rolling(8, min_periods=4).corr(a.shift(1))
    return result


def f29_rdac_040_yoy_accel_persistence_collapse_4q(revenue):
    a = _accel(revenue); ar = a.rolling(8, min_periods=4).corr(a.shift(1))
    result = ((ar < 0) & (ar.shift(4) > 0.5)).astype(float).where(ar.notna() & ar.shift(4).notna(), np.nan)
    return result


def f29_rdac_041_yoy_accel_chow_fstat_proxy_12q(revenue):
    a = _accel(revenue)
    m_all = a.rolling(12, min_periods=4).mean(); s_all = a.rolling(12, min_periods=4).std()
    m1 = a.rolling(6, min_periods=2).mean().shift(6); m2 = a.rolling(6, min_periods=2).mean()
    result = _safe_div((m1 - m_all) ** 2 + (m2 - m_all) ** 2, s_all ** 2)
    return result


def f29_rdac_042_yoy_accel_cusum_max_excursion_12q(revenue):
    a = _accel(revenue); m = a.rolling(12, min_periods=4).mean()
    dev = (a - m).rolling(12, min_periods=4).apply(lambda w: np.nanmax(np.cumsum(w)) if not np.isnan(w).all() else np.nan, raw=True)
    result = dev
    return result


def f29_rdac_043_yoy_accel_cusum_min_excursion_12q(revenue):
    a = _accel(revenue); m = a.rolling(12, min_periods=4).mean()
    dev = (a - m).rolling(12, min_periods=4).apply(lambda w: np.nanmin(np.cumsum(w)) if not np.isnan(w).all() else np.nan, raw=True)
    result = dev
    return result


def f29_rdac_044_yoy_accel_cusum_z_12q(revenue):
    a = _accel(revenue); m = a.rolling(12, min_periods=4).mean(); s = a.rolling(12, min_periods=4).std()
    cu = (a - m).rolling(12, min_periods=4).apply(lambda w: np.nanmax(np.abs(np.cumsum(w))) if not np.isnan(w).all() else np.nan, raw=True)
    result = _safe_div(cu, s)
    return result


def f29_rdac_045_yoy_accel_max_abs_residual_recency_8q(revenue):
    a = _accel(revenue); m = a.rolling(8, min_periods=3).mean(); r = (a - m).abs()
    result = r.rolling(8, min_periods=3).apply(lambda w: float(len(w) - 1 - int(np.nanargmax(w))) if not np.isnan(w).all() else np.nan, raw=True)
    return result


def f29_rdac_046_yoy_accel_breakpoint_count_16q(revenue):
    a = _accel(revenue); d = a.diff(); s = d.rolling(16, min_periods=5).std()
    result = _rolling_count(d.abs() > 2.0 * s, 16)
    return result


def f29_rdac_047_yoy_accel_likelihood_break_proxy_12q(revenue):
    a = _accel(revenue)
    m1 = a.rolling(6, min_periods=2).mean().shift(6); m2 = a.rolling(6, min_periods=2).mean()
    s1 = a.rolling(6, min_periods=2).std().shift(6); s2 = a.rolling(6, min_periods=2).std()
    result = _safe_div((m1 - m2) ** 2, (s1 ** 2 + s2 ** 2))
    return result


def f29_rdac_048_yoy_accel_break_recency_max_fstat_12q(revenue):
    a = _accel(revenue)
    fs = pd.concat([_safe_div((a.rolling(k, min_periods=2).mean().shift(12 - k) - a.rolling(12 - k, min_periods=2).mean()) ** 2, a.rolling(12, min_periods=4).var()).rename(k) for k in range(3, 10)], axis=1)
    result = fs.idxmax(axis=1).where(a.notna(), np.nan).astype(float)
    return result


def f29_rdac_049_yoy_accel_var_ratio_test_zscore_20q(revenue):
    a = _accel(revenue)
    vr = _safe_div(a.rolling(4, min_periods=2).var(), a.rolling(12, min_periods=4).var())
    result = _rolling_zscore(vr - 1.0, 20)
    return result


def f29_rdac_050_yoy_accel_var_regime_up_significance_12q(revenue):
    a = _accel(revenue)
    v1 = a.rolling(6, min_periods=2).var().shift(6); v2 = a.rolling(6, min_periods=2).var()
    result = _safe_div(v2 - v1, v1.abs())
    return result


def f29_rdac_051_yoy_accel_var_regime_down_significance_12q(revenue):
    a = _accel(revenue)
    v1 = a.rolling(6, min_periods=2).var().shift(6); v2 = a.rolling(6, min_periods=2).var()
    result = _safe_div(v1 - v2, v1.abs())
    return result


def f29_rdac_052_yoy_accel_mean_diff_t_stat_12q(revenue):
    a = _accel(revenue)
    m1 = a.rolling(6, min_periods=3).mean().shift(6); m2 = a.rolling(6, min_periods=3).mean()
    s1 = a.rolling(6, min_periods=3).std().shift(6); s2 = a.rolling(6, min_periods=3).std()
    se = ((s1 ** 2 + s2 ** 2) / 6.0).pow(0.5)
    result = _safe_div(m2 - m1, se)
    return result


def f29_rdac_053_yoy_accel_mean_t_signif_down(revenue):
    a = _accel(revenue)
    m1 = a.rolling(6, min_periods=3).mean().shift(6); m2 = a.rolling(6, min_periods=3).mean()
    s1 = a.rolling(6, min_periods=3).std().shift(6); s2 = a.rolling(6, min_periods=3).std()
    se = ((s1 ** 2 + s2 ** 2) / 6.0).pow(0.5)
    t = _safe_div(m2 - m1, se)
    result = (t < -2.0).astype(float).where(t.notna(), np.nan)
    return result


def f29_rdac_054_yoy_accel_mean_t_signif_up(revenue):
    a = _accel(revenue)
    m1 = a.rolling(6, min_periods=3).mean().shift(6); m2 = a.rolling(6, min_periods=3).mean()
    s1 = a.rolling(6, min_periods=3).std().shift(6); s2 = a.rolling(6, min_periods=3).std()
    se = ((s1 ** 2 + s2 ** 2) / 6.0).pow(0.5)
    t = _safe_div(m2 - m1, se)
    result = (t > 2.0).astype(float).where(t.notna(), np.nan)
    return result


def f29_rdac_055_yoy_accel_ks_style_cdf_shift_16q(revenue):
    a = _accel(revenue)
    med1 = a.rolling(8, min_periods=3).median().shift(8); med2 = a.rolling(8, min_periods=3).median()
    iqr = (a.rolling(16, min_periods=5).quantile(0.75) - a.rolling(16, min_periods=5).quantile(0.25))
    result = _safe_div((med2 - med1).abs(), iqr)
    return result


def f29_rdac_056_yoy_accel_median_break_4q_vs_16q(revenue):
    a = _accel(revenue)
    result = a.rolling(4, min_periods=2).median() - a.rolling(16, min_periods=5).median()
    return result


def f29_rdac_057_yoy_accel_resid_var_jump_4q_vs_16q(revenue):
    a = _accel(revenue); m4 = a.rolling(4, min_periods=2).mean(); m16 = a.rolling(16, min_periods=5).mean()
    r4 = (a - m4) ** 2; r16 = (a - m16) ** 2
    result = _safe_div(r4.rolling(4, min_periods=2).mean(), r16.rolling(16, min_periods=5).mean())
    return result


def f29_rdac_058_yoy_accel_regression_intercept_break_4q_vs_12q(revenue):
    a = _accel(revenue)
    sl4 = _rolling_slope(a, 4); sl12 = _rolling_slope(a, 12)
    m4 = a.rolling(4, min_periods=2).mean(); m12 = a.rolling(12, min_periods=4).mean()
    ic4 = m4 - sl4 * 1.5; ic12 = m12 - sl12 * 5.5
    result = ic4 - ic12
    return result


def f29_rdac_059_yoy_accel_regression_slope_break_4q_vs_12q(revenue):
    a = _accel(revenue)
    result = _rolling_slope(a, 4) - _rolling_slope(a, 12)
    return result


def f29_rdac_060_yoy_accel_combined_break_composite_8q(revenue):
    a = _accel(revenue); d = a.diff(); s = d.rolling(8, min_periods=3).std()
    cliff = _rolling_count(d < -0.05, 8)
    jump = _rolling_count(d.abs() > 2.0 * s, 8)
    newlow = _rolling_count(a == a.rolling(12, min_periods=4).min(), 8)
    result = (cliff.fillna(0) + jump.fillna(0) + newlow.fillna(0)).where(a.notna(), np.nan)
    return result


def f29_rdac_061_rev_gp_accel_both_worst_quartile_12q(revenue, gp):
    ar = _accel(revenue); ag = _accel(gp)
    qr = _rolling_quantile(ar, 12, 0.25); qg = _rolling_quantile(ag, 12, 0.25)
    result = ((ar <= qr) & (ag <= qg)).astype(float).where(ar.notna() & ag.notna(), np.nan)
    return result


def f29_rdac_062_rev_cogs_accel_both_z_below_m15_8q(revenue, cogs):
    zr = _rolling_zscore(_accel(revenue), 8); zc = _rolling_zscore(_accel(cogs), 8)
    result = ((zr < -1.5) & (zc < -1.5)).astype(float).where(zr.notna() & zc.notna(), np.nan)
    return result


def f29_rdac_063_rev_netinc_accel_co_decline_indicator(revenue, netinc):
    ar = _accel(revenue); an = _accel(netinc)
    result = ((ar < 0) & (an < 0)).astype(float).where(ar.notna() & an.notna(), np.nan)
    return result


def f29_rdac_064_triple_rev_cogs_netinc_accel_decline_indicator(revenue, cogs, netinc):
    ar = _accel(revenue); ac = _accel(cogs); an = _accel(netinc)
    result = ((ar < 0) & (ac < 0) & (an < 0)).astype(float).where(ar.notna() & ac.notna() & an.notna(), np.nan)
    return result


def f29_rdac_065_rev_netinc_co_decline_streak(revenue, netinc):
    ar = _accel(revenue); an = _accel(netinc)
    result = _consec_true_streak((ar < 0) & (an < 0)).astype(float)
    return result


def f29_rdac_066_rev_netinc_co_decline_fraction_8q(revenue, netinc):
    ar = _accel(revenue); an = _accel(netinc)
    result = _rolling_frac((ar < 0) & (an < 0), 8)
    return result


def f29_rdac_067_composite_accel_zavg_rev_gp_netinc_8q(revenue, gp, netinc):
    zr = _rolling_zscore(_accel(revenue), 8); zg = _rolling_zscore(_accel(gp), 8); zn = _rolling_zscore(_accel(netinc), 8)
    result = pd.concat([zr, zg, zn], axis=1).mean(axis=1)
    return result


def f29_rdac_068_composite_accel_abs_z_rev_gp_netinc_8q(revenue, gp, netinc):
    zr = _rolling_zscore(_accel(revenue), 8); zg = _rolling_zscore(_accel(gp), 8); zn = _rolling_zscore(_accel(netinc), 8)
    result = pd.concat([zr.abs(), zg.abs(), zn.abs()], axis=1).mean(axis=1)
    return result


def f29_rdac_069_dispersion_accel_z_rev_gp_netinc_8q(revenue, gp, netinc):
    zr = _rolling_zscore(_accel(revenue), 8); zg = _rolling_zscore(_accel(gp), 8); zn = _rolling_zscore(_accel(netinc), 8)
    result = pd.concat([zr, zg, zn], axis=1).std(axis=1)
    return result


def f29_rdac_070_rev_minus_netinc_accel_z_gap_8q(revenue, netinc):
    zr = _rolling_zscore(_accel(revenue), 8); zn = _rolling_zscore(_accel(netinc), 8)
    result = zr - zn
    return result


def f29_rdac_071_quality_deterioration_rev_up_netinc_down(revenue, netinc):
    zr = _rolling_zscore(_accel(revenue), 8); zn = _rolling_zscore(_accel(netinc), 8)
    result = ((zr > 0) & (zn < -1.0)).astype(float).where(zr.notna() & zn.notna(), np.nan)
    return result


def f29_rdac_072_cogs_yoy_pos_rev_yoy_neg_margin_death(revenue, cogs):
    yr = _yoy_pct(revenue); yc = _yoy_pct(cogs)
    result = ((yc > 0) & (yr < 0)).astype(float).where(yr.notna() & yc.notna(), np.nan)
    return result


def f29_rdac_073_rev_yoy_ttm_accel_both_neg_indicator(revenue):
    a1 = _accel(revenue); a2 = _ttm_accel(revenue)
    result = ((a1 < 0) & (a2 < 0)).astype(float).where(a1.notna() & a2.notna(), np.nan)
    return result


def f29_rdac_074_rev_yoy_qoq_accel_both_worst_quartile_12q(revenue):
    ay = _accel(revenue); aq = _qaccel(revenue)
    qy = _rolling_quantile(ay, 12, 0.25); qq = _rolling_quantile(aq, 12, 0.25)
    result = ((ay <= qy) & (aq <= qq)).astype(float).where(ay.notna() & aq.notna(), np.nan)
    return result


def f29_rdac_075_rev_x_netinc_accel_z_interaction_8q(revenue, netinc):
    zr = _rolling_zscore(_accel(revenue), 8); zn = _rolling_zscore(_accel(netinc), 8)
    result = zr * zn
    return result


REVENUE_DECELERATION_ACCELERATION_BASE_REGISTRY_001_075 = {
    "f29_rdac_001_yoy_accel_zscore_8q": {"inputs": ["revenue"], "func": f29_rdac_001_yoy_accel_zscore_8q},
    "f29_rdac_002_yoy_accel_zscore_12q": {"inputs": ["revenue"], "func": f29_rdac_002_yoy_accel_zscore_12q},
    "f29_rdac_003_ttm_yoy_accel_zscore_12q": {"inputs": ["revenue"], "func": f29_rdac_003_ttm_yoy_accel_zscore_12q},
    "f29_rdac_004_qoq_accel_zscore_8q": {"inputs": ["revenue"], "func": f29_rdac_004_qoq_accel_zscore_8q},
    "f29_rdac_005_yoy_accel_below_minus_2sd_8q": {"inputs": ["revenue"], "func": f29_rdac_005_yoy_accel_below_minus_2sd_8q},
    "f29_rdac_006_yoy_accel_jump_magnitude_vs_8q_mad": {"inputs": ["revenue"], "func": f29_rdac_006_yoy_accel_jump_magnitude_vs_8q_mad},
    "f29_rdac_007_yoy_accel_drop_from_8q_max": {"inputs": ["revenue"], "func": f29_rdac_007_yoy_accel_drop_from_8q_max},
    "f29_rdac_008_qoq_accel_drop_from_8q_max": {"inputs": ["revenue"], "func": f29_rdac_008_qoq_accel_drop_from_8q_max},
    "f29_rdac_009_yoy_accel_in_worst_quartile_12q": {"inputs": ["revenue"], "func": f29_rdac_009_yoy_accel_in_worst_quartile_12q},
    "f29_rdac_010_yoy_accel_range_position_8q": {"inputs": ["revenue"], "func": f29_rdac_010_yoy_accel_range_position_8q},
    "f29_rdac_011_yoy_accel_sudden_drop_vs_8q_mad": {"inputs": ["revenue"], "func": f29_rdac_011_yoy_accel_sudden_drop_vs_8q_mad},
    "f29_rdac_012_yoy_accel_one_q_cliff_10pp": {"inputs": ["revenue"], "func": f29_rdac_012_yoy_accel_one_q_cliff_10pp},
    "f29_rdac_013_qoq_accel_one_q_cliff_5pp": {"inputs": ["revenue"], "func": f29_rdac_013_qoq_accel_one_q_cliff_5pp},
    "f29_rdac_014_yoy_accel_cliff_count_4q": {"inputs": ["revenue"], "func": f29_rdac_014_yoy_accel_cliff_count_4q},
    "f29_rdac_015_yoy_accel_cliff_count_8q": {"inputs": ["revenue"], "func": f29_rdac_015_yoy_accel_cliff_count_8q},
    "f29_rdac_016_yoy_accel_cliff_streak": {"inputs": ["revenue"], "func": f29_rdac_016_yoy_accel_cliff_streak},
    "f29_rdac_017_yoy_accel_down_up_asymmetry_8q": {"inputs": ["revenue"], "func": f29_rdac_017_yoy_accel_down_up_asymmetry_8q},
    "f29_rdac_018_yoy_accel_hard_floor_breach_m25pp_8q": {"inputs": ["revenue"], "func": f29_rdac_018_yoy_accel_hard_floor_breach_m25pp_8q},
    "f29_rdac_019_yoy_accel_hard_floor_breach_m15pp_8q": {"inputs": ["revenue"], "func": f29_rdac_019_yoy_accel_hard_floor_breach_m15pp_8q},
    "f29_rdac_020_yoy_accel_strictly_decreasing_streak": {"inputs": ["revenue"], "func": f29_rdac_020_yoy_accel_strictly_decreasing_streak},
    "f29_rdac_021_yoy_accel_slope_4q_sign_flip": {"inputs": ["revenue"], "func": f29_rdac_021_yoy_accel_slope_4q_sign_flip},
    "f29_rdac_022_yoy_accel_ema4_sign_flip_pos_to_neg": {"inputs": ["revenue"], "func": f29_rdac_022_yoy_accel_ema4_sign_flip_pos_to_neg},
    "f29_rdac_023_yoy_accel_inflection_magnitude_8q": {"inputs": ["revenue"], "func": f29_rdac_023_yoy_accel_inflection_magnitude_8q},
    "f29_rdac_024_yoy_accel_mean_shift_z_4v12": {"inputs": ["revenue"], "func": f29_rdac_024_yoy_accel_mean_shift_z_4v12},
    "f29_rdac_025_yoy_accel_mean_shift_down_indicator": {"inputs": ["revenue"], "func": f29_rdac_025_yoy_accel_mean_shift_down_indicator},
    "f29_rdac_026_yoy_accel_variance_ratio_4q_12q": {"inputs": ["revenue"], "func": f29_rdac_026_yoy_accel_variance_ratio_4q_12q},
    "f29_rdac_027_yoy_accel_variance_ratio_zscore_16q": {"inputs": ["revenue"], "func": f29_rdac_027_yoy_accel_variance_ratio_zscore_16q},
    "f29_rdac_028_yoy_accel_var_shift_up_indicator": {"inputs": ["revenue"], "func": f29_rdac_028_yoy_accel_var_shift_up_indicator},
    "f29_rdac_029_yoy_accel_max_mean_shift_recency_12q": {"inputs": ["revenue"], "func": f29_rdac_029_yoy_accel_max_mean_shift_recency_12q},
    "f29_rdac_030_yoy_accel_regime_stickiness_bad_quartile_4q_in_20q": {"inputs": ["revenue"], "func": f29_rdac_030_yoy_accel_regime_stickiness_bad_quartile_4q_in_20q},
    "f29_rdac_031_yoy_accel_new_low_12q_indicator": {"inputs": ["revenue"], "func": f29_rdac_031_yoy_accel_new_low_12q_indicator},
    "f29_rdac_032_yoy_accel_and_yoy_compound_new_low_12q": {"inputs": ["revenue"], "func": f29_rdac_032_yoy_accel_and_yoy_compound_new_low_12q},
    "f29_rdac_033_yoy_accel_chow_like_fstat_mid_12q": {"inputs": ["revenue"], "func": f29_rdac_033_yoy_accel_chow_like_fstat_mid_12q},
    "f29_rdac_034_yoy_accel_max_split_diff_recency_12q": {"inputs": ["revenue"], "func": f29_rdac_034_yoy_accel_max_split_diff_recency_12q},
    "f29_rdac_035_yoy_accel_local_concavity_sign": {"inputs": ["revenue"], "func": f29_rdac_035_yoy_accel_local_concavity_sign},
    "f29_rdac_036_yoy_accel_convexity_flip_pos_to_neg": {"inputs": ["revenue"], "func": f29_rdac_036_yoy_accel_convexity_flip_pos_to_neg},
    "f29_rdac_037_yoy_accel_convexity_flip_neg_to_pos": {"inputs": ["revenue"], "func": f29_rdac_037_yoy_accel_convexity_flip_neg_to_pos},
    "f29_rdac_038_yoy_accel_phase_shift_4q_vs_12q_norm": {"inputs": ["revenue"], "func": f29_rdac_038_yoy_accel_phase_shift_4q_vs_12q_norm},
    "f29_rdac_039_yoy_accel_ar1_persistence_8q": {"inputs": ["revenue"], "func": f29_rdac_039_yoy_accel_ar1_persistence_8q},
    "f29_rdac_040_yoy_accel_persistence_collapse_4q": {"inputs": ["revenue"], "func": f29_rdac_040_yoy_accel_persistence_collapse_4q},
    "f29_rdac_041_yoy_accel_chow_fstat_proxy_12q": {"inputs": ["revenue"], "func": f29_rdac_041_yoy_accel_chow_fstat_proxy_12q},
    "f29_rdac_042_yoy_accel_cusum_max_excursion_12q": {"inputs": ["revenue"], "func": f29_rdac_042_yoy_accel_cusum_max_excursion_12q},
    "f29_rdac_043_yoy_accel_cusum_min_excursion_12q": {"inputs": ["revenue"], "func": f29_rdac_043_yoy_accel_cusum_min_excursion_12q},
    "f29_rdac_044_yoy_accel_cusum_z_12q": {"inputs": ["revenue"], "func": f29_rdac_044_yoy_accel_cusum_z_12q},
    "f29_rdac_045_yoy_accel_max_abs_residual_recency_8q": {"inputs": ["revenue"], "func": f29_rdac_045_yoy_accel_max_abs_residual_recency_8q},
    "f29_rdac_046_yoy_accel_breakpoint_count_16q": {"inputs": ["revenue"], "func": f29_rdac_046_yoy_accel_breakpoint_count_16q},
    "f29_rdac_047_yoy_accel_likelihood_break_proxy_12q": {"inputs": ["revenue"], "func": f29_rdac_047_yoy_accel_likelihood_break_proxy_12q},
    "f29_rdac_048_yoy_accel_break_recency_max_fstat_12q": {"inputs": ["revenue"], "func": f29_rdac_048_yoy_accel_break_recency_max_fstat_12q},
    "f29_rdac_049_yoy_accel_var_ratio_test_zscore_20q": {"inputs": ["revenue"], "func": f29_rdac_049_yoy_accel_var_ratio_test_zscore_20q},
    "f29_rdac_050_yoy_accel_var_regime_up_significance_12q": {"inputs": ["revenue"], "func": f29_rdac_050_yoy_accel_var_regime_up_significance_12q},
    "f29_rdac_051_yoy_accel_var_regime_down_significance_12q": {"inputs": ["revenue"], "func": f29_rdac_051_yoy_accel_var_regime_down_significance_12q},
    "f29_rdac_052_yoy_accel_mean_diff_t_stat_12q": {"inputs": ["revenue"], "func": f29_rdac_052_yoy_accel_mean_diff_t_stat_12q},
    "f29_rdac_053_yoy_accel_mean_t_signif_down": {"inputs": ["revenue"], "func": f29_rdac_053_yoy_accel_mean_t_signif_down},
    "f29_rdac_054_yoy_accel_mean_t_signif_up": {"inputs": ["revenue"], "func": f29_rdac_054_yoy_accel_mean_t_signif_up},
    "f29_rdac_055_yoy_accel_ks_style_cdf_shift_16q": {"inputs": ["revenue"], "func": f29_rdac_055_yoy_accel_ks_style_cdf_shift_16q},
    "f29_rdac_056_yoy_accel_median_break_4q_vs_16q": {"inputs": ["revenue"], "func": f29_rdac_056_yoy_accel_median_break_4q_vs_16q},
    "f29_rdac_057_yoy_accel_resid_var_jump_4q_vs_16q": {"inputs": ["revenue"], "func": f29_rdac_057_yoy_accel_resid_var_jump_4q_vs_16q},
    "f29_rdac_058_yoy_accel_regression_intercept_break_4q_vs_12q": {"inputs": ["revenue"], "func": f29_rdac_058_yoy_accel_regression_intercept_break_4q_vs_12q},
    "f29_rdac_059_yoy_accel_regression_slope_break_4q_vs_12q": {"inputs": ["revenue"], "func": f29_rdac_059_yoy_accel_regression_slope_break_4q_vs_12q},
    "f29_rdac_060_yoy_accel_combined_break_composite_8q": {"inputs": ["revenue"], "func": f29_rdac_060_yoy_accel_combined_break_composite_8q},
    "f29_rdac_061_rev_gp_accel_both_worst_quartile_12q": {"inputs": ["revenue", "gp"], "func": f29_rdac_061_rev_gp_accel_both_worst_quartile_12q},
    "f29_rdac_062_rev_cogs_accel_both_z_below_m15_8q": {"inputs": ["revenue", "cogs"], "func": f29_rdac_062_rev_cogs_accel_both_z_below_m15_8q},
    "f29_rdac_063_rev_netinc_accel_co_decline_indicator": {"inputs": ["revenue", "netinc"], "func": f29_rdac_063_rev_netinc_accel_co_decline_indicator},
    "f29_rdac_064_triple_rev_cogs_netinc_accel_decline_indicator": {"inputs": ["revenue", "cogs", "netinc"], "func": f29_rdac_064_triple_rev_cogs_netinc_accel_decline_indicator},
    "f29_rdac_065_rev_netinc_co_decline_streak": {"inputs": ["revenue", "netinc"], "func": f29_rdac_065_rev_netinc_co_decline_streak},
    "f29_rdac_066_rev_netinc_co_decline_fraction_8q": {"inputs": ["revenue", "netinc"], "func": f29_rdac_066_rev_netinc_co_decline_fraction_8q},
    "f29_rdac_067_composite_accel_zavg_rev_gp_netinc_8q": {"inputs": ["revenue", "gp", "netinc"], "func": f29_rdac_067_composite_accel_zavg_rev_gp_netinc_8q},
    "f29_rdac_068_composite_accel_abs_z_rev_gp_netinc_8q": {"inputs": ["revenue", "gp", "netinc"], "func": f29_rdac_068_composite_accel_abs_z_rev_gp_netinc_8q},
    "f29_rdac_069_dispersion_accel_z_rev_gp_netinc_8q": {"inputs": ["revenue", "gp", "netinc"], "func": f29_rdac_069_dispersion_accel_z_rev_gp_netinc_8q},
    "f29_rdac_070_rev_minus_netinc_accel_z_gap_8q": {"inputs": ["revenue", "netinc"], "func": f29_rdac_070_rev_minus_netinc_accel_z_gap_8q},
    "f29_rdac_071_quality_deterioration_rev_up_netinc_down": {"inputs": ["revenue", "netinc"], "func": f29_rdac_071_quality_deterioration_rev_up_netinc_down},
    "f29_rdac_072_cogs_yoy_pos_rev_yoy_neg_margin_death": {"inputs": ["revenue", "cogs"], "func": f29_rdac_072_cogs_yoy_pos_rev_yoy_neg_margin_death},
    "f29_rdac_073_rev_yoy_ttm_accel_both_neg_indicator": {"inputs": ["revenue"], "func": f29_rdac_073_rev_yoy_ttm_accel_both_neg_indicator},
    "f29_rdac_074_rev_yoy_qoq_accel_both_worst_quartile_12q": {"inputs": ["revenue"], "func": f29_rdac_074_rev_yoy_qoq_accel_both_worst_quartile_12q},
    "f29_rdac_075_rev_x_netinc_accel_z_interaction_8q": {"inputs": ["revenue", "netinc"], "func": f29_rdac_075_rev_x_netinc_accel_z_interaction_8q},
}
