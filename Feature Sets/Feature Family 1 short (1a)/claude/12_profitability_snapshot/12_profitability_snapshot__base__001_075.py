"""profitability_snapshot base features 001-075 — Pipeline 1a-inverse short-side blowup family.

75 distinct hypotheses about profitability at the price peak (continued in __base__076_150.py).
Inputs: SF1 quarterly fundamentals. PIT-clean: right-anchored rolling, explicit min_periods,
no centered windows, no forward-looking shifts.
"""
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
    idx = num.index if hasattr(num, "index") else None
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


# ============================================================
#                    FEATURES 001-075
# ============================================================

# ---- Block A: margin levels (001-020) ----

def f12_psnp_001_gross_margin_ttm(gp, revenue):
    return _safe_div(_ttm(gp), _ttm(revenue))


def f12_psnp_002_operating_margin_ttm(opinc, revenue):
    return _safe_div(_ttm(opinc), _ttm(revenue))


def f12_psnp_003_ebitda_margin_ttm(ebitda, revenue):
    return _safe_div(_ttm(ebitda), _ttm(revenue))


def f12_psnp_004_ebit_margin_ttm(ebit, revenue):
    return _safe_div(_ttm(ebit), _ttm(revenue))


def f12_psnp_005_net_margin_ttm(netinc, revenue):
    return _safe_div(_ttm(netinc), _ttm(revenue))


def f12_psnp_006_fcf_margin_ttm(fcf, revenue):
    return _safe_div(_ttm(fcf), _ttm(revenue))


def f12_psnp_007_ocf_margin_ttm(ncfo, revenue):
    return _safe_div(_ttm(ncfo), _ttm(revenue))


def f12_psnp_008_pretax_margin_ttm(ebit, intexp, revenue):
    return _safe_div(_ttm(ebit) - _ttm(intexp), _ttm(revenue))


def f12_psnp_009_nopat_margin_proxy(ebit, taxexp, revenue):
    eff_tax = _safe_div(_ttm(taxexp), _ttm(ebit).abs())
    nopat = _ttm(ebit) * (1.0 - eff_tax.clip(lower=0.0, upper=0.6))
    return _safe_div(nopat, _ttm(revenue))


def f12_psnp_010_sgna_margin_ttm(sgna, revenue):
    return -_safe_div(_ttm(sgna), _ttm(revenue))


def f12_psnp_011_rnd_margin_ttm(rnd, revenue):
    return -_safe_div(_ttm(rnd), _ttm(revenue))


def f12_psnp_012_capex_margin_ttm(capex, revenue):
    return -_safe_div(_ttm(capex).abs(), _ttm(revenue))


def f12_psnp_013_tax_margin_ttm(taxexp, revenue):
    return -_safe_div(_ttm(taxexp), _ttm(revenue))


def f12_psnp_014_interest_margin_ttm(intexp, revenue):
    return -_safe_div(_ttm(intexp), _ttm(revenue))


def f12_psnp_015_depamor_margin_ttm(depamor, revenue):
    return -_safe_div(_ttm(depamor), _ttm(revenue))


def f12_psnp_016_opex_margin_ttm(opex, revenue):
    return -_safe_div(_ttm(opex), _ttm(revenue))


def f12_psnp_017_gross_minus_sgna_margin_ttm(gp, sgna, revenue):
    return _safe_div(_ttm(gp) - _ttm(sgna), _ttm(revenue))


def f12_psnp_018_ebitda_minus_capex_margin_ttm(ebitda, capex, revenue):
    return _safe_div(_ttm(ebitda) - _ttm(capex).abs(), _ttm(revenue))


def f12_psnp_019_revenue_minus_cogs_minus_rnd_margin(gp, rnd, revenue):
    return _safe_div(_ttm(gp) - _ttm(rnd), _ttm(revenue))


def f12_psnp_020_cash_pretax_proxy_margin(ncfo, taxexp, revenue):
    return _safe_div(_ttm(ncfo) + _ttm(taxexp), _ttm(revenue))


# ---- Block B: return on capital (021-040) ----

def f12_psnp_021_roa_ttm(netinc, assets):
    return _safe_div(_ttm(netinc), assets)


def f12_psnp_022_roa_ebit_ttm(ebit, assets):
    return _safe_div(_ttm(ebit), assets)


def f12_psnp_023_roe_ttm(netinc, equity):
    return _safe_div(_ttm(netinc), equity)


def f12_psnp_024_roe_ebitda(ebitda, equity):
    return _safe_div(_ttm(ebitda), equity)


def f12_psnp_025_roic_pretax(ebit, equity, debt):
    return _safe_div(_ttm(ebit), equity + debt)


def f12_psnp_026_roic_nopat_proxy(ebit, taxexp, equity, debt):
    eff_tax = _safe_div(_ttm(taxexp), _ttm(ebit).abs()).clip(lower=0.0, upper=0.6)
    nopat = _ttm(ebit) * (1.0 - eff_tax)
    return _safe_div(nopat, equity + debt)


def f12_psnp_027_return_on_tangible_assets(netinc, assets, intangibles):
    return _safe_div(_ttm(netinc), assets - intangibles)


def f12_psnp_028_return_on_tangible_equity(netinc, equity, intangibles):
    return _safe_div(_ttm(netinc), equity - intangibles)


def f12_psnp_029_roic_minus_cash(ebit, equity, debt, cashneq):
    return _safe_div(_ttm(ebit), equity + debt - cashneq)


def f12_psnp_030_roa_q_annualized(netinc, assets):
    return _safe_div(netinc * 4.0, assets)


def f12_psnp_031_roa_q_minus_4q_avg(netinc, assets):
    r = _safe_div(_ttm(netinc), assets)
    return r - r.rolling(4, min_periods=2).mean()


def f12_psnp_032_cash_roa(ncfo, assets):
    return _safe_div(_ttm(ncfo), assets)


def f12_psnp_033_cash_roe(ncfo, equity):
    return _safe_div(_ttm(ncfo), equity)


def f12_psnp_034_cash_roic(ncfo, equity, debt):
    return _safe_div(_ttm(ncfo), equity + debt)


def f12_psnp_035_fcf_roa(fcf, assets):
    return _safe_div(_ttm(fcf), assets)


def f12_psnp_036_fcf_roe(fcf, equity):
    return _safe_div(_ttm(fcf), equity)


def f12_psnp_037_return_on_retained_earnings(netinc, retearn):
    return _safe_div(_ttm(netinc), retearn.abs())


def f12_psnp_038_return_on_workingcapital(opinc, workingcapital):
    return _safe_div(_ttm(opinc), workingcapital.abs())


def f12_psnp_039_return_on_ppe(opinc, ppnenet):
    return _safe_div(_ttm(opinc), ppnenet)


def f12_psnp_040_return_on_avg_4q_assets(netinc, assets):
    return _safe_div(_ttm(netinc), assets.rolling(4, min_periods=2).mean())


# ---- Block C: earnings quality & accruals (041-060) ----

def f12_psnp_041_accruals_to_assets(netinc, ncfo, assets):
    return _safe_div(_ttm(netinc) - _ttm(ncfo), assets)


def f12_psnp_042_accruals_to_revenue(netinc, ncfo, revenue):
    return _safe_div(_ttm(netinc) - _ttm(ncfo), _ttm(revenue).abs())


def f12_psnp_043_earnings_quality_ncfo_to_netinc(ncfo, netinc):
    return _safe_div(_ttm(ncfo), _ttm(netinc).abs())


def f12_psnp_044_fcf_to_netinc(fcf, netinc):
    return _safe_div(_ttm(fcf), _ttm(netinc).abs())


def f12_psnp_045_ebitda_to_netinc(ebitda, netinc):
    return _safe_div(_ttm(ebitda), _ttm(netinc).abs())


def f12_psnp_046_smoothed_ncfo_to_netinc_8q(ncfo, netinc):
    return _safe_div(ncfo.rolling(8, min_periods=3).mean(), netinc.rolling(8, min_periods=3).mean().abs())


def f12_psnp_047_bs_accruals_share_of_avg_assets(workingcapital, assets):
    return _safe_div(workingcapital.diff(), assets.rolling(4, min_periods=2).mean())


def f12_psnp_048_cf_accruals_share_of_avg_assets(netinc, ncfo, assets):
    return _safe_div(_ttm(netinc) - _ttm(ncfo), assets.rolling(4, min_periods=2).mean())


def f12_psnp_049_accrual_share_volatility_8q(netinc, ncfo, revenue):
    a = _safe_div(netinc - ncfo, revenue.abs())
    return a.rolling(8, min_periods=3).std()


def f12_psnp_050_earnings_to_cash_gap_zscore_12q(netinc, ncfo):
    return _rolling_zscore(_ttm(netinc) - _ttm(ncfo), 12, 4)


def f12_psnp_051_netinc_minus_ebitda_share(netinc, ebitda, revenue):
    return _safe_div(_ttm(netinc) - _ttm(ebitda), _ttm(revenue).abs())


def f12_psnp_052_ebitda_minus_ebit_to_revenue(ebitda, ebit, revenue):
    return _safe_div(_ttm(ebitda) - _ttm(ebit), _ttm(revenue).abs())


def f12_psnp_053_opinc_minus_netinc_to_revenue(opinc, netinc, revenue):
    return _safe_div(_ttm(opinc) - _ttm(netinc), _ttm(revenue).abs())


def f12_psnp_054_nonop_income_share(netinc, opinc, taxexp):
    eff_tax = _safe_div(_ttm(taxexp), _ttm(opinc).abs()).clip(lower=0.0, upper=0.6)
    op_aftertax = _ttm(opinc) * (1.0 - eff_tax)
    return _safe_div(_ttm(netinc) - op_aftertax, _ttm(netinc).abs())


def f12_psnp_055_ebit_minus_ncfo_to_assets(ebit, ncfo, assets):
    return _safe_div(_ttm(ebit) - _ttm(ncfo), assets)


def f12_psnp_056_netinc_stability_8q(netinc):
    return -_safe_div(_ttm(netinc).rolling(8, min_periods=3).std(),
                       _ttm(netinc).rolling(8, min_periods=3).mean().abs())


def f12_psnp_057_ncfo_stability_8q(ncfo):
    return -_safe_div(_ttm(ncfo).rolling(8, min_periods=3).std(),
                       _ttm(ncfo).rolling(8, min_periods=3).mean().abs())


def f12_psnp_058_opcf_volatility_8q(ncfo):
    return ncfo.rolling(8, min_periods=3).std()


def f12_psnp_059_ebitda_minus_ncfo_to_assets(ebitda, ncfo, assets):
    return _safe_div(_ttm(ebitda) - _ttm(ncfo), assets)


def f12_psnp_060_accrual_share_q_minus_8q_mean(netinc, ncfo, revenue):
    a = _safe_div(netinc - ncfo, revenue.abs())
    return a - a.rolling(8, min_periods=3).mean()


# ---- Block D: returns vs history / regime (061-075) ----

def f12_psnp_061_roa_zscore_8q(netinc, assets):
    return _rolling_zscore(_safe_div(_ttm(netinc), assets), 8, 3)


def f12_psnp_062_roe_zscore_8q(netinc, equity):
    return _rolling_zscore(_safe_div(_ttm(netinc), equity), 8, 3)


def f12_psnp_063_roic_zscore_8q(ebit, equity, debt):
    return _rolling_zscore(_safe_div(_ttm(ebit), equity + debt), 8, 3)


def f12_psnp_064_gross_margin_zscore_8q(gp, revenue):
    return _rolling_zscore(_safe_div(_ttm(gp), _ttm(revenue)), 8, 3)


def f12_psnp_065_operating_margin_zscore_8q(opinc, revenue):
    return _rolling_zscore(_safe_div(_ttm(opinc), _ttm(revenue)), 8, 3)


def f12_psnp_066_ebitda_margin_zscore_8q(ebitda, revenue):
    return _rolling_zscore(_safe_div(_ttm(ebitda), _ttm(revenue)), 8, 3)


def f12_psnp_067_net_margin_zscore_8q(netinc, revenue):
    return _rolling_zscore(_safe_div(_ttm(netinc), _ttm(revenue)), 8, 3)


def f12_psnp_068_fcf_margin_zscore_12q(fcf, revenue):
    return _rolling_zscore(_safe_div(_ttm(fcf), _ttm(revenue)), 12, 4)


def f12_psnp_069_ocf_margin_zscore_8q(ncfo, revenue):
    return _rolling_zscore(_safe_div(_ttm(ncfo), _ttm(revenue)), 8, 3)


def f12_psnp_070_roa_minus_8q_max(netinc, assets):
    r = _safe_div(_ttm(netinc), assets)
    return r - r.rolling(8, min_periods=3).max()


def f12_psnp_071_gross_margin_minus_8q_max(gp, revenue):
    m = _safe_div(_ttm(gp), _ttm(revenue))
    return m - m.rolling(8, min_periods=3).max()


def f12_psnp_072_ebitda_margin_minus_8q_max(ebitda, revenue):
    m = _safe_div(_ttm(ebitda), _ttm(revenue))
    return m - m.rolling(8, min_periods=3).max()


def f12_psnp_073_net_margin_minus_8q_max(netinc, revenue):
    m = _safe_div(_ttm(netinc), _ttm(revenue))
    return m - m.rolling(8, min_periods=3).max()


def f12_psnp_074_operating_margin_q_vs_4q_avg(opinc, revenue):
    return _safe_div(opinc, revenue) - _safe_div(_ttm(opinc), _ttm(revenue))


def f12_psnp_075_roa_q_vs_4q_avg(netinc, assets):
    return _safe_div(netinc * 4.0, assets) - _safe_div(_ttm(netinc), assets)


# ============================================================
#                        REGISTRY
# ============================================================

PROFITABILITY_SNAPSHOT_BASE_REGISTRY_001_075 = {
    "f12_psnp_001_gross_margin_ttm": {"inputs": ["gp", "revenue"], "func": f12_psnp_001_gross_margin_ttm},
    "f12_psnp_002_operating_margin_ttm": {"inputs": ["opinc", "revenue"], "func": f12_psnp_002_operating_margin_ttm},
    "f12_psnp_003_ebitda_margin_ttm": {"inputs": ["ebitda", "revenue"], "func": f12_psnp_003_ebitda_margin_ttm},
    "f12_psnp_004_ebit_margin_ttm": {"inputs": ["ebit", "revenue"], "func": f12_psnp_004_ebit_margin_ttm},
    "f12_psnp_005_net_margin_ttm": {"inputs": ["netinc", "revenue"], "func": f12_psnp_005_net_margin_ttm},
    "f12_psnp_006_fcf_margin_ttm": {"inputs": ["fcf", "revenue"], "func": f12_psnp_006_fcf_margin_ttm},
    "f12_psnp_007_ocf_margin_ttm": {"inputs": ["ncfo", "revenue"], "func": f12_psnp_007_ocf_margin_ttm},
    "f12_psnp_008_pretax_margin_ttm": {"inputs": ["ebit", "intexp", "revenue"], "func": f12_psnp_008_pretax_margin_ttm},
    "f12_psnp_009_nopat_margin_proxy": {"inputs": ["ebit", "taxexp", "revenue"], "func": f12_psnp_009_nopat_margin_proxy},
    "f12_psnp_010_sgna_margin_ttm": {"inputs": ["sgna", "revenue"], "func": f12_psnp_010_sgna_margin_ttm},
    "f12_psnp_011_rnd_margin_ttm": {"inputs": ["rnd", "revenue"], "func": f12_psnp_011_rnd_margin_ttm},
    "f12_psnp_012_capex_margin_ttm": {"inputs": ["capex", "revenue"], "func": f12_psnp_012_capex_margin_ttm},
    "f12_psnp_013_tax_margin_ttm": {"inputs": ["taxexp", "revenue"], "func": f12_psnp_013_tax_margin_ttm},
    "f12_psnp_014_interest_margin_ttm": {"inputs": ["intexp", "revenue"], "func": f12_psnp_014_interest_margin_ttm},
    "f12_psnp_015_depamor_margin_ttm": {"inputs": ["depamor", "revenue"], "func": f12_psnp_015_depamor_margin_ttm},
    "f12_psnp_016_opex_margin_ttm": {"inputs": ["opex", "revenue"], "func": f12_psnp_016_opex_margin_ttm},
    "f12_psnp_017_gross_minus_sgna_margin_ttm": {"inputs": ["gp", "sgna", "revenue"], "func": f12_psnp_017_gross_minus_sgna_margin_ttm},
    "f12_psnp_018_ebitda_minus_capex_margin_ttm": {"inputs": ["ebitda", "capex", "revenue"], "func": f12_psnp_018_ebitda_minus_capex_margin_ttm},
    "f12_psnp_019_revenue_minus_cogs_minus_rnd_margin": {"inputs": ["gp", "rnd", "revenue"], "func": f12_psnp_019_revenue_minus_cogs_minus_rnd_margin},
    "f12_psnp_020_cash_pretax_proxy_margin": {"inputs": ["ncfo", "taxexp", "revenue"], "func": f12_psnp_020_cash_pretax_proxy_margin},
    "f12_psnp_021_roa_ttm": {"inputs": ["netinc", "assets"], "func": f12_psnp_021_roa_ttm},
    "f12_psnp_022_roa_ebit_ttm": {"inputs": ["ebit", "assets"], "func": f12_psnp_022_roa_ebit_ttm},
    "f12_psnp_023_roe_ttm": {"inputs": ["netinc", "equity"], "func": f12_psnp_023_roe_ttm},
    "f12_psnp_024_roe_ebitda": {"inputs": ["ebitda", "equity"], "func": f12_psnp_024_roe_ebitda},
    "f12_psnp_025_roic_pretax": {"inputs": ["ebit", "equity", "debt"], "func": f12_psnp_025_roic_pretax},
    "f12_psnp_026_roic_nopat_proxy": {"inputs": ["ebit", "taxexp", "equity", "debt"], "func": f12_psnp_026_roic_nopat_proxy},
    "f12_psnp_027_return_on_tangible_assets": {"inputs": ["netinc", "assets", "intangibles"], "func": f12_psnp_027_return_on_tangible_assets},
    "f12_psnp_028_return_on_tangible_equity": {"inputs": ["netinc", "equity", "intangibles"], "func": f12_psnp_028_return_on_tangible_equity},
    "f12_psnp_029_roic_minus_cash": {"inputs": ["ebit", "equity", "debt", "cashneq"], "func": f12_psnp_029_roic_minus_cash},
    "f12_psnp_030_roa_q_annualized": {"inputs": ["netinc", "assets"], "func": f12_psnp_030_roa_q_annualized},
    "f12_psnp_031_roa_q_minus_4q_avg": {"inputs": ["netinc", "assets"], "func": f12_psnp_031_roa_q_minus_4q_avg},
    "f12_psnp_032_cash_roa": {"inputs": ["ncfo", "assets"], "func": f12_psnp_032_cash_roa},
    "f12_psnp_033_cash_roe": {"inputs": ["ncfo", "equity"], "func": f12_psnp_033_cash_roe},
    "f12_psnp_034_cash_roic": {"inputs": ["ncfo", "equity", "debt"], "func": f12_psnp_034_cash_roic},
    "f12_psnp_035_fcf_roa": {"inputs": ["fcf", "assets"], "func": f12_psnp_035_fcf_roa},
    "f12_psnp_036_fcf_roe": {"inputs": ["fcf", "equity"], "func": f12_psnp_036_fcf_roe},
    "f12_psnp_037_return_on_retained_earnings": {"inputs": ["netinc", "retearn"], "func": f12_psnp_037_return_on_retained_earnings},
    "f12_psnp_038_return_on_workingcapital": {"inputs": ["opinc", "workingcapital"], "func": f12_psnp_038_return_on_workingcapital},
    "f12_psnp_039_return_on_ppe": {"inputs": ["opinc", "ppnenet"], "func": f12_psnp_039_return_on_ppe},
    "f12_psnp_040_return_on_avg_4q_assets": {"inputs": ["netinc", "assets"], "func": f12_psnp_040_return_on_avg_4q_assets},
    "f12_psnp_041_accruals_to_assets": {"inputs": ["netinc", "ncfo", "assets"], "func": f12_psnp_041_accruals_to_assets},
    "f12_psnp_042_accruals_to_revenue": {"inputs": ["netinc", "ncfo", "revenue"], "func": f12_psnp_042_accruals_to_revenue},
    "f12_psnp_043_earnings_quality_ncfo_to_netinc": {"inputs": ["ncfo", "netinc"], "func": f12_psnp_043_earnings_quality_ncfo_to_netinc},
    "f12_psnp_044_fcf_to_netinc": {"inputs": ["fcf", "netinc"], "func": f12_psnp_044_fcf_to_netinc},
    "f12_psnp_045_ebitda_to_netinc": {"inputs": ["ebitda", "netinc"], "func": f12_psnp_045_ebitda_to_netinc},
    "f12_psnp_046_smoothed_ncfo_to_netinc_8q": {"inputs": ["ncfo", "netinc"], "func": f12_psnp_046_smoothed_ncfo_to_netinc_8q},
    "f12_psnp_047_bs_accruals_share_of_avg_assets": {"inputs": ["workingcapital", "assets"], "func": f12_psnp_047_bs_accruals_share_of_avg_assets},
    "f12_psnp_048_cf_accruals_share_of_avg_assets": {"inputs": ["netinc", "ncfo", "assets"], "func": f12_psnp_048_cf_accruals_share_of_avg_assets},
    "f12_psnp_049_accrual_share_volatility_8q": {"inputs": ["netinc", "ncfo", "revenue"], "func": f12_psnp_049_accrual_share_volatility_8q},
    "f12_psnp_050_earnings_to_cash_gap_zscore_12q": {"inputs": ["netinc", "ncfo"], "func": f12_psnp_050_earnings_to_cash_gap_zscore_12q},
    "f12_psnp_051_netinc_minus_ebitda_share": {"inputs": ["netinc", "ebitda", "revenue"], "func": f12_psnp_051_netinc_minus_ebitda_share},
    "f12_psnp_052_ebitda_minus_ebit_to_revenue": {"inputs": ["ebitda", "ebit", "revenue"], "func": f12_psnp_052_ebitda_minus_ebit_to_revenue},
    "f12_psnp_053_opinc_minus_netinc_to_revenue": {"inputs": ["opinc", "netinc", "revenue"], "func": f12_psnp_053_opinc_minus_netinc_to_revenue},
    "f12_psnp_054_nonop_income_share": {"inputs": ["netinc", "opinc", "taxexp"], "func": f12_psnp_054_nonop_income_share},
    "f12_psnp_055_ebit_minus_ncfo_to_assets": {"inputs": ["ebit", "ncfo", "assets"], "func": f12_psnp_055_ebit_minus_ncfo_to_assets},
    "f12_psnp_056_netinc_stability_8q": {"inputs": ["netinc"], "func": f12_psnp_056_netinc_stability_8q},
    "f12_psnp_057_ncfo_stability_8q": {"inputs": ["ncfo"], "func": f12_psnp_057_ncfo_stability_8q},
    "f12_psnp_058_opcf_volatility_8q": {"inputs": ["ncfo"], "func": f12_psnp_058_opcf_volatility_8q},
    "f12_psnp_059_ebitda_minus_ncfo_to_assets": {"inputs": ["ebitda", "ncfo", "assets"], "func": f12_psnp_059_ebitda_minus_ncfo_to_assets},
    "f12_psnp_060_accrual_share_q_minus_8q_mean": {"inputs": ["netinc", "ncfo", "revenue"], "func": f12_psnp_060_accrual_share_q_minus_8q_mean},
    "f12_psnp_061_roa_zscore_8q": {"inputs": ["netinc", "assets"], "func": f12_psnp_061_roa_zscore_8q},
    "f12_psnp_062_roe_zscore_8q": {"inputs": ["netinc", "equity"], "func": f12_psnp_062_roe_zscore_8q},
    "f12_psnp_063_roic_zscore_8q": {"inputs": ["ebit", "equity", "debt"], "func": f12_psnp_063_roic_zscore_8q},
    "f12_psnp_064_gross_margin_zscore_8q": {"inputs": ["gp", "revenue"], "func": f12_psnp_064_gross_margin_zscore_8q},
    "f12_psnp_065_operating_margin_zscore_8q": {"inputs": ["opinc", "revenue"], "func": f12_psnp_065_operating_margin_zscore_8q},
    "f12_psnp_066_ebitda_margin_zscore_8q": {"inputs": ["ebitda", "revenue"], "func": f12_psnp_066_ebitda_margin_zscore_8q},
    "f12_psnp_067_net_margin_zscore_8q": {"inputs": ["netinc", "revenue"], "func": f12_psnp_067_net_margin_zscore_8q},
    "f12_psnp_068_fcf_margin_zscore_12q": {"inputs": ["fcf", "revenue"], "func": f12_psnp_068_fcf_margin_zscore_12q},
    "f12_psnp_069_ocf_margin_zscore_8q": {"inputs": ["ncfo", "revenue"], "func": f12_psnp_069_ocf_margin_zscore_8q},
    "f12_psnp_070_roa_minus_8q_max": {"inputs": ["netinc", "assets"], "func": f12_psnp_070_roa_minus_8q_max},
    "f12_psnp_071_gross_margin_minus_8q_max": {"inputs": ["gp", "revenue"], "func": f12_psnp_071_gross_margin_minus_8q_max},
    "f12_psnp_072_ebitda_margin_minus_8q_max": {"inputs": ["ebitda", "revenue"], "func": f12_psnp_072_ebitda_margin_minus_8q_max},
    "f12_psnp_073_net_margin_minus_8q_max": {"inputs": ["netinc", "revenue"], "func": f12_psnp_073_net_margin_minus_8q_max},
    "f12_psnp_074_operating_margin_q_vs_4q_avg": {"inputs": ["opinc", "revenue"], "func": f12_psnp_074_operating_margin_q_vs_4q_avg},
    "f12_psnp_075_roa_q_vs_4q_avg": {"inputs": ["netinc", "assets"], "func": f12_psnp_075_roa_q_vs_4q_avg},
}
