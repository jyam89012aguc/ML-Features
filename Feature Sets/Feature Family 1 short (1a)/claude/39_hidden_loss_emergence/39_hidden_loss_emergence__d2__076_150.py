"""hidden_loss_emergence d2 features 076-150 — order-2 difference of corresponding base features.

Each function inlines the base body and wraps the return value with .diff().diff(). Self-contained; helpers redefined locally per HANDOFF."""
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

def f39_hlem_076_sgna_qoq_jump_zscore_8q_d2(sgna):
    return _rolling_zscore(sgna.diff().clip(lower=0), 8, 3).diff().diff()

def f39_hlem_077_sgna_yoy_minus_revenue_yoy_d2(sgna, revenue):
    return (_yoy_pct(_ttm(sgna)) - _yoy_pct(_ttm(revenue))).diff().diff()

def f39_hlem_078_sgna_share_of_revenue_qoq_jump_d2(sgna, revenue):
    return _safe_div(sgna, revenue.abs()).diff().clip(lower=0).diff().diff()

def f39_hlem_079_opex_qoq_jump_zscore_8q_d2(opex):
    return _rolling_zscore(opex.diff().clip(lower=0), 8, 3).diff().diff()

def f39_hlem_080_opex_minus_cor_share_of_revenue_d2(opex, cor, revenue):
    return _safe_div(opex - cor, revenue.abs()).diff().diff()

def f39_hlem_081_opex_spike_intensity_8q_d2(opex):
    return _safe_div(opex - opex.rolling(8, min_periods=3).mean(), opex.rolling(8, min_periods=3).std().replace(0, np.nan)).diff().diff()

def f39_hlem_082_opinc_q_minus_4q_avg_d2(opinc):
    return (opinc - opinc.rolling(4, min_periods=2).mean()).diff().diff()

def f39_hlem_083_opinc_q_minus_4q_avg_share_of_revenue_d2(opinc, revenue):
    return _safe_div(opinc - opinc.rolling(4, min_periods=2).mean(), revenue.abs()).diff().diff()

def f39_hlem_084_opex_minus_avg_4q_share_d2(opex):
    m = opex.rolling(4, min_periods=2).mean()
    return _safe_div(opex - m, m.abs()).diff().diff()

def f39_hlem_085_nonrecurring_charge_proxy_opinc_decline_d2(opinc):
    return (-opinc.diff().clip(upper=0).abs()).diff().diff()

def f39_hlem_086_opex_yoy_minus_revenue_yoy_d2(opex, revenue):
    return (_yoy_pct(_ttm(opex)) - _yoy_pct(_ttm(revenue))).diff().diff()

def f39_hlem_087_sgna_zscore_12q_d2(sgna):
    return _rolling_zscore(sgna, 12, 4).diff().diff()

def f39_hlem_088_opex_growth_minus_assets_growth_d2(opex, assets):
    return (_yoy_pct(_ttm(opex)) - _yoy_pct(assets)).diff().diff()

def f39_hlem_089_opex_to_assets_qoq_jump_d2(opex, assets):
    return _safe_div(_ttm(opex), assets).diff().clip(lower=0).diff().diff()

def f39_hlem_090_consecutive_opex_increase_streak_8q_d2(opex):
    incr = (opex.diff() > 0).astype(int)
    return incr.rolling(8, min_periods=3).apply(lambda w: int(w[::-1].cumprod().sum()), raw=True).diff().diff()

def f39_hlem_091_taxexp_qoq_pct_jump_d2(taxexp):
    return _qoq_pct(taxexp).clip(lower=0).diff().diff()

def f39_hlem_092_taxexp_yoy_pct_d2(taxexp):
    return _yoy_pct(_ttm(taxexp)).diff().diff()

def f39_hlem_093_effective_tax_rate_yoy_change_d2(taxexp, ebit):
    etr = _safe_div(_ttm(taxexp), _ttm(ebit))
    return _yoy(etr).diff().diff()

def f39_hlem_094_effective_tax_rate_zscore_12q_d2(taxexp, ebit):
    etr = _safe_div(_ttm(taxexp), _ttm(ebit))
    return _rolling_zscore(etr, 12, 4).diff().diff()

def f39_hlem_095_taxexp_minus_ebit_change_share_d2(taxexp, ebit, revenue):
    return _safe_div(_ttm(taxexp).diff() - _ttm(ebit).diff(), _ttm(revenue).abs()).diff().diff()

def f39_hlem_096_tax_pretax_gap_yoy_d2(taxexp, ebit):
    return _yoy(_safe_div(_ttm(taxexp), _ttm(ebit).abs())).diff().diff()

def f39_hlem_097_nonop_income_share_qoq_jump_d2(netinc, opinc, taxexp):
    eff = _safe_div(_ttm(taxexp), _ttm(opinc).abs()).clip(lower=0, upper=0.6)
    op_after = _ttm(opinc) * (1.0 - eff)
    nonop = _safe_div(_ttm(netinc) - op_after, _ttm(netinc).abs())
    return nonop.diff().diff().diff()

def f39_hlem_098_negative_belowline_q_count_8q_d2(netinc, opinc):
    gap = netinc - opinc < 0
    return gap.astype(float).rolling(8, min_periods=3).sum().diff().diff()

def f39_hlem_099_netinc_minus_ebit_share_zscore_8q_d2(netinc, ebit, revenue):
    g = _safe_div(_ttm(netinc) - _ttm(ebit), _ttm(revenue).abs())
    return _rolling_zscore(g, 8, 3).diff().diff()

def f39_hlem_100_ebit_minus_netinc_to_revenue_jump_d2(ebit, netinc, revenue):
    g = _safe_div(_ttm(ebit) - _ttm(netinc), _ttm(revenue).abs())
    return g.diff().clip(lower=0).diff().diff()

def f39_hlem_101_tax_burden_qoq_anomaly_d2(taxexp, revenue):
    burden = _safe_div(taxexp, revenue.abs())
    return _rolling_zscore(burden, 8, 3).diff().diff()

def f39_hlem_102_deferred_tax_proxy_via_taxexp_vs_ncfo_change_d2(taxexp, ncfo):
    return (_yoy(taxexp) - _yoy(ncfo)).diff().diff()

def f39_hlem_103_nontax_charges_proxy_d2(netinc, ebit, intexp, taxexp):
    eff = _safe_div(_ttm(taxexp), _ttm(ebit).abs()).clip(lower=0, upper=0.6)
    pretax = _ttm(ebit) - _ttm(intexp)
    expected_ni = pretax * (1.0 - eff)
    return (_ttm(netinc) - expected_ni).diff().diff()

def f39_hlem_104_unusual_item_proxy_via_netinc_swing_d2(netinc, opinc):
    return (netinc.diff() - opinc.diff() * 0.7).diff().diff()

def f39_hlem_105_one_off_loss_intensity_via_netinc_swing_8q_d2(netinc):
    return (-_rolling_zscore(netinc.diff().clip(upper=0).abs(), 8, 3)).diff().diff()

def f39_hlem_106_receivables_writedown_intensity_d2(receivables):
    return _safe_div(receivables.diff().clip(upper=0).abs(), receivables.shift(1).abs()).diff().diff()

def f39_hlem_107_receivables_yoy_decline_when_revenue_up_d2(receivables, revenue):
    flag = (_yoy(receivables) < 0) & (_yoy(_ttm(revenue)) > 0)
    return (flag.astype(float) * _safe_div(_yoy(receivables).abs(), receivables.shift(4).abs())).diff().diff()

def f39_hlem_108_receivables_minus_revenue_share_yoy_d2(receivables, revenue):
    return _yoy(_safe_div(receivables, _ttm(revenue))).diff().diff()

def f39_hlem_109_receivables_qoq_drop_zscore_8q_d2(receivables):
    return (-_rolling_zscore(receivables.diff().clip(upper=0).abs(), 8, 3)).diff().diff()

def f39_hlem_110_allowance_for_doubt_emergence_proxy_d2(receivables, revenue):
    ratio = _safe_div(receivables, revenue.abs())
    return (-ratio.diff().clip(upper=0)).diff().diff()

def f39_hlem_111_accrual_reversal_signal_d2(netinc, ncfo):
    return (-(netinc - ncfo).diff()).diff().diff()

def f39_hlem_112_accrual_swing_zscore_8q_d2(netinc, ncfo):
    a = netinc - ncfo
    return _rolling_zscore(a.diff(), 8, 3).diff().diff()

def f39_hlem_113_receivables_to_revenue_qoq_drop_d2(receivables, revenue):
    return _safe_div(receivables, revenue.abs()).diff().clip(upper=0).diff().diff()

def f39_hlem_114_negative_receivables_change_q_count_8q_d2(receivables):
    return (receivables.diff() < 0).rolling(8, min_periods=3).sum().diff().diff()

def f39_hlem_115_asset_quality_index_decline_proxy_d2(receivables, assets):
    return (-_yoy(_safe_div(receivables, assets))).diff().diff()

def f39_hlem_116_workingcapital_writedown_intensity_d2(workingcapital):
    return _safe_div(workingcapital.diff().clip(upper=0).abs(), workingcapital.shift(1).abs()).diff().diff()

def f39_hlem_117_wc_writedown_share_of_assets_d2(workingcapital, assets):
    return _safe_div(workingcapital.diff().clip(upper=0).abs(), assets).diff().diff()

def f39_hlem_118_inventory_minus_receivables_change_drag_d2(inventory, receivables, revenue):
    return _safe_div((inventory.diff() - receivables.diff()).clip(lower=0), _ttm(revenue).abs()).diff().diff()

def f39_hlem_119_asset_purification_proxy_d2(assets, intangibles):
    return (_yoy_pct(assets - intangibles) - _yoy_pct(assets)).diff().diff()

def f39_hlem_120_quality_purification_signal_d2(assets, intangibles, equity):
    tangible_ratio = _safe_div(assets - intangibles, equity.abs())
    return tangible_ratio.diff().diff().diff()

def f39_hlem_121_netinc_minus_ncfo_qoq_jump_d2(netinc, ncfo):
    return (netinc - ncfo).diff().clip(lower=0).diff().diff()

def f39_hlem_122_ebitda_minus_ncfo_to_assets_zscore_8q_d2(ebitda, ncfo, assets):
    g = _safe_div(_ttm(ebitda) - _ttm(ncfo), assets)
    return _rolling_zscore(g, 8, 3).diff().diff()

def f39_hlem_123_ncfo_minus_netinc_yoy_change_d2(ncfo, netinc):
    return _yoy(_ttm(ncfo) - _ttm(netinc)).diff().diff()

def f39_hlem_124_fcf_minus_netinc_qoq_change_d2(fcf, netinc):
    return (fcf - netinc).diff().diff().diff()

def f39_hlem_125_cash_flow_quality_decline_zscore_8q_d2(ncfo, netinc):
    cq = _safe_div(_ttm(ncfo), _ttm(netinc).abs())
    return (-_rolling_zscore(cq.diff().clip(upper=0).abs(), 8, 3)).diff().diff()

def f39_hlem_126_ncfo_drop_with_netinc_stable_flag_d2(ncfo, netinc):
    ncfo_drop = _yoy(_ttm(ncfo)) < 0
    netinc_stable = _yoy_pct(_ttm(netinc)).abs() < 0.05
    return (ncfo_drop & netinc_stable).astype(float).diff().diff()

def f39_hlem_127_netinc_up_with_ncfo_decline_flag_d2(ncfo, netinc):
    return ((_yoy(_ttm(netinc)) > 0) & (_yoy(_ttm(ncfo)) < 0)).astype(float).diff().diff()

def f39_hlem_128_ebit_minus_ncfo_share_of_revenue_jump_d2(ebit, ncfo, revenue):
    g = _safe_div(_ttm(ebit) - _ttm(ncfo), _ttm(revenue).abs())
    return g.diff().clip(lower=0).diff().diff()

def f39_hlem_129_cash_to_book_earnings_yoy_change_d2(ncfo, netinc):
    return _yoy(_safe_div(_ttm(ncfo), _ttm(netinc).abs())).diff().diff()

def f39_hlem_130_ocf_failure_q_count_recent_8q_d2(ncfo):
    return (ncfo < 0).rolling(8, min_periods=3).sum().diff().diff()

def f39_hlem_131_divergence_zscore_netinc_vs_ncfo_12q_d2(netinc, ncfo):
    div = _ttm(netinc) - _ttm(ncfo)
    return _rolling_zscore(div, 12, 4).diff().diff()

def f39_hlem_132_earnings_minus_cash_gap_zscore_12q_d2(netinc, ncfo, assets):
    g = _safe_div(_ttm(netinc) - _ttm(ncfo), assets)
    return _rolling_zscore(g, 12, 4).diff().diff()

def f39_hlem_133_accrual_emergence_signal_zscore_12q_d2(netinc, ncfo, assets):
    a = _safe_div(_ttm(netinc) - _ttm(ncfo), assets)
    return _rolling_zscore(a.diff(), 12, 4).diff().diff()

def f39_hlem_134_earnings_quality_collapse_signal_q_d2(ncfo, netinc):
    cq = _safe_div(ncfo, netinc.abs())
    return (cq - cq.rolling(4, min_periods=2).mean().shift(1)).diff().diff()

def f39_hlem_135_cash_quality_divergence_aggregate_d2(netinc, ncfo, fcf, assets):
    g1 = _safe_div(_ttm(netinc) - _ttm(ncfo), assets)
    g2 = _safe_div(_ttm(netinc) - _ttm(fcf), assets)
    return ((_rolling_zscore(g1, 12, 4) + _rolling_zscore(g2, 12, 4)) / 2.0).diff().diff()

def f39_hlem_136_hidden_loss_composite_zscore_d2(intangibles, ppnenet, retearn, netinc, ncfo, assets):
    z_int = -_rolling_zscore(intangibles.diff().clip(upper=0).abs(), 12, 4)
    z_ppe = -_rolling_zscore(ppnenet.diff().clip(upper=0).abs(), 12, 4)
    z_re = -_rolling_zscore(retearn.diff().clip(upper=0).abs(), 12, 4)
    z_acc = _rolling_zscore(_safe_div(_ttm(netinc) - _ttm(ncfo), assets), 12, 4)
    return ((z_int + z_ppe + z_re + z_acc) / 4.0).diff().diff()

def f39_hlem_137_asset_writedown_intensity_composite_d2(intangibles, ppnenet, assets):
    wd = intangibles.diff().clip(upper=0).abs() + ppnenet.diff().clip(upper=0).abs()
    return _safe_div(wd, assets).diff().diff()

def f39_hlem_138_one_off_charge_emergence_score_d2(opinc, netinc, opex):
    a = -opinc.diff().clip(upper=0).abs()
    b = -netinc.diff().clip(upper=0).abs()
    c = opex.diff().clip(lower=0)
    return (_rolling_zscore(a, 8, 3) + _rolling_zscore(b, 8, 3) + _rolling_zscore(c, 8, 3)).diff().diff()

def f39_hlem_139_earnings_quality_collapse_composite_d2(netinc, ncfo, fcf, assets):
    a = _safe_div(_ttm(netinc) - _ttm(ncfo), assets)
    b = _safe_div(_ttm(netinc) - _ttm(fcf), assets)
    return (_rolling_zscore(a, 12, 4) + _rolling_zscore(b, 12, 4)).diff().diff()

def f39_hlem_140_liability_growth_revenue_stall_composite_d2(liabilities, revenue, assets):
    liab_g = _yoy_pct(liabilities)
    rev_g = _yoy_pct(_ttm(revenue))
    stall = (rev_g < 0.02).astype(float)
    return (liab_g * stall).diff().diff()

def f39_hlem_141_retearn_compression_score_8q_d2(retearn, equity):
    ratio = _safe_div(retearn, equity)
    return (-ratio.diff().rolling(8, min_periods=3).sum()).diff().diff()

def f39_hlem_142_shock_quarter_count_8q_d2(netinc, opinc, ncfo, revenue):
    rev_norm = _ttm(revenue).abs().replace(0, np.nan)
    ni_shock = (netinc / rev_norm).diff().abs() > 0.05
    op_shock = (opinc / rev_norm).diff().abs() > 0.05
    cf_shock = (ncfo / rev_norm).diff().abs() > 0.05
    return (ni_shock.astype(float) + op_shock.astype(float) + cf_shock.astype(float)).rolling(8, min_periods=3).sum().diff().diff()

def f39_hlem_143_hidden_loss_dispersion_zscore_8q_d2(netinc, ncfo, opinc):
    df = pd.concat([netinc.diff(), ncfo.diff(), opinc.diff()], axis=1)
    return _rolling_zscore(df.std(axis=1), 8, 3).diff().diff()

def f39_hlem_144_impairment_signal_aggregate_d2(intangibles, ppnenet, depamor, assets):
    z1 = -_rolling_zscore(intangibles.diff().clip(upper=0).abs(), 8, 3)
    z2 = -_rolling_zscore(ppnenet.diff().clip(upper=0).abs(), 8, 3)
    z3 = _rolling_zscore(_ttm(depamor) / assets.replace(0, np.nan), 8, 3)
    return ((z1 + z2 + z3) / 3.0).diff().diff()

def f39_hlem_145_accrual_reversal_aggregate_zscore_d2(netinc, ncfo, receivables, inventory, assets):
    a1 = _safe_div(_ttm(netinc) - _ttm(ncfo), assets)
    a2 = _safe_div(receivables.diff() + inventory.diff(), assets)
    return (_rolling_zscore(a1.diff(), 8, 3) + _rolling_zscore(a2, 8, 3)).diff().diff()

def f39_hlem_146_quality_decline_persistence_score_12q_d2(ncfo, netinc):
    cq = _safe_div(_ttm(ncfo), _ttm(netinc).abs())
    drops = (cq.diff() < 0).astype(int)
    return drops.rolling(12, min_periods=4).apply(lambda w: int(w[::-1].cumprod().sum()), raw=True).diff().diff()

def f39_hlem_147_equity_destruction_signal_zscore_8q_d2(equity, assets):
    ratio = _safe_div(equity, assets)
    return (-_rolling_zscore(ratio.diff().clip(upper=0).abs(), 8, 3)).diff().diff()

def f39_hlem_148_negative_eps_emergence_signal_8q_d2(eps):
    flag = (eps < 0).astype(float)
    first_neg = flag * (1.0 - flag.shift(1).fillna(0))
    return first_neg.rolling(8, min_periods=3).sum().diff().diff()

def f39_hlem_149_surprise_loss_q_proxy_d2(netinc, revenue):
    margin = _safe_div(netinc, revenue.abs())
    z = _rolling_zscore(margin, 12, 4)
    return z.clip(upper=0).abs().diff().diff()

def f39_hlem_150_hidden_loss_aggregate_composite_d2(intangibles, ppnenet, retearn, netinc, ncfo, equity, assets):
    z_int = -_rolling_zscore(intangibles.diff().clip(upper=0).abs(), 12, 4)
    z_ppe = -_rolling_zscore(ppnenet.diff().clip(upper=0).abs(), 12, 4)
    z_re = -_rolling_zscore(retearn.diff().clip(upper=0).abs(), 12, 4)
    z_eq = -_rolling_zscore(equity.diff().clip(upper=0).abs(), 12, 4)
    z_acc = _rolling_zscore(_safe_div(_ttm(netinc) - _ttm(ncfo), assets), 12, 4)
    return ((z_int + z_ppe + z_re + z_eq + z_acc) / 5.0).diff().diff()
HIDDEN_LOSS_EMERGENCE_D2_REGISTRY_076_150 = {'f39_hlem_076_sgna_qoq_jump_zscore_8q_d2': {'inputs': ['sgna'], 'func': f39_hlem_076_sgna_qoq_jump_zscore_8q_d2}, 'f39_hlem_077_sgna_yoy_minus_revenue_yoy_d2': {'inputs': ['sgna', 'revenue'], 'func': f39_hlem_077_sgna_yoy_minus_revenue_yoy_d2}, 'f39_hlem_078_sgna_share_of_revenue_qoq_jump_d2': {'inputs': ['sgna', 'revenue'], 'func': f39_hlem_078_sgna_share_of_revenue_qoq_jump_d2}, 'f39_hlem_079_opex_qoq_jump_zscore_8q_d2': {'inputs': ['opex'], 'func': f39_hlem_079_opex_qoq_jump_zscore_8q_d2}, 'f39_hlem_080_opex_minus_cor_share_of_revenue_d2': {'inputs': ['opex', 'cor', 'revenue'], 'func': f39_hlem_080_opex_minus_cor_share_of_revenue_d2}, 'f39_hlem_081_opex_spike_intensity_8q_d2': {'inputs': ['opex'], 'func': f39_hlem_081_opex_spike_intensity_8q_d2}, 'f39_hlem_082_opinc_q_minus_4q_avg_d2': {'inputs': ['opinc'], 'func': f39_hlem_082_opinc_q_minus_4q_avg_d2}, 'f39_hlem_083_opinc_q_minus_4q_avg_share_of_revenue_d2': {'inputs': ['opinc', 'revenue'], 'func': f39_hlem_083_opinc_q_minus_4q_avg_share_of_revenue_d2}, 'f39_hlem_084_opex_minus_avg_4q_share_d2': {'inputs': ['opex'], 'func': f39_hlem_084_opex_minus_avg_4q_share_d2}, 'f39_hlem_085_nonrecurring_charge_proxy_opinc_decline_d2': {'inputs': ['opinc'], 'func': f39_hlem_085_nonrecurring_charge_proxy_opinc_decline_d2}, 'f39_hlem_086_opex_yoy_minus_revenue_yoy_d2': {'inputs': ['opex', 'revenue'], 'func': f39_hlem_086_opex_yoy_minus_revenue_yoy_d2}, 'f39_hlem_087_sgna_zscore_12q_d2': {'inputs': ['sgna'], 'func': f39_hlem_087_sgna_zscore_12q_d2}, 'f39_hlem_088_opex_growth_minus_assets_growth_d2': {'inputs': ['opex', 'assets'], 'func': f39_hlem_088_opex_growth_minus_assets_growth_d2}, 'f39_hlem_089_opex_to_assets_qoq_jump_d2': {'inputs': ['opex', 'assets'], 'func': f39_hlem_089_opex_to_assets_qoq_jump_d2}, 'f39_hlem_090_consecutive_opex_increase_streak_8q_d2': {'inputs': ['opex'], 'func': f39_hlem_090_consecutive_opex_increase_streak_8q_d2}, 'f39_hlem_091_taxexp_qoq_pct_jump_d2': {'inputs': ['taxexp'], 'func': f39_hlem_091_taxexp_qoq_pct_jump_d2}, 'f39_hlem_092_taxexp_yoy_pct_d2': {'inputs': ['taxexp'], 'func': f39_hlem_092_taxexp_yoy_pct_d2}, 'f39_hlem_093_effective_tax_rate_yoy_change_d2': {'inputs': ['taxexp', 'ebit'], 'func': f39_hlem_093_effective_tax_rate_yoy_change_d2}, 'f39_hlem_094_effective_tax_rate_zscore_12q_d2': {'inputs': ['taxexp', 'ebit'], 'func': f39_hlem_094_effective_tax_rate_zscore_12q_d2}, 'f39_hlem_095_taxexp_minus_ebit_change_share_d2': {'inputs': ['taxexp', 'ebit', 'revenue'], 'func': f39_hlem_095_taxexp_minus_ebit_change_share_d2}, 'f39_hlem_096_tax_pretax_gap_yoy_d2': {'inputs': ['taxexp', 'ebit'], 'func': f39_hlem_096_tax_pretax_gap_yoy_d2}, 'f39_hlem_097_nonop_income_share_qoq_jump_d2': {'inputs': ['netinc', 'opinc', 'taxexp'], 'func': f39_hlem_097_nonop_income_share_qoq_jump_d2}, 'f39_hlem_098_negative_belowline_q_count_8q_d2': {'inputs': ['netinc', 'opinc'], 'func': f39_hlem_098_negative_belowline_q_count_8q_d2}, 'f39_hlem_099_netinc_minus_ebit_share_zscore_8q_d2': {'inputs': ['netinc', 'ebit', 'revenue'], 'func': f39_hlem_099_netinc_minus_ebit_share_zscore_8q_d2}, 'f39_hlem_100_ebit_minus_netinc_to_revenue_jump_d2': {'inputs': ['ebit', 'netinc', 'revenue'], 'func': f39_hlem_100_ebit_minus_netinc_to_revenue_jump_d2}, 'f39_hlem_101_tax_burden_qoq_anomaly_d2': {'inputs': ['taxexp', 'revenue'], 'func': f39_hlem_101_tax_burden_qoq_anomaly_d2}, 'f39_hlem_102_deferred_tax_proxy_via_taxexp_vs_ncfo_change_d2': {'inputs': ['taxexp', 'ncfo'], 'func': f39_hlem_102_deferred_tax_proxy_via_taxexp_vs_ncfo_change_d2}, 'f39_hlem_103_nontax_charges_proxy_d2': {'inputs': ['netinc', 'ebit', 'intexp', 'taxexp'], 'func': f39_hlem_103_nontax_charges_proxy_d2}, 'f39_hlem_104_unusual_item_proxy_via_netinc_swing_d2': {'inputs': ['netinc', 'opinc'], 'func': f39_hlem_104_unusual_item_proxy_via_netinc_swing_d2}, 'f39_hlem_105_one_off_loss_intensity_via_netinc_swing_8q_d2': {'inputs': ['netinc'], 'func': f39_hlem_105_one_off_loss_intensity_via_netinc_swing_8q_d2}, 'f39_hlem_106_receivables_writedown_intensity_d2': {'inputs': ['receivables'], 'func': f39_hlem_106_receivables_writedown_intensity_d2}, 'f39_hlem_107_receivables_yoy_decline_when_revenue_up_d2': {'inputs': ['receivables', 'revenue'], 'func': f39_hlem_107_receivables_yoy_decline_when_revenue_up_d2}, 'f39_hlem_108_receivables_minus_revenue_share_yoy_d2': {'inputs': ['receivables', 'revenue'], 'func': f39_hlem_108_receivables_minus_revenue_share_yoy_d2}, 'f39_hlem_109_receivables_qoq_drop_zscore_8q_d2': {'inputs': ['receivables'], 'func': f39_hlem_109_receivables_qoq_drop_zscore_8q_d2}, 'f39_hlem_110_allowance_for_doubt_emergence_proxy_d2': {'inputs': ['receivables', 'revenue'], 'func': f39_hlem_110_allowance_for_doubt_emergence_proxy_d2}, 'f39_hlem_111_accrual_reversal_signal_d2': {'inputs': ['netinc', 'ncfo'], 'func': f39_hlem_111_accrual_reversal_signal_d2}, 'f39_hlem_112_accrual_swing_zscore_8q_d2': {'inputs': ['netinc', 'ncfo'], 'func': f39_hlem_112_accrual_swing_zscore_8q_d2}, 'f39_hlem_113_receivables_to_revenue_qoq_drop_d2': {'inputs': ['receivables', 'revenue'], 'func': f39_hlem_113_receivables_to_revenue_qoq_drop_d2}, 'f39_hlem_114_negative_receivables_change_q_count_8q_d2': {'inputs': ['receivables'], 'func': f39_hlem_114_negative_receivables_change_q_count_8q_d2}, 'f39_hlem_115_asset_quality_index_decline_proxy_d2': {'inputs': ['receivables', 'assets'], 'func': f39_hlem_115_asset_quality_index_decline_proxy_d2}, 'f39_hlem_116_workingcapital_writedown_intensity_d2': {'inputs': ['workingcapital'], 'func': f39_hlem_116_workingcapital_writedown_intensity_d2}, 'f39_hlem_117_wc_writedown_share_of_assets_d2': {'inputs': ['workingcapital', 'assets'], 'func': f39_hlem_117_wc_writedown_share_of_assets_d2}, 'f39_hlem_118_inventory_minus_receivables_change_drag_d2': {'inputs': ['inventory', 'receivables', 'revenue'], 'func': f39_hlem_118_inventory_minus_receivables_change_drag_d2}, 'f39_hlem_119_asset_purification_proxy_d2': {'inputs': ['assets', 'intangibles'], 'func': f39_hlem_119_asset_purification_proxy_d2}, 'f39_hlem_120_quality_purification_signal_d2': {'inputs': ['assets', 'intangibles', 'equity'], 'func': f39_hlem_120_quality_purification_signal_d2}, 'f39_hlem_121_netinc_minus_ncfo_qoq_jump_d2': {'inputs': ['netinc', 'ncfo'], 'func': f39_hlem_121_netinc_minus_ncfo_qoq_jump_d2}, 'f39_hlem_122_ebitda_minus_ncfo_to_assets_zscore_8q_d2': {'inputs': ['ebitda', 'ncfo', 'assets'], 'func': f39_hlem_122_ebitda_minus_ncfo_to_assets_zscore_8q_d2}, 'f39_hlem_123_ncfo_minus_netinc_yoy_change_d2': {'inputs': ['ncfo', 'netinc'], 'func': f39_hlem_123_ncfo_minus_netinc_yoy_change_d2}, 'f39_hlem_124_fcf_minus_netinc_qoq_change_d2': {'inputs': ['fcf', 'netinc'], 'func': f39_hlem_124_fcf_minus_netinc_qoq_change_d2}, 'f39_hlem_125_cash_flow_quality_decline_zscore_8q_d2': {'inputs': ['ncfo', 'netinc'], 'func': f39_hlem_125_cash_flow_quality_decline_zscore_8q_d2}, 'f39_hlem_126_ncfo_drop_with_netinc_stable_flag_d2': {'inputs': ['ncfo', 'netinc'], 'func': f39_hlem_126_ncfo_drop_with_netinc_stable_flag_d2}, 'f39_hlem_127_netinc_up_with_ncfo_decline_flag_d2': {'inputs': ['ncfo', 'netinc'], 'func': f39_hlem_127_netinc_up_with_ncfo_decline_flag_d2}, 'f39_hlem_128_ebit_minus_ncfo_share_of_revenue_jump_d2': {'inputs': ['ebit', 'ncfo', 'revenue'], 'func': f39_hlem_128_ebit_minus_ncfo_share_of_revenue_jump_d2}, 'f39_hlem_129_cash_to_book_earnings_yoy_change_d2': {'inputs': ['ncfo', 'netinc'], 'func': f39_hlem_129_cash_to_book_earnings_yoy_change_d2}, 'f39_hlem_130_ocf_failure_q_count_recent_8q_d2': {'inputs': ['ncfo'], 'func': f39_hlem_130_ocf_failure_q_count_recent_8q_d2}, 'f39_hlem_131_divergence_zscore_netinc_vs_ncfo_12q_d2': {'inputs': ['netinc', 'ncfo'], 'func': f39_hlem_131_divergence_zscore_netinc_vs_ncfo_12q_d2}, 'f39_hlem_132_earnings_minus_cash_gap_zscore_12q_d2': {'inputs': ['netinc', 'ncfo', 'assets'], 'func': f39_hlem_132_earnings_minus_cash_gap_zscore_12q_d2}, 'f39_hlem_133_accrual_emergence_signal_zscore_12q_d2': {'inputs': ['netinc', 'ncfo', 'assets'], 'func': f39_hlem_133_accrual_emergence_signal_zscore_12q_d2}, 'f39_hlem_134_earnings_quality_collapse_signal_q_d2': {'inputs': ['ncfo', 'netinc'], 'func': f39_hlem_134_earnings_quality_collapse_signal_q_d2}, 'f39_hlem_135_cash_quality_divergence_aggregate_d2': {'inputs': ['netinc', 'ncfo', 'fcf', 'assets'], 'func': f39_hlem_135_cash_quality_divergence_aggregate_d2}, 'f39_hlem_136_hidden_loss_composite_zscore_d2': {'inputs': ['intangibles', 'ppnenet', 'retearn', 'netinc', 'ncfo', 'assets'], 'func': f39_hlem_136_hidden_loss_composite_zscore_d2}, 'f39_hlem_137_asset_writedown_intensity_composite_d2': {'inputs': ['intangibles', 'ppnenet', 'assets'], 'func': f39_hlem_137_asset_writedown_intensity_composite_d2}, 'f39_hlem_138_one_off_charge_emergence_score_d2': {'inputs': ['opinc', 'netinc', 'opex'], 'func': f39_hlem_138_one_off_charge_emergence_score_d2}, 'f39_hlem_139_earnings_quality_collapse_composite_d2': {'inputs': ['netinc', 'ncfo', 'fcf', 'assets'], 'func': f39_hlem_139_earnings_quality_collapse_composite_d2}, 'f39_hlem_140_liability_growth_revenue_stall_composite_d2': {'inputs': ['liabilities', 'revenue', 'assets'], 'func': f39_hlem_140_liability_growth_revenue_stall_composite_d2}, 'f39_hlem_141_retearn_compression_score_8q_d2': {'inputs': ['retearn', 'equity'], 'func': f39_hlem_141_retearn_compression_score_8q_d2}, 'f39_hlem_142_shock_quarter_count_8q_d2': {'inputs': ['netinc', 'opinc', 'ncfo', 'revenue'], 'func': f39_hlem_142_shock_quarter_count_8q_d2}, 'f39_hlem_143_hidden_loss_dispersion_zscore_8q_d2': {'inputs': ['netinc', 'ncfo', 'opinc'], 'func': f39_hlem_143_hidden_loss_dispersion_zscore_8q_d2}, 'f39_hlem_144_impairment_signal_aggregate_d2': {'inputs': ['intangibles', 'ppnenet', 'depamor', 'assets'], 'func': f39_hlem_144_impairment_signal_aggregate_d2}, 'f39_hlem_145_accrual_reversal_aggregate_zscore_d2': {'inputs': ['netinc', 'ncfo', 'receivables', 'inventory', 'assets'], 'func': f39_hlem_145_accrual_reversal_aggregate_zscore_d2}, 'f39_hlem_146_quality_decline_persistence_score_12q_d2': {'inputs': ['ncfo', 'netinc'], 'func': f39_hlem_146_quality_decline_persistence_score_12q_d2}, 'f39_hlem_147_equity_destruction_signal_zscore_8q_d2': {'inputs': ['equity', 'assets'], 'func': f39_hlem_147_equity_destruction_signal_zscore_8q_d2}, 'f39_hlem_148_negative_eps_emergence_signal_8q_d2': {'inputs': ['eps'], 'func': f39_hlem_148_negative_eps_emergence_signal_8q_d2}, 'f39_hlem_149_surprise_loss_q_proxy_d2': {'inputs': ['netinc', 'revenue'], 'func': f39_hlem_149_surprise_loss_q_proxy_d2}, 'f39_hlem_150_hidden_loss_aggregate_composite_d2': {'inputs': ['intangibles', 'ppnenet', 'retearn', 'netinc', 'ncfo', 'equity', 'assets'], 'func': f39_hlem_150_hidden_loss_aggregate_composite_d2}}