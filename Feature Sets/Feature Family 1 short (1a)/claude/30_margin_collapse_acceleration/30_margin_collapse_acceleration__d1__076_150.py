"""margin_collapse_acceleration d1 features 076_150 — Pipeline 1a-inverse short-side blowup family.

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


def f30_mcac_076_rev_growing_margins_down_indicator_gm_d1(revenue, gp):
    g = _gm(revenue, gp).diff(); r = _yoy_pct(revenue)
    result = ((r > 0) & (g < 0)).astype(float).where(r.notna() & g.notna(), np.nan)
    return result.diff()


def f30_mcac_077_rev_growing_margins_down_indicator_om_d1(revenue, opinc):
    o = _om(revenue, opinc).diff(); r = _yoy_pct(revenue)
    result = ((r > 0) & (o < 0)).astype(float).where(r.notna() & o.notna(), np.nan)
    return result.diff()


def f30_mcac_078_rev_growing_margins_down_indicator_nm_d1(revenue, netinc):
    n = _nm(revenue, netinc).diff(); r = _yoy_pct(revenue)
    result = ((r > 0) & (n < 0)).astype(float).where(r.notna() & n.notna(), np.nan)
    return result.diff()


def f30_mcac_079_operating_deleverage_om_vs_rev_growth_8q_d1(revenue, opinc):
    o = _om(revenue, opinc); r = _yoy_pct(revenue)
    result = -o.rolling(8, min_periods=4).corr(r)
    return result.diff()


def f30_mcac_080_operating_deleverage_intensity_d1(revenue, opinc):
    o = _om(revenue, opinc).diff(); r = _yoy_pct(revenue)
    result = _safe_div(-o, r.abs())
    return result.diff()


def f30_mcac_081_rev_up_om_down_streak_d1(revenue, opinc):
    o = _om(revenue, opinc).diff(); r = _yoy_pct(revenue)
    result = _consec_true_streak((r > 0) & (o < 0)).astype(float)
    return result.diff()


def f30_mcac_082_rev_up_gm_down_count_8q_d1(revenue, gp):
    g = _gm(revenue, gp).diff(); r = _yoy_pct(revenue)
    result = _rolling_count((r > 0) & (g < 0), 8)
    return result.diff()


def f30_mcac_083_cogs_accel_minus_rev_accel_gap_yoy_d1(revenue, cogs):
    rc = _yoy_pct(cogs).diff(); rr = _yoy_pct(revenue).diff()
    result = rc - rr
    return result.diff()


def f30_mcac_084_sgna_accel_minus_rev_accel_gap_yoy_d1(revenue, sgna):
    rc = _yoy_pct(sgna).diff(); rr = _yoy_pct(revenue).diff()
    result = rc - rr
    return result.diff()


def f30_mcac_085_opex_accel_minus_rev_accel_gap_yoy_d1(revenue, opex):
    rc = _yoy_pct(opex).diff(); rr = _yoy_pct(revenue).diff()
    result = rc - rr
    return result.diff()


def f30_mcac_086_cogs_to_rev_accel_zscore_8q_d1(revenue, cogs):
    r = _safe_div(cogs, revenue.abs()).diff().diff()
    result = _rolling_zscore(r, 8)
    return result.diff()


def f30_mcac_087_sgna_to_rev_accel_zscore_8q_d1(revenue, sgna):
    r = _safe_div(sgna, revenue.abs()).diff().diff()
    result = _rolling_zscore(r, 8)
    return result.diff()


def f30_mcac_088_opex_to_rev_accel_zscore_8q_d1(revenue, opex):
    r = _safe_div(opex, revenue.abs()).diff().diff()
    result = _rolling_zscore(r, 8)
    return result.diff()


def f30_mcac_089_depamor_to_rev_accel_zscore_8q_d1(revenue, depamor):
    r = _safe_div(depamor, revenue.abs()).diff().diff()
    result = _rolling_zscore(r, 8)
    return result.diff()


def f30_mcac_090_cost_stack_synchronized_jump_indicator_d1(revenue, cogs, sgna, opex):
    rc = _safe_div(cogs, revenue.abs()).diff(); rs = _safe_div(sgna, revenue.abs()).diff(); ro = _safe_div(opex, revenue.abs()).diff()
    result = ((rc > 0) & (rs > 0) & (ro > 0)).astype(float).where(rc.notna() & rs.notna() & ro.notna(), np.nan)
    return result.diff()


def f30_mcac_091_cost_stack_synchronized_jump_count_8q_d1(revenue, cogs, sgna, opex):
    rc = _safe_div(cogs, revenue.abs()).diff(); rs = _safe_div(sgna, revenue.abs()).diff(); ro = _safe_div(opex, revenue.abs()).diff()
    result = _rolling_count((rc > 0) & (rs > 0) & (ro > 0), 8)
    return result.diff()


def f30_mcac_092_gm_om_spread_collapse_8q_d1(revenue, gp, opinc):
    sp = _gm(revenue, gp) - _om(revenue, opinc)
    result = sp - sp.rolling(8, min_periods=3).max()
    return result.diff()


def f30_mcac_093_om_nm_spread_collapse_8q_d1(revenue, opinc, netinc):
    sp = _om(revenue, opinc) - _nm(revenue, netinc)
    result = sp - sp.rolling(8, min_periods=3).max()
    return result.diff()


def f30_mcac_094_em_gm_ratio_collapse_8q_d1(revenue, gp, ebitda):
    r = _safe_div(_em(revenue, ebitda), _gm(revenue, gp).abs())
    result = r - r.rolling(8, min_periods=3).max()
    return result.diff()


def f30_mcac_095_gm_om_em_nm_descending_invariant_breach_d1(revenue, gp, opinc, ebitda, netinc):
    g = _gm(revenue, gp); o = _om(revenue, opinc); e = _em(revenue, ebitda); n = _nm(revenue, netinc)
    breach = ((g < o) | (o < e) | (e < n)).astype(float)
    result = breach.where(g.notna() & o.notna() & e.notna() & n.notna(), np.nan)
    return result.diff()


def f30_mcac_096_cogs_to_rev_jump_one_q_3pp_d1(revenue, cogs):
    r = _safe_div(cogs, revenue.abs()).diff()
    result = (r > 0.03).astype(float).where(r.notna(), np.nan)
    return result.diff()


def f30_mcac_097_sgna_to_rev_jump_one_q_2pp_d1(revenue, sgna):
    r = _safe_div(sgna, revenue.abs()).diff()
    result = (r > 0.02).astype(float).where(r.notna(), np.nan)
    return result.diff()


def f30_mcac_098_depamor_to_rev_jump_one_q_1pp_d1(revenue, depamor):
    r = _safe_div(depamor, revenue.abs()).diff()
    result = (r > 0.01).astype(float).where(r.notna(), np.nan)
    return result.diff()


def f30_mcac_099_cost_jumps_count_8q_any_line_d1(revenue, cogs, sgna, opex):
    c = (_safe_div(cogs, revenue.abs()).diff() > 0.02).astype(float); s = (_safe_div(sgna, revenue.abs()).diff() > 0.01).astype(float); o = (_safe_div(opex, revenue.abs()).diff() > 0.02).astype(float)
    any_jump = ((c + s + o) > 0).astype(float)
    result = any_jump.rolling(8, min_periods=2).sum()
    return result.diff()


def f30_mcac_100_cost_jumps_count_8q_2plus_lines_d1(revenue, cogs, sgna, opex):
    c = (_safe_div(cogs, revenue.abs()).diff() > 0.02).astype(float); s = (_safe_div(sgna, revenue.abs()).diff() > 0.01).astype(float); o = (_safe_div(opex, revenue.abs()).diff() > 0.02).astype(float)
    multi = ((c + s + o) >= 2).astype(float)
    result = multi.rolling(8, min_periods=2).sum()
    return result.diff()


def f30_mcac_101_gm_drawdown_from_12q_max_d1(revenue, gp):
    m = _gm(revenue, gp)
    result = m.rolling(12, min_periods=4).max() - m
    return result.diff()


def f30_mcac_102_om_drawdown_from_12q_max_d1(revenue, opinc):
    m = _om(revenue, opinc)
    result = m.rolling(12, min_periods=4).max() - m
    return result.diff()


def f30_mcac_103_nm_drawdown_from_16q_max_d1(revenue, netinc):
    m = _nm(revenue, netinc)
    result = m.rolling(16, min_periods=5).max() - m
    return result.diff()


def f30_mcac_104_em_drawdown_from_12q_max_d1(revenue, ebitda):
    m = _em(revenue, ebitda)
    result = m.rolling(12, min_periods=4).max() - m
    return result.diff()


def f30_mcac_105_om_q_since_12q_max_d1(revenue, opinc):
    m = _om(revenue, opinc)
    result = m.rolling(12, min_periods=4).apply(lambda w: float(len(w) - 1 - int(np.nanargmax(w))) if not np.isnan(w).all() else np.nan, raw=True)
    return result.diff()


def f30_mcac_106_gm_drawdown_velocity_8q_d1(revenue, gp):
    m = _gm(revenue, gp); depth = m.rolling(12, min_periods=4).max() - m
    dur = m.rolling(12, min_periods=4).apply(lambda w: float(len(w) - 1 - int(np.nanargmax(w))) if not np.isnan(w).all() else np.nan, raw=True)
    result = _safe_div(depth, dur.replace(0, np.nan))
    return result.diff()


def f30_mcac_107_om_recovery_rate_from_8q_min_d1(revenue, opinc):
    m = _om(revenue, opinc); mn = m.rolling(8, min_periods=3).min(); mx = m.rolling(8, min_periods=3).max()
    result = _safe_div(m - mn, mx - mn)
    return result.diff()


def f30_mcac_108_om_accel_pain_ratio_8q_d1(revenue, opinc):
    a = _om(revenue, opinc).diff().diff(); neg = a.where(a < 0).abs().rolling(8, min_periods=2).sum(); tot = a.abs().rolling(8, min_periods=2).sum()
    result = _safe_div(neg, tot)
    return result.diff()


def f30_mcac_109_gm_accel_curve_signed_area_8q_d1(revenue, gp):
    result = _gm(revenue, gp).diff().diff().rolling(8, min_periods=3).sum()
    return result.diff()


def f30_mcac_110_om_ulcer_index_neg_dd_rms_8q_d1(revenue, opinc):
    a = _om(revenue, opinc).diff(); dd = (a.rolling(8, min_periods=3).max() - a).clip(lower=0)
    result = (dd ** 2).rolling(8, min_periods=3).mean().pow(0.5)
    return result.diff()


def f30_mcac_111_nm_drawdown_event_count_2pp_12q_d1(revenue, netinc):
    m = _nm(revenue, netinc); dd = m.rolling(12, min_periods=4).max() - m
    result = _rolling_count(dd > 0.02, 12)
    return result.diff()


def f30_mcac_112_gm_stairstep_down_count_8q_d1(revenue, gp):
    m = _gm(revenue, gp); nl = (m == m.rolling(12, min_periods=4).min()).astype(float)
    result = nl.rolling(8, min_periods=2).sum()
    return result.diff()


def f30_mcac_113_om_convex_chord_deviation_8q_d1(revenue, opinc):
    m = _om(revenue, opinc); chord = (m + m.shift(7)) / 2.0
    result = m.rolling(8, min_periods=3).mean() - chord
    return result.diff()


def f30_mcac_114_om_consecutive_decline_streak_d1(revenue, opinc):
    m = _om(revenue, opinc)
    result = _consec_true_streak(m < m.shift(1)).astype(float)
    return result.diff()


def f30_mcac_115_composite_margin_broken_down_score_8q_d1(revenue, gp, opinc):
    g = _gm(revenue, gp); o = _om(revenue, opinc)
    gd = (g.diff() < -0.02).astype(float).rolling(8, min_periods=2).sum(); od = (o.diff() < -0.02).astype(float).rolling(8, min_periods=2).sum()
    glo = (g == g.rolling(12, min_periods=4).min()).astype(float).rolling(8, min_periods=2).sum()
    result = gd.fillna(0) + od.fillna(0) + glo.fillna(0)
    return result.diff()


def f30_mcac_116_om_drawdown_acceleration_4q_d1(revenue, opinc):
    m = _om(revenue, opinc); dd = m.rolling(12, min_periods=4).max() - m
    result = dd - dd.shift(4)
    return result.diff()


def f30_mcac_117_gm_max_drawdown_16q_d1(revenue, gp):
    m = _gm(revenue, gp)
    result = m.rolling(16, min_periods=5).max() - m.rolling(16, min_periods=5).min()
    return result.diff()


def f30_mcac_118_om_accel_skew_8q_d1(revenue, opinc):
    result = _om(revenue, opinc).diff().diff().rolling(8, min_periods=4).skew()
    return result.diff()


def f30_mcac_119_om_accel_kurt_8q_d1(revenue, opinc):
    result = _om(revenue, opinc).diff().diff().rolling(8, min_periods=4).kurt()
    return result.diff()


def f30_mcac_120_gm_accel_skew_change_8q_vs_12q_d1(revenue, gp):
    a = _gm(revenue, gp).diff().diff()
    result = a.rolling(8, min_periods=4).skew() - a.rolling(12, min_periods=5).skew()
    return result.diff()


def f30_mcac_121_nm_accel_kurt_change_8q_vs_12q_d1(revenue, netinc):
    a = _nm(revenue, netinc).diff().diff()
    result = a.rolling(8, min_periods=4).kurt() - a.rolling(12, min_periods=5).kurt()
    return result.diff()


def f30_mcac_122_om_accel_cv_8q_d1(revenue, opinc):
    a = _om(revenue, opinc).diff().diff()
    result = _safe_div(a.rolling(8, min_periods=3).std(), a.rolling(8, min_periods=3).mean().abs())
    return result.diff()


def f30_mcac_123_gm_accel_quantile_dispersion_q90_q10_12q_d1(revenue, gp):
    a = _gm(revenue, gp).diff().diff()
    result = a.rolling(12, min_periods=4).quantile(0.9) - a.rolling(12, min_periods=4).quantile(0.1)
    return result.diff()


def f30_mcac_124_om_accel_neg_tail_4q_in_16q_q25_d1(revenue, opinc):
    a = _om(revenue, opinc).diff().diff(); q25 = a.rolling(16, min_periods=5).quantile(0.25)
    result = _rolling_count(a < q25, 4)
    return result.diff()


def f30_mcac_125_nm_accel_right_tail_collapse_q90_neg_8q_d1(revenue, netinc):
    a = _nm(revenue, netinc).diff().diff(); q90 = a.rolling(8, min_periods=3).quantile(0.9)
    result = (q90 < 0).astype(float).where(q90.notna(), np.nan)
    return result.diff()


def f30_mcac_126_gm_accel_median_z_signed_8q_d1(revenue, gp):
    a = _gm(revenue, gp).diff().diff()
    result = _safe_div(a.rolling(8, min_periods=3).median(), a.rolling(8, min_periods=3).std())
    return result.diff()


def f30_mcac_127_om_accel_mean_minus_median_8q_d1(revenue, opinc):
    a = _om(revenue, opinc).diff().diff()
    result = a.rolling(8, min_periods=3).mean() - a.rolling(8, min_periods=3).median()
    return result.diff()


def f30_mcac_128_gm_accel_winsorized_z_10pct_8q_d1(revenue, gp):
    a = _gm(revenue, gp).diff().diff(); w = _winsorize(a, 0.1, 0.9, 8)
    result = _rolling_zscore(w, 8)
    return result.diff()


def f30_mcac_129_om_accel_sign_runlength_var_8q_d1(revenue, opinc):
    a = _om(revenue, opinc).diff().diff(); sg = _sign_safe(a)
    flip = (sg != sg.shift(1)).astype(float)
    result = flip.rolling(8, min_periods=3).sum()
    return result.diff()


def f30_mcac_130_om_accel_persistence_lag1_8q_d1(revenue, opinc):
    a = _om(revenue, opinc).diff().diff()
    result = _safe_div((a * a.shift(1)).rolling(8, min_periods=3).sum(), (a ** 2).rolling(8, min_periods=3).sum())
    return result.diff()


def f30_mcac_131_gm_smoothed_raw_accel_sign_disagree_d1(revenue, gp):
    a = _gm(revenue, gp).diff().diff(); em = _ema(a, 4)
    result = (_sign_safe(em) != _sign_safe(a)).astype(float).where(a.notna() & em.notna(), np.nan)
    return result.diff()


def f30_mcac_132_om_ema_long_short_cross_disagree_d1(revenue, opinc):
    a = _om(revenue, opinc).diff().diff(); e4 = _ema(a, 4); e12 = _ema(a, 12)
    result = (_sign_safe(e4) != _sign_safe(e12)).astype(float).where(e4.notna() & e12.notna(), np.nan)
    return result.diff()


def f30_mcac_133_nm_ema4_below_ema12_persistent_3q_d1(revenue, netinc):
    a = _nm(revenue, netinc).diff().diff(); e4 = _ema(a, 4); e12 = _ema(a, 12)
    result = _max_consec_true(e4 < e12, 8).astype(float)
    return result.diff()


def f30_mcac_134_om_2nd_diff_zscore_8q_d1(revenue, opinc):
    c = _om(revenue, opinc).diff().diff().diff()
    result = _rolling_zscore(c, 8)
    return result.diff()


def f30_mcac_135_gm_2nd_diff_flip_pos_to_neg_d1(revenue, gp):
    c = _gm(revenue, gp).diff().diff().diff()
    result = ((c < 0) & (c.shift(1) >= 0)).astype(float).where(c.notna() & c.shift(1).notna(), np.nan)
    return result.diff()


def f30_mcac_136_nm_slope_sign_flip_pos_to_neg_d1(revenue, netinc):
    sl = _rolling_slope(_nm(revenue, netinc), 4)
    result = ((sl < 0) & (sl.shift(1) >= 0)).astype(float).where(sl.notna() & sl.shift(1).notna(), np.nan)
    return result.diff()


def f30_mcac_137_om_accel_slope_4q_d1(revenue, opinc):
    result = _rolling_slope(_om(revenue, opinc).diff().diff(), 4)
    return result.diff()


def f30_mcac_138_gm_dev_from_8q_median_d1(revenue, gp):
    m = _gm(revenue, gp)
    result = m - m.rolling(8, min_periods=3).median()
    return result.diff()


def f30_mcac_139_om_hampel_negative_outlier_12q_d1(revenue, opinc):
    a = _om(revenue, opinc).diff().diff(); med = a.rolling(12, min_periods=4).median(); mad = _rolling_mad(a, 12)
    result = ((med - a) > 3.0 * mad).astype(float).where(a.notna() & mad.notna(), np.nan)
    return result.diff()


def f30_mcac_140_nm_rolling_rank_pct_16q_d1(revenue, netinc):
    result = _rolling_rank_pct(_nm(revenue, netinc), 16)
    return result.diff()


def f30_mcac_141_composite_margin_crash_5_binaries_8q_d1(revenue, gp, opinc):
    g = _gm(revenue, gp); o = _om(revenue, opinc); ag = g.diff(); ao = o.diff()
    b1 = _rolling_count(ag < -0.02, 8); b2 = _rolling_count(ao < -0.02, 8); b3 = _rolling_count(g == g.rolling(12, min_periods=4).min(), 8); b4 = _rolling_count(o == o.rolling(12, min_periods=4).min(), 8); b5 = _consec_true_streak((ag < 0) & (ao < 0)).astype(float).rolling(8, min_periods=2).max()
    result = b1.fillna(0) + b2.fillna(0) + b3.fillna(0) + b4.fillna(0) + b5.fillna(0)
    return result.diff()


def f30_mcac_142_weighted_margin_crash_z_clip_m3_8q_d1(revenue, opinc):
    z = _rolling_zscore(_om(revenue, opinc).diff().diff(), 8).clip(lower=-3.0, upper=0)
    result = -z.rolling(8, min_periods=3).sum()
    return result.diff()


def f30_mcac_143_multi_horizon_margin_crash_score_om_d1(revenue, opinc):
    a = _om(revenue, opinc).diff().diff()
    z4 = _rolling_zscore(a, 4).clip(lower=-3, upper=0); z8 = _rolling_zscore(a, 8).clip(lower=-3, upper=0); z12 = _rolling_zscore(a, 12).clip(lower=-3, upper=0)
    result = -(z4 + z8 + z12)
    return result.diff()


def f30_mcac_144_ewm_decay_margin_crash_8q_nm_neg_d1(revenue, netinc):
    a = _nm(revenue, netinc).diff().clip(upper=0)
    result = -a.ewm(span=8, adjust=False, min_periods=3).mean()
    return result.diff()


def f30_mcac_145_logit_margin_crash_probability_om_d1(revenue, opinc):
    z = _rolling_zscore(_om(revenue, opinc).diff().diff(), 12)
    result = 1.0 / (1.0 + np.exp(z.clip(lower=-10, upper=10)))
    return result.diff()


def f30_mcac_146_mahalanobis_dist_om_accel_slope_8q_d1(revenue, opinc):
    a = _om(revenue, opinc).diff().diff(); s = _rolling_slope(a, 8)
    za = _rolling_zscore(a, 12); zs = _rolling_zscore(s, 12)
    result = (za ** 2 + zs ** 2).pow(0.5)
    return result.diff()


def f30_mcac_147_hotelling_t_om_accel_vol_8q_d1(revenue, opinc):
    a = _om(revenue, opinc).diff().diff(); v = a.rolling(4, min_periods=2).std()
    za = _rolling_zscore(a, 12); zv = _rolling_zscore(v, 12)
    result = za.abs() + zv.abs()
    return result.diff()


def f30_mcac_148_nm_terminal_distance_5y_proxy_d1(revenue, netinc):
    m = _nm(revenue, netinc); mn = m.rolling(20, min_periods=6).min(); mx = m.rolling(20, min_periods=6).max()
    result = _safe_div(m - mn, mx.abs())
    return result.diff()


def f30_mcac_149_margin_trend_velocity_collapse_4q_over_12q_d1(revenue, opinc):
    m = _om(revenue, opinc); s4 = _rolling_slope(m, 4); s12 = _rolling_slope(m, 12)
    result = _safe_div(s4, s12.abs())
    return result.diff()


def f30_mcac_150_all_margins_firing_down_composite_8q_d1(revenue, gp, opinc, ebitda, netinc):
    g = _rolling_zscore(_gm(revenue, gp).diff().diff(), 8); o = _rolling_zscore(_om(revenue, opinc).diff().diff(), 8); e = _rolling_zscore(_em(revenue, ebitda).diff().diff(), 8); n = _rolling_zscore(_nm(revenue, netinc).diff().diff(), 8)
    z = pd.concat([g, o, e, n], axis=1).clip(lower=-3, upper=0)
    result = -z.sum(axis=1)
    return result.diff()


MARGIN_COLLAPSE_ACCELERATION_D1_REGISTRY_076_150 = {
    "f30_mcac_076_rev_growing_margins_down_indicator_gm_d1": {"inputs": ["revenue", "gp"], "func": f30_mcac_076_rev_growing_margins_down_indicator_gm_d1},
    "f30_mcac_077_rev_growing_margins_down_indicator_om_d1": {"inputs": ["revenue", "opinc"], "func": f30_mcac_077_rev_growing_margins_down_indicator_om_d1},
    "f30_mcac_078_rev_growing_margins_down_indicator_nm_d1": {"inputs": ["revenue", "netinc"], "func": f30_mcac_078_rev_growing_margins_down_indicator_nm_d1},
    "f30_mcac_079_operating_deleverage_om_vs_rev_growth_8q_d1": {"inputs": ["revenue", "opinc"], "func": f30_mcac_079_operating_deleverage_om_vs_rev_growth_8q_d1},
    "f30_mcac_080_operating_deleverage_intensity_d1": {"inputs": ["revenue", "opinc"], "func": f30_mcac_080_operating_deleverage_intensity_d1},
    "f30_mcac_081_rev_up_om_down_streak_d1": {"inputs": ["revenue", "opinc"], "func": f30_mcac_081_rev_up_om_down_streak_d1},
    "f30_mcac_082_rev_up_gm_down_count_8q_d1": {"inputs": ["revenue", "gp"], "func": f30_mcac_082_rev_up_gm_down_count_8q_d1},
    "f30_mcac_083_cogs_accel_minus_rev_accel_gap_yoy_d1": {"inputs": ["revenue", "cogs"], "func": f30_mcac_083_cogs_accel_minus_rev_accel_gap_yoy_d1},
    "f30_mcac_084_sgna_accel_minus_rev_accel_gap_yoy_d1": {"inputs": ["revenue", "sgna"], "func": f30_mcac_084_sgna_accel_minus_rev_accel_gap_yoy_d1},
    "f30_mcac_085_opex_accel_minus_rev_accel_gap_yoy_d1": {"inputs": ["revenue", "opex"], "func": f30_mcac_085_opex_accel_minus_rev_accel_gap_yoy_d1},
    "f30_mcac_086_cogs_to_rev_accel_zscore_8q_d1": {"inputs": ["revenue", "cogs"], "func": f30_mcac_086_cogs_to_rev_accel_zscore_8q_d1},
    "f30_mcac_087_sgna_to_rev_accel_zscore_8q_d1": {"inputs": ["revenue", "sgna"], "func": f30_mcac_087_sgna_to_rev_accel_zscore_8q_d1},
    "f30_mcac_088_opex_to_rev_accel_zscore_8q_d1": {"inputs": ["revenue", "opex"], "func": f30_mcac_088_opex_to_rev_accel_zscore_8q_d1},
    "f30_mcac_089_depamor_to_rev_accel_zscore_8q_d1": {"inputs": ["revenue", "depamor"], "func": f30_mcac_089_depamor_to_rev_accel_zscore_8q_d1},
    "f30_mcac_090_cost_stack_synchronized_jump_indicator_d1": {"inputs": ["revenue", "cogs", "sgna", "opex"], "func": f30_mcac_090_cost_stack_synchronized_jump_indicator_d1},
    "f30_mcac_091_cost_stack_synchronized_jump_count_8q_d1": {"inputs": ["revenue", "cogs", "sgna", "opex"], "func": f30_mcac_091_cost_stack_synchronized_jump_count_8q_d1},
    "f30_mcac_092_gm_om_spread_collapse_8q_d1": {"inputs": ["revenue", "gp", "opinc"], "func": f30_mcac_092_gm_om_spread_collapse_8q_d1},
    "f30_mcac_093_om_nm_spread_collapse_8q_d1": {"inputs": ["revenue", "opinc", "netinc"], "func": f30_mcac_093_om_nm_spread_collapse_8q_d1},
    "f30_mcac_094_em_gm_ratio_collapse_8q_d1": {"inputs": ["revenue", "gp", "ebitda"], "func": f30_mcac_094_em_gm_ratio_collapse_8q_d1},
    "f30_mcac_095_gm_om_em_nm_descending_invariant_breach_d1": {"inputs": ["revenue", "gp", "opinc", "ebitda", "netinc"], "func": f30_mcac_095_gm_om_em_nm_descending_invariant_breach_d1},
    "f30_mcac_096_cogs_to_rev_jump_one_q_3pp_d1": {"inputs": ["revenue", "cogs"], "func": f30_mcac_096_cogs_to_rev_jump_one_q_3pp_d1},
    "f30_mcac_097_sgna_to_rev_jump_one_q_2pp_d1": {"inputs": ["revenue", "sgna"], "func": f30_mcac_097_sgna_to_rev_jump_one_q_2pp_d1},
    "f30_mcac_098_depamor_to_rev_jump_one_q_1pp_d1": {"inputs": ["revenue", "depamor"], "func": f30_mcac_098_depamor_to_rev_jump_one_q_1pp_d1},
    "f30_mcac_099_cost_jumps_count_8q_any_line_d1": {"inputs": ["revenue", "cogs", "sgna", "opex"], "func": f30_mcac_099_cost_jumps_count_8q_any_line_d1},
    "f30_mcac_100_cost_jumps_count_8q_2plus_lines_d1": {"inputs": ["revenue", "cogs", "sgna", "opex"], "func": f30_mcac_100_cost_jumps_count_8q_2plus_lines_d1},
    "f30_mcac_101_gm_drawdown_from_12q_max_d1": {"inputs": ["revenue", "gp"], "func": f30_mcac_101_gm_drawdown_from_12q_max_d1},
    "f30_mcac_102_om_drawdown_from_12q_max_d1": {"inputs": ["revenue", "opinc"], "func": f30_mcac_102_om_drawdown_from_12q_max_d1},
    "f30_mcac_103_nm_drawdown_from_16q_max_d1": {"inputs": ["revenue", "netinc"], "func": f30_mcac_103_nm_drawdown_from_16q_max_d1},
    "f30_mcac_104_em_drawdown_from_12q_max_d1": {"inputs": ["revenue", "ebitda"], "func": f30_mcac_104_em_drawdown_from_12q_max_d1},
    "f30_mcac_105_om_q_since_12q_max_d1": {"inputs": ["revenue", "opinc"], "func": f30_mcac_105_om_q_since_12q_max_d1},
    "f30_mcac_106_gm_drawdown_velocity_8q_d1": {"inputs": ["revenue", "gp"], "func": f30_mcac_106_gm_drawdown_velocity_8q_d1},
    "f30_mcac_107_om_recovery_rate_from_8q_min_d1": {"inputs": ["revenue", "opinc"], "func": f30_mcac_107_om_recovery_rate_from_8q_min_d1},
    "f30_mcac_108_om_accel_pain_ratio_8q_d1": {"inputs": ["revenue", "opinc"], "func": f30_mcac_108_om_accel_pain_ratio_8q_d1},
    "f30_mcac_109_gm_accel_curve_signed_area_8q_d1": {"inputs": ["revenue", "gp"], "func": f30_mcac_109_gm_accel_curve_signed_area_8q_d1},
    "f30_mcac_110_om_ulcer_index_neg_dd_rms_8q_d1": {"inputs": ["revenue", "opinc"], "func": f30_mcac_110_om_ulcer_index_neg_dd_rms_8q_d1},
    "f30_mcac_111_nm_drawdown_event_count_2pp_12q_d1": {"inputs": ["revenue", "netinc"], "func": f30_mcac_111_nm_drawdown_event_count_2pp_12q_d1},
    "f30_mcac_112_gm_stairstep_down_count_8q_d1": {"inputs": ["revenue", "gp"], "func": f30_mcac_112_gm_stairstep_down_count_8q_d1},
    "f30_mcac_113_om_convex_chord_deviation_8q_d1": {"inputs": ["revenue", "opinc"], "func": f30_mcac_113_om_convex_chord_deviation_8q_d1},
    "f30_mcac_114_om_consecutive_decline_streak_d1": {"inputs": ["revenue", "opinc"], "func": f30_mcac_114_om_consecutive_decline_streak_d1},
    "f30_mcac_115_composite_margin_broken_down_score_8q_d1": {"inputs": ["revenue", "gp", "opinc"], "func": f30_mcac_115_composite_margin_broken_down_score_8q_d1},
    "f30_mcac_116_om_drawdown_acceleration_4q_d1": {"inputs": ["revenue", "opinc"], "func": f30_mcac_116_om_drawdown_acceleration_4q_d1},
    "f30_mcac_117_gm_max_drawdown_16q_d1": {"inputs": ["revenue", "gp"], "func": f30_mcac_117_gm_max_drawdown_16q_d1},
    "f30_mcac_118_om_accel_skew_8q_d1": {"inputs": ["revenue", "opinc"], "func": f30_mcac_118_om_accel_skew_8q_d1},
    "f30_mcac_119_om_accel_kurt_8q_d1": {"inputs": ["revenue", "opinc"], "func": f30_mcac_119_om_accel_kurt_8q_d1},
    "f30_mcac_120_gm_accel_skew_change_8q_vs_12q_d1": {"inputs": ["revenue", "gp"], "func": f30_mcac_120_gm_accel_skew_change_8q_vs_12q_d1},
    "f30_mcac_121_nm_accel_kurt_change_8q_vs_12q_d1": {"inputs": ["revenue", "netinc"], "func": f30_mcac_121_nm_accel_kurt_change_8q_vs_12q_d1},
    "f30_mcac_122_om_accel_cv_8q_d1": {"inputs": ["revenue", "opinc"], "func": f30_mcac_122_om_accel_cv_8q_d1},
    "f30_mcac_123_gm_accel_quantile_dispersion_q90_q10_12q_d1": {"inputs": ["revenue", "gp"], "func": f30_mcac_123_gm_accel_quantile_dispersion_q90_q10_12q_d1},
    "f30_mcac_124_om_accel_neg_tail_4q_in_16q_q25_d1": {"inputs": ["revenue", "opinc"], "func": f30_mcac_124_om_accel_neg_tail_4q_in_16q_q25_d1},
    "f30_mcac_125_nm_accel_right_tail_collapse_q90_neg_8q_d1": {"inputs": ["revenue", "netinc"], "func": f30_mcac_125_nm_accel_right_tail_collapse_q90_neg_8q_d1},
    "f30_mcac_126_gm_accel_median_z_signed_8q_d1": {"inputs": ["revenue", "gp"], "func": f30_mcac_126_gm_accel_median_z_signed_8q_d1},
    "f30_mcac_127_om_accel_mean_minus_median_8q_d1": {"inputs": ["revenue", "opinc"], "func": f30_mcac_127_om_accel_mean_minus_median_8q_d1},
    "f30_mcac_128_gm_accel_winsorized_z_10pct_8q_d1": {"inputs": ["revenue", "gp"], "func": f30_mcac_128_gm_accel_winsorized_z_10pct_8q_d1},
    "f30_mcac_129_om_accel_sign_runlength_var_8q_d1": {"inputs": ["revenue", "opinc"], "func": f30_mcac_129_om_accel_sign_runlength_var_8q_d1},
    "f30_mcac_130_om_accel_persistence_lag1_8q_d1": {"inputs": ["revenue", "opinc"], "func": f30_mcac_130_om_accel_persistence_lag1_8q_d1},
    "f30_mcac_131_gm_smoothed_raw_accel_sign_disagree_d1": {"inputs": ["revenue", "gp"], "func": f30_mcac_131_gm_smoothed_raw_accel_sign_disagree_d1},
    "f30_mcac_132_om_ema_long_short_cross_disagree_d1": {"inputs": ["revenue", "opinc"], "func": f30_mcac_132_om_ema_long_short_cross_disagree_d1},
    "f30_mcac_133_nm_ema4_below_ema12_persistent_3q_d1": {"inputs": ["revenue", "netinc"], "func": f30_mcac_133_nm_ema4_below_ema12_persistent_3q_d1},
    "f30_mcac_134_om_2nd_diff_zscore_8q_d1": {"inputs": ["revenue", "opinc"], "func": f30_mcac_134_om_2nd_diff_zscore_8q_d1},
    "f30_mcac_135_gm_2nd_diff_flip_pos_to_neg_d1": {"inputs": ["revenue", "gp"], "func": f30_mcac_135_gm_2nd_diff_flip_pos_to_neg_d1},
    "f30_mcac_136_nm_slope_sign_flip_pos_to_neg_d1": {"inputs": ["revenue", "netinc"], "func": f30_mcac_136_nm_slope_sign_flip_pos_to_neg_d1},
    "f30_mcac_137_om_accel_slope_4q_d1": {"inputs": ["revenue", "opinc"], "func": f30_mcac_137_om_accel_slope_4q_d1},
    "f30_mcac_138_gm_dev_from_8q_median_d1": {"inputs": ["revenue", "gp"], "func": f30_mcac_138_gm_dev_from_8q_median_d1},
    "f30_mcac_139_om_hampel_negative_outlier_12q_d1": {"inputs": ["revenue", "opinc"], "func": f30_mcac_139_om_hampel_negative_outlier_12q_d1},
    "f30_mcac_140_nm_rolling_rank_pct_16q_d1": {"inputs": ["revenue", "netinc"], "func": f30_mcac_140_nm_rolling_rank_pct_16q_d1},
    "f30_mcac_141_composite_margin_crash_5_binaries_8q_d1": {"inputs": ["revenue", "gp", "opinc"], "func": f30_mcac_141_composite_margin_crash_5_binaries_8q_d1},
    "f30_mcac_142_weighted_margin_crash_z_clip_m3_8q_d1": {"inputs": ["revenue", "opinc"], "func": f30_mcac_142_weighted_margin_crash_z_clip_m3_8q_d1},
    "f30_mcac_143_multi_horizon_margin_crash_score_om_d1": {"inputs": ["revenue", "opinc"], "func": f30_mcac_143_multi_horizon_margin_crash_score_om_d1},
    "f30_mcac_144_ewm_decay_margin_crash_8q_nm_neg_d1": {"inputs": ["revenue", "netinc"], "func": f30_mcac_144_ewm_decay_margin_crash_8q_nm_neg_d1},
    "f30_mcac_145_logit_margin_crash_probability_om_d1": {"inputs": ["revenue", "opinc"], "func": f30_mcac_145_logit_margin_crash_probability_om_d1},
    "f30_mcac_146_mahalanobis_dist_om_accel_slope_8q_d1": {"inputs": ["revenue", "opinc"], "func": f30_mcac_146_mahalanobis_dist_om_accel_slope_8q_d1},
    "f30_mcac_147_hotelling_t_om_accel_vol_8q_d1": {"inputs": ["revenue", "opinc"], "func": f30_mcac_147_hotelling_t_om_accel_vol_8q_d1},
    "f30_mcac_148_nm_terminal_distance_5y_proxy_d1": {"inputs": ["revenue", "netinc"], "func": f30_mcac_148_nm_terminal_distance_5y_proxy_d1},
    "f30_mcac_149_margin_trend_velocity_collapse_4q_over_12q_d1": {"inputs": ["revenue", "opinc"], "func": f30_mcac_149_margin_trend_velocity_collapse_4q_over_12q_d1},
    "f30_mcac_150_all_margins_firing_down_composite_8q_d1": {"inputs": ["revenue", "gp", "opinc", "ebitda", "netinc"], "func": f30_mcac_150_all_margins_firing_down_composite_8q_d1},
}
