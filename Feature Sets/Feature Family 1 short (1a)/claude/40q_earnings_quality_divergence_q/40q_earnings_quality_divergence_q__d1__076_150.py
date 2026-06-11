"""earnings_quality_divergence_q d1 features 076-150 — order-1 difference of corresponding base features.

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

def _signed_log_abs(s, eps=1e-12):
    if isinstance(s, pd.Series):
        a = s.abs()
        return np.sign(s) * np.log(a.where(a > eps, np.nan))
    a = np.abs(s)
    return np.sign(s) * np.log(np.where(a > eps, a, np.nan))

def _rolling_zscore(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    m = s.rolling(window, min_periods=min_periods).mean()
    sd = s.rolling(window, min_periods=min_periods).std()
    return (s - m) / sd.replace(0, np.nan)

def _ttm(s):
    return s.rolling(4, min_periods=1).sum()

def _avg4(s):
    return s.rolling(4, min_periods=1).mean()

def _yoy(s):
    return s - s.shift(4)

def _yoy_pct(s):
    return _safe_div(s - s.shift(4), s.shift(4).abs())

def _qoq_pct(s):
    return _safe_div(s.diff(), s.shift(1).abs())

def f40q_eqdgq_076_revenue_growth_minus_earnings_growth_yoy_d1(revenue, netinc):
    return (_yoy_pct(_ttm(revenue)) - _yoy_pct(_ttm(netinc))).diff()

def f40q_eqdgq_077_revenue_growth_minus_ocf_growth_yoy_d1(revenue, ncfo):
    return (_yoy_pct(_ttm(revenue)) - _yoy_pct(_ttm(ncfo))).diff()

def f40q_eqdgq_078_margin_growth_minus_revenue_growth_d1(opinc, revenue):
    m = _safe_div(_ttm(opinc), _ttm(revenue))
    return (_yoy_pct(m) - _yoy_pct(_ttm(revenue))).diff()

def f40q_eqdgq_079_dso_growth_minus_revenue_growth_d1(receivables, revenue):
    dso = _safe_div(365.0 * receivables, _ttm(revenue))
    return (_yoy_pct(dso) - _yoy_pct(_ttm(revenue))).diff()

def f40q_eqdgq_080_dio_growth_minus_revenue_growth_d1(inventory, revenue, cor):
    dio = _safe_div(365.0 * inventory, _ttm(cor))
    return (_yoy_pct(dio) - _yoy_pct(_ttm(revenue))).diff()

def f40q_eqdgq_081_revenue_quality_vs_earnings_quality_gap_d1(revenue, ncfo, netinc):
    rq = _safe_div(_ttm(ncfo), _ttm(revenue).abs())
    eq = _safe_div(_ttm(ncfo), _ttm(netinc).abs())
    return (rq - eq).diff()

def f40q_eqdgq_082_accrual_growth_minus_revenue_growth_d1(netinc, ncfo, revenue):
    accr = _safe_div(_ttm(netinc) - _ttm(ncfo), _ttm(revenue).abs())
    return accr.diff(4).diff()

def f40q_eqdgq_083_receivables_yoy_minus_revenue_yoy_share_d1(receivables, revenue):
    return (_yoy_pct(receivables) - _yoy_pct(_ttm(revenue))).diff()

def f40q_eqdgq_084_inventory_yoy_minus_revenue_yoy_share_d1(inventory, revenue):
    return (_yoy_pct(inventory) - _yoy_pct(_ttm(revenue))).diff()

def f40q_eqdgq_085_workingcapital_yoy_minus_revenue_yoy_d1(workingcapital, revenue):
    return (_yoy_pct(workingcapital) - _yoy_pct(_ttm(revenue))).diff()

def f40q_eqdgq_086_revenue_growth_vs_assets_growth_d1(revenue, assets):
    return (_yoy_pct(_ttm(revenue)) - _yoy_pct(assets)).diff()

def f40q_eqdgq_087_revenue_growth_vs_employee_proxy_d1(revenue, opex):
    return (_yoy_pct(_ttm(revenue)) - _yoy_pct(_ttm(opex))).diff()

def f40q_eqdgq_088_quality_gap_zscore_8q_d1(revenue, netinc, ncfo):
    g = _safe_div(_ttm(ncfo) - _ttm(netinc), _ttm(revenue).abs())
    return _rolling_zscore(g, 8, 3).diff()

def f40q_eqdgq_089_growth_quality_divergence_aggregate_d1(revenue, netinc, ncfo):
    rg = _yoy_pct(_ttm(revenue))
    ng = _yoy_pct(_ttm(netinc))
    cg = _yoy_pct(_ttm(ncfo))
    return (rg - (ng + cg) / 2.0).diff()

def f40q_eqdgq_090_rev_to_ar_growth_inversion_count_8q_d1(revenue, receivables):
    inv = (_yoy_pct(_ttm(revenue)) < 0) & (_yoy_pct(receivables) > 0)
    return inv.astype(float).rolling(8, min_periods=3).sum().diff()

def f40q_eqdgq_091_earnings_smoothness_lag1_autocorr_8q_d1(netinc):
    return netinc.rolling(8, min_periods=4).apply(lambda w: np.corrcoef(w[:-1], w[1:])[0, 1] if np.std(w[:-1]) > 0 and np.std(w[1:]) > 0 else np.nan, raw=True).diff()

def f40q_eqdgq_092_earnings_smoothness_via_negative_correl_accrual_cf_8q_d1(netinc, ncfo):
    accr = netinc - ncfo
    return accr.rolling(8, min_periods=4).apply(lambda w: np.corrcoef(w, np.arange(len(w)))[0, 1] if np.std(w) > 0 else np.nan, raw=True).diff()

def f40q_eqdgq_093_earnings_volatility_minus_cf_volatility_d1(netinc, ncfo):
    return (netinc.rolling(8, min_periods=3).std() - ncfo.rolling(8, min_periods=3).std()).diff()

def f40q_eqdgq_094_cf_volatility_minus_earnings_volatility_zscore_d1(netinc, ncfo):
    diff = ncfo.rolling(8, min_periods=3).std() - netinc.rolling(8, min_periods=3).std()
    return _rolling_zscore(diff, 12, 4).diff()

def f40q_eqdgq_095_low_variance_earnings_suspicion_8q_d1(netinc, revenue):
    cv_ni = _safe_div(netinc.rolling(8, min_periods=3).std(), netinc.rolling(8, min_periods=3).mean().abs())
    cv_rev = _safe_div(revenue.rolling(8, min_periods=3).std(), revenue.rolling(8, min_periods=3).mean().abs())
    return (cv_rev - cv_ni).diff()

def f40q_eqdgq_096_target_beat_smoothing_proxy_8q_d1(netinc):
    return ((netinc - netinc.shift(1)).abs() < netinc.abs() * 0.02).rolling(8, min_periods=3).sum().diff()

def f40q_eqdgq_097_earnings_q_close_to_zero_count_8q_d1(netinc, revenue):
    near_zero = _safe_div(netinc, revenue.abs()).abs() < 0.005
    return near_zero.rolling(8, min_periods=3).sum().diff()

def f40q_eqdgq_098_positive_eps_just_above_zero_count_8q_d1(eps):
    return ((eps > 0) & (eps < 0.05)).rolling(8, min_periods=3).sum().diff()

def f40q_eqdgq_099_eps_change_close_to_zero_count_8q_d1(eps):
    return (eps.diff().abs() < 0.01).rolling(8, min_periods=3).sum().diff()

def f40q_eqdgq_100_smoothing_index_kothari_style_d1(netinc, ncfo, assets):
    accr = (netinc - ncfo) / assets.replace(0, np.nan)
    cf = ncfo / assets.replace(0, np.nan)
    return accr.rolling(8, min_periods=4).apply(lambda w: np.nan, raw=True).fillna(accr.rolling(8, min_periods=4).corr(cf)).diff()

def f40q_eqdgq_101_earnings_distribution_kink_proxy_d1(netinc):
    return ((netinc >= 0) & (netinc.shift(1) < 0)).astype(float).diff()

def f40q_eqdgq_102_smoothing_via_low_accrual_volatility_8q_d1(netinc, ncfo, assets):
    a = (netinc - ncfo) / assets.replace(0, np.nan)
    return (-a.rolling(8, min_periods=3).std()).diff()

def f40q_eqdgq_103_persistence_score_netinc_lag1_4q_d1(netinc):
    return netinc.rolling(4, min_periods=2).apply(lambda w: np.corrcoef(w[:-1], w[1:])[0, 1] if len(w) >= 2 and np.std(w[:-1]) > 0 and (np.std(w[1:]) > 0) else np.nan, raw=True).diff()

def f40q_eqdgq_104_predictability_minus_persistence_diff_d1(netinc, ncfo):
    p_ni = netinc.rolling(8, min_periods=4).apply(lambda w: np.corrcoef(w[:-1], w[1:])[0, 1] if np.std(w[:-1]) > 0 and np.std(w[1:]) > 0 else np.nan, raw=True)
    p_cf = ncfo.rolling(8, min_periods=4).apply(lambda w: np.corrcoef(w[:-1], w[1:])[0, 1] if np.std(w[:-1]) > 0 and np.std(w[1:]) > 0 else np.nan, raw=True)
    return (p_ni - p_cf).diff()

def f40q_eqdgq_105_qoq_earnings_change_skew_8q_d1(netinc):
    return netinc.diff().rolling(8, min_periods=4).skew().diff()

def f40q_eqdgq_106_dsri_days_sales_receivables_index_d1(receivables, revenue):
    dso = _safe_div(365.0 * receivables, _ttm(revenue))
    return _safe_div(dso, dso.shift(4)).diff()

def f40q_eqdgq_107_gmi_gross_margin_index_d1(gp, revenue):
    gm = _safe_div(_ttm(gp), _ttm(revenue))
    return _safe_div(gm.shift(4), gm).diff()

def f40q_eqdgq_108_aqi_asset_quality_index_d1(assets, ppnenet, assetsc):
    nonproductive = _safe_div(assets - assetsc - ppnenet, assets)
    return _safe_div(nonproductive, nonproductive.shift(4)).diff()

def f40q_eqdgq_109_sgi_sales_growth_index_d1(revenue):
    return _safe_div(_ttm(revenue), _ttm(revenue).shift(4)).diff()

def f40q_eqdgq_110_depi_depreciation_index_d1(depamor, ppnenet):
    rate = _safe_div(_ttm(depamor), _ttm(depamor) + ppnenet)
    return _safe_div(rate.shift(4), rate).diff()

def f40q_eqdgq_111_sgai_sgna_index_d1(sgna, revenue):
    ratio = _safe_div(_ttm(sgna), _ttm(revenue))
    return _safe_div(ratio, ratio.shift(4)).diff()

def f40q_eqdgq_112_lvgi_leverage_index_d1(liabilities, assets):
    lev = _safe_div(liabilities, assets)
    return _safe_div(lev, lev.shift(4)).diff()

def f40q_eqdgq_113_tata_total_accruals_to_assets_d1(netinc, ncfo, assets):
    return _safe_div(_ttm(netinc) - _ttm(ncfo), assets).diff()

def f40q_eqdgq_114_beneish_m_partial_5sig_d1(receivables, revenue, gp, sgna, depamor, ppnenet):
    dsri = _safe_div(_safe_div(365.0 * receivables, _ttm(revenue)), _safe_div(365.0 * receivables, _ttm(revenue)).shift(4))
    gm = _safe_div(_ttm(gp), _ttm(revenue))
    gmi = _safe_div(gm.shift(4), gm)
    sgi = _safe_div(_ttm(revenue), _ttm(revenue).shift(4))
    rate = _safe_div(_ttm(depamor), _ttm(depamor) + ppnenet)
    depi = _safe_div(rate.shift(4), rate)
    sgai = _safe_div(_safe_div(_ttm(sgna), _ttm(revenue)), _safe_div(_ttm(sgna), _ttm(revenue)).shift(4))
    return (dsri + gmi + sgi + depi + sgai).diff()

def f40q_eqdgq_115_modified_jones_residual_proxy_d1(revenue, receivables, ppnenet, assets):
    rev_growth = _ttm(revenue).diff(4)
    ar_growth = receivables.diff(4)
    expected_accr = (rev_growth - ar_growth + ppnenet) / assets.replace(0, np.nan)
    return (-expected_accr).diff()

def f40q_eqdgq_116_dechow_dichev_quality_proxy_d1(ncfo, assets):
    a = _safe_div(ncfo, assets)
    return a.rolling(8, min_periods=4).apply(lambda w: np.corrcoef(w[:-1], w[1:])[0, 1] if np.std(w[:-1]) > 0 and np.std(w[1:]) > 0 else np.nan, raw=True).diff()

def f40q_eqdgq_117_revenue_per_dollar_receivables_yoy_d1(revenue, receivables):
    rpr = _safe_div(_ttm(revenue), receivables)
    return _yoy_pct(rpr).diff()

def f40q_eqdgq_118_inventory_turnover_minus_industry_proxy_d1(cor, inventory):
    inv_t = _safe_div(_ttm(cor), inventory)
    return (inv_t - inv_t.rolling(20, min_periods=6).mean()).diff()

def f40q_eqdgq_119_capitalization_intensity_yoy_d1(intangibles, ppnenet, assets):
    cap = _safe_div(intangibles + ppnenet, assets)
    return _yoy(cap).diff()

def f40q_eqdgq_120_accrual_quality_decline_zscore_12q_d1(netinc, ncfo, assets):
    q = _safe_div(_ttm(ncfo), _ttm(netinc).abs())
    return (-_rolling_zscore(q.diff().clip(upper=0).abs(), 12, 4)).diff()

def f40q_eqdgq_121_quality_composite_zscore_aggregate_d1(netinc, ncfo, fcf, assets):
    z1 = _rolling_zscore(_safe_div(_ttm(netinc) - _ttm(ncfo), assets), 12, 4)
    z2 = _rolling_zscore(_safe_div(_ttm(netinc) - _ttm(fcf), assets), 12, 4)
    return ((z1 + z2) / 2.0).diff()

def f40q_eqdgq_122_accrual_anomaly_score_q_d1(netinc, ncfo, assets):
    a = _safe_div(_ttm(netinc) - _ttm(ncfo), assets)
    return _rolling_zscore(a, 12, 4).diff()

def f40q_eqdgq_123_quality_decay_persistence_score_d1(ncfo, netinc):
    q = _safe_div(_ttm(ncfo), _ttm(netinc).abs())
    return (-q.diff().rolling(8, min_periods=3).sum().clip(upper=0)).diff()

def f40q_eqdgq_124_persistent_low_quality_q_count_8q_d1(ncfo, netinc):
    q = _safe_div(ncfo, netinc.abs())
    return (q < 0.5).astype(float).rolling(8, min_periods=3).sum().diff()

def f40q_eqdgq_125_eq_divergence_aggregate_5component_d1(netinc, ncfo, fcf, opinc, ebitda, assets):
    z1 = _rolling_zscore(_safe_div(_ttm(netinc) - _ttm(ncfo), assets), 12, 4)
    z2 = _rolling_zscore(_safe_div(_ttm(netinc) - _ttm(fcf), assets), 12, 4)
    z3 = _rolling_zscore(_safe_div(_ttm(opinc) - _ttm(ncfo), assets), 12, 4)
    z4 = _rolling_zscore(_safe_div(_ttm(ebitda) - _ttm(ncfo), assets), 12, 4)
    z5 = _rolling_zscore(_safe_div(_ttm(netinc) - _ttm(opinc), assets), 12, 4)
    return ((z1 + z2 + z3 + z4 + z5) / 5.0).diff()

def f40q_eqdgq_126_quality_collapse_trigger_4q_d1(ncfo, netinc):
    q = _safe_div(ncfo, netinc.abs())
    return (q.rolling(4, min_periods=2).mean() - q.rolling(8, min_periods=3).mean()).diff()

def f40q_eqdgq_127_quality_volatility_zscore_12q_d1(ncfo, netinc):
    q = _safe_div(_ttm(ncfo), _ttm(netinc).abs())
    return _rolling_zscore(q.rolling(4, min_periods=2).std(), 12, 4).diff()

def f40q_eqdgq_128_earnings_quality_q4_minus_q1_swing_d1(ncfo, netinc):
    q = _safe_div(ncfo, netinc.abs())
    return (q - q.shift(3)).diff()

def f40q_eqdgq_129_negative_quality_persistence_score_8q_d1(ncfo, netinc):
    q = _safe_div(ncfo, netinc.abs())
    neg = (q < 0).astype(int)
    return neg.rolling(8, min_periods=3).apply(lambda w: int(w[::-1].cumprod().sum()), raw=True).diff()

def f40q_eqdgq_130_quality_inconsistency_index_8q_d1(ncfo, netinc, fcf):
    q1 = _safe_div(ncfo, netinc.abs())
    q2 = _safe_div(fcf, netinc.abs())
    return (q1 - q2).rolling(8, min_periods=3).std().diff()

def f40q_eqdgq_131_revenue_to_ncfo_growth_decoupling_d1(revenue, ncfo):
    return (_yoy_pct(_ttm(revenue)) - _yoy_pct(_ttm(ncfo))).diff()

def f40q_eqdgq_132_revenue_to_netinc_growth_decoupling_d1(revenue, netinc):
    return (_yoy_pct(_ttm(revenue)) - _yoy_pct(_ttm(netinc))).diff()

def f40q_eqdgq_133_combined_quality_decline_signal_d1(netinc, ncfo, fcf, opinc):
    a = -_rolling_zscore(_safe_div(_ttm(ncfo), _ttm(netinc).abs()), 12, 4)
    b = -_rolling_zscore(_safe_div(_ttm(fcf), _ttm(netinc).abs()), 12, 4)
    c = -_rolling_zscore(_safe_div(_ttm(opinc), _ttm(netinc).abs()), 12, 4)
    return ((a + b + c) / 3.0).diff()

def f40q_eqdgq_134_accrual_aware_revenue_growth_d1(revenue, netinc, ncfo):
    quality_drag = _safe_div(_ttm(netinc) - _ttm(ncfo), _ttm(revenue).abs())
    return (_yoy_pct(_ttm(revenue)) - quality_drag).diff()

def f40q_eqdgq_135_capex_to_depamor_minus_1_to_assets_d1(capex, depamor, assets):
    return _safe_div(_ttm(capex).abs() - _ttm(depamor), assets).diff()

def f40q_eqdgq_136_special_items_aggregate_via_belowline_d1(netinc, opinc, taxexp):
    eff = _safe_div(_ttm(taxexp), _ttm(opinc).abs()).clip(lower=0, upper=0.6)
    nonop = _safe_div(_ttm(netinc) - _ttm(opinc) * (1.0 - eff), _ttm(netinc).abs())
    return nonop.abs().diff()

def f40q_eqdgq_137_quality_breakdown_diffusion_index_8q_d1(netinc, ncfo, fcf, opinc):
    drops = pd.concat([(netinc - ncfo).diff() > 0, (netinc - fcf).diff() > 0, (netinc - opinc).diff() > 0], axis=1).sum(axis=1)
    return drops.rolling(8, min_periods=3).mean().diff()

def f40q_eqdgq_138_quality_disagreement_index_8q_d1(netinc, ncfo, fcf, opinc):
    df = pd.concat([_yoy(_ttm(netinc)), _yoy(_ttm(ncfo)), _yoy(_ttm(fcf)), _yoy(_ttm(opinc))], axis=1)
    return (df.std(axis=1) / df.abs().mean(axis=1).replace(0, np.nan)).diff()

def f40q_eqdgq_139_negative_accrual_dominance_8q_d1(netinc, ncfo):
    a = netinc - ncfo
    return (a < 0).rolling(8, min_periods=3).mean().diff()

def f40q_eqdgq_140_accrual_acceleration_zscore_12q_d1(netinc, ncfo, assets):
    a = _safe_div(netinc - ncfo, assets)
    return _rolling_zscore(a.diff(), 12, 4).diff()

def f40q_eqdgq_141_earnings_persistence_index_long_term_8q_d1(netinc, assets):
    e = _safe_div(_ttm(netinc), assets)
    return e.rolling(8, min_periods=4).apply(lambda w: np.corrcoef(w[:-1], w[1:])[0, 1] if np.std(w[:-1]) > 0 and np.std(w[1:]) > 0 else np.nan, raw=True).diff()

def f40q_eqdgq_142_quality_minus_growth_score_d1(ncfo, netinc, revenue):
    q = _safe_div(_ttm(ncfo), _ttm(netinc).abs())
    g = _yoy_pct(_ttm(revenue))
    return (q - g.clip(lower=0)).diff()

def f40q_eqdgq_143_aggressive_revenue_recognition_proxy_d1(receivables, revenue, deferredrev):
    return _safe_div(receivables.diff() - deferredrev.diff(), _ttm(revenue).abs()).diff()

def f40q_eqdgq_144_smoothing_ratio_score_8q_d1(netinc, ncfo, revenue):
    cv_ni = _safe_div(netinc.rolling(8, min_periods=3).std(), netinc.rolling(8, min_periods=3).mean().abs())
    cv_cf = _safe_div(ncfo.rolling(8, min_periods=3).std(), ncfo.rolling(8, min_periods=3).mean().abs())
    return (cv_cf - cv_ni).diff()

def f40q_eqdgq_145_eq_collapse_signal_aggregate_d1(ncfo, netinc, fcf, opinc):
    sig1 = _safe_div(_ttm(ncfo), _ttm(netinc).abs()).diff().clip(upper=0)
    sig2 = _safe_div(_ttm(fcf), _ttm(netinc).abs()).diff().clip(upper=0)
    sig3 = _safe_div(_ttm(opinc), _ttm(netinc).abs()).diff().clip(upper=0)
    return (-(sig1 + sig2 + sig3)).diff()

def f40q_eqdgq_146_quality_dispersion_among_measures_8q_d1(netinc, ncfo, fcf, opinc, revenue):
    rev = _ttm(revenue).abs().replace(0, np.nan)
    df = pd.concat([_ttm(netinc) / rev, _ttm(ncfo) / rev, _ttm(fcf) / rev, _ttm(opinc) / rev], axis=1)
    return df.rolling(8, min_periods=3).std().mean(axis=1).diff()

def f40q_eqdgq_147_quality_falloff_signal_4q_d1(ncfo, netinc):
    q = _safe_div(ncfo, netinc.abs())
    return (q.rolling(4, min_periods=2).min() - q.rolling(4, min_periods=2).max().shift(4)).diff()

def f40q_eqdgq_148_quality_anomaly_streak_8q_d1(ncfo, netinc):
    q = _safe_div(_ttm(ncfo), _ttm(netinc).abs())
    drops = (q.diff() < 0).astype(int)
    return drops.rolling(8, min_periods=3).apply(lambda w: int(w[::-1].cumprod().sum()), raw=True).diff()

def f40q_eqdgq_149_quality_zscore_minus_long_avg_d1(ncfo, netinc):
    q = _safe_div(_ttm(ncfo), _ttm(netinc).abs())
    return (q - q.rolling(20, min_periods=6).mean()).diff()

def f40q_eqdgq_150_full_quality_divergence_composite_d1(netinc, ncfo, fcf, opinc, ebitda, assets, revenue):
    z1 = _rolling_zscore(_safe_div(_ttm(netinc) - _ttm(ncfo), assets), 12, 4)
    z2 = _rolling_zscore(_safe_div(_ttm(netinc) - _ttm(fcf), assets), 12, 4)
    z3 = _rolling_zscore(_safe_div(_ttm(opinc) - _ttm(ncfo), assets), 12, 4)
    z4 = _rolling_zscore(_safe_div(_ttm(ebitda) - _ttm(ncfo), _ttm(revenue).abs()), 12, 4)
    return ((z1 + z2 + z3 + z4) / 4.0).diff()
EARNINGS_QUALITY_DIVERGENCE_Q_D1_REGISTRY_076_150 = {'f40q_eqdgq_076_revenue_growth_minus_earnings_growth_yoy_d1': {'inputs': ['revenue', 'netinc'], 'func': f40q_eqdgq_076_revenue_growth_minus_earnings_growth_yoy_d1}, 'f40q_eqdgq_077_revenue_growth_minus_ocf_growth_yoy_d1': {'inputs': ['revenue', 'ncfo'], 'func': f40q_eqdgq_077_revenue_growth_minus_ocf_growth_yoy_d1}, 'f40q_eqdgq_078_margin_growth_minus_revenue_growth_d1': {'inputs': ['opinc', 'revenue'], 'func': f40q_eqdgq_078_margin_growth_minus_revenue_growth_d1}, 'f40q_eqdgq_079_dso_growth_minus_revenue_growth_d1': {'inputs': ['receivables', 'revenue'], 'func': f40q_eqdgq_079_dso_growth_minus_revenue_growth_d1}, 'f40q_eqdgq_080_dio_growth_minus_revenue_growth_d1': {'inputs': ['inventory', 'revenue', 'cor'], 'func': f40q_eqdgq_080_dio_growth_minus_revenue_growth_d1}, 'f40q_eqdgq_081_revenue_quality_vs_earnings_quality_gap_d1': {'inputs': ['revenue', 'ncfo', 'netinc'], 'func': f40q_eqdgq_081_revenue_quality_vs_earnings_quality_gap_d1}, 'f40q_eqdgq_082_accrual_growth_minus_revenue_growth_d1': {'inputs': ['netinc', 'ncfo', 'revenue'], 'func': f40q_eqdgq_082_accrual_growth_minus_revenue_growth_d1}, 'f40q_eqdgq_083_receivables_yoy_minus_revenue_yoy_share_d1': {'inputs': ['receivables', 'revenue'], 'func': f40q_eqdgq_083_receivables_yoy_minus_revenue_yoy_share_d1}, 'f40q_eqdgq_084_inventory_yoy_minus_revenue_yoy_share_d1': {'inputs': ['inventory', 'revenue'], 'func': f40q_eqdgq_084_inventory_yoy_minus_revenue_yoy_share_d1}, 'f40q_eqdgq_085_workingcapital_yoy_minus_revenue_yoy_d1': {'inputs': ['workingcapital', 'revenue'], 'func': f40q_eqdgq_085_workingcapital_yoy_minus_revenue_yoy_d1}, 'f40q_eqdgq_086_revenue_growth_vs_assets_growth_d1': {'inputs': ['revenue', 'assets'], 'func': f40q_eqdgq_086_revenue_growth_vs_assets_growth_d1}, 'f40q_eqdgq_087_revenue_growth_vs_employee_proxy_d1': {'inputs': ['revenue', 'opex'], 'func': f40q_eqdgq_087_revenue_growth_vs_employee_proxy_d1}, 'f40q_eqdgq_088_quality_gap_zscore_8q_d1': {'inputs': ['revenue', 'netinc', 'ncfo'], 'func': f40q_eqdgq_088_quality_gap_zscore_8q_d1}, 'f40q_eqdgq_089_growth_quality_divergence_aggregate_d1': {'inputs': ['revenue', 'netinc', 'ncfo'], 'func': f40q_eqdgq_089_growth_quality_divergence_aggregate_d1}, 'f40q_eqdgq_090_rev_to_ar_growth_inversion_count_8q_d1': {'inputs': ['revenue', 'receivables'], 'func': f40q_eqdgq_090_rev_to_ar_growth_inversion_count_8q_d1}, 'f40q_eqdgq_091_earnings_smoothness_lag1_autocorr_8q_d1': {'inputs': ['netinc'], 'func': f40q_eqdgq_091_earnings_smoothness_lag1_autocorr_8q_d1}, 'f40q_eqdgq_092_earnings_smoothness_via_negative_correl_accrual_cf_8q_d1': {'inputs': ['netinc', 'ncfo'], 'func': f40q_eqdgq_092_earnings_smoothness_via_negative_correl_accrual_cf_8q_d1}, 'f40q_eqdgq_093_earnings_volatility_minus_cf_volatility_d1': {'inputs': ['netinc', 'ncfo'], 'func': f40q_eqdgq_093_earnings_volatility_minus_cf_volatility_d1}, 'f40q_eqdgq_094_cf_volatility_minus_earnings_volatility_zscore_d1': {'inputs': ['netinc', 'ncfo'], 'func': f40q_eqdgq_094_cf_volatility_minus_earnings_volatility_zscore_d1}, 'f40q_eqdgq_095_low_variance_earnings_suspicion_8q_d1': {'inputs': ['netinc', 'revenue'], 'func': f40q_eqdgq_095_low_variance_earnings_suspicion_8q_d1}, 'f40q_eqdgq_096_target_beat_smoothing_proxy_8q_d1': {'inputs': ['netinc'], 'func': f40q_eqdgq_096_target_beat_smoothing_proxy_8q_d1}, 'f40q_eqdgq_097_earnings_q_close_to_zero_count_8q_d1': {'inputs': ['netinc', 'revenue'], 'func': f40q_eqdgq_097_earnings_q_close_to_zero_count_8q_d1}, 'f40q_eqdgq_098_positive_eps_just_above_zero_count_8q_d1': {'inputs': ['eps'], 'func': f40q_eqdgq_098_positive_eps_just_above_zero_count_8q_d1}, 'f40q_eqdgq_099_eps_change_close_to_zero_count_8q_d1': {'inputs': ['eps'], 'func': f40q_eqdgq_099_eps_change_close_to_zero_count_8q_d1}, 'f40q_eqdgq_100_smoothing_index_kothari_style_d1': {'inputs': ['netinc', 'ncfo', 'assets'], 'func': f40q_eqdgq_100_smoothing_index_kothari_style_d1}, 'f40q_eqdgq_101_earnings_distribution_kink_proxy_d1': {'inputs': ['netinc'], 'func': f40q_eqdgq_101_earnings_distribution_kink_proxy_d1}, 'f40q_eqdgq_102_smoothing_via_low_accrual_volatility_8q_d1': {'inputs': ['netinc', 'ncfo', 'assets'], 'func': f40q_eqdgq_102_smoothing_via_low_accrual_volatility_8q_d1}, 'f40q_eqdgq_103_persistence_score_netinc_lag1_4q_d1': {'inputs': ['netinc'], 'func': f40q_eqdgq_103_persistence_score_netinc_lag1_4q_d1}, 'f40q_eqdgq_104_predictability_minus_persistence_diff_d1': {'inputs': ['netinc', 'ncfo'], 'func': f40q_eqdgq_104_predictability_minus_persistence_diff_d1}, 'f40q_eqdgq_105_qoq_earnings_change_skew_8q_d1': {'inputs': ['netinc'], 'func': f40q_eqdgq_105_qoq_earnings_change_skew_8q_d1}, 'f40q_eqdgq_106_dsri_days_sales_receivables_index_d1': {'inputs': ['receivables', 'revenue'], 'func': f40q_eqdgq_106_dsri_days_sales_receivables_index_d1}, 'f40q_eqdgq_107_gmi_gross_margin_index_d1': {'inputs': ['gp', 'revenue'], 'func': f40q_eqdgq_107_gmi_gross_margin_index_d1}, 'f40q_eqdgq_108_aqi_asset_quality_index_d1': {'inputs': ['assets', 'ppnenet', 'assetsc'], 'func': f40q_eqdgq_108_aqi_asset_quality_index_d1}, 'f40q_eqdgq_109_sgi_sales_growth_index_d1': {'inputs': ['revenue'], 'func': f40q_eqdgq_109_sgi_sales_growth_index_d1}, 'f40q_eqdgq_110_depi_depreciation_index_d1': {'inputs': ['depamor', 'ppnenet'], 'func': f40q_eqdgq_110_depi_depreciation_index_d1}, 'f40q_eqdgq_111_sgai_sgna_index_d1': {'inputs': ['sgna', 'revenue'], 'func': f40q_eqdgq_111_sgai_sgna_index_d1}, 'f40q_eqdgq_112_lvgi_leverage_index_d1': {'inputs': ['liabilities', 'assets'], 'func': f40q_eqdgq_112_lvgi_leverage_index_d1}, 'f40q_eqdgq_113_tata_total_accruals_to_assets_d1': {'inputs': ['netinc', 'ncfo', 'assets'], 'func': f40q_eqdgq_113_tata_total_accruals_to_assets_d1}, 'f40q_eqdgq_114_beneish_m_partial_5sig_d1': {'inputs': ['receivables', 'revenue', 'gp', 'sgna', 'depamor', 'ppnenet'], 'func': f40q_eqdgq_114_beneish_m_partial_5sig_d1}, 'f40q_eqdgq_115_modified_jones_residual_proxy_d1': {'inputs': ['revenue', 'receivables', 'ppnenet', 'assets'], 'func': f40q_eqdgq_115_modified_jones_residual_proxy_d1}, 'f40q_eqdgq_116_dechow_dichev_quality_proxy_d1': {'inputs': ['ncfo', 'assets'], 'func': f40q_eqdgq_116_dechow_dichev_quality_proxy_d1}, 'f40q_eqdgq_117_revenue_per_dollar_receivables_yoy_d1': {'inputs': ['revenue', 'receivables'], 'func': f40q_eqdgq_117_revenue_per_dollar_receivables_yoy_d1}, 'f40q_eqdgq_118_inventory_turnover_minus_industry_proxy_d1': {'inputs': ['cor', 'inventory'], 'func': f40q_eqdgq_118_inventory_turnover_minus_industry_proxy_d1}, 'f40q_eqdgq_119_capitalization_intensity_yoy_d1': {'inputs': ['intangibles', 'ppnenet', 'assets'], 'func': f40q_eqdgq_119_capitalization_intensity_yoy_d1}, 'f40q_eqdgq_120_accrual_quality_decline_zscore_12q_d1': {'inputs': ['netinc', 'ncfo', 'assets'], 'func': f40q_eqdgq_120_accrual_quality_decline_zscore_12q_d1}, 'f40q_eqdgq_121_quality_composite_zscore_aggregate_d1': {'inputs': ['netinc', 'ncfo', 'fcf', 'assets'], 'func': f40q_eqdgq_121_quality_composite_zscore_aggregate_d1}, 'f40q_eqdgq_122_accrual_anomaly_score_q_d1': {'inputs': ['netinc', 'ncfo', 'assets'], 'func': f40q_eqdgq_122_accrual_anomaly_score_q_d1}, 'f40q_eqdgq_123_quality_decay_persistence_score_d1': {'inputs': ['ncfo', 'netinc'], 'func': f40q_eqdgq_123_quality_decay_persistence_score_d1}, 'f40q_eqdgq_124_persistent_low_quality_q_count_8q_d1': {'inputs': ['ncfo', 'netinc'], 'func': f40q_eqdgq_124_persistent_low_quality_q_count_8q_d1}, 'f40q_eqdgq_125_eq_divergence_aggregate_5component_d1': {'inputs': ['netinc', 'ncfo', 'fcf', 'opinc', 'ebitda', 'assets'], 'func': f40q_eqdgq_125_eq_divergence_aggregate_5component_d1}, 'f40q_eqdgq_126_quality_collapse_trigger_4q_d1': {'inputs': ['ncfo', 'netinc'], 'func': f40q_eqdgq_126_quality_collapse_trigger_4q_d1}, 'f40q_eqdgq_127_quality_volatility_zscore_12q_d1': {'inputs': ['ncfo', 'netinc'], 'func': f40q_eqdgq_127_quality_volatility_zscore_12q_d1}, 'f40q_eqdgq_128_earnings_quality_q4_minus_q1_swing_d1': {'inputs': ['ncfo', 'netinc'], 'func': f40q_eqdgq_128_earnings_quality_q4_minus_q1_swing_d1}, 'f40q_eqdgq_129_negative_quality_persistence_score_8q_d1': {'inputs': ['ncfo', 'netinc'], 'func': f40q_eqdgq_129_negative_quality_persistence_score_8q_d1}, 'f40q_eqdgq_130_quality_inconsistency_index_8q_d1': {'inputs': ['ncfo', 'netinc', 'fcf'], 'func': f40q_eqdgq_130_quality_inconsistency_index_8q_d1}, 'f40q_eqdgq_131_revenue_to_ncfo_growth_decoupling_d1': {'inputs': ['revenue', 'ncfo'], 'func': f40q_eqdgq_131_revenue_to_ncfo_growth_decoupling_d1}, 'f40q_eqdgq_132_revenue_to_netinc_growth_decoupling_d1': {'inputs': ['revenue', 'netinc'], 'func': f40q_eqdgq_132_revenue_to_netinc_growth_decoupling_d1}, 'f40q_eqdgq_133_combined_quality_decline_signal_d1': {'inputs': ['netinc', 'ncfo', 'fcf', 'opinc'], 'func': f40q_eqdgq_133_combined_quality_decline_signal_d1}, 'f40q_eqdgq_134_accrual_aware_revenue_growth_d1': {'inputs': ['revenue', 'netinc', 'ncfo'], 'func': f40q_eqdgq_134_accrual_aware_revenue_growth_d1}, 'f40q_eqdgq_135_capex_to_depamor_minus_1_to_assets_d1': {'inputs': ['capex', 'depamor', 'assets'], 'func': f40q_eqdgq_135_capex_to_depamor_minus_1_to_assets_d1}, 'f40q_eqdgq_136_special_items_aggregate_via_belowline_d1': {'inputs': ['netinc', 'opinc', 'taxexp'], 'func': f40q_eqdgq_136_special_items_aggregate_via_belowline_d1}, 'f40q_eqdgq_137_quality_breakdown_diffusion_index_8q_d1': {'inputs': ['netinc', 'ncfo', 'fcf', 'opinc'], 'func': f40q_eqdgq_137_quality_breakdown_diffusion_index_8q_d1}, 'f40q_eqdgq_138_quality_disagreement_index_8q_d1': {'inputs': ['netinc', 'ncfo', 'fcf', 'opinc'], 'func': f40q_eqdgq_138_quality_disagreement_index_8q_d1}, 'f40q_eqdgq_139_negative_accrual_dominance_8q_d1': {'inputs': ['netinc', 'ncfo'], 'func': f40q_eqdgq_139_negative_accrual_dominance_8q_d1}, 'f40q_eqdgq_140_accrual_acceleration_zscore_12q_d1': {'inputs': ['netinc', 'ncfo', 'assets'], 'func': f40q_eqdgq_140_accrual_acceleration_zscore_12q_d1}, 'f40q_eqdgq_141_earnings_persistence_index_long_term_8q_d1': {'inputs': ['netinc', 'assets'], 'func': f40q_eqdgq_141_earnings_persistence_index_long_term_8q_d1}, 'f40q_eqdgq_142_quality_minus_growth_score_d1': {'inputs': ['ncfo', 'netinc', 'revenue'], 'func': f40q_eqdgq_142_quality_minus_growth_score_d1}, 'f40q_eqdgq_143_aggressive_revenue_recognition_proxy_d1': {'inputs': ['receivables', 'revenue', 'deferredrev'], 'func': f40q_eqdgq_143_aggressive_revenue_recognition_proxy_d1}, 'f40q_eqdgq_144_smoothing_ratio_score_8q_d1': {'inputs': ['netinc', 'ncfo', 'revenue'], 'func': f40q_eqdgq_144_smoothing_ratio_score_8q_d1}, 'f40q_eqdgq_145_eq_collapse_signal_aggregate_d1': {'inputs': ['ncfo', 'netinc', 'fcf', 'opinc'], 'func': f40q_eqdgq_145_eq_collapse_signal_aggregate_d1}, 'f40q_eqdgq_146_quality_dispersion_among_measures_8q_d1': {'inputs': ['netinc', 'ncfo', 'fcf', 'opinc', 'revenue'], 'func': f40q_eqdgq_146_quality_dispersion_among_measures_8q_d1}, 'f40q_eqdgq_147_quality_falloff_signal_4q_d1': {'inputs': ['ncfo', 'netinc'], 'func': f40q_eqdgq_147_quality_falloff_signal_4q_d1}, 'f40q_eqdgq_148_quality_anomaly_streak_8q_d1': {'inputs': ['ncfo', 'netinc'], 'func': f40q_eqdgq_148_quality_anomaly_streak_8q_d1}, 'f40q_eqdgq_149_quality_zscore_minus_long_avg_d1': {'inputs': ['ncfo', 'netinc'], 'func': f40q_eqdgq_149_quality_zscore_minus_long_avg_d1}, 'f40q_eqdgq_150_full_quality_divergence_composite_d1': {'inputs': ['netinc', 'ncfo', 'fcf', 'opinc', 'ebitda', 'assets', 'revenue'], 'func': f40q_eqdgq_150_full_quality_divergence_composite_d1}}