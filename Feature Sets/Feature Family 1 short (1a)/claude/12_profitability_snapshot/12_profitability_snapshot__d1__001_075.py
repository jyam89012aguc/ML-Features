"""profitability_snapshot d1 features 001-075 — order-1 difference of corresponding base features.

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

def _safe_log(s, eps=1e-12):
    if isinstance(s, pd.Series):
        return np.log(s.where(s > eps, np.nan))
    arr = np.where(s > eps, s, np.nan)
    return np.log(arr)

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

def f12_psnp_001_gross_margin_ttm_d1(gp, revenue):
    return _safe_div(_ttm(gp), _ttm(revenue)).diff()

def f12_psnp_002_operating_margin_ttm_d1(opinc, revenue):
    return _safe_div(_ttm(opinc), _ttm(revenue)).diff()

def f12_psnp_003_ebitda_margin_ttm_d1(ebitda, revenue):
    return _safe_div(_ttm(ebitda), _ttm(revenue)).diff()

def f12_psnp_004_ebit_margin_ttm_d1(ebit, revenue):
    return _safe_div(_ttm(ebit), _ttm(revenue)).diff()

def f12_psnp_005_net_margin_ttm_d1(netinc, revenue):
    return _safe_div(_ttm(netinc), _ttm(revenue)).diff()

def f12_psnp_006_fcf_margin_ttm_d1(fcf, revenue):
    return _safe_div(_ttm(fcf), _ttm(revenue)).diff()

def f12_psnp_007_ocf_margin_ttm_d1(ncfo, revenue):
    return _safe_div(_ttm(ncfo), _ttm(revenue)).diff()

def f12_psnp_008_pretax_margin_ttm_d1(ebit, intexp, revenue):
    return _safe_div(_ttm(ebit) - _ttm(intexp), _ttm(revenue)).diff()

def f12_psnp_009_nopat_margin_proxy_d1(ebit, taxexp, revenue):
    eff_tax = _safe_div(_ttm(taxexp), _ttm(ebit).abs())
    nopat = _ttm(ebit) * (1.0 - eff_tax.clip(lower=0.0, upper=0.6))
    return _safe_div(nopat, _ttm(revenue)).diff()

def f12_psnp_010_sgna_margin_ttm_d1(sgna, revenue):
    return (-_safe_div(_ttm(sgna), _ttm(revenue))).diff()

def f12_psnp_011_rnd_margin_ttm_d1(rnd, revenue):
    return (-_safe_div(_ttm(rnd), _ttm(revenue))).diff()

def f12_psnp_012_capex_margin_ttm_d1(capex, revenue):
    return (-_safe_div(_ttm(capex).abs(), _ttm(revenue))).diff()

def f12_psnp_013_tax_margin_ttm_d1(taxexp, revenue):
    return (-_safe_div(_ttm(taxexp), _ttm(revenue))).diff()

def f12_psnp_014_interest_margin_ttm_d1(intexp, revenue):
    return (-_safe_div(_ttm(intexp), _ttm(revenue))).diff()

def f12_psnp_015_depamor_margin_ttm_d1(depamor, revenue):
    return (-_safe_div(_ttm(depamor), _ttm(revenue))).diff()

def f12_psnp_016_opex_margin_ttm_d1(opex, revenue):
    return (-_safe_div(_ttm(opex), _ttm(revenue))).diff()

def f12_psnp_017_gross_minus_sgna_margin_ttm_d1(gp, sgna, revenue):
    return _safe_div(_ttm(gp) - _ttm(sgna), _ttm(revenue)).diff()

def f12_psnp_018_ebitda_minus_capex_margin_ttm_d1(ebitda, capex, revenue):
    return _safe_div(_ttm(ebitda) - _ttm(capex).abs(), _ttm(revenue)).diff()

def f12_psnp_019_revenue_minus_cogs_minus_rnd_margin_d1(gp, rnd, revenue):
    return _safe_div(_ttm(gp) - _ttm(rnd), _ttm(revenue)).diff()

def f12_psnp_020_cash_pretax_proxy_margin_d1(ncfo, taxexp, revenue):
    return _safe_div(_ttm(ncfo) + _ttm(taxexp), _ttm(revenue)).diff()

def f12_psnp_021_roa_ttm_d1(netinc, assets):
    return _safe_div(_ttm(netinc), assets).diff()

def f12_psnp_022_roa_ebit_ttm_d1(ebit, assets):
    return _safe_div(_ttm(ebit), assets).diff()

def f12_psnp_023_roe_ttm_d1(netinc, equity):
    return _safe_div(_ttm(netinc), equity).diff()

def f12_psnp_024_roe_ebitda_d1(ebitda, equity):
    return _safe_div(_ttm(ebitda), equity).diff()

def f12_psnp_025_roic_pretax_d1(ebit, equity, debt):
    return _safe_div(_ttm(ebit), equity + debt).diff()

def f12_psnp_026_roic_nopat_proxy_d1(ebit, taxexp, equity, debt):
    eff_tax = _safe_div(_ttm(taxexp), _ttm(ebit).abs()).clip(lower=0.0, upper=0.6)
    nopat = _ttm(ebit) * (1.0 - eff_tax)
    return _safe_div(nopat, equity + debt).diff()

def f12_psnp_027_return_on_tangible_assets_d1(netinc, assets, intangibles):
    return _safe_div(_ttm(netinc), assets - intangibles).diff()

def f12_psnp_028_return_on_tangible_equity_d1(netinc, equity, intangibles):
    return _safe_div(_ttm(netinc), equity - intangibles).diff()

def f12_psnp_029_roic_minus_cash_d1(ebit, equity, debt, cashneq):
    return _safe_div(_ttm(ebit), equity + debt - cashneq).diff()

def f12_psnp_030_roa_q_annualized_d1(netinc, assets):
    return _safe_div(netinc * 4.0, assets).diff()

def f12_psnp_031_roa_q_minus_4q_avg_d1(netinc, assets):
    r = _safe_div(_ttm(netinc), assets)
    return (r - r.rolling(4, min_periods=2).mean()).diff()

def f12_psnp_032_cash_roa_d1(ncfo, assets):
    return _safe_div(_ttm(ncfo), assets).diff()

def f12_psnp_033_cash_roe_d1(ncfo, equity):
    return _safe_div(_ttm(ncfo), equity).diff()

def f12_psnp_034_cash_roic_d1(ncfo, equity, debt):
    return _safe_div(_ttm(ncfo), equity + debt).diff()

def f12_psnp_035_fcf_roa_d1(fcf, assets):
    return _safe_div(_ttm(fcf), assets).diff()

def f12_psnp_036_fcf_roe_d1(fcf, equity):
    return _safe_div(_ttm(fcf), equity).diff()

def f12_psnp_037_return_on_retained_earnings_d1(netinc, retearn):
    return _safe_div(_ttm(netinc), retearn.abs()).diff()

def f12_psnp_038_return_on_workingcapital_d1(opinc, workingcapital):
    return _safe_div(_ttm(opinc), workingcapital.abs()).diff()

def f12_psnp_039_return_on_ppe_d1(opinc, ppnenet):
    return _safe_div(_ttm(opinc), ppnenet).diff()

def f12_psnp_040_return_on_avg_4q_assets_d1(netinc, assets):
    return _safe_div(_ttm(netinc), assets.rolling(4, min_periods=2).mean()).diff()

def f12_psnp_041_accruals_to_assets_d1(netinc, ncfo, assets):
    return _safe_div(_ttm(netinc) - _ttm(ncfo), assets).diff()

def f12_psnp_042_accruals_to_revenue_d1(netinc, ncfo, revenue):
    return _safe_div(_ttm(netinc) - _ttm(ncfo), _ttm(revenue).abs()).diff()

def f12_psnp_043_earnings_quality_ncfo_to_netinc_d1(ncfo, netinc):
    return _safe_div(_ttm(ncfo), _ttm(netinc).abs()).diff()

def f12_psnp_044_fcf_to_netinc_d1(fcf, netinc):
    return _safe_div(_ttm(fcf), _ttm(netinc).abs()).diff()

def f12_psnp_045_ebitda_to_netinc_d1(ebitda, netinc):
    return _safe_div(_ttm(ebitda), _ttm(netinc).abs()).diff()

def f12_psnp_046_smoothed_ncfo_to_netinc_8q_d1(ncfo, netinc):
    return _safe_div(ncfo.rolling(8, min_periods=3).mean(), netinc.rolling(8, min_periods=3).mean().abs()).diff()

def f12_psnp_047_bs_accruals_share_of_avg_assets_d1(workingcapital, assets):
    return _safe_div(workingcapital.diff(), assets.rolling(4, min_periods=2).mean()).diff()

def f12_psnp_048_cf_accruals_share_of_avg_assets_d1(netinc, ncfo, assets):
    return _safe_div(_ttm(netinc) - _ttm(ncfo), assets.rolling(4, min_periods=2).mean()).diff()

def f12_psnp_049_accrual_share_volatility_8q_d1(netinc, ncfo, revenue):
    a = _safe_div(netinc - ncfo, revenue.abs())
    return a.rolling(8, min_periods=3).std().diff()

def f12_psnp_050_earnings_to_cash_gap_zscore_12q_d1(netinc, ncfo):
    return _rolling_zscore(_ttm(netinc) - _ttm(ncfo), 12, 4).diff()

def f12_psnp_051_netinc_minus_ebitda_share_d1(netinc, ebitda, revenue):
    return _safe_div(_ttm(netinc) - _ttm(ebitda), _ttm(revenue).abs()).diff()

def f12_psnp_052_ebitda_minus_ebit_to_revenue_d1(ebitda, ebit, revenue):
    return _safe_div(_ttm(ebitda) - _ttm(ebit), _ttm(revenue).abs()).diff()

def f12_psnp_053_opinc_minus_netinc_to_revenue_d1(opinc, netinc, revenue):
    return _safe_div(_ttm(opinc) - _ttm(netinc), _ttm(revenue).abs()).diff()

def f12_psnp_054_nonop_income_share_d1(netinc, opinc, taxexp):
    eff_tax = _safe_div(_ttm(taxexp), _ttm(opinc).abs()).clip(lower=0.0, upper=0.6)
    op_aftertax = _ttm(opinc) * (1.0 - eff_tax)
    return _safe_div(_ttm(netinc) - op_aftertax, _ttm(netinc).abs()).diff()

def f12_psnp_055_ebit_minus_ncfo_to_assets_d1(ebit, ncfo, assets):
    return _safe_div(_ttm(ebit) - _ttm(ncfo), assets).diff()

def f12_psnp_056_netinc_stability_8q_d1(netinc):
    return (-_safe_div(_ttm(netinc).rolling(8, min_periods=3).std(), _ttm(netinc).rolling(8, min_periods=3).mean().abs())).diff()

def f12_psnp_057_ncfo_stability_8q_d1(ncfo):
    return (-_safe_div(_ttm(ncfo).rolling(8, min_periods=3).std(), _ttm(ncfo).rolling(8, min_periods=3).mean().abs())).diff()

def f12_psnp_058_opcf_volatility_8q_d1(ncfo):
    return ncfo.rolling(8, min_periods=3).std().diff()

def f12_psnp_059_ebitda_minus_ncfo_to_assets_d1(ebitda, ncfo, assets):
    return _safe_div(_ttm(ebitda) - _ttm(ncfo), assets).diff()

def f12_psnp_060_accrual_share_q_minus_8q_mean_d1(netinc, ncfo, revenue):
    a = _safe_div(netinc - ncfo, revenue.abs())
    return (a - a.rolling(8, min_periods=3).mean()).diff()

def f12_psnp_061_roa_zscore_8q_d1(netinc, assets):
    return _rolling_zscore(_safe_div(_ttm(netinc), assets), 8, 3).diff()

def f12_psnp_062_roe_zscore_8q_d1(netinc, equity):
    return _rolling_zscore(_safe_div(_ttm(netinc), equity), 8, 3).diff()

def f12_psnp_063_roic_zscore_8q_d1(ebit, equity, debt):
    return _rolling_zscore(_safe_div(_ttm(ebit), equity + debt), 8, 3).diff()

def f12_psnp_064_gross_margin_zscore_8q_d1(gp, revenue):
    return _rolling_zscore(_safe_div(_ttm(gp), _ttm(revenue)), 8, 3).diff()

def f12_psnp_065_operating_margin_zscore_8q_d1(opinc, revenue):
    return _rolling_zscore(_safe_div(_ttm(opinc), _ttm(revenue)), 8, 3).diff()

def f12_psnp_066_ebitda_margin_zscore_8q_d1(ebitda, revenue):
    return _rolling_zscore(_safe_div(_ttm(ebitda), _ttm(revenue)), 8, 3).diff()

def f12_psnp_067_net_margin_zscore_8q_d1(netinc, revenue):
    return _rolling_zscore(_safe_div(_ttm(netinc), _ttm(revenue)), 8, 3).diff()

def f12_psnp_068_fcf_margin_zscore_12q_d1(fcf, revenue):
    return _rolling_zscore(_safe_div(_ttm(fcf), _ttm(revenue)), 12, 4).diff()

def f12_psnp_069_ocf_margin_zscore_8q_d1(ncfo, revenue):
    return _rolling_zscore(_safe_div(_ttm(ncfo), _ttm(revenue)), 8, 3).diff()

def f12_psnp_070_roa_minus_8q_max_d1(netinc, assets):
    r = _safe_div(_ttm(netinc), assets)
    return (r - r.rolling(8, min_periods=3).max()).diff()

def f12_psnp_071_gross_margin_minus_8q_max_d1(gp, revenue):
    m = _safe_div(_ttm(gp), _ttm(revenue))
    return (m - m.rolling(8, min_periods=3).max()).diff()

def f12_psnp_072_ebitda_margin_minus_8q_max_d1(ebitda, revenue):
    m = _safe_div(_ttm(ebitda), _ttm(revenue))
    return (m - m.rolling(8, min_periods=3).max()).diff()

def f12_psnp_073_net_margin_minus_8q_max_d1(netinc, revenue):
    m = _safe_div(_ttm(netinc), _ttm(revenue))
    return (m - m.rolling(8, min_periods=3).max()).diff()

def f12_psnp_074_operating_margin_q_vs_4q_avg_d1(opinc, revenue):
    return (_safe_div(opinc, revenue) - _safe_div(_ttm(opinc), _ttm(revenue))).diff()

def f12_psnp_075_roa_q_vs_4q_avg_d1(netinc, assets):
    return (_safe_div(netinc * 4.0, assets) - _safe_div(_ttm(netinc), assets)).diff()
PROFITABILITY_SNAPSHOT_D1_REGISTRY_001_075 = {'f12_psnp_001_gross_margin_ttm_d1': {'inputs': ['gp', 'revenue'], 'func': f12_psnp_001_gross_margin_ttm_d1}, 'f12_psnp_002_operating_margin_ttm_d1': {'inputs': ['opinc', 'revenue'], 'func': f12_psnp_002_operating_margin_ttm_d1}, 'f12_psnp_003_ebitda_margin_ttm_d1': {'inputs': ['ebitda', 'revenue'], 'func': f12_psnp_003_ebitda_margin_ttm_d1}, 'f12_psnp_004_ebit_margin_ttm_d1': {'inputs': ['ebit', 'revenue'], 'func': f12_psnp_004_ebit_margin_ttm_d1}, 'f12_psnp_005_net_margin_ttm_d1': {'inputs': ['netinc', 'revenue'], 'func': f12_psnp_005_net_margin_ttm_d1}, 'f12_psnp_006_fcf_margin_ttm_d1': {'inputs': ['fcf', 'revenue'], 'func': f12_psnp_006_fcf_margin_ttm_d1}, 'f12_psnp_007_ocf_margin_ttm_d1': {'inputs': ['ncfo', 'revenue'], 'func': f12_psnp_007_ocf_margin_ttm_d1}, 'f12_psnp_008_pretax_margin_ttm_d1': {'inputs': ['ebit', 'intexp', 'revenue'], 'func': f12_psnp_008_pretax_margin_ttm_d1}, 'f12_psnp_009_nopat_margin_proxy_d1': {'inputs': ['ebit', 'taxexp', 'revenue'], 'func': f12_psnp_009_nopat_margin_proxy_d1}, 'f12_psnp_010_sgna_margin_ttm_d1': {'inputs': ['sgna', 'revenue'], 'func': f12_psnp_010_sgna_margin_ttm_d1}, 'f12_psnp_011_rnd_margin_ttm_d1': {'inputs': ['rnd', 'revenue'], 'func': f12_psnp_011_rnd_margin_ttm_d1}, 'f12_psnp_012_capex_margin_ttm_d1': {'inputs': ['capex', 'revenue'], 'func': f12_psnp_012_capex_margin_ttm_d1}, 'f12_psnp_013_tax_margin_ttm_d1': {'inputs': ['taxexp', 'revenue'], 'func': f12_psnp_013_tax_margin_ttm_d1}, 'f12_psnp_014_interest_margin_ttm_d1': {'inputs': ['intexp', 'revenue'], 'func': f12_psnp_014_interest_margin_ttm_d1}, 'f12_psnp_015_depamor_margin_ttm_d1': {'inputs': ['depamor', 'revenue'], 'func': f12_psnp_015_depamor_margin_ttm_d1}, 'f12_psnp_016_opex_margin_ttm_d1': {'inputs': ['opex', 'revenue'], 'func': f12_psnp_016_opex_margin_ttm_d1}, 'f12_psnp_017_gross_minus_sgna_margin_ttm_d1': {'inputs': ['gp', 'sgna', 'revenue'], 'func': f12_psnp_017_gross_minus_sgna_margin_ttm_d1}, 'f12_psnp_018_ebitda_minus_capex_margin_ttm_d1': {'inputs': ['ebitda', 'capex', 'revenue'], 'func': f12_psnp_018_ebitda_minus_capex_margin_ttm_d1}, 'f12_psnp_019_revenue_minus_cogs_minus_rnd_margin_d1': {'inputs': ['gp', 'rnd', 'revenue'], 'func': f12_psnp_019_revenue_minus_cogs_minus_rnd_margin_d1}, 'f12_psnp_020_cash_pretax_proxy_margin_d1': {'inputs': ['ncfo', 'taxexp', 'revenue'], 'func': f12_psnp_020_cash_pretax_proxy_margin_d1}, 'f12_psnp_021_roa_ttm_d1': {'inputs': ['netinc', 'assets'], 'func': f12_psnp_021_roa_ttm_d1}, 'f12_psnp_022_roa_ebit_ttm_d1': {'inputs': ['ebit', 'assets'], 'func': f12_psnp_022_roa_ebit_ttm_d1}, 'f12_psnp_023_roe_ttm_d1': {'inputs': ['netinc', 'equity'], 'func': f12_psnp_023_roe_ttm_d1}, 'f12_psnp_024_roe_ebitda_d1': {'inputs': ['ebitda', 'equity'], 'func': f12_psnp_024_roe_ebitda_d1}, 'f12_psnp_025_roic_pretax_d1': {'inputs': ['ebit', 'equity', 'debt'], 'func': f12_psnp_025_roic_pretax_d1}, 'f12_psnp_026_roic_nopat_proxy_d1': {'inputs': ['ebit', 'taxexp', 'equity', 'debt'], 'func': f12_psnp_026_roic_nopat_proxy_d1}, 'f12_psnp_027_return_on_tangible_assets_d1': {'inputs': ['netinc', 'assets', 'intangibles'], 'func': f12_psnp_027_return_on_tangible_assets_d1}, 'f12_psnp_028_return_on_tangible_equity_d1': {'inputs': ['netinc', 'equity', 'intangibles'], 'func': f12_psnp_028_return_on_tangible_equity_d1}, 'f12_psnp_029_roic_minus_cash_d1': {'inputs': ['ebit', 'equity', 'debt', 'cashneq'], 'func': f12_psnp_029_roic_minus_cash_d1}, 'f12_psnp_030_roa_q_annualized_d1': {'inputs': ['netinc', 'assets'], 'func': f12_psnp_030_roa_q_annualized_d1}, 'f12_psnp_031_roa_q_minus_4q_avg_d1': {'inputs': ['netinc', 'assets'], 'func': f12_psnp_031_roa_q_minus_4q_avg_d1}, 'f12_psnp_032_cash_roa_d1': {'inputs': ['ncfo', 'assets'], 'func': f12_psnp_032_cash_roa_d1}, 'f12_psnp_033_cash_roe_d1': {'inputs': ['ncfo', 'equity'], 'func': f12_psnp_033_cash_roe_d1}, 'f12_psnp_034_cash_roic_d1': {'inputs': ['ncfo', 'equity', 'debt'], 'func': f12_psnp_034_cash_roic_d1}, 'f12_psnp_035_fcf_roa_d1': {'inputs': ['fcf', 'assets'], 'func': f12_psnp_035_fcf_roa_d1}, 'f12_psnp_036_fcf_roe_d1': {'inputs': ['fcf', 'equity'], 'func': f12_psnp_036_fcf_roe_d1}, 'f12_psnp_037_return_on_retained_earnings_d1': {'inputs': ['netinc', 'retearn'], 'func': f12_psnp_037_return_on_retained_earnings_d1}, 'f12_psnp_038_return_on_workingcapital_d1': {'inputs': ['opinc', 'workingcapital'], 'func': f12_psnp_038_return_on_workingcapital_d1}, 'f12_psnp_039_return_on_ppe_d1': {'inputs': ['opinc', 'ppnenet'], 'func': f12_psnp_039_return_on_ppe_d1}, 'f12_psnp_040_return_on_avg_4q_assets_d1': {'inputs': ['netinc', 'assets'], 'func': f12_psnp_040_return_on_avg_4q_assets_d1}, 'f12_psnp_041_accruals_to_assets_d1': {'inputs': ['netinc', 'ncfo', 'assets'], 'func': f12_psnp_041_accruals_to_assets_d1}, 'f12_psnp_042_accruals_to_revenue_d1': {'inputs': ['netinc', 'ncfo', 'revenue'], 'func': f12_psnp_042_accruals_to_revenue_d1}, 'f12_psnp_043_earnings_quality_ncfo_to_netinc_d1': {'inputs': ['ncfo', 'netinc'], 'func': f12_psnp_043_earnings_quality_ncfo_to_netinc_d1}, 'f12_psnp_044_fcf_to_netinc_d1': {'inputs': ['fcf', 'netinc'], 'func': f12_psnp_044_fcf_to_netinc_d1}, 'f12_psnp_045_ebitda_to_netinc_d1': {'inputs': ['ebitda', 'netinc'], 'func': f12_psnp_045_ebitda_to_netinc_d1}, 'f12_psnp_046_smoothed_ncfo_to_netinc_8q_d1': {'inputs': ['ncfo', 'netinc'], 'func': f12_psnp_046_smoothed_ncfo_to_netinc_8q_d1}, 'f12_psnp_047_bs_accruals_share_of_avg_assets_d1': {'inputs': ['workingcapital', 'assets'], 'func': f12_psnp_047_bs_accruals_share_of_avg_assets_d1}, 'f12_psnp_048_cf_accruals_share_of_avg_assets_d1': {'inputs': ['netinc', 'ncfo', 'assets'], 'func': f12_psnp_048_cf_accruals_share_of_avg_assets_d1}, 'f12_psnp_049_accrual_share_volatility_8q_d1': {'inputs': ['netinc', 'ncfo', 'revenue'], 'func': f12_psnp_049_accrual_share_volatility_8q_d1}, 'f12_psnp_050_earnings_to_cash_gap_zscore_12q_d1': {'inputs': ['netinc', 'ncfo'], 'func': f12_psnp_050_earnings_to_cash_gap_zscore_12q_d1}, 'f12_psnp_051_netinc_minus_ebitda_share_d1': {'inputs': ['netinc', 'ebitda', 'revenue'], 'func': f12_psnp_051_netinc_minus_ebitda_share_d1}, 'f12_psnp_052_ebitda_minus_ebit_to_revenue_d1': {'inputs': ['ebitda', 'ebit', 'revenue'], 'func': f12_psnp_052_ebitda_minus_ebit_to_revenue_d1}, 'f12_psnp_053_opinc_minus_netinc_to_revenue_d1': {'inputs': ['opinc', 'netinc', 'revenue'], 'func': f12_psnp_053_opinc_minus_netinc_to_revenue_d1}, 'f12_psnp_054_nonop_income_share_d1': {'inputs': ['netinc', 'opinc', 'taxexp'], 'func': f12_psnp_054_nonop_income_share_d1}, 'f12_psnp_055_ebit_minus_ncfo_to_assets_d1': {'inputs': ['ebit', 'ncfo', 'assets'], 'func': f12_psnp_055_ebit_minus_ncfo_to_assets_d1}, 'f12_psnp_056_netinc_stability_8q_d1': {'inputs': ['netinc'], 'func': f12_psnp_056_netinc_stability_8q_d1}, 'f12_psnp_057_ncfo_stability_8q_d1': {'inputs': ['ncfo'], 'func': f12_psnp_057_ncfo_stability_8q_d1}, 'f12_psnp_058_opcf_volatility_8q_d1': {'inputs': ['ncfo'], 'func': f12_psnp_058_opcf_volatility_8q_d1}, 'f12_psnp_059_ebitda_minus_ncfo_to_assets_d1': {'inputs': ['ebitda', 'ncfo', 'assets'], 'func': f12_psnp_059_ebitda_minus_ncfo_to_assets_d1}, 'f12_psnp_060_accrual_share_q_minus_8q_mean_d1': {'inputs': ['netinc', 'ncfo', 'revenue'], 'func': f12_psnp_060_accrual_share_q_minus_8q_mean_d1}, 'f12_psnp_061_roa_zscore_8q_d1': {'inputs': ['netinc', 'assets'], 'func': f12_psnp_061_roa_zscore_8q_d1}, 'f12_psnp_062_roe_zscore_8q_d1': {'inputs': ['netinc', 'equity'], 'func': f12_psnp_062_roe_zscore_8q_d1}, 'f12_psnp_063_roic_zscore_8q_d1': {'inputs': ['ebit', 'equity', 'debt'], 'func': f12_psnp_063_roic_zscore_8q_d1}, 'f12_psnp_064_gross_margin_zscore_8q_d1': {'inputs': ['gp', 'revenue'], 'func': f12_psnp_064_gross_margin_zscore_8q_d1}, 'f12_psnp_065_operating_margin_zscore_8q_d1': {'inputs': ['opinc', 'revenue'], 'func': f12_psnp_065_operating_margin_zscore_8q_d1}, 'f12_psnp_066_ebitda_margin_zscore_8q_d1': {'inputs': ['ebitda', 'revenue'], 'func': f12_psnp_066_ebitda_margin_zscore_8q_d1}, 'f12_psnp_067_net_margin_zscore_8q_d1': {'inputs': ['netinc', 'revenue'], 'func': f12_psnp_067_net_margin_zscore_8q_d1}, 'f12_psnp_068_fcf_margin_zscore_12q_d1': {'inputs': ['fcf', 'revenue'], 'func': f12_psnp_068_fcf_margin_zscore_12q_d1}, 'f12_psnp_069_ocf_margin_zscore_8q_d1': {'inputs': ['ncfo', 'revenue'], 'func': f12_psnp_069_ocf_margin_zscore_8q_d1}, 'f12_psnp_070_roa_minus_8q_max_d1': {'inputs': ['netinc', 'assets'], 'func': f12_psnp_070_roa_minus_8q_max_d1}, 'f12_psnp_071_gross_margin_minus_8q_max_d1': {'inputs': ['gp', 'revenue'], 'func': f12_psnp_071_gross_margin_minus_8q_max_d1}, 'f12_psnp_072_ebitda_margin_minus_8q_max_d1': {'inputs': ['ebitda', 'revenue'], 'func': f12_psnp_072_ebitda_margin_minus_8q_max_d1}, 'f12_psnp_073_net_margin_minus_8q_max_d1': {'inputs': ['netinc', 'revenue'], 'func': f12_psnp_073_net_margin_minus_8q_max_d1}, 'f12_psnp_074_operating_margin_q_vs_4q_avg_d1': {'inputs': ['opinc', 'revenue'], 'func': f12_psnp_074_operating_margin_q_vs_4q_avg_d1}, 'f12_psnp_075_roa_q_vs_4q_avg_d1': {'inputs': ['netinc', 'assets'], 'func': f12_psnp_075_roa_q_vs_4q_avg_d1}}