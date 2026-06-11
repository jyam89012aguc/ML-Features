"""margin_collapse_acceleration d2 features 001_075 — Pipeline 1a-inverse short-side blowup family.

Pattern-detection hypotheses on gross/op/ebitda/net MARGIN acceleration & collapse dynamics.
Distinct from family 22 (mctj) which owns levels/slopes/compression rates. Per HANDOFF §6
families 29-36 special rule: base = pattern features on margin acceleration, NOT raw 2nd derivs.
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


def _gm(revenue, gp):
    return _safe_div(gp, revenue.abs())


def _om(revenue, opinc):
    return _safe_div(opinc, revenue.abs())


def _em(revenue, ebitda):
    return _safe_div(ebitda, revenue.abs())


def _nm(revenue, netinc):
    return _safe_div(netinc, revenue.abs())


def _gm_ttm(revenue, gp):
    return _safe_div(_ttm(gp), _ttm(revenue).abs())


def _om_ttm(revenue, opinc):
    return _safe_div(_ttm(opinc), _ttm(revenue).abs())


def _em_ttm(revenue, ebitda):
    return _safe_div(_ttm(ebitda), _ttm(revenue).abs())


def _nm_ttm(revenue, netinc):
    return _safe_div(_ttm(netinc), _ttm(revenue).abs())


def _margin_accel(margin_series):
    """Acceleration of a margin time series — qoq change in margin (signed pp)."""
    return margin_series.diff().diff()


def _margin_yoy_accel(margin_series):
    """yoy-change-in-margin acceleration (Δ of yoy diff)."""
    return (margin_series - margin_series.shift(4)).diff()


def f30_mcac_001_gm_accel_zscore_8q_d2(revenue, gp):
    a = _gm(revenue, gp).diff().diff()
    result = _rolling_zscore(a, 8)
    return result.diff().diff()


def f30_mcac_002_om_accel_zscore_8q_d2(revenue, opinc):
    a = _om(revenue, opinc).diff().diff()
    result = _rolling_zscore(a, 8)
    return result.diff().diff()


def f30_mcac_003_em_accel_zscore_8q_d2(revenue, ebitda):
    a = _em(revenue, ebitda).diff().diff()
    result = _rolling_zscore(a, 8)
    return result.diff().diff()


def f30_mcac_004_nm_accel_zscore_8q_d2(revenue, netinc):
    a = _nm(revenue, netinc).diff().diff()
    result = _rolling_zscore(a, 8)
    return result.diff().diff()


def f30_mcac_005_gm_ttm_accel_zscore_12q_d2(revenue, gp):
    a = _gm_ttm(revenue, gp).diff().diff()
    result = _rolling_zscore(a, 12)
    return result.diff().diff()


def f30_mcac_006_om_accel_below_m2sd_8q_d2(revenue, opinc):
    a = _om(revenue, opinc).diff().diff(); z = _rolling_zscore(a, 8)
    result = (z < -2.0).astype(float).where(z.notna(), np.nan)
    return result.diff().diff()


def f30_mcac_007_gm_drop_from_8q_max_pp_d2(revenue, gp):
    m = _gm(revenue, gp)
    result = m - m.rolling(8, min_periods=3).max()
    return result.diff().diff()


def f30_mcac_008_om_drop_from_8q_max_pp_d2(revenue, opinc):
    m = _om(revenue, opinc)
    result = m - m.rolling(8, min_periods=3).max()
    return result.diff().diff()


def f30_mcac_009_em_drop_from_12q_max_pp_d2(revenue, ebitda):
    m = _em(revenue, ebitda)
    result = m - m.rolling(12, min_periods=4).max()
    return result.diff().diff()


def f30_mcac_010_nm_drop_from_8q_max_pp_d2(revenue, netinc):
    m = _nm(revenue, netinc)
    result = m - m.rolling(8, min_periods=3).max()
    return result.diff().diff()


def f30_mcac_011_gm_one_q_cliff_3pp_d2(revenue, gp):
    d = _gm(revenue, gp).diff()
    result = (d < -0.03).astype(float).where(d.notna(), np.nan)
    return result.diff().diff()


def f30_mcac_012_om_one_q_cliff_2pp_d2(revenue, opinc):
    d = _om(revenue, opinc).diff()
    result = (d < -0.02).astype(float).where(d.notna(), np.nan)
    return result.diff().diff()


def f30_mcac_013_nm_one_q_cliff_2pp_d2(revenue, netinc):
    d = _nm(revenue, netinc).diff()
    result = (d < -0.02).astype(float).where(d.notna(), np.nan)
    return result.diff().diff()


def f30_mcac_014_gm_cliff_count_8q_d2(revenue, gp):
    d = _gm(revenue, gp).diff()
    result = _rolling_count(d < -0.03, 8)
    return result.diff().diff()


def f30_mcac_015_om_cliff_count_8q_d2(revenue, opinc):
    d = _om(revenue, opinc).diff()
    result = _rolling_count(d < -0.02, 8)
    return result.diff().diff()


def f30_mcac_016_gm_decline_streak_d2(revenue, gp):
    m = _gm(revenue, gp)
    result = _consec_true_streak(m < m.shift(1)).astype(float)
    return result.diff().diff()


def f30_mcac_017_om_decline_streak_d2(revenue, opinc):
    m = _om(revenue, opinc)
    result = _consec_true_streak(m < m.shift(1)).astype(float)
    return result.diff().diff()


def f30_mcac_018_nm_decline_streak_d2(revenue, netinc):
    m = _nm(revenue, netinc)
    result = _consec_true_streak(m < m.shift(1)).astype(float)
    return result.diff().diff()


def f30_mcac_019_gm_accel_range_position_8q_d2(revenue, gp):
    a = _gm(revenue, gp).diff().diff()
    mn = a.rolling(8, min_periods=3).min(); mx = a.rolling(8, min_periods=3).max()
    result = _safe_div(a - mn, mx - mn)
    return result.diff().diff()


def f30_mcac_020_om_strictly_decreasing_streak_d2(revenue, opinc):
    m = _om(revenue, opinc)
    b = (m < m.shift(1)) & (m.shift(1) < m.shift(2))
    result = _consec_true_streak(b).astype(float)
    return result.diff().diff()


def f30_mcac_021_gm_slope_4q_sign_flip_d2(revenue, gp):
    m = _gm(revenue, gp); sl = _rolling_slope(m, 4)
    result = (_sign_safe(sl) != _sign_safe(sl.shift(1))).astype(float).where(sl.notna() & sl.shift(1).notna(), np.nan)
    return result.diff().diff()


def f30_mcac_022_om_ema4_sign_flip_pos_to_neg_d2(revenue, opinc):
    em = _ema(_om(revenue, opinc).diff(), 4)
    result = ((em < 0) & (em.shift(1) >= 0)).astype(float).where(em.notna() & em.shift(1).notna(), np.nan)
    return result.diff().diff()


def f30_mcac_023_nm_inflection_magnitude_8q_d2(revenue, netinc):
    m = _nm(revenue, netinc); a = m.diff().diff()
    sd = a.rolling(12, min_periods=4).std()
    result = _safe_div((a - a.shift(8)).abs(), sd)
    return result.diff().diff()


def f30_mcac_024_gm_mean_shift_z_4v12_d2(revenue, gp):
    m = _gm(revenue, gp); m4 = m.rolling(4, min_periods=2).mean(); m12 = m.rolling(12, min_periods=4).mean(); s12 = m.rolling(12, min_periods=4).std()
    result = _safe_div(m4 - m12, s12)
    return result.diff().diff()


def f30_mcac_025_om_mean_shift_down_indicator_d2(revenue, opinc):
    m = _om(revenue, opinc); m4 = m.rolling(4, min_periods=2).mean(); m12 = m.rolling(12, min_periods=4).mean(); s12 = m.rolling(12, min_periods=4).std()
    z = _safe_div(m4 - m12, s12)
    result = (z < -1.0).astype(float).where(z.notna(), np.nan)
    return result.diff().diff()


def f30_mcac_026_gm_variance_ratio_4q_12q_d2(revenue, gp):
    m = _gm(revenue, gp); a = m.diff().diff()
    result = _safe_div(a.rolling(4, min_periods=2).var(), a.rolling(12, min_periods=4).var())
    return result.diff().diff()


def f30_mcac_027_om_variance_jump_zscore_16q_d2(revenue, opinc):
    a = _om(revenue, opinc).diff().diff()
    vr = _safe_div(a.rolling(4, min_periods=2).var(), a.rolling(12, min_periods=4).var())
    result = _rolling_zscore(vr, 16)
    return result.diff().diff()


def f30_mcac_028_nm_var_shift_up_indicator_d2(revenue, netinc):
    a = _nm(revenue, netinc).diff().diff()
    vr = _safe_div(a.rolling(4, min_periods=2).var(), a.rolling(12, min_periods=4).var())
    result = (vr > 2.0).astype(float).where(vr.notna(), np.nan)
    return result.diff().diff()


def f30_mcac_029_gm_regime_stickiness_bad_quartile_4q_in_20q_d2(revenue, gp):
    m = _gm(revenue, gp); q25 = _rolling_quantile(m, 20, 0.25)
    result = _rolling_frac(m <= q25, 4)
    return result.diff().diff()


def f30_mcac_030_om_new_low_12q_indicator_d2(revenue, opinc):
    m = _om(revenue, opinc)
    result = (m == m.rolling(12, min_periods=4).min()).astype(float).where(m.notna(), np.nan)
    return result.diff().diff()


def f30_mcac_031_nm_and_om_compound_new_low_12q_d2(revenue, opinc, netinc):
    om = _om(revenue, opinc); nm = _nm(revenue, netinc)
    a = (om == om.rolling(12, min_periods=4).min()); b = (nm == nm.rolling(12, min_periods=4).min())
    result = (a & b).astype(float).where(om.notna() & nm.notna(), np.nan)
    return result.diff().diff()


def f30_mcac_032_gm_chow_fstat_proxy_12q_d2(revenue, gp):
    m = _gm(revenue, gp)
    m1 = m.rolling(6, min_periods=3).mean().shift(6); m2 = m.rolling(6, min_periods=3).mean(); s12 = m.rolling(12, min_periods=4).std()
    result = _safe_div((m1 - m2).abs(), s12)
    return result.diff().diff()


def f30_mcac_033_om_concavity_sign_d2(revenue, opinc):
    result = _sign_safe(_om(revenue, opinc).diff().diff())
    return result.diff().diff()


def f30_mcac_034_gm_convexity_flip_pos_to_neg_d2(revenue, gp):
    c = _gm(revenue, gp).diff().diff()
    result = ((c < 0) & (c.shift(1) >= 0)).astype(float).where(c.notna() & c.shift(1).notna(), np.nan)
    return result.diff().diff()


def f30_mcac_035_nm_convexity_flip_neg_to_pos_d2(revenue, netinc):
    c = _nm(revenue, netinc).diff().diff()
    result = ((c > 0) & (c.shift(1) <= 0)).astype(float).where(c.notna() & c.shift(1).notna(), np.nan)
    return result.diff().diff()


def f30_mcac_036_om_phase_shift_4q_vs_12q_norm_d2(revenue, opinc):
    m = _om(revenue, opinc); m4 = m.rolling(4, min_periods=2).mean(); m12 = m.rolling(12, min_periods=4).mean()
    result = _safe_div(m4 - m12, m12.abs())
    return result.diff().diff()


def f30_mcac_037_gm_ar1_persistence_8q_d2(revenue, gp):
    m = _gm(revenue, gp)
    result = m.rolling(8, min_periods=4).corr(m.shift(1))
    return result.diff().diff()


def f30_mcac_038_om_persistence_collapse_4q_d2(revenue, opinc):
    m = _om(revenue, opinc); ar = m.rolling(8, min_periods=4).corr(m.shift(1))
    result = ((ar < 0) & (ar.shift(4) > 0.5)).astype(float).where(ar.notna() & ar.shift(4).notna(), np.nan)
    return result.diff().diff()


def f30_mcac_039_nm_local_concavity_test_d2(revenue, netinc):
    m = _nm(revenue, netinc)
    result = _sign_safe(m.diff().diff())
    return result.diff().diff()


def f30_mcac_040_gm_break_recency_max_split_diff_12q_d2(revenue, gp):
    m = _gm(revenue, gp)
    diffs = pd.concat([(m.rolling(k, min_periods=2).mean().shift(12 - k) - m.rolling(12 - k, min_periods=2).mean()).abs() for k in range(3, 10)], axis=1)
    result = diffs.idxmax(axis=1).where(m.notna(), np.nan).astype(float)
    return result.diff().diff()


def f30_mcac_041_om_cusum_max_excursion_12q_d2(revenue, opinc):
    m = _om(revenue, opinc); mu = m.rolling(12, min_periods=4).mean()
    result = (m - mu).rolling(12, min_periods=4).apply(lambda w: np.nanmax(np.cumsum(w)) if not np.isnan(w).all() else np.nan, raw=True)
    return result.diff().diff()


def f30_mcac_042_gm_cusum_min_excursion_12q_d2(revenue, gp):
    m = _gm(revenue, gp); mu = m.rolling(12, min_periods=4).mean()
    result = (m - mu).rolling(12, min_periods=4).apply(lambda w: np.nanmin(np.cumsum(w)) if not np.isnan(w).all() else np.nan, raw=True)
    return result.diff().diff()


def f30_mcac_043_nm_cusum_z_12q_d2(revenue, netinc):
    m = _nm(revenue, netinc); mu = m.rolling(12, min_periods=4).mean(); sd = m.rolling(12, min_periods=4).std()
    cu = (m - mu).rolling(12, min_periods=4).apply(lambda w: np.nanmax(np.abs(np.cumsum(w))) if not np.isnan(w).all() else np.nan, raw=True)
    result = _safe_div(cu, sd)
    return result.diff().diff()


def f30_mcac_044_om_max_abs_residual_recency_8q_d2(revenue, opinc):
    m = _om(revenue, opinc); mu = m.rolling(8, min_periods=3).mean(); r = (m - mu).abs()
    result = r.rolling(8, min_periods=3).apply(lambda w: float(len(w) - 1 - int(np.nanargmax(w))) if not np.isnan(w).all() else np.nan, raw=True)
    return result.diff().diff()


def f30_mcac_045_gm_breakpoint_count_16q_d2(revenue, gp):
    m = _gm(revenue, gp); d = m.diff(); s = d.rolling(16, min_periods=5).std()
    result = _rolling_count(d.abs() > 2.0 * s, 16)
    return result.diff().diff()


def f30_mcac_046_nm_likelihood_break_proxy_12q_d2(revenue, netinc):
    m = _nm(revenue, netinc)
    m1 = m.rolling(6, min_periods=2).mean().shift(6); m2 = m.rolling(6, min_periods=2).mean()
    s1 = m.rolling(6, min_periods=2).std().shift(6); s2 = m.rolling(6, min_periods=2).std()
    result = _safe_div((m1 - m2) ** 2, (s1 ** 2 + s2 ** 2))
    return result.diff().diff()


def f30_mcac_047_om_break_recency_max_fstat_12q_d2(revenue, opinc):
    m = _om(revenue, opinc)
    fs = pd.concat([_safe_div((m.rolling(k, min_periods=2).mean().shift(12 - k) - m.rolling(12 - k, min_periods=2).mean()) ** 2, m.rolling(12, min_periods=4).var()) for k in range(3, 10)], axis=1)
    result = fs.idxmax(axis=1).where(m.notna(), np.nan).astype(float)
    return result.diff().diff()


def f30_mcac_048_gm_var_ratio_test_zscore_20q_d2(revenue, gp):
    m = _gm(revenue, gp)
    vr = _safe_div(m.rolling(4, min_periods=2).var(), m.rolling(12, min_periods=4).var())
    result = _rolling_zscore(vr - 1.0, 20)
    return result.diff().diff()


def f30_mcac_049_nm_var_regime_up_significance_12q_d2(revenue, netinc):
    m = _nm(revenue, netinc)
    v1 = m.rolling(6, min_periods=2).var().shift(6); v2 = m.rolling(6, min_periods=2).var()
    result = _safe_div(v2 - v1, v1.abs())
    return result.diff().diff()


def f30_mcac_050_om_var_regime_down_significance_12q_d2(revenue, opinc):
    m = _om(revenue, opinc)
    v1 = m.rolling(6, min_periods=2).var().shift(6); v2 = m.rolling(6, min_periods=2).var()
    result = _safe_div(v1 - v2, v1.abs())
    return result.diff().diff()


def f30_mcac_051_gm_mean_diff_t_stat_12q_d2(revenue, gp):
    m = _gm(revenue, gp)
    m1 = m.rolling(6, min_periods=3).mean().shift(6); m2 = m.rolling(6, min_periods=3).mean()
    s1 = m.rolling(6, min_periods=3).std().shift(6); s2 = m.rolling(6, min_periods=3).std()
    se = ((s1 ** 2 + s2 ** 2) / 6.0).pow(0.5)
    result = _safe_div(m2 - m1, se)
    return result.diff().diff()


def f30_mcac_052_nm_mean_t_signif_down_d2(revenue, netinc):
    m = _nm(revenue, netinc)
    m1 = m.rolling(6, min_periods=3).mean().shift(6); m2 = m.rolling(6, min_periods=3).mean()
    s1 = m.rolling(6, min_periods=3).std().shift(6); s2 = m.rolling(6, min_periods=3).std()
    se = ((s1 ** 2 + s2 ** 2) / 6.0).pow(0.5)
    t = _safe_div(m2 - m1, se)
    result = (t < -2.0).astype(float).where(t.notna(), np.nan)
    return result.diff().diff()


def f30_mcac_053_gm_ks_style_cdf_shift_16q_d2(revenue, gp):
    m = _gm(revenue, gp)
    med1 = m.rolling(8, min_periods=3).median().shift(8); med2 = m.rolling(8, min_periods=3).median()
    iqr = (m.rolling(16, min_periods=5).quantile(0.75) - m.rolling(16, min_periods=5).quantile(0.25))
    result = _safe_div((med2 - med1).abs(), iqr)
    return result.diff().diff()


def f30_mcac_054_om_median_break_4q_vs_16q_d2(revenue, opinc):
    m = _om(revenue, opinc)
    result = m.rolling(4, min_periods=2).median() - m.rolling(16, min_periods=5).median()
    return result.diff().diff()


def f30_mcac_055_nm_resid_var_jump_4q_vs_16q_d2(revenue, netinc):
    m = _nm(revenue, netinc); m4 = m.rolling(4, min_periods=2).mean(); m16 = m.rolling(16, min_periods=5).mean()
    r4 = (m - m4) ** 2; r16 = (m - m16) ** 2
    result = _safe_div(r4.rolling(4, min_periods=2).mean(), r16.rolling(16, min_periods=5).mean())
    return result.diff().diff()


def f30_mcac_056_gm_regression_slope_break_4q_vs_12q_d2(revenue, gp):
    m = _gm(revenue, gp)
    result = _rolling_slope(m, 4) - _rolling_slope(m, 12)
    return result.diff().diff()


def f30_mcac_057_om_regression_slope_break_4q_vs_12q_d2(revenue, opinc):
    m = _om(revenue, opinc)
    result = _rolling_slope(m, 4) - _rolling_slope(m, 12)
    return result.diff().diff()


def f30_mcac_058_nm_regression_slope_break_4q_vs_12q_d2(revenue, netinc):
    m = _nm(revenue, netinc)
    result = _rolling_slope(m, 4) - _rolling_slope(m, 12)
    return result.diff().diff()


def f30_mcac_059_em_combined_break_composite_8q_d2(revenue, ebitda):
    m = _em(revenue, ebitda); d = m.diff(); s = d.rolling(8, min_periods=3).std()
    cliff = _rolling_count(d < -0.02, 8); jump = _rolling_count(d.abs() > 2.0 * s, 8); newlow = _rolling_count(m == m.rolling(12, min_periods=4).min(), 8)
    result = (cliff.fillna(0) + jump.fillna(0) + newlow.fillna(0)).where(m.notna(), np.nan)
    return result.diff().diff()


def f30_mcac_060_gm_quandt_max_fstat_12q_d2(revenue, gp):
    m = _gm(revenue, gp)
    fs = pd.concat([_safe_div((m.rolling(k, min_periods=2).mean().shift(12 - k) - m.rolling(12 - k, min_periods=2).mean()) ** 2, m.rolling(12, min_periods=4).var()) for k in range(3, 10)], axis=1)
    result = fs.max(axis=1)
    return result.diff().diff()


def f30_mcac_061_gm_om_both_decline_indicator_d2(revenue, gp, opinc):
    g = _gm(revenue, gp).diff(); o = _om(revenue, opinc).diff()
    result = ((g < 0) & (o < 0)).astype(float).where(g.notna() & o.notna(), np.nan)
    return result.diff().diff()


def f30_mcac_062_gm_om_nm_triple_decline_indicator_d2(revenue, gp, opinc, netinc):
    g = _gm(revenue, gp).diff(); o = _om(revenue, opinc).diff(); n = _nm(revenue, netinc).diff()
    result = ((g < 0) & (o < 0) & (n < 0)).astype(float).where(g.notna() & o.notna() & n.notna(), np.nan)
    return result.diff().diff()


def f30_mcac_063_four_margin_co_decline_indicator_d2(revenue, gp, opinc, ebitda, netinc):
    g = _gm(revenue, gp).diff(); o = _om(revenue, opinc).diff(); e = _em(revenue, ebitda).diff(); n = _nm(revenue, netinc).diff()
    result = ((g < 0) & (o < 0) & (e < 0) & (n < 0)).astype(float).where(g.notna() & o.notna() & e.notna() & n.notna(), np.nan)
    return result.diff().diff()


def f30_mcac_064_gm_om_co_decline_streak_d2(revenue, gp, opinc):
    g = _gm(revenue, gp).diff(); o = _om(revenue, opinc).diff()
    result = _consec_true_streak((g < 0) & (o < 0)).astype(float)
    return result.diff().diff()


def f30_mcac_065_om_nm_co_decline_fraction_8q_d2(revenue, opinc, netinc):
    o = _om(revenue, opinc).diff(); n = _nm(revenue, netinc).diff()
    result = _rolling_frac((o < 0) & (n < 0), 8)
    return result.diff().diff()


def f30_mcac_066_four_margin_compound_score_signed_8q_d2(revenue, gp, opinc, ebitda, netinc):
    g = _rolling_zscore(_gm(revenue, gp).diff(), 8); o = _rolling_zscore(_om(revenue, opinc).diff(), 8); e = _rolling_zscore(_em(revenue, ebitda).diff(), 8); n = _rolling_zscore(_nm(revenue, netinc).diff(), 8)
    result = pd.concat([g, o, e, n], axis=1).mean(axis=1)
    return result.diff().diff()


def f30_mcac_067_four_margin_compound_score_abs_8q_d2(revenue, gp, opinc, ebitda, netinc):
    g = _rolling_zscore(_gm(revenue, gp).diff(), 8); o = _rolling_zscore(_om(revenue, opinc).diff(), 8); e = _rolling_zscore(_em(revenue, ebitda).diff(), 8); n = _rolling_zscore(_nm(revenue, netinc).diff(), 8)
    result = pd.concat([g.abs(), o.abs(), e.abs(), n.abs()], axis=1).mean(axis=1)
    return result.diff().diff()


def f30_mcac_068_four_margin_dispersion_z_8q_d2(revenue, gp, opinc, ebitda, netinc):
    g = _rolling_zscore(_gm(revenue, gp).diff(), 8); o = _rolling_zscore(_om(revenue, opinc).diff(), 8); e = _rolling_zscore(_em(revenue, ebitda).diff(), 8); n = _rolling_zscore(_nm(revenue, netinc).diff(), 8)
    result = pd.concat([g, o, e, n], axis=1).std(axis=1)
    return result.diff().diff()


def f30_mcac_069_gm_minus_nm_accel_z_gap_8q_d2(revenue, gp, netinc):
    g = _rolling_zscore(_gm(revenue, gp).diff().diff(), 8); n = _rolling_zscore(_nm(revenue, netinc).diff().diff(), 8)
    result = g - n
    return result.diff().diff()


def f30_mcac_070_cascade_gm_leads_nm_lag_4q_d2(revenue, gp, netinc):
    g = _gm(revenue, gp).diff(); n = _nm(revenue, netinc).diff()
    result = ((g.shift(4) < 0) & (n < 0)).astype(float).where(g.shift(4).notna() & n.notna(), np.nan)
    return result.diff().diff()


def f30_mcac_071_cascade_om_leads_nm_lag_2q_d2(revenue, opinc, netinc):
    o = _om(revenue, opinc).diff(); n = _nm(revenue, netinc).diff()
    result = ((o.shift(2) < 0) & (n < 0)).astype(float).where(o.shift(2).notna() & n.notna(), np.nan)
    return result.diff().diff()


def f30_mcac_072_sign_agreement_count_4margins_decline_d2(revenue, gp, opinc, ebitda, netinc):
    g = (_gm(revenue, gp).diff() < 0).astype(float); o = (_om(revenue, opinc).diff() < 0).astype(float); e = (_em(revenue, ebitda).diff() < 0).astype(float); n = (_nm(revenue, netinc).diff() < 0).astype(float)
    result = (g + o + e + n).where(_gm(revenue, gp).notna(), np.nan)
    return result.diff().diff()


def f30_mcac_073_sign_agreement_count_4margins_sum_4q_d2(revenue, gp, opinc, ebitda, netinc):
    g = (_gm(revenue, gp).diff() < 0).astype(float); o = (_om(revenue, opinc).diff() < 0).astype(float); e = (_em(revenue, ebitda).diff() < 0).astype(float); n = (_nm(revenue, netinc).diff() < 0).astype(float)
    result = (g + o + e + n).rolling(4, min_periods=2).sum()
    return result.diff().diff()


def f30_mcac_074_cross_margin_corr_gm_om_8q_d2(revenue, gp, opinc):
    g = _gm(revenue, gp).diff(); o = _om(revenue, opinc).diff()
    result = g.rolling(8, min_periods=4).corr(o)
    return result.diff().diff()


def f30_mcac_075_worst_margin_z_signed_8q_d2(revenue, gp, opinc, ebitda, netinc):
    g = _rolling_zscore(_gm(revenue, gp).diff().diff(), 8); o = _rolling_zscore(_om(revenue, opinc).diff().diff(), 8); e = _rolling_zscore(_em(revenue, ebitda).diff().diff(), 8); n = _rolling_zscore(_nm(revenue, netinc).diff().diff(), 8)
    result = pd.concat([g, o, e, n], axis=1).min(axis=1)
    return result.diff().diff()


MARGIN_COLLAPSE_ACCELERATION_D2_REGISTRY_001_075 = {
    "f30_mcac_001_gm_accel_zscore_8q_d2": {"inputs": ["revenue", "gp"], "func": f30_mcac_001_gm_accel_zscore_8q_d2},
    "f30_mcac_002_om_accel_zscore_8q_d2": {"inputs": ["revenue", "opinc"], "func": f30_mcac_002_om_accel_zscore_8q_d2},
    "f30_mcac_003_em_accel_zscore_8q_d2": {"inputs": ["revenue", "ebitda"], "func": f30_mcac_003_em_accel_zscore_8q_d2},
    "f30_mcac_004_nm_accel_zscore_8q_d2": {"inputs": ["revenue", "netinc"], "func": f30_mcac_004_nm_accel_zscore_8q_d2},
    "f30_mcac_005_gm_ttm_accel_zscore_12q_d2": {"inputs": ["revenue", "gp"], "func": f30_mcac_005_gm_ttm_accel_zscore_12q_d2},
    "f30_mcac_006_om_accel_below_m2sd_8q_d2": {"inputs": ["revenue", "opinc"], "func": f30_mcac_006_om_accel_below_m2sd_8q_d2},
    "f30_mcac_007_gm_drop_from_8q_max_pp_d2": {"inputs": ["revenue", "gp"], "func": f30_mcac_007_gm_drop_from_8q_max_pp_d2},
    "f30_mcac_008_om_drop_from_8q_max_pp_d2": {"inputs": ["revenue", "opinc"], "func": f30_mcac_008_om_drop_from_8q_max_pp_d2},
    "f30_mcac_009_em_drop_from_12q_max_pp_d2": {"inputs": ["revenue", "ebitda"], "func": f30_mcac_009_em_drop_from_12q_max_pp_d2},
    "f30_mcac_010_nm_drop_from_8q_max_pp_d2": {"inputs": ["revenue", "netinc"], "func": f30_mcac_010_nm_drop_from_8q_max_pp_d2},
    "f30_mcac_011_gm_one_q_cliff_3pp_d2": {"inputs": ["revenue", "gp"], "func": f30_mcac_011_gm_one_q_cliff_3pp_d2},
    "f30_mcac_012_om_one_q_cliff_2pp_d2": {"inputs": ["revenue", "opinc"], "func": f30_mcac_012_om_one_q_cliff_2pp_d2},
    "f30_mcac_013_nm_one_q_cliff_2pp_d2": {"inputs": ["revenue", "netinc"], "func": f30_mcac_013_nm_one_q_cliff_2pp_d2},
    "f30_mcac_014_gm_cliff_count_8q_d2": {"inputs": ["revenue", "gp"], "func": f30_mcac_014_gm_cliff_count_8q_d2},
    "f30_mcac_015_om_cliff_count_8q_d2": {"inputs": ["revenue", "opinc"], "func": f30_mcac_015_om_cliff_count_8q_d2},
    "f30_mcac_016_gm_decline_streak_d2": {"inputs": ["revenue", "gp"], "func": f30_mcac_016_gm_decline_streak_d2},
    "f30_mcac_017_om_decline_streak_d2": {"inputs": ["revenue", "opinc"], "func": f30_mcac_017_om_decline_streak_d2},
    "f30_mcac_018_nm_decline_streak_d2": {"inputs": ["revenue", "netinc"], "func": f30_mcac_018_nm_decline_streak_d2},
    "f30_mcac_019_gm_accel_range_position_8q_d2": {"inputs": ["revenue", "gp"], "func": f30_mcac_019_gm_accel_range_position_8q_d2},
    "f30_mcac_020_om_strictly_decreasing_streak_d2": {"inputs": ["revenue", "opinc"], "func": f30_mcac_020_om_strictly_decreasing_streak_d2},
    "f30_mcac_021_gm_slope_4q_sign_flip_d2": {"inputs": ["revenue", "gp"], "func": f30_mcac_021_gm_slope_4q_sign_flip_d2},
    "f30_mcac_022_om_ema4_sign_flip_pos_to_neg_d2": {"inputs": ["revenue", "opinc"], "func": f30_mcac_022_om_ema4_sign_flip_pos_to_neg_d2},
    "f30_mcac_023_nm_inflection_magnitude_8q_d2": {"inputs": ["revenue", "netinc"], "func": f30_mcac_023_nm_inflection_magnitude_8q_d2},
    "f30_mcac_024_gm_mean_shift_z_4v12_d2": {"inputs": ["revenue", "gp"], "func": f30_mcac_024_gm_mean_shift_z_4v12_d2},
    "f30_mcac_025_om_mean_shift_down_indicator_d2": {"inputs": ["revenue", "opinc"], "func": f30_mcac_025_om_mean_shift_down_indicator_d2},
    "f30_mcac_026_gm_variance_ratio_4q_12q_d2": {"inputs": ["revenue", "gp"], "func": f30_mcac_026_gm_variance_ratio_4q_12q_d2},
    "f30_mcac_027_om_variance_jump_zscore_16q_d2": {"inputs": ["revenue", "opinc"], "func": f30_mcac_027_om_variance_jump_zscore_16q_d2},
    "f30_mcac_028_nm_var_shift_up_indicator_d2": {"inputs": ["revenue", "netinc"], "func": f30_mcac_028_nm_var_shift_up_indicator_d2},
    "f30_mcac_029_gm_regime_stickiness_bad_quartile_4q_in_20q_d2": {"inputs": ["revenue", "gp"], "func": f30_mcac_029_gm_regime_stickiness_bad_quartile_4q_in_20q_d2},
    "f30_mcac_030_om_new_low_12q_indicator_d2": {"inputs": ["revenue", "opinc"], "func": f30_mcac_030_om_new_low_12q_indicator_d2},
    "f30_mcac_031_nm_and_om_compound_new_low_12q_d2": {"inputs": ["revenue", "opinc", "netinc"], "func": f30_mcac_031_nm_and_om_compound_new_low_12q_d2},
    "f30_mcac_032_gm_chow_fstat_proxy_12q_d2": {"inputs": ["revenue", "gp"], "func": f30_mcac_032_gm_chow_fstat_proxy_12q_d2},
    "f30_mcac_033_om_concavity_sign_d2": {"inputs": ["revenue", "opinc"], "func": f30_mcac_033_om_concavity_sign_d2},
    "f30_mcac_034_gm_convexity_flip_pos_to_neg_d2": {"inputs": ["revenue", "gp"], "func": f30_mcac_034_gm_convexity_flip_pos_to_neg_d2},
    "f30_mcac_035_nm_convexity_flip_neg_to_pos_d2": {"inputs": ["revenue", "netinc"], "func": f30_mcac_035_nm_convexity_flip_neg_to_pos_d2},
    "f30_mcac_036_om_phase_shift_4q_vs_12q_norm_d2": {"inputs": ["revenue", "opinc"], "func": f30_mcac_036_om_phase_shift_4q_vs_12q_norm_d2},
    "f30_mcac_037_gm_ar1_persistence_8q_d2": {"inputs": ["revenue", "gp"], "func": f30_mcac_037_gm_ar1_persistence_8q_d2},
    "f30_mcac_038_om_persistence_collapse_4q_d2": {"inputs": ["revenue", "opinc"], "func": f30_mcac_038_om_persistence_collapse_4q_d2},
    "f30_mcac_039_nm_local_concavity_test_d2": {"inputs": ["revenue", "netinc"], "func": f30_mcac_039_nm_local_concavity_test_d2},
    "f30_mcac_040_gm_break_recency_max_split_diff_12q_d2": {"inputs": ["revenue", "gp"], "func": f30_mcac_040_gm_break_recency_max_split_diff_12q_d2},
    "f30_mcac_041_om_cusum_max_excursion_12q_d2": {"inputs": ["revenue", "opinc"], "func": f30_mcac_041_om_cusum_max_excursion_12q_d2},
    "f30_mcac_042_gm_cusum_min_excursion_12q_d2": {"inputs": ["revenue", "gp"], "func": f30_mcac_042_gm_cusum_min_excursion_12q_d2},
    "f30_mcac_043_nm_cusum_z_12q_d2": {"inputs": ["revenue", "netinc"], "func": f30_mcac_043_nm_cusum_z_12q_d2},
    "f30_mcac_044_om_max_abs_residual_recency_8q_d2": {"inputs": ["revenue", "opinc"], "func": f30_mcac_044_om_max_abs_residual_recency_8q_d2},
    "f30_mcac_045_gm_breakpoint_count_16q_d2": {"inputs": ["revenue", "gp"], "func": f30_mcac_045_gm_breakpoint_count_16q_d2},
    "f30_mcac_046_nm_likelihood_break_proxy_12q_d2": {"inputs": ["revenue", "netinc"], "func": f30_mcac_046_nm_likelihood_break_proxy_12q_d2},
    "f30_mcac_047_om_break_recency_max_fstat_12q_d2": {"inputs": ["revenue", "opinc"], "func": f30_mcac_047_om_break_recency_max_fstat_12q_d2},
    "f30_mcac_048_gm_var_ratio_test_zscore_20q_d2": {"inputs": ["revenue", "gp"], "func": f30_mcac_048_gm_var_ratio_test_zscore_20q_d2},
    "f30_mcac_049_nm_var_regime_up_significance_12q_d2": {"inputs": ["revenue", "netinc"], "func": f30_mcac_049_nm_var_regime_up_significance_12q_d2},
    "f30_mcac_050_om_var_regime_down_significance_12q_d2": {"inputs": ["revenue", "opinc"], "func": f30_mcac_050_om_var_regime_down_significance_12q_d2},
    "f30_mcac_051_gm_mean_diff_t_stat_12q_d2": {"inputs": ["revenue", "gp"], "func": f30_mcac_051_gm_mean_diff_t_stat_12q_d2},
    "f30_mcac_052_nm_mean_t_signif_down_d2": {"inputs": ["revenue", "netinc"], "func": f30_mcac_052_nm_mean_t_signif_down_d2},
    "f30_mcac_053_gm_ks_style_cdf_shift_16q_d2": {"inputs": ["revenue", "gp"], "func": f30_mcac_053_gm_ks_style_cdf_shift_16q_d2},
    "f30_mcac_054_om_median_break_4q_vs_16q_d2": {"inputs": ["revenue", "opinc"], "func": f30_mcac_054_om_median_break_4q_vs_16q_d2},
    "f30_mcac_055_nm_resid_var_jump_4q_vs_16q_d2": {"inputs": ["revenue", "netinc"], "func": f30_mcac_055_nm_resid_var_jump_4q_vs_16q_d2},
    "f30_mcac_056_gm_regression_slope_break_4q_vs_12q_d2": {"inputs": ["revenue", "gp"], "func": f30_mcac_056_gm_regression_slope_break_4q_vs_12q_d2},
    "f30_mcac_057_om_regression_slope_break_4q_vs_12q_d2": {"inputs": ["revenue", "opinc"], "func": f30_mcac_057_om_regression_slope_break_4q_vs_12q_d2},
    "f30_mcac_058_nm_regression_slope_break_4q_vs_12q_d2": {"inputs": ["revenue", "netinc"], "func": f30_mcac_058_nm_regression_slope_break_4q_vs_12q_d2},
    "f30_mcac_059_em_combined_break_composite_8q_d2": {"inputs": ["revenue", "ebitda"], "func": f30_mcac_059_em_combined_break_composite_8q_d2},
    "f30_mcac_060_gm_quandt_max_fstat_12q_d2": {"inputs": ["revenue", "gp"], "func": f30_mcac_060_gm_quandt_max_fstat_12q_d2},
    "f30_mcac_061_gm_om_both_decline_indicator_d2": {"inputs": ["revenue", "gp", "opinc"], "func": f30_mcac_061_gm_om_both_decline_indicator_d2},
    "f30_mcac_062_gm_om_nm_triple_decline_indicator_d2": {"inputs": ["revenue", "gp", "opinc", "netinc"], "func": f30_mcac_062_gm_om_nm_triple_decline_indicator_d2},
    "f30_mcac_063_four_margin_co_decline_indicator_d2": {"inputs": ["revenue", "gp", "opinc", "ebitda", "netinc"], "func": f30_mcac_063_four_margin_co_decline_indicator_d2},
    "f30_mcac_064_gm_om_co_decline_streak_d2": {"inputs": ["revenue", "gp", "opinc"], "func": f30_mcac_064_gm_om_co_decline_streak_d2},
    "f30_mcac_065_om_nm_co_decline_fraction_8q_d2": {"inputs": ["revenue", "opinc", "netinc"], "func": f30_mcac_065_om_nm_co_decline_fraction_8q_d2},
    "f30_mcac_066_four_margin_compound_score_signed_8q_d2": {"inputs": ["revenue", "gp", "opinc", "ebitda", "netinc"], "func": f30_mcac_066_four_margin_compound_score_signed_8q_d2},
    "f30_mcac_067_four_margin_compound_score_abs_8q_d2": {"inputs": ["revenue", "gp", "opinc", "ebitda", "netinc"], "func": f30_mcac_067_four_margin_compound_score_abs_8q_d2},
    "f30_mcac_068_four_margin_dispersion_z_8q_d2": {"inputs": ["revenue", "gp", "opinc", "ebitda", "netinc"], "func": f30_mcac_068_four_margin_dispersion_z_8q_d2},
    "f30_mcac_069_gm_minus_nm_accel_z_gap_8q_d2": {"inputs": ["revenue", "gp", "netinc"], "func": f30_mcac_069_gm_minus_nm_accel_z_gap_8q_d2},
    "f30_mcac_070_cascade_gm_leads_nm_lag_4q_d2": {"inputs": ["revenue", "gp", "netinc"], "func": f30_mcac_070_cascade_gm_leads_nm_lag_4q_d2},
    "f30_mcac_071_cascade_om_leads_nm_lag_2q_d2": {"inputs": ["revenue", "opinc", "netinc"], "func": f30_mcac_071_cascade_om_leads_nm_lag_2q_d2},
    "f30_mcac_072_sign_agreement_count_4margins_decline_d2": {"inputs": ["revenue", "gp", "opinc", "ebitda", "netinc"], "func": f30_mcac_072_sign_agreement_count_4margins_decline_d2},
    "f30_mcac_073_sign_agreement_count_4margins_sum_4q_d2": {"inputs": ["revenue", "gp", "opinc", "ebitda", "netinc"], "func": f30_mcac_073_sign_agreement_count_4margins_sum_4q_d2},
    "f30_mcac_074_cross_margin_corr_gm_om_8q_d2": {"inputs": ["revenue", "gp", "opinc"], "func": f30_mcac_074_cross_margin_corr_gm_om_8q_d2},
    "f30_mcac_075_worst_margin_z_signed_8q_d2": {"inputs": ["revenue", "gp", "opinc", "ebitda", "netinc"], "func": f30_mcac_075_worst_margin_z_signed_8q_d2},
}
