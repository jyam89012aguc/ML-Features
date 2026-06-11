"""cash_burn_acceleration d3 features 076_150 — Pipeline 1a-inverse short-side blowup family.

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


def f31_cbac_076_capex_to_ocf_ratio_8q_rising_d3(capex, ncfo):
    r = _safe_div(capex.abs(), ncfo.abs())
    result = r - r.rolling(8, min_periods=3).min()
    return result.diff().diff().diff()


def f31_cbac_077_capex_growing_ocf_falling_indicator_d3(capex, ncfo):
    result = ((capex.diff() > 0) & (ncfo.diff() < 0)).astype(float).where(capex.diff().notna() & ncfo.diff().notna(), np.nan)
    return result.diff().diff().diff()


def f31_cbac_078_capex_yoy_minus_ocf_yoy_gap_d3(capex, ncfo):
    result = _yoy_pct(capex.abs()) - _yoy_pct(ncfo.abs())
    return result.diff().diff().diff()


def f31_cbac_079_capex_accel_zscore_8q_d3(capex):
    a = capex.abs().diff().diff()
    result = _rolling_zscore(a, 8)
    return result.diff().diff().diff()


def f31_cbac_080_fcf_negative_capex_growing_streak_d3(fcf, capex):
    b = (fcf < 0) & (capex.abs().diff() > 0)
    result = _consec_true_streak(b).astype(float)
    return result.diff().diff().diff()


def f31_cbac_081_ocf_minus_capex_acceleration_d3(ncfo, capex):
    s = ncfo - capex.abs()
    result = s.diff().diff()
    return result.diff().diff().diff()


def f31_cbac_082_receivables_to_revenue_jump_accel_d3(receivables, revenue):
    r = _safe_div(receivables, _ttm(revenue).abs())
    result = r.diff().diff()
    return result.diff().diff().diff()


def f31_cbac_083_receivables_to_revenue_zscore_jump_8q_d3(receivables, revenue):
    r = _safe_div(receivables, _ttm(revenue).abs())
    result = _rolling_zscore(r.diff(), 8)
    return result.diff().diff().diff()


def f31_cbac_084_current_assets_to_current_liab_ratio_collapse_d3(assetsc, liabilitiesc):
    r = _safe_div(assetsc, liabilitiesc.abs())
    result = r - r.rolling(8, min_periods=3).max()
    return result.diff().diff().diff()


def f31_cbac_085_quick_ratio_proxy_collapse_d3(cashneq, receivables, liabilitiesc):
    q = _safe_div(cashneq + receivables, liabilitiesc.abs())
    result = q - q.rolling(8, min_periods=3).max()
    return result.diff().diff().diff()


def f31_cbac_086_cash_to_currentliab_accel_d3(cashneq, liabilitiesc):
    r = _safe_div(cashneq, liabilitiesc.abs())
    result = r.diff().diff()
    return result.diff().diff().diff()


def f31_cbac_087_cash_to_debt_accel_d3(cashneq, debt):
    r = _safe_div(cashneq, debt.abs())
    result = r.diff().diff()
    return result.diff().diff().diff()


def f31_cbac_088_cash_to_debt_collapse_from_8q_max_d3(cashneq, debt):
    r = _safe_div(cashneq, debt.abs())
    result = r - r.rolling(8, min_periods=3).max()
    return result.diff().diff().diff()


def f31_cbac_089_cash_to_currentdebt_below_1_indicator_d3(cashneq, debtc):
    r = _safe_div(cashneq, debtc.abs())
    result = (r < 1.0).astype(float).where(r.notna(), np.nan)
    return result.diff().diff().diff()


def f31_cbac_090_intexp_to_ocf_ratio_acceleration_d3(intexp, ncfo):
    r = _safe_div(intexp.abs(), ncfo.abs())
    result = r.diff().diff()
    return result.diff().diff().diff()


def f31_cbac_091_intexp_coverage_collapse_8q_d3(intexp, ncfo):
    r = _safe_div(ncfo, intexp.abs())
    result = r - r.rolling(8, min_periods=3).max()
    return result.diff().diff().diff()


def f31_cbac_092_growth_capex_minus_da_accel_d3(capex, depamor):
    s = capex.abs() - depamor.abs()
    result = s.diff().diff()
    return result.diff().diff().diff()


def f31_cbac_093_cashneq_to_assets_collapse_8q_d3(cashneq, assets):
    r = _safe_div(cashneq, assets.abs())
    result = r - r.rolling(8, min_periods=3).max()
    return result.diff().diff().diff()


def f31_cbac_094_cashneq_to_equity_collapse_8q_d3(cashneq, equity):
    r = _safe_div(cashneq, equity.abs())
    result = r - r.rolling(8, min_periods=3).max()
    return result.diff().diff().diff()


def f31_cbac_095_fcf_per_revenue_collapse_8q_d3(fcf, revenue):
    r = _safe_div(_ttm(fcf), _ttm(revenue).abs())
    result = r - r.rolling(8, min_periods=3).max()
    return result.diff().diff().diff()


def f31_cbac_096_ocf_to_revenue_accel_d3(ncfo, revenue):
    r = _safe_div(_ttm(ncfo), _ttm(revenue).abs())
    result = r.diff().diff()
    return result.diff().diff().diff()


def f31_cbac_097_ocf_to_netinc_divergence_accel_d3(ncfo, netinc):
    r = _safe_div(ncfo, netinc.abs())
    result = r.diff().diff()
    return result.diff().diff().diff()


def f31_cbac_098_ocf_to_netinc_below_half_indicator_d3(ncfo, netinc):
    r = _safe_div(ncfo, netinc.abs())
    result = (r < 0.5).astype(float).where(r.notna(), np.nan)
    return result.diff().diff().diff()


def f31_cbac_099_discretionary_cash_collapse_8q_d3(ncfo, capex, intexp):
    s = _ttm(ncfo) - _ttm(capex).abs() - _ttm(intexp).abs()
    result = s - s.rolling(8, min_periods=3).max()
    return result.diff().diff().diff()


def f31_cbac_100_discretionary_cash_yoy_collapse_d3(ncfo, capex, intexp):
    s = _ttm(ncfo) - _ttm(capex).abs() - _ttm(intexp).abs()
    result = _safe_div(s - s.shift(4), s.shift(4).abs())
    return result.diff().diff().diff()


def f31_cbac_101_ncfo_cusum_max_excursion_12q_d3(ncfo):
    mu = ncfo.rolling(12, min_periods=4).mean()
    result = (ncfo - mu).rolling(12, min_periods=4).apply(lambda w: np.nanmax(np.cumsum(w)) if not np.isnan(w).all() else np.nan, raw=True)
    return result.diff().diff().diff()


def f31_cbac_102_fcf_cusum_min_excursion_12q_d3(fcf):
    mu = fcf.rolling(12, min_periods=4).mean()
    result = (fcf - mu).rolling(12, min_periods=4).apply(lambda w: np.nanmin(np.cumsum(w)) if not np.isnan(w).all() else np.nan, raw=True)
    return result.diff().diff().diff()


def f31_cbac_103_cashneq_cusum_z_12q_d3(cashneq):
    mu = cashneq.rolling(12, min_periods=4).mean(); sd = cashneq.rolling(12, min_periods=4).std()
    cu = (cashneq - mu).rolling(12, min_periods=4).apply(lambda w: np.nanmax(np.abs(np.cumsum(w))) if not np.isnan(w).all() else np.nan, raw=True)
    result = _safe_div(cu, sd)
    return result.diff().diff().diff()


def f31_cbac_104_ncfo_max_abs_residual_recency_8q_d3(ncfo):
    mu = ncfo.rolling(8, min_periods=3).mean(); r = (ncfo - mu).abs()
    result = r.rolling(8, min_periods=3).apply(lambda w: float(len(w) - 1 - int(np.nanargmax(w))) if not np.isnan(w).all() else np.nan, raw=True)
    return result.diff().diff().diff()


def f31_cbac_105_fcf_breakpoint_count_16q_d3(fcf):
    d = fcf.diff(); s = d.rolling(16, min_periods=5).std()
    result = _rolling_count(d.abs() > 2.0 * s, 16)
    return result.diff().diff().diff()


def f31_cbac_106_ncfo_likelihood_break_proxy_12q_d3(ncfo):
    m1 = ncfo.rolling(6, min_periods=2).mean().shift(6); m2 = ncfo.rolling(6, min_periods=2).mean()
    s1 = ncfo.rolling(6, min_periods=2).std().shift(6); s2 = ncfo.rolling(6, min_periods=2).std()
    result = _safe_div((m1 - m2) ** 2, (s1 ** 2 + s2 ** 2))
    return result.diff().diff().diff()


def f31_cbac_107_cashneq_break_recency_max_fstat_12q_d3(cashneq):
    fs = pd.concat([_safe_div((cashneq.rolling(k, min_periods=2).mean().shift(12 - k) - cashneq.rolling(12 - k, min_periods=2).mean()) ** 2, cashneq.rolling(12, min_periods=4).var()).rename(k) for k in range(3, 10)], axis=1)
    result = fs.idxmax(axis=1).where(cashneq.notna(), np.nan).astype(float)
    return result.diff().diff().diff()


def f31_cbac_108_fcf_var_ratio_test_zscore_20q_d3(fcf):
    vr = _safe_div(fcf.rolling(4, min_periods=2).var(), fcf.rolling(12, min_periods=4).var())
    result = _rolling_zscore(vr - 1.0, 20)
    return result.diff().diff().diff()


def f31_cbac_109_ncfo_var_regime_up_significance_12q_d3(ncfo):
    v1 = ncfo.rolling(6, min_periods=2).var().shift(6); v2 = ncfo.rolling(6, min_periods=2).var()
    result = _safe_div(v2 - v1, v1.abs())
    return result.diff().diff().diff()


def f31_cbac_110_fcf_var_regime_down_significance_12q_d3(fcf):
    v1 = fcf.rolling(6, min_periods=2).var().shift(6); v2 = fcf.rolling(6, min_periods=2).var()
    result = _safe_div(v1 - v2, v1.abs())
    return result.diff().diff().diff()


def f31_cbac_111_cashneq_mean_diff_t_stat_12q_d3(cashneq):
    m1 = cashneq.rolling(6, min_periods=3).mean().shift(6); m2 = cashneq.rolling(6, min_periods=3).mean()
    s1 = cashneq.rolling(6, min_periods=3).std().shift(6); s2 = cashneq.rolling(6, min_periods=3).std()
    se = ((s1 ** 2 + s2 ** 2) / 6.0).pow(0.5)
    result = _safe_div(m2 - m1, se)
    return result.diff().diff().diff()


def f31_cbac_112_ncfo_mean_t_signif_down_d3(ncfo):
    m1 = ncfo.rolling(6, min_periods=3).mean().shift(6); m2 = ncfo.rolling(6, min_periods=3).mean()
    s1 = ncfo.rolling(6, min_periods=3).std().shift(6); s2 = ncfo.rolling(6, min_periods=3).std()
    se = ((s1 ** 2 + s2 ** 2) / 6.0).pow(0.5)
    t = _safe_div(m2 - m1, se)
    result = (t < -2.0).astype(float).where(t.notna(), np.nan)
    return result.diff().diff().diff()


def f31_cbac_113_fcf_ks_style_cdf_shift_16q_d3(fcf):
    med1 = fcf.rolling(8, min_periods=3).median().shift(8); med2 = fcf.rolling(8, min_periods=3).median()
    iqr = (fcf.rolling(16, min_periods=5).quantile(0.75) - fcf.rolling(16, min_periods=5).quantile(0.25))
    result = _safe_div((med2 - med1).abs(), iqr)
    return result.diff().diff().diff()


def f31_cbac_114_cashneq_median_break_4q_vs_16q_d3(cashneq):
    result = cashneq.rolling(4, min_periods=2).median() - cashneq.rolling(16, min_periods=5).median()
    return result.diff().diff().diff()


def f31_cbac_115_ncfo_resid_var_jump_4q_vs_16q_d3(ncfo):
    m4 = ncfo.rolling(4, min_periods=2).mean(); m16 = ncfo.rolling(16, min_periods=5).mean()
    r4 = (ncfo - m4) ** 2; r16 = (ncfo - m16) ** 2
    result = _safe_div(r4.rolling(4, min_periods=2).mean(), r16.rolling(16, min_periods=5).mean())
    return result.diff().diff().diff()


def f31_cbac_116_fcf_regression_slope_break_4q_vs_12q_d3(fcf):
    result = _rolling_slope(fcf, 4) - _rolling_slope(fcf, 12)
    return result.diff().diff().diff()


def f31_cbac_117_ncfo_regression_slope_break_4q_vs_12q_d3(ncfo):
    result = _rolling_slope(ncfo, 4) - _rolling_slope(ncfo, 12)
    return result.diff().diff().diff()


def f31_cbac_118_cashneq_regression_slope_break_4q_vs_12q_d3(cashneq):
    result = _rolling_slope(cashneq, 4) - _rolling_slope(cashneq, 12)
    return result.diff().diff().diff()


def f31_cbac_119_cashneq_combined_break_composite_8q_d3(cashneq):
    d = cashneq.diff(); s = d.rolling(8, min_periods=3).std()
    cliff = _rolling_count(d < -d.rolling(8, min_periods=3).std(), 8); jump = _rolling_count(d.abs() > 2.0 * s, 8); newlow = _rolling_count(cashneq == cashneq.rolling(12, min_periods=4).min(), 8)
    result = (cliff.fillna(0) + jump.fillna(0) + newlow.fillna(0)).where(cashneq.notna(), np.nan)
    return result.diff().diff().diff()


def f31_cbac_120_ncfo_quandt_max_fstat_12q_d3(ncfo):
    fs = pd.concat([_safe_div((ncfo.rolling(k, min_periods=2).mean().shift(12 - k) - ncfo.rolling(12 - k, min_periods=2).mean()) ** 2, ncfo.rolling(12, min_periods=4).var()) for k in range(3, 10)], axis=1)
    result = fs.max(axis=1)
    return result.diff().diff().diff()


def f31_cbac_121_ncfo_drawdown_from_12q_max_d3(ncfo):
    result = ncfo.rolling(12, min_periods=4).max() - ncfo
    return result.diff().diff().diff()


def f31_cbac_122_fcf_drawdown_from_16q_max_d3(fcf):
    result = fcf.rolling(16, min_periods=5).max() - fcf
    return result.diff().diff().diff()


def f31_cbac_123_cashneq_drawdown_from_16q_max_d3(cashneq):
    result = cashneq.rolling(16, min_periods=5).max() - cashneq
    return result.diff().diff().diff()


def f31_cbac_124_ncfo_q_since_16q_max_d3(ncfo):
    result = ncfo.rolling(16, min_periods=5).apply(lambda w: float(len(w) - 1 - int(np.nanargmax(w))) if not np.isnan(w).all() else np.nan, raw=True)
    return result.diff().diff().diff()


def f31_cbac_125_fcf_drawdown_velocity_12q_d3(fcf):
    depth = fcf.rolling(12, min_periods=4).max() - fcf
    dur = fcf.rolling(12, min_periods=4).apply(lambda w: float(len(w) - 1 - int(np.nanargmax(w))) if not np.isnan(w).all() else np.nan, raw=True)
    result = _safe_div(depth, dur.replace(0, np.nan))
    return result.diff().diff().diff()


def f31_cbac_126_ncfo_pain_ratio_8q_d3(ncfo):
    neg = ncfo.diff().where(lambda x: x < 0).abs().rolling(8, min_periods=2).sum(); tot = ncfo.diff().abs().rolling(8, min_periods=2).sum()
    result = _safe_div(neg, tot)
    return result.diff().diff().diff()


def f31_cbac_127_fcf_ulcer_index_neg_dd_rms_8q_d3(fcf):
    dd = (fcf.rolling(8, min_periods=3).max() - fcf).clip(lower=0)
    result = (dd ** 2).rolling(8, min_periods=3).mean().pow(0.5)
    return result.diff().diff().diff()


def f31_cbac_128_ncfo_accel_skew_8q_d3(ncfo):
    result = ncfo.diff().diff().rolling(8, min_periods=4).skew()
    return result.diff().diff().diff()


def f31_cbac_129_ncfo_accel_kurt_8q_d3(ncfo):
    result = ncfo.diff().diff().rolling(8, min_periods=4).kurt()
    return result.diff().diff().diff()


def f31_cbac_130_fcf_accel_skew_change_8q_vs_12q_d3(fcf):
    a = fcf.diff().diff()
    result = a.rolling(8, min_periods=4).skew() - a.rolling(12, min_periods=5).skew()
    return result.diff().diff().diff()


def f31_cbac_131_cashneq_accel_kurt_change_8q_vs_12q_d3(cashneq):
    a = cashneq.diff().diff()
    result = a.rolling(8, min_periods=4).kurt() - a.rolling(12, min_periods=5).kurt()
    return result.diff().diff().diff()


def f31_cbac_132_ncfo_accel_cv_8q_d3(ncfo):
    a = ncfo.diff().diff()
    result = _safe_div(a.rolling(8, min_periods=3).std(), a.rolling(8, min_periods=3).mean().abs())
    return result.diff().diff().diff()


def f31_cbac_133_fcf_accel_quantile_dispersion_q90_q10_12q_d3(fcf):
    a = fcf.diff().diff()
    result = a.rolling(12, min_periods=4).quantile(0.9) - a.rolling(12, min_periods=4).quantile(0.1)
    return result.diff().diff().diff()


def f31_cbac_134_cashneq_accel_neg_tail_4q_in_16q_q25_d3(cashneq):
    a = cashneq.diff().diff(); q25 = a.rolling(16, min_periods=5).quantile(0.25)
    result = _rolling_count(a < q25, 4)
    return result.diff().diff().diff()


def f31_cbac_135_ncfo_accel_right_tail_collapse_q90_neg_8q_d3(ncfo):
    a = ncfo.diff().diff(); q90 = a.rolling(8, min_periods=3).quantile(0.9)
    result = (q90 < 0).astype(float).where(q90.notna(), np.nan)
    return result.diff().diff().diff()


def f31_cbac_136_fcf_accel_winsorized_z_10pct_8q_d3(fcf):
    a = fcf.diff().diff(); w = _winsorize(a, 0.1, 0.9, 8)
    result = _rolling_zscore(w, 8)
    return result.diff().diff().diff()


def f31_cbac_137_cashneq_accel_sign_runlength_var_8q_d3(cashneq):
    a = cashneq.diff().diff(); sg = _sign_safe(a)
    flip = (sg != sg.shift(1)).astype(float)
    result = flip.rolling(8, min_periods=3).sum()
    return result.diff().diff().diff()


def f31_cbac_138_ncfo_accel_persistence_lag1_8q_d3(ncfo):
    a = ncfo.diff().diff()
    result = _safe_div((a * a.shift(1)).rolling(8, min_periods=3).sum(), (a ** 2).rolling(8, min_periods=3).sum())
    return result.diff().diff().diff()


def f31_cbac_139_fcf_consecutive_decline_streak_d3(fcf):
    result = _consec_true_streak(fcf < fcf.shift(1)).astype(float)
    return result.diff().diff().diff()


def f31_cbac_140_ncfo_smoothed_raw_accel_sign_disagree_d3(ncfo):
    a = ncfo.diff().diff(); em = _ema(a, 4)
    result = (_sign_safe(em) != _sign_safe(a)).astype(float).where(a.notna() & em.notna(), np.nan)
    return result.diff().diff().diff()


def f31_cbac_141_composite_burn_crash_5_binaries_8q_d3(ncfo, fcf, cashneq):
    b1 = _rolling_count(ncfo.diff() < 0, 8); b2 = _rolling_count(fcf < 0, 8); b3 = _rolling_count(cashneq == cashneq.rolling(12, min_periods=4).min(), 8); b4 = _rolling_count(fcf.diff().diff() < 0, 8); b5 = _consec_true_streak(ncfo < 0).astype(float).rolling(8, min_periods=2).max()
    result = b1.fillna(0) + b2.fillna(0) + b3.fillna(0) + b4.fillna(0) + b5.fillna(0)
    return result.diff().diff().diff()


def f31_cbac_142_weighted_burn_crash_z_clip_m3_8q_d3(ncfo):
    z = _rolling_zscore(ncfo.diff().diff(), 8).clip(lower=-3.0, upper=0)
    result = -z.rolling(8, min_periods=3).sum()
    return result.diff().diff().diff()


def f31_cbac_143_multi_horizon_burn_crash_score_fcf_d3(fcf):
    a = fcf.diff().diff()
    z4 = _rolling_zscore(a, 4).clip(lower=-3, upper=0); z8 = _rolling_zscore(a, 8).clip(lower=-3, upper=0); z12 = _rolling_zscore(a, 12).clip(lower=-3, upper=0)
    result = -(z4 + z8 + z12)
    return result.diff().diff().diff()


def f31_cbac_144_ewm_decay_burn_score_8q_ncfo_neg_d3(ncfo):
    a = ncfo.clip(upper=0)
    result = -a.ewm(span=8, adjust=False, min_periods=3).mean()
    return result.diff().diff().diff()


def f31_cbac_145_logit_insolvency_probability_proxy_d3(cashneq, ncfo):
    rw = _runway_q(cashneq, ncfo); z = _rolling_zscore(rw, 12)
    result = 1.0 / (1.0 + np.exp(z.clip(lower=-10, upper=10)))
    return result.diff().diff().diff()


def f31_cbac_146_mahalanobis_dist_ncfo_accel_slope_8q_d3(ncfo):
    a = ncfo.diff().diff(); s = _rolling_slope(a, 8)
    za = _rolling_zscore(a, 12); zs = _rolling_zscore(s, 12)
    result = (za ** 2 + zs ** 2).pow(0.5)
    return result.diff().diff().diff()


def f31_cbac_147_hotelling_t_fcf_accel_vol_8q_d3(fcf):
    a = fcf.diff().diff(); v = a.rolling(4, min_periods=2).std()
    za = _rolling_zscore(a, 12); zv = _rolling_zscore(v, 12)
    result = za.abs() + zv.abs()
    return result.diff().diff().diff()


def f31_cbac_148_cashneq_terminal_distance_5y_proxy_d3(cashneq):
    mn = cashneq.rolling(20, min_periods=6).min(); mx = cashneq.rolling(20, min_periods=6).max()
    result = _safe_div(cashneq - mn, mx.abs())
    return result.diff().diff().diff()


def f31_cbac_149_burn_trend_velocity_collapse_4q_over_12q_d3(ncfo):
    s4 = _rolling_slope(ncfo, 4); s12 = _rolling_slope(ncfo, 12)
    result = _safe_div(s4, s12.abs())
    return result.diff().diff().diff()


def f31_cbac_150_all_cash_metrics_firing_down_composite_8q_d3(ncfo, fcf, cashneq):
    zn = _rolling_zscore(ncfo.diff().diff(), 8); zf = _rolling_zscore(fcf.diff().diff(), 8); zc = _rolling_zscore(cashneq.diff().diff(), 8)
    z = pd.concat([zn, zf, zc], axis=1).clip(lower=-3, upper=0)
    result = -z.sum(axis=1)
    return result.diff().diff().diff()


CASH_BURN_ACCELERATION_D3_REGISTRY_076_150 = {
    "f31_cbac_076_capex_to_ocf_ratio_8q_rising_d3": {"inputs": ["capex", "ncfo"], "func": f31_cbac_076_capex_to_ocf_ratio_8q_rising_d3},
    "f31_cbac_077_capex_growing_ocf_falling_indicator_d3": {"inputs": ["capex", "ncfo"], "func": f31_cbac_077_capex_growing_ocf_falling_indicator_d3},
    "f31_cbac_078_capex_yoy_minus_ocf_yoy_gap_d3": {"inputs": ["capex", "ncfo"], "func": f31_cbac_078_capex_yoy_minus_ocf_yoy_gap_d3},
    "f31_cbac_079_capex_accel_zscore_8q_d3": {"inputs": ["capex"], "func": f31_cbac_079_capex_accel_zscore_8q_d3},
    "f31_cbac_080_fcf_negative_capex_growing_streak_d3": {"inputs": ["fcf", "capex"], "func": f31_cbac_080_fcf_negative_capex_growing_streak_d3},
    "f31_cbac_081_ocf_minus_capex_acceleration_d3": {"inputs": ["ncfo", "capex"], "func": f31_cbac_081_ocf_minus_capex_acceleration_d3},
    "f31_cbac_082_receivables_to_revenue_jump_accel_d3": {"inputs": ["receivables", "revenue"], "func": f31_cbac_082_receivables_to_revenue_jump_accel_d3},
    "f31_cbac_083_receivables_to_revenue_zscore_jump_8q_d3": {"inputs": ["receivables", "revenue"], "func": f31_cbac_083_receivables_to_revenue_zscore_jump_8q_d3},
    "f31_cbac_084_current_assets_to_current_liab_ratio_collapse_d3": {"inputs": ["assetsc", "liabilitiesc"], "func": f31_cbac_084_current_assets_to_current_liab_ratio_collapse_d3},
    "f31_cbac_085_quick_ratio_proxy_collapse_d3": {"inputs": ["cashneq", "receivables", "liabilitiesc"], "func": f31_cbac_085_quick_ratio_proxy_collapse_d3},
    "f31_cbac_086_cash_to_currentliab_accel_d3": {"inputs": ["cashneq", "liabilitiesc"], "func": f31_cbac_086_cash_to_currentliab_accel_d3},
    "f31_cbac_087_cash_to_debt_accel_d3": {"inputs": ["cashneq", "debt"], "func": f31_cbac_087_cash_to_debt_accel_d3},
    "f31_cbac_088_cash_to_debt_collapse_from_8q_max_d3": {"inputs": ["cashneq", "debt"], "func": f31_cbac_088_cash_to_debt_collapse_from_8q_max_d3},
    "f31_cbac_089_cash_to_currentdebt_below_1_indicator_d3": {"inputs": ["cashneq", "debtc"], "func": f31_cbac_089_cash_to_currentdebt_below_1_indicator_d3},
    "f31_cbac_090_intexp_to_ocf_ratio_acceleration_d3": {"inputs": ["intexp", "ncfo"], "func": f31_cbac_090_intexp_to_ocf_ratio_acceleration_d3},
    "f31_cbac_091_intexp_coverage_collapse_8q_d3": {"inputs": ["intexp", "ncfo"], "func": f31_cbac_091_intexp_coverage_collapse_8q_d3},
    "f31_cbac_092_growth_capex_minus_da_accel_d3": {"inputs": ["capex", "depamor"], "func": f31_cbac_092_growth_capex_minus_da_accel_d3},
    "f31_cbac_093_cashneq_to_assets_collapse_8q_d3": {"inputs": ["cashneq", "assets"], "func": f31_cbac_093_cashneq_to_assets_collapse_8q_d3},
    "f31_cbac_094_cashneq_to_equity_collapse_8q_d3": {"inputs": ["cashneq", "equity"], "func": f31_cbac_094_cashneq_to_equity_collapse_8q_d3},
    "f31_cbac_095_fcf_per_revenue_collapse_8q_d3": {"inputs": ["fcf", "revenue"], "func": f31_cbac_095_fcf_per_revenue_collapse_8q_d3},
    "f31_cbac_096_ocf_to_revenue_accel_d3": {"inputs": ["ncfo", "revenue"], "func": f31_cbac_096_ocf_to_revenue_accel_d3},
    "f31_cbac_097_ocf_to_netinc_divergence_accel_d3": {"inputs": ["ncfo", "netinc"], "func": f31_cbac_097_ocf_to_netinc_divergence_accel_d3},
    "f31_cbac_098_ocf_to_netinc_below_half_indicator_d3": {"inputs": ["ncfo", "netinc"], "func": f31_cbac_098_ocf_to_netinc_below_half_indicator_d3},
    "f31_cbac_099_discretionary_cash_collapse_8q_d3": {"inputs": ["ncfo", "capex", "intexp"], "func": f31_cbac_099_discretionary_cash_collapse_8q_d3},
    "f31_cbac_100_discretionary_cash_yoy_collapse_d3": {"inputs": ["ncfo", "capex", "intexp"], "func": f31_cbac_100_discretionary_cash_yoy_collapse_d3},
    "f31_cbac_101_ncfo_cusum_max_excursion_12q_d3": {"inputs": ["ncfo"], "func": f31_cbac_101_ncfo_cusum_max_excursion_12q_d3},
    "f31_cbac_102_fcf_cusum_min_excursion_12q_d3": {"inputs": ["fcf"], "func": f31_cbac_102_fcf_cusum_min_excursion_12q_d3},
    "f31_cbac_103_cashneq_cusum_z_12q_d3": {"inputs": ["cashneq"], "func": f31_cbac_103_cashneq_cusum_z_12q_d3},
    "f31_cbac_104_ncfo_max_abs_residual_recency_8q_d3": {"inputs": ["ncfo"], "func": f31_cbac_104_ncfo_max_abs_residual_recency_8q_d3},
    "f31_cbac_105_fcf_breakpoint_count_16q_d3": {"inputs": ["fcf"], "func": f31_cbac_105_fcf_breakpoint_count_16q_d3},
    "f31_cbac_106_ncfo_likelihood_break_proxy_12q_d3": {"inputs": ["ncfo"], "func": f31_cbac_106_ncfo_likelihood_break_proxy_12q_d3},
    "f31_cbac_107_cashneq_break_recency_max_fstat_12q_d3": {"inputs": ["cashneq"], "func": f31_cbac_107_cashneq_break_recency_max_fstat_12q_d3},
    "f31_cbac_108_fcf_var_ratio_test_zscore_20q_d3": {"inputs": ["fcf"], "func": f31_cbac_108_fcf_var_ratio_test_zscore_20q_d3},
    "f31_cbac_109_ncfo_var_regime_up_significance_12q_d3": {"inputs": ["ncfo"], "func": f31_cbac_109_ncfo_var_regime_up_significance_12q_d3},
    "f31_cbac_110_fcf_var_regime_down_significance_12q_d3": {"inputs": ["fcf"], "func": f31_cbac_110_fcf_var_regime_down_significance_12q_d3},
    "f31_cbac_111_cashneq_mean_diff_t_stat_12q_d3": {"inputs": ["cashneq"], "func": f31_cbac_111_cashneq_mean_diff_t_stat_12q_d3},
    "f31_cbac_112_ncfo_mean_t_signif_down_d3": {"inputs": ["ncfo"], "func": f31_cbac_112_ncfo_mean_t_signif_down_d3},
    "f31_cbac_113_fcf_ks_style_cdf_shift_16q_d3": {"inputs": ["fcf"], "func": f31_cbac_113_fcf_ks_style_cdf_shift_16q_d3},
    "f31_cbac_114_cashneq_median_break_4q_vs_16q_d3": {"inputs": ["cashneq"], "func": f31_cbac_114_cashneq_median_break_4q_vs_16q_d3},
    "f31_cbac_115_ncfo_resid_var_jump_4q_vs_16q_d3": {"inputs": ["ncfo"], "func": f31_cbac_115_ncfo_resid_var_jump_4q_vs_16q_d3},
    "f31_cbac_116_fcf_regression_slope_break_4q_vs_12q_d3": {"inputs": ["fcf"], "func": f31_cbac_116_fcf_regression_slope_break_4q_vs_12q_d3},
    "f31_cbac_117_ncfo_regression_slope_break_4q_vs_12q_d3": {"inputs": ["ncfo"], "func": f31_cbac_117_ncfo_regression_slope_break_4q_vs_12q_d3},
    "f31_cbac_118_cashneq_regression_slope_break_4q_vs_12q_d3": {"inputs": ["cashneq"], "func": f31_cbac_118_cashneq_regression_slope_break_4q_vs_12q_d3},
    "f31_cbac_119_cashneq_combined_break_composite_8q_d3": {"inputs": ["cashneq"], "func": f31_cbac_119_cashneq_combined_break_composite_8q_d3},
    "f31_cbac_120_ncfo_quandt_max_fstat_12q_d3": {"inputs": ["ncfo"], "func": f31_cbac_120_ncfo_quandt_max_fstat_12q_d3},
    "f31_cbac_121_ncfo_drawdown_from_12q_max_d3": {"inputs": ["ncfo"], "func": f31_cbac_121_ncfo_drawdown_from_12q_max_d3},
    "f31_cbac_122_fcf_drawdown_from_16q_max_d3": {"inputs": ["fcf"], "func": f31_cbac_122_fcf_drawdown_from_16q_max_d3},
    "f31_cbac_123_cashneq_drawdown_from_16q_max_d3": {"inputs": ["cashneq"], "func": f31_cbac_123_cashneq_drawdown_from_16q_max_d3},
    "f31_cbac_124_ncfo_q_since_16q_max_d3": {"inputs": ["ncfo"], "func": f31_cbac_124_ncfo_q_since_16q_max_d3},
    "f31_cbac_125_fcf_drawdown_velocity_12q_d3": {"inputs": ["fcf"], "func": f31_cbac_125_fcf_drawdown_velocity_12q_d3},
    "f31_cbac_126_ncfo_pain_ratio_8q_d3": {"inputs": ["ncfo"], "func": f31_cbac_126_ncfo_pain_ratio_8q_d3},
    "f31_cbac_127_fcf_ulcer_index_neg_dd_rms_8q_d3": {"inputs": ["fcf"], "func": f31_cbac_127_fcf_ulcer_index_neg_dd_rms_8q_d3},
    "f31_cbac_128_ncfo_accel_skew_8q_d3": {"inputs": ["ncfo"], "func": f31_cbac_128_ncfo_accel_skew_8q_d3},
    "f31_cbac_129_ncfo_accel_kurt_8q_d3": {"inputs": ["ncfo"], "func": f31_cbac_129_ncfo_accel_kurt_8q_d3},
    "f31_cbac_130_fcf_accel_skew_change_8q_vs_12q_d3": {"inputs": ["fcf"], "func": f31_cbac_130_fcf_accel_skew_change_8q_vs_12q_d3},
    "f31_cbac_131_cashneq_accel_kurt_change_8q_vs_12q_d3": {"inputs": ["cashneq"], "func": f31_cbac_131_cashneq_accel_kurt_change_8q_vs_12q_d3},
    "f31_cbac_132_ncfo_accel_cv_8q_d3": {"inputs": ["ncfo"], "func": f31_cbac_132_ncfo_accel_cv_8q_d3},
    "f31_cbac_133_fcf_accel_quantile_dispersion_q90_q10_12q_d3": {"inputs": ["fcf"], "func": f31_cbac_133_fcf_accel_quantile_dispersion_q90_q10_12q_d3},
    "f31_cbac_134_cashneq_accel_neg_tail_4q_in_16q_q25_d3": {"inputs": ["cashneq"], "func": f31_cbac_134_cashneq_accel_neg_tail_4q_in_16q_q25_d3},
    "f31_cbac_135_ncfo_accel_right_tail_collapse_q90_neg_8q_d3": {"inputs": ["ncfo"], "func": f31_cbac_135_ncfo_accel_right_tail_collapse_q90_neg_8q_d3},
    "f31_cbac_136_fcf_accel_winsorized_z_10pct_8q_d3": {"inputs": ["fcf"], "func": f31_cbac_136_fcf_accel_winsorized_z_10pct_8q_d3},
    "f31_cbac_137_cashneq_accel_sign_runlength_var_8q_d3": {"inputs": ["cashneq"], "func": f31_cbac_137_cashneq_accel_sign_runlength_var_8q_d3},
    "f31_cbac_138_ncfo_accel_persistence_lag1_8q_d3": {"inputs": ["ncfo"], "func": f31_cbac_138_ncfo_accel_persistence_lag1_8q_d3},
    "f31_cbac_139_fcf_consecutive_decline_streak_d3": {"inputs": ["fcf"], "func": f31_cbac_139_fcf_consecutive_decline_streak_d3},
    "f31_cbac_140_ncfo_smoothed_raw_accel_sign_disagree_d3": {"inputs": ["ncfo"], "func": f31_cbac_140_ncfo_smoothed_raw_accel_sign_disagree_d3},
    "f31_cbac_141_composite_burn_crash_5_binaries_8q_d3": {"inputs": ["ncfo", "fcf", "cashneq"], "func": f31_cbac_141_composite_burn_crash_5_binaries_8q_d3},
    "f31_cbac_142_weighted_burn_crash_z_clip_m3_8q_d3": {"inputs": ["ncfo"], "func": f31_cbac_142_weighted_burn_crash_z_clip_m3_8q_d3},
    "f31_cbac_143_multi_horizon_burn_crash_score_fcf_d3": {"inputs": ["fcf"], "func": f31_cbac_143_multi_horizon_burn_crash_score_fcf_d3},
    "f31_cbac_144_ewm_decay_burn_score_8q_ncfo_neg_d3": {"inputs": ["ncfo"], "func": f31_cbac_144_ewm_decay_burn_score_8q_ncfo_neg_d3},
    "f31_cbac_145_logit_insolvency_probability_proxy_d3": {"inputs": ["cashneq", "ncfo"], "func": f31_cbac_145_logit_insolvency_probability_proxy_d3},
    "f31_cbac_146_mahalanobis_dist_ncfo_accel_slope_8q_d3": {"inputs": ["ncfo"], "func": f31_cbac_146_mahalanobis_dist_ncfo_accel_slope_8q_d3},
    "f31_cbac_147_hotelling_t_fcf_accel_vol_8q_d3": {"inputs": ["fcf"], "func": f31_cbac_147_hotelling_t_fcf_accel_vol_8q_d3},
    "f31_cbac_148_cashneq_terminal_distance_5y_proxy_d3": {"inputs": ["cashneq"], "func": f31_cbac_148_cashneq_terminal_distance_5y_proxy_d3},
    "f31_cbac_149_burn_trend_velocity_collapse_4q_over_12q_d3": {"inputs": ["ncfo"], "func": f31_cbac_149_burn_trend_velocity_collapse_4q_over_12q_d3},
    "f31_cbac_150_all_cash_metrics_firing_down_composite_8q_d3": {"inputs": ["ncfo", "fcf", "cashneq"], "func": f31_cbac_150_all_cash_metrics_firing_down_composite_8q_d3},
}
