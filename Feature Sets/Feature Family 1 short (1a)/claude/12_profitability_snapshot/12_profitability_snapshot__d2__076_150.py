"""profitability_snapshot d2 features 076-150 — order-2 difference of corresponding base features.

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

def _sign_change(s):
    sgn = np.sign(s.fillna(0.0))
    return (sgn != sgn.shift(1)).fillna(False).astype(float)

def f12_psnp_076_signed_log_eps_ttm_d2(eps):
    return _signed_log_abs(_ttm(eps)).diff().diff()

def f12_psnp_077_signed_log_eps_dil_ttm_d2(epsdil):
    return _signed_log_abs(_ttm(epsdil)).diff().diff()

def f12_psnp_078_eps_growth_yoy_d2(eps):
    return _yoy_pct(_ttm(eps)).diff().diff()

def f12_psnp_079_eps_growth_qoq_d2(eps):
    return _yoy_pct(eps).diff().diff()

def f12_psnp_080_payout_ratio_dps_to_eps_d2(dps, eps):
    return _safe_div(dps, eps.abs()).diff().diff()

def f12_psnp_081_dps_growth_yoy_d2(dps):
    return _yoy_pct(dps).diff().diff()

def f12_psnp_082_ebitda_per_share_ttm_d2(ebitda, shareswadil):
    return _safe_div(_ttm(ebitda), shareswadil).diff().diff()

def f12_psnp_083_fcf_per_share_ttm_d2(fcf, shareswadil):
    return _safe_div(_ttm(fcf), shareswadil).diff().diff()

def f12_psnp_084_ocf_per_share_ttm_d2(ncfo, shareswadil):
    return _safe_div(_ttm(ncfo), shareswadil).diff().diff()

def f12_psnp_085_book_value_per_share_d2(equity, shareswadil):
    return _safe_div(equity, shareswadil).diff().diff()

def f12_psnp_086_tangible_book_per_share_d2(equity, intangibles, shareswadil):
    return _safe_div(equity - intangibles, shareswadil).diff().diff()

def f12_psnp_087_eps_dil_minus_basic_drag_d2(eps, epsdil):
    return _safe_div(eps - epsdil, eps.abs()).diff().diff()

def f12_psnp_088_eps_zscore_8q_d2(eps):
    return _rolling_zscore(_ttm(eps), 8, 3).diff().diff()

def f12_psnp_089_ebitda_per_share_zscore_8q_d2(ebitda, shareswadil):
    return _rolling_zscore(_safe_div(_ttm(ebitda), shareswadil), 8, 3).diff().diff()

def f12_psnp_090_fcf_per_share_growth_yoy_d2(fcf, shareswadil):
    return _yoy_pct(_safe_div(_ttm(fcf), shareswadil)).diff().diff()

def f12_psnp_091_dps_yield_to_bvps_d2(dps, equity, shareswadil):
    bvps = _safe_div(equity, shareswadil)
    return _safe_div(dps, bvps).diff().diff()

def f12_psnp_092_payout_to_fcf_ttm_d2(dps, fcf, shareswadil):
    fcfps = _safe_div(_ttm(fcf), shareswadil)
    return _safe_div(dps, fcfps.abs()).diff().diff()

def f12_psnp_093_eps_yoy_minus_revenue_yoy_d2(eps, revenue):
    return (_yoy_pct(_ttm(eps)) - _yoy_pct(_ttm(revenue))).diff().diff()

def f12_psnp_094_ebitda_per_share_yoy_minus_revenue_per_share_yoy_d2(ebitda, revenue, shareswadil):
    return (_yoy_pct(_safe_div(_ttm(ebitda), shareswadil)) - _yoy_pct(_safe_div(_ttm(revenue), shareswadil))).diff().diff()

def f12_psnp_095_bvps_growth_yoy_d2(equity, shareswadil):
    return _yoy_pct(_safe_div(equity, shareswadil)).diff().diff()

def f12_psnp_096_gross_profit_to_assets_d2(gp, assets):
    return _safe_div(_ttm(gp), assets).diff().diff()

def f12_psnp_097_operating_income_to_assets_d2(opinc, assets):
    return _safe_div(_ttm(opinc), assets).diff().diff()

def f12_psnp_098_ebitda_to_assets_d2(ebitda, assets):
    return _safe_div(_ttm(ebitda), assets).diff().diff()

def f12_psnp_099_netinc_share_of_opinc_d2(netinc, opinc):
    return _safe_div(_ttm(netinc), _ttm(opinc).abs()).diff().diff()

def f12_psnp_100_ebit_to_total_capital_d2(ebit, equity, debt):
    return _safe_div(_ttm(ebit), equity + debt).diff().diff()

def f12_psnp_101_opinc_to_invested_capital_d2(opinc, equity, debt):
    return _safe_div(_ttm(opinc), equity + debt).diff().diff()

def f12_psnp_102_fcf_to_total_capital_d2(fcf, equity, debt):
    return _safe_div(_ttm(fcf), equity + debt).diff().diff()

def f12_psnp_103_ebitda_to_total_capital_d2(ebitda, equity, debt):
    return _safe_div(_ttm(ebitda), equity + debt).diff().diff()

def f12_psnp_104_operating_leverage_yoy_d2(ebit, revenue):
    return _safe_div(_yoy_pct(_ttm(ebit)), _yoy_pct(_ttm(revenue)).abs()).diff().diff()

def f12_psnp_105_financial_leverage_yoy_d2(netinc, ebit):
    return _safe_div(_yoy_pct(_ttm(netinc)), _yoy_pct(_ttm(ebit)).abs()).diff().diff()

def f12_psnp_106_total_leverage_yoy_d2(netinc, revenue):
    return _safe_div(_yoy_pct(_ttm(netinc)), _yoy_pct(_ttm(revenue)).abs()).diff().diff()

def f12_psnp_107_gross_to_operating_margin_gap_d2(gp, opinc, revenue):
    return _safe_div(_ttm(gp) - _ttm(opinc), _ttm(revenue).abs()).diff().diff()

def f12_psnp_108_ebitda_to_ebit_ratio_d2(ebitda, ebit):
    return _safe_div(_ttm(ebitda), _ttm(ebit).abs()).diff().diff()

def f12_psnp_109_opinc_to_ebitda_d2(opinc, ebitda):
    return _safe_div(_ttm(opinc), _ttm(ebitda).abs()).diff().diff()

def f12_psnp_110_netinc_share_of_ebitda_d2(netinc, ebitda):
    return _safe_div(_ttm(netinc), _ttm(ebitda).abs()).diff().diff()

def f12_psnp_111_effective_tax_rate_ttm_d2(taxexp, ebit):
    return _safe_div(_ttm(taxexp), _ttm(ebit)).diff().diff()

def f12_psnp_112_tax_to_revenue_volatility_8q_d2(taxexp, revenue):
    return _safe_div(_ttm(taxexp), _ttm(revenue)).rolling(8, min_periods=3).std().diff().diff()

def f12_psnp_113_interest_coverage_ebit_d2(ebit, intexp):
    return _safe_div(_ttm(ebit), _ttm(intexp).abs()).diff().diff()

def f12_psnp_114_interest_coverage_ebitda_d2(ebitda, intexp):
    return _safe_div(_ttm(ebitda), _ttm(intexp).abs()).diff().diff()

def f12_psnp_115_opinc_minus_interest_margin_d2(opinc, intexp, revenue):
    return _safe_div(_ttm(opinc) - _ttm(intexp), _ttm(revenue).abs()).diff().diff()

def f12_psnp_116_cash_to_book_tax_ratio_d2(taxexp, ncfo, ebit):
    return _safe_div(_ttm(taxexp), _ttm(ebit).abs() - _ttm(ncfo).abs() + 1e-09).diff().diff()

def f12_psnp_117_negative_tax_q_share_8q_d2(taxexp):
    return (taxexp < 0).rolling(8, min_periods=3).mean().diff().diff()

def f12_psnp_118_pretax_to_ebit_ratio_d2(ebit, intexp):
    return _safe_div(_ttm(ebit) - _ttm(intexp), _ttm(ebit).abs()).diff().diff()

def f12_psnp_119_fcf_after_interest_margin_d2(fcf, intexp, revenue):
    return _safe_div(_ttm(fcf) - _ttm(intexp).abs(), _ttm(revenue).abs()).diff().diff()

def f12_psnp_120_nopat_to_ebit_ratio_d2(ebit, taxexp):
    eff_tax = _safe_div(_ttm(taxexp), _ttm(ebit).abs()).clip(lower=0.0, upper=0.6)
    return (1.0 - eff_tax).diff().diff()

def f12_psnp_121_roa_cv_8q_d2(netinc, assets):
    r = _safe_div(_ttm(netinc), assets)
    return _safe_div(r.rolling(8, min_periods=3).std(), r.rolling(8, min_periods=3).mean().abs()).diff().diff()

def f12_psnp_122_roe_cv_8q_d2(netinc, equity):
    r = _safe_div(_ttm(netinc), equity)
    return _safe_div(r.rolling(8, min_periods=3).std(), r.rolling(8, min_periods=3).mean().abs()).diff().diff()

def f12_psnp_123_ebitda_margin_cv_12q_d2(ebitda, revenue):
    m = _safe_div(_ttm(ebitda), _ttm(revenue))
    return _safe_div(m.rolling(12, min_periods=4).std(), m.rolling(12, min_periods=4).mean().abs()).diff().diff()

def f12_psnp_124_operating_margin_cv_12q_d2(opinc, revenue):
    m = _safe_div(_ttm(opinc), _ttm(revenue))
    return _safe_div(m.rolling(12, min_periods=4).std(), m.rolling(12, min_periods=4).mean().abs()).diff().diff()

def f12_psnp_125_gross_margin_cv_12q_d2(gp, revenue):
    m = _safe_div(_ttm(gp), _ttm(revenue))
    return _safe_div(m.rolling(12, min_periods=4).std(), m.rolling(12, min_periods=4).mean().abs()).diff().diff()

def f12_psnp_126_negative_netinc_q_share_8q_d2(netinc):
    return (netinc < 0).rolling(8, min_periods=3).mean().diff().diff()

def f12_psnp_127_negative_opinc_q_share_8q_d2(opinc):
    return (opinc < 0).rolling(8, min_periods=3).mean().diff().diff()

def f12_psnp_128_negative_fcf_q_share_8q_d2(fcf):
    return (fcf < 0).rolling(8, min_periods=3).mean().diff().diff()

def f12_psnp_129_negative_ebitda_q_share_8q_d2(ebitda):
    return (ebitda < 0).rolling(8, min_periods=3).mean().diff().diff()

def f12_psnp_130_eps_sign_change_count_8q_d2(eps):
    return _sign_change(eps).rolling(8, min_periods=3).sum().diff().diff()

def f12_psnp_131_consecutive_profitable_q_streak_12q_d2(netinc):
    pos = (netinc > 0).astype(int)
    return pos.rolling(12, min_periods=3).apply(lambda w: int(w[::-1].cumprod().sum()), raw=True).diff().diff()

def f12_psnp_132_consecutive_unprofitable_q_streak_12q_d2(netinc):
    neg = (netinc <= 0).astype(int)
    return neg.rolling(12, min_periods=3).apply(lambda w: int(w[::-1].cumprod().sum()), raw=True).diff().diff()

def f12_psnp_133_earnings_seasonality_q4_vs_q1_d2(netinc):
    return _safe_div(netinc, netinc.shift(2).abs()).diff().diff()

def f12_psnp_134_margin_compression_q_count_8q_d2(opinc, revenue):
    m = _safe_div(opinc, revenue)
    return (m.diff() < 0).rolling(8, min_periods=3).sum().diff().diff()

def f12_psnp_135_profitability_consistency_composite_d2(netinc, ncfo, opinc):
    z_ni = _rolling_zscore(_ttm(netinc), 12, 4)
    z_cf = _rolling_zscore(_ttm(ncfo), 12, 4)
    z_op = _rolling_zscore(_ttm(opinc), 12, 4)
    return ((z_ni + z_cf + z_op) / 3.0).diff().diff()

def f12_psnp_136_piotroski_partial_5sig_d2(netinc, ncfo, assets, revenue, gp):
    s1 = (netinc > 0).astype(float)
    s2 = (ncfo > 0).astype(float)
    s3 = (_ttm(netinc) - _ttm(netinc).shift(4) > 0).astype(float)
    s4 = (_ttm(ncfo) > _ttm(netinc)).astype(float)
    gm = _safe_div(_ttm(gp), _ttm(revenue))
    s5 = (gm - gm.shift(4) > 0).astype(float)
    return (s1 + s2 + s3 + s4 + s5).diff().diff()

def f12_psnp_137_quality_composite_zscore_d2(netinc, gp, ebitda, fcf, assets, revenue):
    z_roa = _rolling_zscore(_safe_div(_ttm(netinc), assets), 12, 4)
    z_gm = _rolling_zscore(_safe_div(_ttm(gp), _ttm(revenue)), 12, 4)
    z_em = _rolling_zscore(_safe_div(_ttm(ebitda), _ttm(revenue)), 12, 4)
    z_fm = _rolling_zscore(_safe_div(_ttm(fcf), _ttm(revenue)), 12, 4)
    return ((z_roa + z_gm + z_em + z_fm) / 4.0).diff().diff()

def f12_psnp_138_profitability_history_decile_proxy_d2(netinc, assets):
    r = _safe_div(_ttm(netinc), assets)
    return r.rolling(20, min_periods=6).rank(pct=True).diff().diff()

def f12_psnp_139_core_profitability_research_adj_d2(ebit, rnd, assets):
    return _safe_div(_ttm(ebit) + _ttm(rnd), assets).diff().diff()

def f12_psnp_140_margin_minus_revenue_growth_gap_d2(opinc, revenue):
    return (_safe_div(_ttm(opinc), _ttm(revenue)) - _yoy_pct(_ttm(revenue))).diff().diff()

def f12_psnp_141_owner_earnings_proxy_to_assets_d2(ncfo, capex, assets):
    return _safe_div(_ttm(ncfo) - _ttm(capex).abs(), assets).diff().diff()

def f12_psnp_142_cash_earnings_yield_to_invcap_d2(ncfo, equity, debt):
    return _safe_div(_ttm(ncfo), equity + debt).diff().diff()

def f12_psnp_143_roic_minus_8q_avg_d2(ebit, equity, debt):
    r = _safe_div(_ttm(ebit), equity + debt)
    return (r - r.rolling(8, min_periods=3).mean()).diff().diff()

def f12_psnp_144_novymarx_gp_to_assets_d2(gp, assets):
    return _safe_div(_ttm(gp), assets).diff().diff()

def f12_psnp_145_operating_efficiency_composite_d2(gp, opinc, ebitda, revenue):
    rev = _ttm(revenue).replace(0, np.nan)
    return ((_ttm(gp) + _ttm(opinc) + _ttm(ebitda)) / (3.0 * rev)).diff().diff()

def f12_psnp_146_capital_efficiency_composite_d2(netinc, ebit, ebitda, assets, equity, debt):
    roa = _safe_div(_ttm(netinc), assets)
    roe = _safe_div(_ttm(netinc), equity)
    roic = _safe_div(_ttm(ebit), equity + debt)
    return ((roa + roe + roic) / 3.0).diff().diff()

def f12_psnp_147_earnings_diversity_score_d2(netinc, opinc, ncfo):
    df = pd.concat([_ttm(netinc), _ttm(opinc), _ttm(ncfo)], axis=1)
    return (-df.std(axis=1)).diff().diff()

def f12_psnp_148_cash_quality_4q_min_to_avg_d2(ncfo, netinc):
    return _safe_div(ncfo.rolling(4, min_periods=2).min(), netinc.rolling(4, min_periods=2).mean().abs()).diff().diff()

def f12_psnp_149_negative_growth_negative_margin_composite_d2(opinc, revenue):
    m = _safe_div(_ttm(opinc), _ttm(revenue))
    rev_yoy = _yoy_pct(_ttm(revenue))
    return (-(m.clip(upper=0).abs() * rev_yoy.clip(upper=0).abs())).diff().diff()

def f12_psnp_150_profitability_collapse_signal_d2(opinc, revenue):
    m = _safe_div(opinc, revenue)
    return (m - m.rolling(4, min_periods=2).mean().shift(1)).diff().diff()
PROFITABILITY_SNAPSHOT_D2_REGISTRY_076_150 = {'f12_psnp_076_signed_log_eps_ttm_d2': {'inputs': ['eps'], 'func': f12_psnp_076_signed_log_eps_ttm_d2}, 'f12_psnp_077_signed_log_eps_dil_ttm_d2': {'inputs': ['epsdil'], 'func': f12_psnp_077_signed_log_eps_dil_ttm_d2}, 'f12_psnp_078_eps_growth_yoy_d2': {'inputs': ['eps'], 'func': f12_psnp_078_eps_growth_yoy_d2}, 'f12_psnp_079_eps_growth_qoq_d2': {'inputs': ['eps'], 'func': f12_psnp_079_eps_growth_qoq_d2}, 'f12_psnp_080_payout_ratio_dps_to_eps_d2': {'inputs': ['dps', 'eps'], 'func': f12_psnp_080_payout_ratio_dps_to_eps_d2}, 'f12_psnp_081_dps_growth_yoy_d2': {'inputs': ['dps'], 'func': f12_psnp_081_dps_growth_yoy_d2}, 'f12_psnp_082_ebitda_per_share_ttm_d2': {'inputs': ['ebitda', 'shareswadil'], 'func': f12_psnp_082_ebitda_per_share_ttm_d2}, 'f12_psnp_083_fcf_per_share_ttm_d2': {'inputs': ['fcf', 'shareswadil'], 'func': f12_psnp_083_fcf_per_share_ttm_d2}, 'f12_psnp_084_ocf_per_share_ttm_d2': {'inputs': ['ncfo', 'shareswadil'], 'func': f12_psnp_084_ocf_per_share_ttm_d2}, 'f12_psnp_085_book_value_per_share_d2': {'inputs': ['equity', 'shareswadil'], 'func': f12_psnp_085_book_value_per_share_d2}, 'f12_psnp_086_tangible_book_per_share_d2': {'inputs': ['equity', 'intangibles', 'shareswadil'], 'func': f12_psnp_086_tangible_book_per_share_d2}, 'f12_psnp_087_eps_dil_minus_basic_drag_d2': {'inputs': ['eps', 'epsdil'], 'func': f12_psnp_087_eps_dil_minus_basic_drag_d2}, 'f12_psnp_088_eps_zscore_8q_d2': {'inputs': ['eps'], 'func': f12_psnp_088_eps_zscore_8q_d2}, 'f12_psnp_089_ebitda_per_share_zscore_8q_d2': {'inputs': ['ebitda', 'shareswadil'], 'func': f12_psnp_089_ebitda_per_share_zscore_8q_d2}, 'f12_psnp_090_fcf_per_share_growth_yoy_d2': {'inputs': ['fcf', 'shareswadil'], 'func': f12_psnp_090_fcf_per_share_growth_yoy_d2}, 'f12_psnp_091_dps_yield_to_bvps_d2': {'inputs': ['dps', 'equity', 'shareswadil'], 'func': f12_psnp_091_dps_yield_to_bvps_d2}, 'f12_psnp_092_payout_to_fcf_ttm_d2': {'inputs': ['dps', 'fcf', 'shareswadil'], 'func': f12_psnp_092_payout_to_fcf_ttm_d2}, 'f12_psnp_093_eps_yoy_minus_revenue_yoy_d2': {'inputs': ['eps', 'revenue'], 'func': f12_psnp_093_eps_yoy_minus_revenue_yoy_d2}, 'f12_psnp_094_ebitda_per_share_yoy_minus_revenue_per_share_yoy_d2': {'inputs': ['ebitda', 'revenue', 'shareswadil'], 'func': f12_psnp_094_ebitda_per_share_yoy_minus_revenue_per_share_yoy_d2}, 'f12_psnp_095_bvps_growth_yoy_d2': {'inputs': ['equity', 'shareswadil'], 'func': f12_psnp_095_bvps_growth_yoy_d2}, 'f12_psnp_096_gross_profit_to_assets_d2': {'inputs': ['gp', 'assets'], 'func': f12_psnp_096_gross_profit_to_assets_d2}, 'f12_psnp_097_operating_income_to_assets_d2': {'inputs': ['opinc', 'assets'], 'func': f12_psnp_097_operating_income_to_assets_d2}, 'f12_psnp_098_ebitda_to_assets_d2': {'inputs': ['ebitda', 'assets'], 'func': f12_psnp_098_ebitda_to_assets_d2}, 'f12_psnp_099_netinc_share_of_opinc_d2': {'inputs': ['netinc', 'opinc'], 'func': f12_psnp_099_netinc_share_of_opinc_d2}, 'f12_psnp_100_ebit_to_total_capital_d2': {'inputs': ['ebit', 'equity', 'debt'], 'func': f12_psnp_100_ebit_to_total_capital_d2}, 'f12_psnp_101_opinc_to_invested_capital_d2': {'inputs': ['opinc', 'equity', 'debt'], 'func': f12_psnp_101_opinc_to_invested_capital_d2}, 'f12_psnp_102_fcf_to_total_capital_d2': {'inputs': ['fcf', 'equity', 'debt'], 'func': f12_psnp_102_fcf_to_total_capital_d2}, 'f12_psnp_103_ebitda_to_total_capital_d2': {'inputs': ['ebitda', 'equity', 'debt'], 'func': f12_psnp_103_ebitda_to_total_capital_d2}, 'f12_psnp_104_operating_leverage_yoy_d2': {'inputs': ['ebit', 'revenue'], 'func': f12_psnp_104_operating_leverage_yoy_d2}, 'f12_psnp_105_financial_leverage_yoy_d2': {'inputs': ['netinc', 'ebit'], 'func': f12_psnp_105_financial_leverage_yoy_d2}, 'f12_psnp_106_total_leverage_yoy_d2': {'inputs': ['netinc', 'revenue'], 'func': f12_psnp_106_total_leverage_yoy_d2}, 'f12_psnp_107_gross_to_operating_margin_gap_d2': {'inputs': ['gp', 'opinc', 'revenue'], 'func': f12_psnp_107_gross_to_operating_margin_gap_d2}, 'f12_psnp_108_ebitda_to_ebit_ratio_d2': {'inputs': ['ebitda', 'ebit'], 'func': f12_psnp_108_ebitda_to_ebit_ratio_d2}, 'f12_psnp_109_opinc_to_ebitda_d2': {'inputs': ['opinc', 'ebitda'], 'func': f12_psnp_109_opinc_to_ebitda_d2}, 'f12_psnp_110_netinc_share_of_ebitda_d2': {'inputs': ['netinc', 'ebitda'], 'func': f12_psnp_110_netinc_share_of_ebitda_d2}, 'f12_psnp_111_effective_tax_rate_ttm_d2': {'inputs': ['taxexp', 'ebit'], 'func': f12_psnp_111_effective_tax_rate_ttm_d2}, 'f12_psnp_112_tax_to_revenue_volatility_8q_d2': {'inputs': ['taxexp', 'revenue'], 'func': f12_psnp_112_tax_to_revenue_volatility_8q_d2}, 'f12_psnp_113_interest_coverage_ebit_d2': {'inputs': ['ebit', 'intexp'], 'func': f12_psnp_113_interest_coverage_ebit_d2}, 'f12_psnp_114_interest_coverage_ebitda_d2': {'inputs': ['ebitda', 'intexp'], 'func': f12_psnp_114_interest_coverage_ebitda_d2}, 'f12_psnp_115_opinc_minus_interest_margin_d2': {'inputs': ['opinc', 'intexp', 'revenue'], 'func': f12_psnp_115_opinc_minus_interest_margin_d2}, 'f12_psnp_116_cash_to_book_tax_ratio_d2': {'inputs': ['taxexp', 'ncfo', 'ebit'], 'func': f12_psnp_116_cash_to_book_tax_ratio_d2}, 'f12_psnp_117_negative_tax_q_share_8q_d2': {'inputs': ['taxexp'], 'func': f12_psnp_117_negative_tax_q_share_8q_d2}, 'f12_psnp_118_pretax_to_ebit_ratio_d2': {'inputs': ['ebit', 'intexp'], 'func': f12_psnp_118_pretax_to_ebit_ratio_d2}, 'f12_psnp_119_fcf_after_interest_margin_d2': {'inputs': ['fcf', 'intexp', 'revenue'], 'func': f12_psnp_119_fcf_after_interest_margin_d2}, 'f12_psnp_120_nopat_to_ebit_ratio_d2': {'inputs': ['ebit', 'taxexp'], 'func': f12_psnp_120_nopat_to_ebit_ratio_d2}, 'f12_psnp_121_roa_cv_8q_d2': {'inputs': ['netinc', 'assets'], 'func': f12_psnp_121_roa_cv_8q_d2}, 'f12_psnp_122_roe_cv_8q_d2': {'inputs': ['netinc', 'equity'], 'func': f12_psnp_122_roe_cv_8q_d2}, 'f12_psnp_123_ebitda_margin_cv_12q_d2': {'inputs': ['ebitda', 'revenue'], 'func': f12_psnp_123_ebitda_margin_cv_12q_d2}, 'f12_psnp_124_operating_margin_cv_12q_d2': {'inputs': ['opinc', 'revenue'], 'func': f12_psnp_124_operating_margin_cv_12q_d2}, 'f12_psnp_125_gross_margin_cv_12q_d2': {'inputs': ['gp', 'revenue'], 'func': f12_psnp_125_gross_margin_cv_12q_d2}, 'f12_psnp_126_negative_netinc_q_share_8q_d2': {'inputs': ['netinc'], 'func': f12_psnp_126_negative_netinc_q_share_8q_d2}, 'f12_psnp_127_negative_opinc_q_share_8q_d2': {'inputs': ['opinc'], 'func': f12_psnp_127_negative_opinc_q_share_8q_d2}, 'f12_psnp_128_negative_fcf_q_share_8q_d2': {'inputs': ['fcf'], 'func': f12_psnp_128_negative_fcf_q_share_8q_d2}, 'f12_psnp_129_negative_ebitda_q_share_8q_d2': {'inputs': ['ebitda'], 'func': f12_psnp_129_negative_ebitda_q_share_8q_d2}, 'f12_psnp_130_eps_sign_change_count_8q_d2': {'inputs': ['eps'], 'func': f12_psnp_130_eps_sign_change_count_8q_d2}, 'f12_psnp_131_consecutive_profitable_q_streak_12q_d2': {'inputs': ['netinc'], 'func': f12_psnp_131_consecutive_profitable_q_streak_12q_d2}, 'f12_psnp_132_consecutive_unprofitable_q_streak_12q_d2': {'inputs': ['netinc'], 'func': f12_psnp_132_consecutive_unprofitable_q_streak_12q_d2}, 'f12_psnp_133_earnings_seasonality_q4_vs_q1_d2': {'inputs': ['netinc'], 'func': f12_psnp_133_earnings_seasonality_q4_vs_q1_d2}, 'f12_psnp_134_margin_compression_q_count_8q_d2': {'inputs': ['opinc', 'revenue'], 'func': f12_psnp_134_margin_compression_q_count_8q_d2}, 'f12_psnp_135_profitability_consistency_composite_d2': {'inputs': ['netinc', 'ncfo', 'opinc'], 'func': f12_psnp_135_profitability_consistency_composite_d2}, 'f12_psnp_136_piotroski_partial_5sig_d2': {'inputs': ['netinc', 'ncfo', 'assets', 'revenue', 'gp'], 'func': f12_psnp_136_piotroski_partial_5sig_d2}, 'f12_psnp_137_quality_composite_zscore_d2': {'inputs': ['netinc', 'gp', 'ebitda', 'fcf', 'assets', 'revenue'], 'func': f12_psnp_137_quality_composite_zscore_d2}, 'f12_psnp_138_profitability_history_decile_proxy_d2': {'inputs': ['netinc', 'assets'], 'func': f12_psnp_138_profitability_history_decile_proxy_d2}, 'f12_psnp_139_core_profitability_research_adj_d2': {'inputs': ['ebit', 'rnd', 'assets'], 'func': f12_psnp_139_core_profitability_research_adj_d2}, 'f12_psnp_140_margin_minus_revenue_growth_gap_d2': {'inputs': ['opinc', 'revenue'], 'func': f12_psnp_140_margin_minus_revenue_growth_gap_d2}, 'f12_psnp_141_owner_earnings_proxy_to_assets_d2': {'inputs': ['ncfo', 'capex', 'assets'], 'func': f12_psnp_141_owner_earnings_proxy_to_assets_d2}, 'f12_psnp_142_cash_earnings_yield_to_invcap_d2': {'inputs': ['ncfo', 'equity', 'debt'], 'func': f12_psnp_142_cash_earnings_yield_to_invcap_d2}, 'f12_psnp_143_roic_minus_8q_avg_d2': {'inputs': ['ebit', 'equity', 'debt'], 'func': f12_psnp_143_roic_minus_8q_avg_d2}, 'f12_psnp_144_novymarx_gp_to_assets_d2': {'inputs': ['gp', 'assets'], 'func': f12_psnp_144_novymarx_gp_to_assets_d2}, 'f12_psnp_145_operating_efficiency_composite_d2': {'inputs': ['gp', 'opinc', 'ebitda', 'revenue'], 'func': f12_psnp_145_operating_efficiency_composite_d2}, 'f12_psnp_146_capital_efficiency_composite_d2': {'inputs': ['netinc', 'ebit', 'ebitda', 'assets', 'equity', 'debt'], 'func': f12_psnp_146_capital_efficiency_composite_d2}, 'f12_psnp_147_earnings_diversity_score_d2': {'inputs': ['netinc', 'opinc', 'ncfo'], 'func': f12_psnp_147_earnings_diversity_score_d2}, 'f12_psnp_148_cash_quality_4q_min_to_avg_d2': {'inputs': ['ncfo', 'netinc'], 'func': f12_psnp_148_cash_quality_4q_min_to_avg_d2}, 'f12_psnp_149_negative_growth_negative_margin_composite_d2': {'inputs': ['opinc', 'revenue'], 'func': f12_psnp_149_negative_growth_negative_margin_composite_d2}, 'f12_psnp_150_profitability_collapse_signal_d2': {'inputs': ['opinc', 'revenue'], 'func': f12_psnp_150_profitability_collapse_signal_d2}}