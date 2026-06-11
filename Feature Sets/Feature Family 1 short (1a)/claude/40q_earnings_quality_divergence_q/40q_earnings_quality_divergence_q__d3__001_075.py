"""earnings_quality_divergence_q d3 features 001-075 — order-3 difference of corresponding base features.

Each function inlines the base body and wraps the return value with .diff().diff().diff(). Self-contained; helpers redefined locally per HANDOFF."""
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

def f40q_eqdgq_001_sloan_accrual_ratio_balance_sheet_d3(workingcapital, depamor, assets):
    return _safe_div(workingcapital.diff() - _ttm(depamor), assets.rolling(4, min_periods=2).mean()).diff().diff().diff()

def f40q_eqdgq_002_sloan_accrual_ratio_cash_flow_d3(netinc, ncfo, assets):
    return _safe_div(_ttm(netinc) - _ttm(ncfo), assets.rolling(4, min_periods=2).mean()).diff().diff().diff()

def f40q_eqdgq_003_total_accruals_to_revenue_ttm_d3(netinc, ncfo, revenue):
    return _safe_div(_ttm(netinc) - _ttm(ncfo), _ttm(revenue).abs()).diff().diff().diff()

def f40q_eqdgq_004_total_accruals_to_avg_assets_yoy_change_d3(netinc, ncfo, assets):
    accr = _safe_div(_ttm(netinc) - _ttm(ncfo), assets.rolling(4, min_periods=2).mean())
    return _yoy(accr).diff().diff().diff()

def f40q_eqdgq_005_accrual_quality_dispersion_8q_d3(netinc, ncfo, assets):
    a = _safe_div(netinc - ncfo, assets)
    return a.rolling(8, min_periods=3).std().diff().diff().diff()

def f40q_eqdgq_006_working_capital_accruals_to_assets_d3(receivables, inventory, payables, assets):
    delta_nwc = receivables.diff() + inventory.diff() - payables.diff()
    return _safe_div(delta_nwc, assets).diff().diff().diff()

def f40q_eqdgq_007_accruals_persistence_lag1_autocorr_8q_d3(netinc, ncfo, assets):
    a = _safe_div(netinc - ncfo, assets)
    return a.rolling(8, min_periods=4).apply(lambda w: np.corrcoef(w[:-1], w[1:])[0, 1] if np.std(w[:-1]) > 0 and np.std(w[1:]) > 0 else np.nan, raw=True).diff().diff().diff()

def f40q_eqdgq_008_discretionary_accrual_proxy_d3(netinc, ncfo, revenue, assets):
    accr = _safe_div(_ttm(netinc) - _ttm(ncfo), assets)
    rev_g = _yoy_pct(_ttm(revenue))
    expected = rev_g * 0.05
    return (accr - expected).diff().diff().diff()

def f40q_eqdgq_009_abs_accrual_intensity_ttm_d3(netinc, ncfo, assets):
    return _safe_div((_ttm(netinc) - _ttm(ncfo)).abs(), assets).diff().diff().diff()

def f40q_eqdgq_010_accrual_volatility_zscore_12q_d3(netinc, ncfo, assets):
    a = _safe_div(netinc - ncfo, assets)
    return _rolling_zscore(a.rolling(4, min_periods=2).std(), 12, 4).diff().diff().diff()

def f40q_eqdgq_011_positive_accrual_q_share_8q_d3(netinc, ncfo):
    return (netinc - ncfo > 0).rolling(8, min_periods=3).mean().diff().diff().diff()

def f40q_eqdgq_012_extreme_accrual_q_count_8q_d3(netinc, ncfo, assets):
    a = _safe_div(netinc - ncfo, assets)
    z = _rolling_zscore(a, 12, 4)
    return (z.abs() > 1.5).astype(float).rolling(8, min_periods=3).sum().diff().diff().diff()

def f40q_eqdgq_013_accruals_yoy_pct_change_d3(netinc, ncfo):
    return _yoy_pct(_ttm(netinc) - _ttm(ncfo)).diff().diff().diff()

def f40q_eqdgq_014_accruals_to_netinc_share_d3(netinc, ncfo):
    return _safe_div(_ttm(netinc) - _ttm(ncfo), _ttm(netinc).abs()).diff().diff().diff()

def f40q_eqdgq_015_cash_to_accrual_earnings_ratio_d3(ncfo, netinc):
    return _safe_div(_ttm(ncfo), _ttm(netinc)).diff().diff().diff()

def f40q_eqdgq_016_accrual_quality_minus_4q_avg_d3(netinc, ncfo, assets):
    a = _safe_div(netinc - ncfo, assets)
    return (a - a.rolling(4, min_periods=2).mean()).diff().diff().diff()

def f40q_eqdgq_017_long_term_accrual_proxy_d3(ppnenet, intangibles, assets):
    return _safe_div((ppnenet.diff() + intangibles.diff()).abs(), assets).diff().diff().diff()

def f40q_eqdgq_018_short_term_accrual_proxy_d3(receivables, inventory, assets):
    return _safe_div(receivables.diff() + inventory.diff(), assets).diff().diff().diff()

def f40q_eqdgq_019_st_vs_lt_accrual_gap_d3(receivables, inventory, ppnenet, intangibles, assets):
    st = _safe_div(receivables.diff() + inventory.diff(), assets)
    lt = _safe_div((ppnenet.diff() + intangibles.diff()).abs(), assets)
    return (st - lt).diff().diff().diff()

def f40q_eqdgq_020_accrual_concentration_qoq_d3(netinc, ncfo, assets):
    a = _safe_div(netinc - ncfo, assets)
    abs_q = a.abs()
    return _safe_div(abs_q, abs_q.rolling(4, min_periods=2).sum()).diff().diff().diff()

def f40q_eqdgq_021_normal_accrual_proxy_via_assets_d3(netinc, ncfo, assets):
    a = _safe_div(_ttm(netinc) - _ttm(ncfo), assets)
    long_avg = a.rolling(20, min_periods=6).mean()
    return (a - long_avg).diff().diff().diff()

def f40q_eqdgq_022_special_item_proxy_netinc_swing_d3(netinc):
    return _rolling_zscore(netinc.diff().abs(), 12, 4).diff().diff().diff()

def f40q_eqdgq_023_accruals_persistence_4q_minus_8q_d3(netinc, ncfo, assets):
    a = _safe_div(netinc - ncfo, assets)
    return (a.rolling(4, min_periods=2).mean() - a.rolling(8, min_periods=3).mean()).diff().diff().diff()

def f40q_eqdgq_024_accruals_to_cash_flow_gap_zscore_12q_d3(netinc, ncfo, assets):
    g = _safe_div(_ttm(netinc) - _ttm(ncfo), assets)
    return _rolling_zscore(g, 12, 4).diff().diff().diff()

def f40q_eqdgq_025_negative_accrual_streak_8q_d3(netinc, ncfo):
    neg = (netinc - ncfo < 0).astype(int)
    return neg.rolling(8, min_periods=3).apply(lambda w: int(w[::-1].cumprod().sum()), raw=True).diff().diff().diff()

def f40q_eqdgq_026_effective_tax_rate_dispersion_8q_d3(taxexp, ebit):
    etr = _safe_div(_ttm(taxexp), _ttm(ebit))
    return etr.rolling(8, min_periods=3).std().diff().diff().diff()

def f40q_eqdgq_027_effective_tax_rate_minus_long_avg_d3(taxexp, ebit):
    etr = _safe_div(_ttm(taxexp), _ttm(ebit))
    return (etr - etr.rolling(20, min_periods=6).mean()).diff().diff().diff()

def f40q_eqdgq_028_below_line_share_of_netinc_d3(netinc, opinc, taxexp):
    eff = _safe_div(_ttm(taxexp), _ttm(opinc).abs()).clip(lower=0, upper=0.6)
    op_after = _ttm(opinc) * (1.0 - eff)
    return _safe_div(_ttm(netinc) - op_after, _ttm(netinc).abs()).diff().diff().diff()

def f40q_eqdgq_029_below_line_volatility_8q_d3(netinc, opinc):
    g = netinc - opinc
    return g.rolling(8, min_periods=3).std().diff().diff().diff()

def f40q_eqdgq_030_taxexp_to_ncfo_gap_yoy_d3(taxexp, ncfo):
    return (_yoy(taxexp) - _yoy(ncfo)).diff().diff().diff()

def f40q_eqdgq_031_deferred_tax_proxy_via_taxexp_lag_d3(taxexp, ebit):
    return _safe_div(taxexp.shift(1) - taxexp, ebit.abs()).diff().diff().diff()

def f40q_eqdgq_032_tax_burden_minus_cash_tax_proxy_d3(taxexp, ncfo, ebit):
    return _safe_div(_ttm(taxexp) - (_ttm(ebit) - _ttm(ncfo)).clip(lower=0), _ttm(ebit).abs()).diff().diff().diff()

def f40q_eqdgq_033_negative_taxexp_q_count_8q_d3(taxexp):
    return (taxexp < 0).rolling(8, min_periods=3).sum().diff().diff().diff()

def f40q_eqdgq_034_etr_zero_quarters_count_8q_d3(taxexp, ebit):
    etr = _safe_div(taxexp, ebit.abs())
    return (etr.abs() < 0.05).rolling(8, min_periods=3).sum().diff().diff().diff()

def f40q_eqdgq_035_pretax_minus_aftertax_growth_gap_d3(ebit, netinc):
    return (_yoy_pct(_ttm(ebit)) - _yoy_pct(_ttm(netinc))).diff().diff().diff()

def f40q_eqdgq_036_below_line_q_minus_8q_avg_d3(netinc, opinc):
    g = netinc - opinc
    return (g - g.rolling(8, min_periods=3).mean()).diff().diff().diff()

def f40q_eqdgq_037_tax_to_revenue_zscore_8q_d3(taxexp, revenue):
    return _rolling_zscore(_safe_div(_ttm(taxexp), _ttm(revenue)), 8, 3).diff().diff().diff()

def f40q_eqdgq_038_pretax_income_minus_ebit_to_revenue_d3(ebit, intexp, revenue):
    pretax = _ttm(ebit) - _ttm(intexp)
    return _safe_div(_ttm(ebit) - pretax, _ttm(revenue).abs()).diff().diff().diff()

def f40q_eqdgq_039_below_line_growth_yoy_d3(netinc, opinc):
    return _yoy(_ttm(netinc) - _ttm(opinc)).diff().diff().diff()

def f40q_eqdgq_040_extraordinary_charge_proxy_via_belowline_zscore_8q_d3(netinc, opinc):
    return _rolling_zscore((netinc - opinc).diff(), 8, 3).diff().diff().diff()

def f40q_eqdgq_041_netinc_minus_ncfo_to_revenue_ttm_d3(netinc, ncfo, revenue):
    return _safe_div(_ttm(netinc) - _ttm(ncfo), _ttm(revenue).abs()).diff().diff().diff()

def f40q_eqdgq_042_netinc_minus_fcf_to_revenue_ttm_d3(netinc, fcf, revenue):
    return _safe_div(_ttm(netinc) - _ttm(fcf), _ttm(revenue).abs()).diff().diff().diff()

def f40q_eqdgq_043_ebitda_minus_ncfo_to_revenue_d3(ebitda, ncfo, revenue):
    return _safe_div(_ttm(ebitda) - _ttm(ncfo), _ttm(revenue).abs()).diff().diff().diff()

def f40q_eqdgq_044_ebit_minus_ncfo_to_revenue_d3(ebit, ncfo, revenue):
    return _safe_div(_ttm(ebit) - _ttm(ncfo), _ttm(revenue).abs()).diff().diff().diff()

def f40q_eqdgq_045_opinc_minus_ncfo_to_revenue_d3(opinc, ncfo, revenue):
    return _safe_div(_ttm(opinc) - _ttm(ncfo), _ttm(revenue).abs()).diff().diff().diff()

def f40q_eqdgq_046_gap_zscore_netinc_minus_ncfo_12q_d3(netinc, ncfo, assets):
    g = _safe_div(_ttm(netinc) - _ttm(ncfo), assets)
    return _rolling_zscore(g, 12, 4).diff().diff().diff()

def f40q_eqdgq_047_gap_zscore_netinc_minus_fcf_12q_d3(netinc, fcf, assets):
    g = _safe_div(_ttm(netinc) - _ttm(fcf), assets)
    return _rolling_zscore(g, 12, 4).diff().diff().diff()

def f40q_eqdgq_048_cash_conversion_ratio_8q_min_d3(ncfo, netinc):
    cc = _safe_div(ncfo, netinc.abs())
    return cc.rolling(8, min_periods=3).min().diff().diff().diff()

def f40q_eqdgq_049_cash_conversion_ratio_8q_max_d3(ncfo, netinc):
    cc = _safe_div(ncfo, netinc.abs())
    return cc.rolling(8, min_periods=3).max().diff().diff().diff()

def f40q_eqdgq_050_cash_conversion_dispersion_8q_d3(ncfo, netinc):
    cc = _safe_div(ncfo, netinc.abs())
    return cc.rolling(8, min_periods=3).std().diff().diff().diff()

def f40q_eqdgq_051_fcf_to_netinc_zscore_12q_d3(fcf, netinc):
    cc = _safe_div(fcf, netinc.abs())
    return _rolling_zscore(cc, 12, 4).diff().diff().diff()

def f40q_eqdgq_052_ebitda_to_ncfo_ratio_ttm_d3(ebitda, ncfo):
    return _safe_div(_ttm(ebitda), _ttm(ncfo).abs()).diff().diff().diff()

def f40q_eqdgq_053_persistent_earnings_cash_gap_4q_d3(netinc, ncfo):
    g = netinc - ncfo
    return g.rolling(4, min_periods=2).mean().diff().diff().diff()

def f40q_eqdgq_054_earnings_cash_gap_yoy_change_d3(netinc, ncfo):
    return _yoy(_ttm(netinc) - _ttm(ncfo)).diff().diff().diff()

def f40q_eqdgq_055_gap_inversion_sign_change_count_8q_d3(netinc, ncfo):
    g = netinc - ncfo
    sgn = np.sign(g.fillna(0))
    flips = (sgn != sgn.shift(1)).fillna(False).astype(float)
    return flips.rolling(8, min_periods=3).sum().diff().diff().diff()

def f40q_eqdgq_056_quality_score_ncfo_to_netinc_minus_long_avg_d3(ncfo, netinc):
    cc = _safe_div(_ttm(ncfo), _ttm(netinc).abs())
    return (cc - cc.rolling(20, min_periods=6).mean()).diff().diff().diff()

def f40q_eqdgq_057_earnings_quality_collapse_q_to_4q_avg_d3(ncfo, netinc):
    cc = _safe_div(ncfo, netinc.abs())
    return (cc - cc.rolling(4, min_periods=2).mean().shift(1)).diff().diff().diff()

def f40q_eqdgq_058_negative_cash_conversion_q_count_8q_d3(ncfo, netinc):
    return (_safe_div(ncfo, netinc.abs()) < 0).rolling(8, min_periods=3).sum().diff().diff().diff()

def f40q_eqdgq_059_fcf_minus_netinc_dispersion_12q_d3(fcf, netinc):
    return (fcf - netinc).rolling(12, min_periods=4).std().diff().diff().diff()

def f40q_eqdgq_060_cash_quality_consistency_score_12q_d3(ncfo, netinc):
    cc = _safe_div(_ttm(ncfo), _ttm(netinc).abs())
    return (-_safe_div(cc.rolling(12, min_periods=4).std(), cc.rolling(12, min_periods=4).mean().abs())).diff().diff().diff()

def f40q_eqdgq_061_depamor_to_revenue_zscore_8q_d3(depamor, revenue):
    return _rolling_zscore(_safe_div(_ttm(depamor), _ttm(revenue)), 8, 3).diff().diff().diff()

def f40q_eqdgq_062_depamor_to_assets_zscore_8q_d3(depamor, assets):
    return _rolling_zscore(_safe_div(_ttm(depamor), assets), 8, 3).diff().diff().diff()

def f40q_eqdgq_063_depamor_minus_capex_to_revenue_d3(depamor, capex, revenue):
    return _safe_div(_ttm(depamor) - _ttm(capex).abs(), _ttm(revenue).abs()).diff().diff().diff()

def f40q_eqdgq_064_capex_minus_depamor_persistence_12q_d3(capex, depamor):
    g = _ttm(capex).abs() - _ttm(depamor)
    return g.rolling(12, min_periods=4).mean().diff().diff().diff()

def f40q_eqdgq_065_depamor_yoy_pct_d3(depamor):
    return _yoy_pct(_ttm(depamor)).diff().diff().diff()

def f40q_eqdgq_066_depamor_qoq_pct_d3(depamor):
    return _qoq_pct(depamor).diff().diff().diff()

def f40q_eqdgq_067_depamor_share_of_ebitda_minus_ebit_d3(depamor, ebitda, ebit):
    expected = _ttm(ebitda) - _ttm(ebit)
    return _safe_div(_ttm(depamor) - expected, _ttm(ebitda).abs()).diff().diff().diff()

def f40q_eqdgq_068_depamor_to_ppe_ratio_d3(depamor, ppnenet):
    return _safe_div(_ttm(depamor), ppnenet).diff().diff().diff()

def f40q_eqdgq_069_depamor_to_ppe_zscore_12q_d3(depamor, ppnenet):
    return _rolling_zscore(_safe_div(_ttm(depamor), ppnenet), 12, 4).diff().diff().diff()

def f40q_eqdgq_070_depamor_to_intangibles_ratio_d3(depamor, intangibles):
    return _safe_div(_ttm(depamor), intangibles).diff().diff().diff()

def f40q_eqdgq_071_capex_to_depamor_ratio_yoy_d3(capex, depamor):
    return _yoy(_safe_div(_ttm(capex).abs(), _ttm(depamor))).diff().diff().diff()

def f40q_eqdgq_072_underinvestment_proxy_d3(capex, depamor, assets):
    return _safe_div(_ttm(depamor) - _ttm(capex).abs(), assets).clip(lower=0).diff().diff().diff()

def f40q_eqdgq_073_overinvestment_proxy_d3(capex, depamor, assets):
    return _safe_div(_ttm(capex).abs() - _ttm(depamor), assets).clip(lower=0).diff().diff().diff()

def f40q_eqdgq_074_depamor_minus_ebitda_gap_volatility_8q_d3(depamor, ebitda):
    return (_ttm(depamor) - _ttm(ebitda)).rolling(8, min_periods=3).std().diff().diff().diff()

def f40q_eqdgq_075_depamor_consistency_zscore_12q_d3(depamor, revenue):
    ratio = _safe_div(_ttm(depamor), _ttm(revenue))
    return _rolling_zscore(ratio, 12, 4).diff().diff().diff()
EARNINGS_QUALITY_DIVERGENCE_Q_D3_REGISTRY_001_075 = {'f40q_eqdgq_001_sloan_accrual_ratio_balance_sheet_d3': {'inputs': ['workingcapital', 'depamor', 'assets'], 'func': f40q_eqdgq_001_sloan_accrual_ratio_balance_sheet_d3}, 'f40q_eqdgq_002_sloan_accrual_ratio_cash_flow_d3': {'inputs': ['netinc', 'ncfo', 'assets'], 'func': f40q_eqdgq_002_sloan_accrual_ratio_cash_flow_d3}, 'f40q_eqdgq_003_total_accruals_to_revenue_ttm_d3': {'inputs': ['netinc', 'ncfo', 'revenue'], 'func': f40q_eqdgq_003_total_accruals_to_revenue_ttm_d3}, 'f40q_eqdgq_004_total_accruals_to_avg_assets_yoy_change_d3': {'inputs': ['netinc', 'ncfo', 'assets'], 'func': f40q_eqdgq_004_total_accruals_to_avg_assets_yoy_change_d3}, 'f40q_eqdgq_005_accrual_quality_dispersion_8q_d3': {'inputs': ['netinc', 'ncfo', 'assets'], 'func': f40q_eqdgq_005_accrual_quality_dispersion_8q_d3}, 'f40q_eqdgq_006_working_capital_accruals_to_assets_d3': {'inputs': ['receivables', 'inventory', 'payables', 'assets'], 'func': f40q_eqdgq_006_working_capital_accruals_to_assets_d3}, 'f40q_eqdgq_007_accruals_persistence_lag1_autocorr_8q_d3': {'inputs': ['netinc', 'ncfo', 'assets'], 'func': f40q_eqdgq_007_accruals_persistence_lag1_autocorr_8q_d3}, 'f40q_eqdgq_008_discretionary_accrual_proxy_d3': {'inputs': ['netinc', 'ncfo', 'revenue', 'assets'], 'func': f40q_eqdgq_008_discretionary_accrual_proxy_d3}, 'f40q_eqdgq_009_abs_accrual_intensity_ttm_d3': {'inputs': ['netinc', 'ncfo', 'assets'], 'func': f40q_eqdgq_009_abs_accrual_intensity_ttm_d3}, 'f40q_eqdgq_010_accrual_volatility_zscore_12q_d3': {'inputs': ['netinc', 'ncfo', 'assets'], 'func': f40q_eqdgq_010_accrual_volatility_zscore_12q_d3}, 'f40q_eqdgq_011_positive_accrual_q_share_8q_d3': {'inputs': ['netinc', 'ncfo'], 'func': f40q_eqdgq_011_positive_accrual_q_share_8q_d3}, 'f40q_eqdgq_012_extreme_accrual_q_count_8q_d3': {'inputs': ['netinc', 'ncfo', 'assets'], 'func': f40q_eqdgq_012_extreme_accrual_q_count_8q_d3}, 'f40q_eqdgq_013_accruals_yoy_pct_change_d3': {'inputs': ['netinc', 'ncfo'], 'func': f40q_eqdgq_013_accruals_yoy_pct_change_d3}, 'f40q_eqdgq_014_accruals_to_netinc_share_d3': {'inputs': ['netinc', 'ncfo'], 'func': f40q_eqdgq_014_accruals_to_netinc_share_d3}, 'f40q_eqdgq_015_cash_to_accrual_earnings_ratio_d3': {'inputs': ['ncfo', 'netinc'], 'func': f40q_eqdgq_015_cash_to_accrual_earnings_ratio_d3}, 'f40q_eqdgq_016_accrual_quality_minus_4q_avg_d3': {'inputs': ['netinc', 'ncfo', 'assets'], 'func': f40q_eqdgq_016_accrual_quality_minus_4q_avg_d3}, 'f40q_eqdgq_017_long_term_accrual_proxy_d3': {'inputs': ['ppnenet', 'intangibles', 'assets'], 'func': f40q_eqdgq_017_long_term_accrual_proxy_d3}, 'f40q_eqdgq_018_short_term_accrual_proxy_d3': {'inputs': ['receivables', 'inventory', 'assets'], 'func': f40q_eqdgq_018_short_term_accrual_proxy_d3}, 'f40q_eqdgq_019_st_vs_lt_accrual_gap_d3': {'inputs': ['receivables', 'inventory', 'ppnenet', 'intangibles', 'assets'], 'func': f40q_eqdgq_019_st_vs_lt_accrual_gap_d3}, 'f40q_eqdgq_020_accrual_concentration_qoq_d3': {'inputs': ['netinc', 'ncfo', 'assets'], 'func': f40q_eqdgq_020_accrual_concentration_qoq_d3}, 'f40q_eqdgq_021_normal_accrual_proxy_via_assets_d3': {'inputs': ['netinc', 'ncfo', 'assets'], 'func': f40q_eqdgq_021_normal_accrual_proxy_via_assets_d3}, 'f40q_eqdgq_022_special_item_proxy_netinc_swing_d3': {'inputs': ['netinc'], 'func': f40q_eqdgq_022_special_item_proxy_netinc_swing_d3}, 'f40q_eqdgq_023_accruals_persistence_4q_minus_8q_d3': {'inputs': ['netinc', 'ncfo', 'assets'], 'func': f40q_eqdgq_023_accruals_persistence_4q_minus_8q_d3}, 'f40q_eqdgq_024_accruals_to_cash_flow_gap_zscore_12q_d3': {'inputs': ['netinc', 'ncfo', 'assets'], 'func': f40q_eqdgq_024_accruals_to_cash_flow_gap_zscore_12q_d3}, 'f40q_eqdgq_025_negative_accrual_streak_8q_d3': {'inputs': ['netinc', 'ncfo'], 'func': f40q_eqdgq_025_negative_accrual_streak_8q_d3}, 'f40q_eqdgq_026_effective_tax_rate_dispersion_8q_d3': {'inputs': ['taxexp', 'ebit'], 'func': f40q_eqdgq_026_effective_tax_rate_dispersion_8q_d3}, 'f40q_eqdgq_027_effective_tax_rate_minus_long_avg_d3': {'inputs': ['taxexp', 'ebit'], 'func': f40q_eqdgq_027_effective_tax_rate_minus_long_avg_d3}, 'f40q_eqdgq_028_below_line_share_of_netinc_d3': {'inputs': ['netinc', 'opinc', 'taxexp'], 'func': f40q_eqdgq_028_below_line_share_of_netinc_d3}, 'f40q_eqdgq_029_below_line_volatility_8q_d3': {'inputs': ['netinc', 'opinc'], 'func': f40q_eqdgq_029_below_line_volatility_8q_d3}, 'f40q_eqdgq_030_taxexp_to_ncfo_gap_yoy_d3': {'inputs': ['taxexp', 'ncfo'], 'func': f40q_eqdgq_030_taxexp_to_ncfo_gap_yoy_d3}, 'f40q_eqdgq_031_deferred_tax_proxy_via_taxexp_lag_d3': {'inputs': ['taxexp', 'ebit'], 'func': f40q_eqdgq_031_deferred_tax_proxy_via_taxexp_lag_d3}, 'f40q_eqdgq_032_tax_burden_minus_cash_tax_proxy_d3': {'inputs': ['taxexp', 'ncfo', 'ebit'], 'func': f40q_eqdgq_032_tax_burden_minus_cash_tax_proxy_d3}, 'f40q_eqdgq_033_negative_taxexp_q_count_8q_d3': {'inputs': ['taxexp'], 'func': f40q_eqdgq_033_negative_taxexp_q_count_8q_d3}, 'f40q_eqdgq_034_etr_zero_quarters_count_8q_d3': {'inputs': ['taxexp', 'ebit'], 'func': f40q_eqdgq_034_etr_zero_quarters_count_8q_d3}, 'f40q_eqdgq_035_pretax_minus_aftertax_growth_gap_d3': {'inputs': ['ebit', 'netinc'], 'func': f40q_eqdgq_035_pretax_minus_aftertax_growth_gap_d3}, 'f40q_eqdgq_036_below_line_q_minus_8q_avg_d3': {'inputs': ['netinc', 'opinc'], 'func': f40q_eqdgq_036_below_line_q_minus_8q_avg_d3}, 'f40q_eqdgq_037_tax_to_revenue_zscore_8q_d3': {'inputs': ['taxexp', 'revenue'], 'func': f40q_eqdgq_037_tax_to_revenue_zscore_8q_d3}, 'f40q_eqdgq_038_pretax_income_minus_ebit_to_revenue_d3': {'inputs': ['ebit', 'intexp', 'revenue'], 'func': f40q_eqdgq_038_pretax_income_minus_ebit_to_revenue_d3}, 'f40q_eqdgq_039_below_line_growth_yoy_d3': {'inputs': ['netinc', 'opinc'], 'func': f40q_eqdgq_039_below_line_growth_yoy_d3}, 'f40q_eqdgq_040_extraordinary_charge_proxy_via_belowline_zscore_8q_d3': {'inputs': ['netinc', 'opinc'], 'func': f40q_eqdgq_040_extraordinary_charge_proxy_via_belowline_zscore_8q_d3}, 'f40q_eqdgq_041_netinc_minus_ncfo_to_revenue_ttm_d3': {'inputs': ['netinc', 'ncfo', 'revenue'], 'func': f40q_eqdgq_041_netinc_minus_ncfo_to_revenue_ttm_d3}, 'f40q_eqdgq_042_netinc_minus_fcf_to_revenue_ttm_d3': {'inputs': ['netinc', 'fcf', 'revenue'], 'func': f40q_eqdgq_042_netinc_minus_fcf_to_revenue_ttm_d3}, 'f40q_eqdgq_043_ebitda_minus_ncfo_to_revenue_d3': {'inputs': ['ebitda', 'ncfo', 'revenue'], 'func': f40q_eqdgq_043_ebitda_minus_ncfo_to_revenue_d3}, 'f40q_eqdgq_044_ebit_minus_ncfo_to_revenue_d3': {'inputs': ['ebit', 'ncfo', 'revenue'], 'func': f40q_eqdgq_044_ebit_minus_ncfo_to_revenue_d3}, 'f40q_eqdgq_045_opinc_minus_ncfo_to_revenue_d3': {'inputs': ['opinc', 'ncfo', 'revenue'], 'func': f40q_eqdgq_045_opinc_minus_ncfo_to_revenue_d3}, 'f40q_eqdgq_046_gap_zscore_netinc_minus_ncfo_12q_d3': {'inputs': ['netinc', 'ncfo', 'assets'], 'func': f40q_eqdgq_046_gap_zscore_netinc_minus_ncfo_12q_d3}, 'f40q_eqdgq_047_gap_zscore_netinc_minus_fcf_12q_d3': {'inputs': ['netinc', 'fcf', 'assets'], 'func': f40q_eqdgq_047_gap_zscore_netinc_minus_fcf_12q_d3}, 'f40q_eqdgq_048_cash_conversion_ratio_8q_min_d3': {'inputs': ['ncfo', 'netinc'], 'func': f40q_eqdgq_048_cash_conversion_ratio_8q_min_d3}, 'f40q_eqdgq_049_cash_conversion_ratio_8q_max_d3': {'inputs': ['ncfo', 'netinc'], 'func': f40q_eqdgq_049_cash_conversion_ratio_8q_max_d3}, 'f40q_eqdgq_050_cash_conversion_dispersion_8q_d3': {'inputs': ['ncfo', 'netinc'], 'func': f40q_eqdgq_050_cash_conversion_dispersion_8q_d3}, 'f40q_eqdgq_051_fcf_to_netinc_zscore_12q_d3': {'inputs': ['fcf', 'netinc'], 'func': f40q_eqdgq_051_fcf_to_netinc_zscore_12q_d3}, 'f40q_eqdgq_052_ebitda_to_ncfo_ratio_ttm_d3': {'inputs': ['ebitda', 'ncfo'], 'func': f40q_eqdgq_052_ebitda_to_ncfo_ratio_ttm_d3}, 'f40q_eqdgq_053_persistent_earnings_cash_gap_4q_d3': {'inputs': ['netinc', 'ncfo'], 'func': f40q_eqdgq_053_persistent_earnings_cash_gap_4q_d3}, 'f40q_eqdgq_054_earnings_cash_gap_yoy_change_d3': {'inputs': ['netinc', 'ncfo'], 'func': f40q_eqdgq_054_earnings_cash_gap_yoy_change_d3}, 'f40q_eqdgq_055_gap_inversion_sign_change_count_8q_d3': {'inputs': ['netinc', 'ncfo'], 'func': f40q_eqdgq_055_gap_inversion_sign_change_count_8q_d3}, 'f40q_eqdgq_056_quality_score_ncfo_to_netinc_minus_long_avg_d3': {'inputs': ['ncfo', 'netinc'], 'func': f40q_eqdgq_056_quality_score_ncfo_to_netinc_minus_long_avg_d3}, 'f40q_eqdgq_057_earnings_quality_collapse_q_to_4q_avg_d3': {'inputs': ['ncfo', 'netinc'], 'func': f40q_eqdgq_057_earnings_quality_collapse_q_to_4q_avg_d3}, 'f40q_eqdgq_058_negative_cash_conversion_q_count_8q_d3': {'inputs': ['ncfo', 'netinc'], 'func': f40q_eqdgq_058_negative_cash_conversion_q_count_8q_d3}, 'f40q_eqdgq_059_fcf_minus_netinc_dispersion_12q_d3': {'inputs': ['fcf', 'netinc'], 'func': f40q_eqdgq_059_fcf_minus_netinc_dispersion_12q_d3}, 'f40q_eqdgq_060_cash_quality_consistency_score_12q_d3': {'inputs': ['ncfo', 'netinc'], 'func': f40q_eqdgq_060_cash_quality_consistency_score_12q_d3}, 'f40q_eqdgq_061_depamor_to_revenue_zscore_8q_d3': {'inputs': ['depamor', 'revenue'], 'func': f40q_eqdgq_061_depamor_to_revenue_zscore_8q_d3}, 'f40q_eqdgq_062_depamor_to_assets_zscore_8q_d3': {'inputs': ['depamor', 'assets'], 'func': f40q_eqdgq_062_depamor_to_assets_zscore_8q_d3}, 'f40q_eqdgq_063_depamor_minus_capex_to_revenue_d3': {'inputs': ['depamor', 'capex', 'revenue'], 'func': f40q_eqdgq_063_depamor_minus_capex_to_revenue_d3}, 'f40q_eqdgq_064_capex_minus_depamor_persistence_12q_d3': {'inputs': ['capex', 'depamor'], 'func': f40q_eqdgq_064_capex_minus_depamor_persistence_12q_d3}, 'f40q_eqdgq_065_depamor_yoy_pct_d3': {'inputs': ['depamor'], 'func': f40q_eqdgq_065_depamor_yoy_pct_d3}, 'f40q_eqdgq_066_depamor_qoq_pct_d3': {'inputs': ['depamor'], 'func': f40q_eqdgq_066_depamor_qoq_pct_d3}, 'f40q_eqdgq_067_depamor_share_of_ebitda_minus_ebit_d3': {'inputs': ['depamor', 'ebitda', 'ebit'], 'func': f40q_eqdgq_067_depamor_share_of_ebitda_minus_ebit_d3}, 'f40q_eqdgq_068_depamor_to_ppe_ratio_d3': {'inputs': ['depamor', 'ppnenet'], 'func': f40q_eqdgq_068_depamor_to_ppe_ratio_d3}, 'f40q_eqdgq_069_depamor_to_ppe_zscore_12q_d3': {'inputs': ['depamor', 'ppnenet'], 'func': f40q_eqdgq_069_depamor_to_ppe_zscore_12q_d3}, 'f40q_eqdgq_070_depamor_to_intangibles_ratio_d3': {'inputs': ['depamor', 'intangibles'], 'func': f40q_eqdgq_070_depamor_to_intangibles_ratio_d3}, 'f40q_eqdgq_071_capex_to_depamor_ratio_yoy_d3': {'inputs': ['capex', 'depamor'], 'func': f40q_eqdgq_071_capex_to_depamor_ratio_yoy_d3}, 'f40q_eqdgq_072_underinvestment_proxy_d3': {'inputs': ['capex', 'depamor', 'assets'], 'func': f40q_eqdgq_072_underinvestment_proxy_d3}, 'f40q_eqdgq_073_overinvestment_proxy_d3': {'inputs': ['capex', 'depamor', 'assets'], 'func': f40q_eqdgq_073_overinvestment_proxy_d3}, 'f40q_eqdgq_074_depamor_minus_ebitda_gap_volatility_8q_d3': {'inputs': ['depamor', 'ebitda'], 'func': f40q_eqdgq_074_depamor_minus_ebitda_gap_volatility_8q_d3}, 'f40q_eqdgq_075_depamor_consistency_zscore_12q_d3': {'inputs': ['depamor', 'revenue'], 'func': f40q_eqdgq_075_depamor_consistency_zscore_12q_d3}}