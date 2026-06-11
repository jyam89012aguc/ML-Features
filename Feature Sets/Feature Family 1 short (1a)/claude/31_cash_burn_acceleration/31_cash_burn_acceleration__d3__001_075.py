"""cash_burn_acceleration d3 features 001_075 — Pipeline 1a-inverse short-side blowup family.

Pattern-detection hypotheses on cash-burn acceleration: cliff-edges, runway crashes,
regime transitions, compound co-deterioration of cash flow / cash balance / capex coverage.
Distinct from family 13 (cbsp — levels) and family 23 (cfdt — slopes). Per HANDOFF §6
families 29-36 special rule: base = pattern features on cash-burn acceleration.
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


def _burn(ncfo):
    """Positive burn = negative OCF magnitude."""
    return (-ncfo).clip(lower=0)


def _ncfo_to_assets(ncfo, assets):
    return _safe_div(ncfo, assets.abs())


def _fcf_to_assets(fcf, assets):
    return _safe_div(fcf, assets.abs())


def _ncfo_to_revenue(ncfo, revenue):
    return _safe_div(_ttm(ncfo), _ttm(revenue).abs())


def _fcf_to_revenue(fcf, revenue):
    return _safe_div(_ttm(fcf), _ttm(revenue).abs())


def _runway_q(cashneq, ncfo):
    burn_q = (-_ttm(ncfo) / 4.0).clip(lower=1e-9)
    return _safe_div(cashneq, burn_q)


def f31_cbac_001_ncfo_accel_zscore_8q_d3(ncfo):
    a = ncfo.diff().diff()
    result = _rolling_zscore(a, 8)
    return result.diff().diff().diff()


def f31_cbac_002_fcf_accel_zscore_8q_d3(fcf):
    a = fcf.diff().diff()
    result = _rolling_zscore(a, 8)
    return result.diff().diff().diff()


def f31_cbac_003_cashneq_accel_zscore_8q_d3(cashneq):
    a = cashneq.diff().diff()
    result = _rolling_zscore(a, 8)
    return result.diff().diff().diff()


def f31_cbac_004_ncfo_to_assets_accel_zscore_8q_d3(ncfo, assets):
    r = _safe_div(ncfo, assets.abs())
    result = _rolling_zscore(r.diff().diff(), 8)
    return result.diff().diff().diff()


def f31_cbac_005_fcf_to_assets_accel_zscore_8q_d3(fcf, assets):
    r = _safe_div(fcf, assets.abs())
    result = _rolling_zscore(r.diff().diff(), 8)
    return result.diff().diff().diff()


def f31_cbac_006_ncfo_accel_below_m2sd_8q_d3(ncfo):
    a = ncfo.diff().diff(); z = _rolling_zscore(a, 8)
    result = (z < -2.0).astype(float).where(z.notna(), np.nan)
    return result.diff().diff().diff()


def f31_cbac_007_fcf_drop_from_8q_max_d3(fcf):
    result = fcf - fcf.rolling(8, min_periods=3).max()
    return result.diff().diff().diff()


def f31_cbac_008_ncfo_drop_from_8q_max_d3(ncfo):
    result = ncfo - ncfo.rolling(8, min_periods=3).max()
    return result.diff().diff().diff()


def f31_cbac_009_cashneq_drop_from_12q_max_d3(cashneq):
    result = cashneq - cashneq.rolling(12, min_periods=4).max()
    return result.diff().diff().diff()


def f31_cbac_010_fcf_one_q_cliff_50pct_of_assets_d3(fcf, assets):
    d = _safe_div(fcf.diff(), assets.abs())
    result = (d < -0.05).astype(float).where(d.notna(), np.nan)
    return result.diff().diff().diff()


def f31_cbac_011_ncfo_one_q_cliff_50pct_of_assets_d3(ncfo, assets):
    d = _safe_div(ncfo.diff(), assets.abs())
    result = (d < -0.05).astype(float).where(d.notna(), np.nan)
    return result.diff().diff().diff()


def f31_cbac_012_fcf_negative_streak_d3(fcf):
    result = _consec_true_streak(fcf < 0).astype(float)
    return result.diff().diff().diff()


def f31_cbac_013_ncfo_negative_streak_d3(ncfo):
    result = _consec_true_streak(ncfo < 0).astype(float)
    return result.diff().diff().diff()


def f31_cbac_014_cashneq_decline_streak_d3(cashneq):
    result = _consec_true_streak(cashneq < cashneq.shift(1)).astype(float)
    return result.diff().diff().diff()


def f31_cbac_015_fcf_negative_count_8q_d3(fcf):
    result = _rolling_count(fcf < 0, 8)
    return result.diff().diff().diff()


def f31_cbac_016_ncfo_accel_jump_magnitude_vs_8q_mad_d3(ncfo):
    a = ncfo.diff().diff(); mad = _rolling_mad(a, 8)
    result = _safe_div(a.abs(), mad)
    return result.diff().diff().diff()


def f31_cbac_017_fcf_accel_range_position_8q_d3(fcf):
    a = fcf.diff().diff(); mn = a.rolling(8, min_periods=3).min(); mx = a.rolling(8, min_periods=3).max()
    result = _safe_div(a - mn, mx - mn)
    return result.diff().diff().diff()


def f31_cbac_018_cashneq_accel_in_worst_quartile_12q_d3(cashneq):
    a = cashneq.diff().diff(); q25 = _rolling_quantile(a, 12, 0.25)
    result = (a <= q25).astype(float).where(a.notna(), np.nan)
    return result.diff().diff().diff()


def f31_cbac_019_fcf_strictly_decreasing_streak_d3(fcf):
    b = (fcf < fcf.shift(1)) & (fcf.shift(1) < fcf.shift(2))
    result = _consec_true_streak(b).astype(float)
    return result.diff().diff().diff()


def f31_cbac_020_ncfo_hard_floor_breach_neg25_of_assets_8q_d3(ncfo, assets):
    r = _safe_div(ncfo, assets.abs())
    result = _rolling_count(r < -0.25, 8)
    return result.diff().diff().diff()


def f31_cbac_021_ncfo_slope_4q_sign_flip_d3(ncfo):
    sl = _rolling_slope(ncfo, 4)
    result = (_sign_safe(sl) != _sign_safe(sl.shift(1))).astype(float).where(sl.notna() & sl.shift(1).notna(), np.nan)
    return result.diff().diff().diff()


def f31_cbac_022_fcf_ema4_sign_flip_pos_to_neg_d3(fcf):
    em = _ema(fcf, 4)
    result = ((em < 0) & (em.shift(1) >= 0)).astype(float).where(em.notna() & em.shift(1).notna(), np.nan)
    return result.diff().diff().diff()


def f31_cbac_023_cashneq_inflection_magnitude_8q_d3(cashneq):
    a = cashneq.diff().diff(); sd = a.rolling(12, min_periods=4).std()
    result = _safe_div((a - a.shift(8)).abs(), sd)
    return result.diff().diff().diff()


def f31_cbac_024_ncfo_mean_shift_z_4v12_d3(ncfo):
    m4 = ncfo.rolling(4, min_periods=2).mean(); m12 = ncfo.rolling(12, min_periods=4).mean(); s12 = ncfo.rolling(12, min_periods=4).std()
    result = _safe_div(m4 - m12, s12)
    return result.diff().diff().diff()


def f31_cbac_025_fcf_mean_shift_down_indicator_d3(fcf):
    m4 = fcf.rolling(4, min_periods=2).mean(); m12 = fcf.rolling(12, min_periods=4).mean(); s12 = fcf.rolling(12, min_periods=4).std()
    z = _safe_div(m4 - m12, s12)
    result = (z < -1.0).astype(float).where(z.notna(), np.nan)
    return result.diff().diff().diff()


def f31_cbac_026_ncfo_variance_ratio_4q_12q_d3(ncfo):
    a = ncfo.diff().diff()
    result = _safe_div(a.rolling(4, min_periods=2).var(), a.rolling(12, min_periods=4).var())
    return result.diff().diff().diff()


def f31_cbac_027_fcf_variance_jump_zscore_16q_d3(fcf):
    a = fcf.diff().diff()
    vr = _safe_div(a.rolling(4, min_periods=2).var(), a.rolling(12, min_periods=4).var())
    result = _rolling_zscore(vr, 16)
    return result.diff().diff().diff()


def f31_cbac_028_cashneq_var_shift_up_indicator_d3(cashneq):
    a = cashneq.diff().diff()
    vr = _safe_div(a.rolling(4, min_periods=2).var(), a.rolling(12, min_periods=4).var())
    result = (vr > 2.0).astype(float).where(vr.notna(), np.nan)
    return result.diff().diff().diff()


def f31_cbac_029_ncfo_regime_stickiness_bad_quartile_4q_in_20q_d3(ncfo):
    q25 = _rolling_quantile(ncfo, 20, 0.25)
    result = _rolling_frac(ncfo <= q25, 4)
    return result.diff().diff().diff()


def f31_cbac_030_fcf_new_low_12q_indicator_d3(fcf):
    result = (fcf == fcf.rolling(12, min_periods=4).min()).astype(float).where(fcf.notna(), np.nan)
    return result.diff().diff().diff()


def f31_cbac_031_ncfo_fcf_compound_new_low_12q_d3(ncfo, fcf):
    a = (ncfo == ncfo.rolling(12, min_periods=4).min()); b = (fcf == fcf.rolling(12, min_periods=4).min())
    result = (a & b).astype(float).where(ncfo.notna() & fcf.notna(), np.nan)
    return result.diff().diff().diff()


def f31_cbac_032_cashneq_chow_fstat_proxy_12q_d3(cashneq):
    m1 = cashneq.rolling(6, min_periods=3).mean().shift(6); m2 = cashneq.rolling(6, min_periods=3).mean(); s12 = cashneq.rolling(12, min_periods=4).std()
    result = _safe_div((m1 - m2).abs(), s12)
    return result.diff().diff().diff()


def f31_cbac_033_ncfo_concavity_sign_d3(ncfo):
    result = _sign_safe(ncfo.diff().diff())
    return result.diff().diff().diff()


def f31_cbac_034_fcf_convexity_flip_pos_to_neg_d3(fcf):
    c = fcf.diff().diff()
    result = ((c < 0) & (c.shift(1) >= 0)).astype(float).where(c.notna() & c.shift(1).notna(), np.nan)
    return result.diff().diff().diff()


def f31_cbac_035_cashneq_convexity_flip_neg_to_pos_d3(cashneq):
    c = cashneq.diff().diff()
    result = ((c > 0) & (c.shift(1) <= 0)).astype(float).where(c.notna() & c.shift(1).notna(), np.nan)
    return result.diff().diff().diff()


def f31_cbac_036_ncfo_phase_shift_4q_vs_12q_norm_d3(ncfo):
    m4 = ncfo.rolling(4, min_periods=2).mean(); m12 = ncfo.rolling(12, min_periods=4).mean()
    result = _safe_div(m4 - m12, m12.abs())
    return result.diff().diff().diff()


def f31_cbac_037_fcf_ar1_persistence_8q_d3(fcf):
    result = fcf.rolling(8, min_periods=4).corr(fcf.shift(1))
    return result.diff().diff().diff()


def f31_cbac_038_ncfo_persistence_collapse_4q_d3(ncfo):
    ar = ncfo.rolling(8, min_periods=4).corr(ncfo.shift(1))
    result = ((ar < 0) & (ar.shift(4) > 0.5)).astype(float).where(ar.notna() & ar.shift(4).notna(), np.nan)
    return result.diff().diff().diff()


def f31_cbac_039_cashneq_local_concavity_test_d3(cashneq):
    result = _sign_safe(cashneq.diff().diff())
    return result.diff().diff().diff()


def f31_cbac_040_ncfo_break_recency_max_split_diff_12q_d3(ncfo):
    diffs = pd.concat([(ncfo.rolling(k, min_periods=2).mean().shift(12 - k) - ncfo.rolling(12 - k, min_periods=2).mean()).abs().rename(k) for k in range(3, 10)], axis=1)
    result = diffs.idxmax(axis=1).where(ncfo.notna(), np.nan).astype(float)
    return result.diff().diff().diff()


def f31_cbac_041_runway_quarters_current_d3(cashneq, ncfo):
    result = _runway_q(cashneq, ncfo)
    return result.diff().diff().diff()


def f31_cbac_042_runway_qoq_diff_qtrs_lost_d3(cashneq, ncfo):
    rw = _runway_q(cashneq, ncfo)
    result = -rw.diff()
    return result.diff().diff().diff()


def f31_cbac_043_runway_acceleration_diff_diff_d3(cashneq, ncfo):
    rw = _runway_q(cashneq, ncfo)
    result = -rw.diff().diff()
    return result.diff().diff().diff()


def f31_cbac_044_runway_pct_drop_4q_d3(cashneq, ncfo):
    rw = _runway_q(cashneq, ncfo)
    result = _safe_div(rw.shift(4) - rw, rw.shift(4).abs())
    return result.diff().diff().diff()


def f31_cbac_045_runway_pct_drop_8q_d3(cashneq, ncfo):
    rw = _runway_q(cashneq, ncfo)
    result = _safe_div(rw.shift(8) - rw, rw.shift(8).abs())
    return result.diff().diff().diff()


def f31_cbac_046_runway_below_4q_indicator_d3(cashneq, ncfo):
    rw = _runway_q(cashneq, ncfo)
    result = (rw < 4.0).astype(float).where(rw.notna(), np.nan)
    return result.diff().diff().diff()


def f31_cbac_047_runway_below_2q_indicator_d3(cashneq, ncfo):
    rw = _runway_q(cashneq, ncfo)
    result = (rw < 2.0).astype(float).where(rw.notna(), np.nan)
    return result.diff().diff().diff()


def f31_cbac_048_runway_drop_from_8q_max_d3(cashneq, ncfo):
    rw = _runway_q(cashneq, ncfo)
    result = rw - rw.rolling(8, min_periods=3).max()
    return result.diff().diff().diff()


def f31_cbac_049_runway_drop_velocity_8q_d3(cashneq, ncfo):
    rw = _runway_q(cashneq, ncfo); depth = rw.rolling(12, min_periods=4).max() - rw
    dur = rw.rolling(12, min_periods=4).apply(lambda w: float(len(w) - 1 - int(np.nanargmax(w))) if not np.isnan(w).all() else np.nan, raw=True)
    result = _safe_div(depth, dur.replace(0, np.nan))
    return result.diff().diff().diff()


def f31_cbac_050_runway_new_low_12q_indicator_d3(cashneq, ncfo):
    rw = _runway_q(cashneq, ncfo)
    result = (rw == rw.rolling(12, min_periods=4).min()).astype(float).where(rw.notna(), np.nan)
    return result.diff().diff().diff()


def f31_cbac_051_runway_zscore_collapse_12q_d3(cashneq, ncfo):
    rw = _runway_q(cashneq, ncfo); z = _rolling_zscore(rw, 12)
    result = (z < -2.0).astype(float).where(z.notna(), np.nan)
    return result.diff().diff().diff()


def f31_cbac_052_burn_rate_acceleration_qoq_d3(ncfo):
    burn = _burn(ncfo)
    result = burn.diff()
    return result.diff().diff().diff()


def f31_cbac_053_burn_rate_zscore_8q_d3(ncfo):
    burn = _burn(ncfo)
    result = _rolling_zscore(burn, 8)
    return result.diff().diff().diff()


def f31_cbac_054_burn_rate_doubling_indicator_yoy_d3(ncfo):
    burn = _burn(ncfo)
    result = (burn > 2.0 * burn.shift(4)).astype(float).where(burn.notna() & burn.shift(4).notna(), np.nan)
    return result.diff().diff().diff()


def f31_cbac_055_cashneq_below_4q_burn_indicator_d3(ncfo, cashneq):
    burn4 = _burn(ncfo).rolling(4, min_periods=2).sum()
    result = (cashneq < burn4).astype(float).where(cashneq.notna() & burn4.notna(), np.nan)
    return result.diff().diff().diff()


def f31_cbac_056_cashneq_to_4q_burn_ratio_d3(ncfo, cashneq):
    burn4 = _burn(ncfo).rolling(4, min_periods=2).sum().replace(0, np.nan)
    result = _safe_div(cashneq, burn4)
    return result.diff().diff().diff()


def f31_cbac_057_cashneq_to_4q_burn_ratio_qoq_drop_d3(ncfo, cashneq):
    burn4 = _burn(ncfo).rolling(4, min_periods=2).sum().replace(0, np.nan); r = _safe_div(cashneq, burn4)
    result = -r.diff()
    return result.diff().diff().diff()


def f31_cbac_058_fcf_burn_intensity_pct_of_assets_d3(fcf, assets):
    result = -_safe_div(_ttm(fcf).clip(upper=0), assets.abs())
    return result.diff().diff().diff()


def f31_cbac_059_fcf_burn_intensity_acceleration_d3(fcf, assets):
    bi = -_safe_div(_ttm(fcf).clip(upper=0), assets.abs())
    result = bi.diff().diff()
    return result.diff().diff().diff()


def f31_cbac_060_runway_terminal_distance_proxy_d3(cashneq, ncfo):
    rw = _runway_q(cashneq, ncfo); mn = rw.rolling(20, min_periods=6).min(); mx = rw.rolling(20, min_periods=6).max()
    result = _safe_div(rw - mn, mx - mn)
    return result.diff().diff().diff()


def f31_cbac_061_ncfo_fcf_both_decline_indicator_d3(ncfo, fcf):
    result = ((ncfo.diff() < 0) & (fcf.diff() < 0)).astype(float).where(ncfo.diff().notna() & fcf.diff().notna(), np.nan)
    return result.diff().diff().diff()


def f31_cbac_062_ncfo_fcf_cashneq_triple_decline_indicator_d3(ncfo, fcf, cashneq):
    result = ((ncfo.diff() < 0) & (fcf.diff() < 0) & (cashneq.diff() < 0)).astype(float).where(ncfo.diff().notna() & fcf.diff().notna() & cashneq.diff().notna(), np.nan)
    return result.diff().diff().diff()


def f31_cbac_063_ncfo_fcf_cashneq_co_decline_streak_d3(ncfo, fcf, cashneq):
    b = (ncfo.diff() < 0) & (fcf.diff() < 0) & (cashneq.diff() < 0)
    result = _consec_true_streak(b).astype(float)
    return result.diff().diff().diff()


def f31_cbac_064_ncfo_fcf_co_decline_fraction_8q_d3(ncfo, fcf):
    result = _rolling_frac((ncfo.diff() < 0) & (fcf.diff() < 0), 8)
    return result.diff().diff().diff()


def f31_cbac_065_three_cash_compound_score_signed_8q_d3(ncfo, fcf, cashneq):
    zn = _rolling_zscore(ncfo.diff(), 8); zf = _rolling_zscore(fcf.diff(), 8); zc = _rolling_zscore(cashneq.diff(), 8)
    result = pd.concat([zn, zf, zc], axis=1).mean(axis=1)
    return result.diff().diff().diff()


def f31_cbac_066_three_cash_compound_score_abs_8q_d3(ncfo, fcf, cashneq):
    zn = _rolling_zscore(ncfo.diff(), 8); zf = _rolling_zscore(fcf.diff(), 8); zc = _rolling_zscore(cashneq.diff(), 8)
    result = pd.concat([zn.abs(), zf.abs(), zc.abs()], axis=1).mean(axis=1)
    return result.diff().diff().diff()


def f31_cbac_067_three_cash_dispersion_z_8q_d3(ncfo, fcf, cashneq):
    zn = _rolling_zscore(ncfo.diff(), 8); zf = _rolling_zscore(fcf.diff(), 8); zc = _rolling_zscore(cashneq.diff(), 8)
    result = pd.concat([zn, zf, zc], axis=1).std(axis=1)
    return result.diff().diff().diff()


def f31_cbac_068_ncfo_minus_netinc_accel_z_gap_8q_d3(ncfo, netinc):
    zn = _rolling_zscore(ncfo.diff().diff(), 8); zi = _rolling_zscore(netinc.diff().diff(), 8)
    result = zn - zi
    return result.diff().diff().diff()


def f31_cbac_069_cascade_ncfo_leads_cashneq_lag_2q_d3(ncfo, cashneq):
    result = ((ncfo.diff().shift(2) < 0) & (cashneq.diff() < 0)).astype(float).where(ncfo.diff().shift(2).notna() & cashneq.diff().notna(), np.nan)
    return result.diff().diff().diff()


def f31_cbac_070_cascade_ncfo_leads_fcf_lag_1q_d3(ncfo, fcf):
    result = ((ncfo.diff().shift(1) < 0) & (fcf.diff() < 0)).astype(float).where(ncfo.diff().shift(1).notna() & fcf.diff().notna(), np.nan)
    return result.diff().diff().diff()


def f31_cbac_071_sign_agreement_count_ncfo_fcf_cashneq_netinc_d3(ncfo, fcf, cashneq, netinc):
    s = (ncfo.diff() < 0).astype(float) + (fcf.diff() < 0).astype(float) + (cashneq.diff() < 0).astype(float) + (netinc.diff() < 0).astype(float)
    result = s.where(ncfo.diff().notna(), np.nan)
    return result.diff().diff().diff()


def f31_cbac_072_sign_agreement_count_sum_4q_d3(ncfo, fcf, cashneq, netinc):
    s = (ncfo.diff() < 0).astype(float) + (fcf.diff() < 0).astype(float) + (cashneq.diff() < 0).astype(float) + (netinc.diff() < 0).astype(float)
    result = s.rolling(4, min_periods=2).sum()
    return result.diff().diff().diff()


def f31_cbac_073_cross_corr_ncfo_fcf_accel_8q_d3(ncfo, fcf):
    result = ncfo.diff().diff().rolling(8, min_periods=4).corr(fcf.diff().diff())
    return result.diff().diff().diff()


def f31_cbac_074_worst_cash_metric_z_signed_8q_d3(ncfo, fcf, cashneq):
    zn = _rolling_zscore(ncfo.diff().diff(), 8); zf = _rolling_zscore(fcf.diff().diff(), 8); zc = _rolling_zscore(cashneq.diff().diff(), 8)
    result = pd.concat([zn, zf, zc], axis=1).min(axis=1)
    return result.diff().diff().diff()


def f31_cbac_075_ncfo_neg_fcf_neg_cashneq_neg_compound_score_d3(ncfo, fcf, cashneq):
    s = (ncfo < 0).astype(float) + (fcf < 0).astype(float) + (cashneq < cashneq.shift(1)).astype(float)
    result = s.where(ncfo.notna() & fcf.notna() & cashneq.notna(), np.nan)
    return result.diff().diff().diff()


CASH_BURN_ACCELERATION_D3_REGISTRY_001_075 = {
    "f31_cbac_001_ncfo_accel_zscore_8q_d3": {"inputs": ["ncfo"], "func": f31_cbac_001_ncfo_accel_zscore_8q_d3},
    "f31_cbac_002_fcf_accel_zscore_8q_d3": {"inputs": ["fcf"], "func": f31_cbac_002_fcf_accel_zscore_8q_d3},
    "f31_cbac_003_cashneq_accel_zscore_8q_d3": {"inputs": ["cashneq"], "func": f31_cbac_003_cashneq_accel_zscore_8q_d3},
    "f31_cbac_004_ncfo_to_assets_accel_zscore_8q_d3": {"inputs": ["ncfo", "assets"], "func": f31_cbac_004_ncfo_to_assets_accel_zscore_8q_d3},
    "f31_cbac_005_fcf_to_assets_accel_zscore_8q_d3": {"inputs": ["fcf", "assets"], "func": f31_cbac_005_fcf_to_assets_accel_zscore_8q_d3},
    "f31_cbac_006_ncfo_accel_below_m2sd_8q_d3": {"inputs": ["ncfo"], "func": f31_cbac_006_ncfo_accel_below_m2sd_8q_d3},
    "f31_cbac_007_fcf_drop_from_8q_max_d3": {"inputs": ["fcf"], "func": f31_cbac_007_fcf_drop_from_8q_max_d3},
    "f31_cbac_008_ncfo_drop_from_8q_max_d3": {"inputs": ["ncfo"], "func": f31_cbac_008_ncfo_drop_from_8q_max_d3},
    "f31_cbac_009_cashneq_drop_from_12q_max_d3": {"inputs": ["cashneq"], "func": f31_cbac_009_cashneq_drop_from_12q_max_d3},
    "f31_cbac_010_fcf_one_q_cliff_50pct_of_assets_d3": {"inputs": ["fcf", "assets"], "func": f31_cbac_010_fcf_one_q_cliff_50pct_of_assets_d3},
    "f31_cbac_011_ncfo_one_q_cliff_50pct_of_assets_d3": {"inputs": ["ncfo", "assets"], "func": f31_cbac_011_ncfo_one_q_cliff_50pct_of_assets_d3},
    "f31_cbac_012_fcf_negative_streak_d3": {"inputs": ["fcf"], "func": f31_cbac_012_fcf_negative_streak_d3},
    "f31_cbac_013_ncfo_negative_streak_d3": {"inputs": ["ncfo"], "func": f31_cbac_013_ncfo_negative_streak_d3},
    "f31_cbac_014_cashneq_decline_streak_d3": {"inputs": ["cashneq"], "func": f31_cbac_014_cashneq_decline_streak_d3},
    "f31_cbac_015_fcf_negative_count_8q_d3": {"inputs": ["fcf"], "func": f31_cbac_015_fcf_negative_count_8q_d3},
    "f31_cbac_016_ncfo_accel_jump_magnitude_vs_8q_mad_d3": {"inputs": ["ncfo"], "func": f31_cbac_016_ncfo_accel_jump_magnitude_vs_8q_mad_d3},
    "f31_cbac_017_fcf_accel_range_position_8q_d3": {"inputs": ["fcf"], "func": f31_cbac_017_fcf_accel_range_position_8q_d3},
    "f31_cbac_018_cashneq_accel_in_worst_quartile_12q_d3": {"inputs": ["cashneq"], "func": f31_cbac_018_cashneq_accel_in_worst_quartile_12q_d3},
    "f31_cbac_019_fcf_strictly_decreasing_streak_d3": {"inputs": ["fcf"], "func": f31_cbac_019_fcf_strictly_decreasing_streak_d3},
    "f31_cbac_020_ncfo_hard_floor_breach_neg25_of_assets_8q_d3": {"inputs": ["ncfo", "assets"], "func": f31_cbac_020_ncfo_hard_floor_breach_neg25_of_assets_8q_d3},
    "f31_cbac_021_ncfo_slope_4q_sign_flip_d3": {"inputs": ["ncfo"], "func": f31_cbac_021_ncfo_slope_4q_sign_flip_d3},
    "f31_cbac_022_fcf_ema4_sign_flip_pos_to_neg_d3": {"inputs": ["fcf"], "func": f31_cbac_022_fcf_ema4_sign_flip_pos_to_neg_d3},
    "f31_cbac_023_cashneq_inflection_magnitude_8q_d3": {"inputs": ["cashneq"], "func": f31_cbac_023_cashneq_inflection_magnitude_8q_d3},
    "f31_cbac_024_ncfo_mean_shift_z_4v12_d3": {"inputs": ["ncfo"], "func": f31_cbac_024_ncfo_mean_shift_z_4v12_d3},
    "f31_cbac_025_fcf_mean_shift_down_indicator_d3": {"inputs": ["fcf"], "func": f31_cbac_025_fcf_mean_shift_down_indicator_d3},
    "f31_cbac_026_ncfo_variance_ratio_4q_12q_d3": {"inputs": ["ncfo"], "func": f31_cbac_026_ncfo_variance_ratio_4q_12q_d3},
    "f31_cbac_027_fcf_variance_jump_zscore_16q_d3": {"inputs": ["fcf"], "func": f31_cbac_027_fcf_variance_jump_zscore_16q_d3},
    "f31_cbac_028_cashneq_var_shift_up_indicator_d3": {"inputs": ["cashneq"], "func": f31_cbac_028_cashneq_var_shift_up_indicator_d3},
    "f31_cbac_029_ncfo_regime_stickiness_bad_quartile_4q_in_20q_d3": {"inputs": ["ncfo"], "func": f31_cbac_029_ncfo_regime_stickiness_bad_quartile_4q_in_20q_d3},
    "f31_cbac_030_fcf_new_low_12q_indicator_d3": {"inputs": ["fcf"], "func": f31_cbac_030_fcf_new_low_12q_indicator_d3},
    "f31_cbac_031_ncfo_fcf_compound_new_low_12q_d3": {"inputs": ["ncfo", "fcf"], "func": f31_cbac_031_ncfo_fcf_compound_new_low_12q_d3},
    "f31_cbac_032_cashneq_chow_fstat_proxy_12q_d3": {"inputs": ["cashneq"], "func": f31_cbac_032_cashneq_chow_fstat_proxy_12q_d3},
    "f31_cbac_033_ncfo_concavity_sign_d3": {"inputs": ["ncfo"], "func": f31_cbac_033_ncfo_concavity_sign_d3},
    "f31_cbac_034_fcf_convexity_flip_pos_to_neg_d3": {"inputs": ["fcf"], "func": f31_cbac_034_fcf_convexity_flip_pos_to_neg_d3},
    "f31_cbac_035_cashneq_convexity_flip_neg_to_pos_d3": {"inputs": ["cashneq"], "func": f31_cbac_035_cashneq_convexity_flip_neg_to_pos_d3},
    "f31_cbac_036_ncfo_phase_shift_4q_vs_12q_norm_d3": {"inputs": ["ncfo"], "func": f31_cbac_036_ncfo_phase_shift_4q_vs_12q_norm_d3},
    "f31_cbac_037_fcf_ar1_persistence_8q_d3": {"inputs": ["fcf"], "func": f31_cbac_037_fcf_ar1_persistence_8q_d3},
    "f31_cbac_038_ncfo_persistence_collapse_4q_d3": {"inputs": ["ncfo"], "func": f31_cbac_038_ncfo_persistence_collapse_4q_d3},
    "f31_cbac_039_cashneq_local_concavity_test_d3": {"inputs": ["cashneq"], "func": f31_cbac_039_cashneq_local_concavity_test_d3},
    "f31_cbac_040_ncfo_break_recency_max_split_diff_12q_d3": {"inputs": ["ncfo"], "func": f31_cbac_040_ncfo_break_recency_max_split_diff_12q_d3},
    "f31_cbac_041_runway_quarters_current_d3": {"inputs": ["cashneq", "ncfo"], "func": f31_cbac_041_runway_quarters_current_d3},
    "f31_cbac_042_runway_qoq_diff_qtrs_lost_d3": {"inputs": ["cashneq", "ncfo"], "func": f31_cbac_042_runway_qoq_diff_qtrs_lost_d3},
    "f31_cbac_043_runway_acceleration_diff_diff_d3": {"inputs": ["cashneq", "ncfo"], "func": f31_cbac_043_runway_acceleration_diff_diff_d3},
    "f31_cbac_044_runway_pct_drop_4q_d3": {"inputs": ["cashneq", "ncfo"], "func": f31_cbac_044_runway_pct_drop_4q_d3},
    "f31_cbac_045_runway_pct_drop_8q_d3": {"inputs": ["cashneq", "ncfo"], "func": f31_cbac_045_runway_pct_drop_8q_d3},
    "f31_cbac_046_runway_below_4q_indicator_d3": {"inputs": ["cashneq", "ncfo"], "func": f31_cbac_046_runway_below_4q_indicator_d3},
    "f31_cbac_047_runway_below_2q_indicator_d3": {"inputs": ["cashneq", "ncfo"], "func": f31_cbac_047_runway_below_2q_indicator_d3},
    "f31_cbac_048_runway_drop_from_8q_max_d3": {"inputs": ["cashneq", "ncfo"], "func": f31_cbac_048_runway_drop_from_8q_max_d3},
    "f31_cbac_049_runway_drop_velocity_8q_d3": {"inputs": ["cashneq", "ncfo"], "func": f31_cbac_049_runway_drop_velocity_8q_d3},
    "f31_cbac_050_runway_new_low_12q_indicator_d3": {"inputs": ["cashneq", "ncfo"], "func": f31_cbac_050_runway_new_low_12q_indicator_d3},
    "f31_cbac_051_runway_zscore_collapse_12q_d3": {"inputs": ["cashneq", "ncfo"], "func": f31_cbac_051_runway_zscore_collapse_12q_d3},
    "f31_cbac_052_burn_rate_acceleration_qoq_d3": {"inputs": ["ncfo"], "func": f31_cbac_052_burn_rate_acceleration_qoq_d3},
    "f31_cbac_053_burn_rate_zscore_8q_d3": {"inputs": ["ncfo"], "func": f31_cbac_053_burn_rate_zscore_8q_d3},
    "f31_cbac_054_burn_rate_doubling_indicator_yoy_d3": {"inputs": ["ncfo"], "func": f31_cbac_054_burn_rate_doubling_indicator_yoy_d3},
    "f31_cbac_055_cashneq_below_4q_burn_indicator_d3": {"inputs": ["ncfo", "cashneq"], "func": f31_cbac_055_cashneq_below_4q_burn_indicator_d3},
    "f31_cbac_056_cashneq_to_4q_burn_ratio_d3": {"inputs": ["ncfo", "cashneq"], "func": f31_cbac_056_cashneq_to_4q_burn_ratio_d3},
    "f31_cbac_057_cashneq_to_4q_burn_ratio_qoq_drop_d3": {"inputs": ["ncfo", "cashneq"], "func": f31_cbac_057_cashneq_to_4q_burn_ratio_qoq_drop_d3},
    "f31_cbac_058_fcf_burn_intensity_pct_of_assets_d3": {"inputs": ["fcf", "assets"], "func": f31_cbac_058_fcf_burn_intensity_pct_of_assets_d3},
    "f31_cbac_059_fcf_burn_intensity_acceleration_d3": {"inputs": ["fcf", "assets"], "func": f31_cbac_059_fcf_burn_intensity_acceleration_d3},
    "f31_cbac_060_runway_terminal_distance_proxy_d3": {"inputs": ["cashneq", "ncfo"], "func": f31_cbac_060_runway_terminal_distance_proxy_d3},
    "f31_cbac_061_ncfo_fcf_both_decline_indicator_d3": {"inputs": ["ncfo", "fcf"], "func": f31_cbac_061_ncfo_fcf_both_decline_indicator_d3},
    "f31_cbac_062_ncfo_fcf_cashneq_triple_decline_indicator_d3": {"inputs": ["ncfo", "fcf", "cashneq"], "func": f31_cbac_062_ncfo_fcf_cashneq_triple_decline_indicator_d3},
    "f31_cbac_063_ncfo_fcf_cashneq_co_decline_streak_d3": {"inputs": ["ncfo", "fcf", "cashneq"], "func": f31_cbac_063_ncfo_fcf_cashneq_co_decline_streak_d3},
    "f31_cbac_064_ncfo_fcf_co_decline_fraction_8q_d3": {"inputs": ["ncfo", "fcf"], "func": f31_cbac_064_ncfo_fcf_co_decline_fraction_8q_d3},
    "f31_cbac_065_three_cash_compound_score_signed_8q_d3": {"inputs": ["ncfo", "fcf", "cashneq"], "func": f31_cbac_065_three_cash_compound_score_signed_8q_d3},
    "f31_cbac_066_three_cash_compound_score_abs_8q_d3": {"inputs": ["ncfo", "fcf", "cashneq"], "func": f31_cbac_066_three_cash_compound_score_abs_8q_d3},
    "f31_cbac_067_three_cash_dispersion_z_8q_d3": {"inputs": ["ncfo", "fcf", "cashneq"], "func": f31_cbac_067_three_cash_dispersion_z_8q_d3},
    "f31_cbac_068_ncfo_minus_netinc_accel_z_gap_8q_d3": {"inputs": ["ncfo", "netinc"], "func": f31_cbac_068_ncfo_minus_netinc_accel_z_gap_8q_d3},
    "f31_cbac_069_cascade_ncfo_leads_cashneq_lag_2q_d3": {"inputs": ["ncfo", "cashneq"], "func": f31_cbac_069_cascade_ncfo_leads_cashneq_lag_2q_d3},
    "f31_cbac_070_cascade_ncfo_leads_fcf_lag_1q_d3": {"inputs": ["ncfo", "fcf"], "func": f31_cbac_070_cascade_ncfo_leads_fcf_lag_1q_d3},
    "f31_cbac_071_sign_agreement_count_ncfo_fcf_cashneq_netinc_d3": {"inputs": ["ncfo", "fcf", "cashneq", "netinc"], "func": f31_cbac_071_sign_agreement_count_ncfo_fcf_cashneq_netinc_d3},
    "f31_cbac_072_sign_agreement_count_sum_4q_d3": {"inputs": ["ncfo", "fcf", "cashneq", "netinc"], "func": f31_cbac_072_sign_agreement_count_sum_4q_d3},
    "f31_cbac_073_cross_corr_ncfo_fcf_accel_8q_d3": {"inputs": ["ncfo", "fcf"], "func": f31_cbac_073_cross_corr_ncfo_fcf_accel_8q_d3},
    "f31_cbac_074_worst_cash_metric_z_signed_8q_d3": {"inputs": ["ncfo", "fcf", "cashneq"], "func": f31_cbac_074_worst_cash_metric_z_signed_8q_d3},
    "f31_cbac_075_ncfo_neg_fcf_neg_cashneq_neg_compound_score_d3": {"inputs": ["ncfo", "fcf", "cashneq"], "func": f31_cbac_075_ncfo_neg_fcf_neg_cashneq_neg_compound_score_d3},
}
