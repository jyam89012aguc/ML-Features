"""cash_burn_snapshot d3 features 001-075 — order-3 difference of corresponding base features.

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

def f13_cbsp_001_signed_log_fcf_ttm_d3(fcf):
    return _signed_log_abs(_ttm(fcf)).diff().diff().diff()

def f13_cbsp_002_fcf_to_assets_ttm_d3(fcf, assets):
    return _safe_div(_ttm(fcf), assets).diff().diff().diff()

def f13_cbsp_003_fcf_q_to_assets_d3(fcf, assets):
    return _safe_div(fcf * 4.0, assets).diff().diff().diff()

def f13_cbsp_004_fcf_q_to_revenue_d3(fcf, revenue):
    return _safe_div(fcf, revenue).diff().diff().diff()

def f13_cbsp_005_ocf_to_assets_ttm_d3(ncfo, assets):
    return _safe_div(_ttm(ncfo), assets).diff().diff().diff()

def f13_cbsp_006_ocf_to_equity_ttm_d3(ncfo, equity):
    return _safe_div(_ttm(ncfo), equity).diff().diff().diff()

def f13_cbsp_007_signed_log_ncfo_ttm_d3(ncfo):
    return _signed_log_abs(_ttm(ncfo)).diff().diff().diff()

def f13_cbsp_008_capex_to_ocf_ratio_d3(capex, ncfo):
    return _safe_div(_ttm(capex).abs(), _ttm(ncfo).abs()).diff().diff().diff()

def f13_cbsp_009_fcf_to_ocf_ratio_d3(fcf, ncfo):
    return _safe_div(_ttm(fcf), _ttm(ncfo).abs()).diff().diff().diff()

def f13_cbsp_010_ocf_to_netinc_ratio_d3(ncfo, netinc):
    return _safe_div(_ttm(ncfo), _ttm(netinc).abs()).diff().diff().diff()

def f13_cbsp_011_burn_intensity_to_assets_d3(fcf, assets):
    return (-_safe_div(_ttm(fcf).clip(upper=0).abs(), assets)).diff().diff().diff()

def f13_cbsp_012_ncfo_to_equity_proxy_d3(ncfo, equity):
    return _safe_div(_ttm(ncfo), equity.abs()).diff().diff().diff()

def f13_cbsp_013_growth_capex_to_assets_d3(capex, depamor, assets):
    return _safe_div(_ttm(capex).abs() - _ttm(depamor), assets).diff().diff().diff()

def f13_cbsp_014_discretionary_cash_to_revenue_d3(ncfo, capex, intexp, revenue):
    return _safe_div(_ttm(ncfo) - _ttm(capex).abs() - _ttm(intexp).abs(), _ttm(revenue).abs()).diff().diff().diff()

def f13_cbsp_015_fcf_q_share_of_4q_d3(fcf):
    return _safe_div(fcf, _ttm(fcf).abs()).diff().diff().diff()

def f13_cbsp_016_cash_to_equity_d3(cashneq, equity):
    return _safe_div(cashneq, equity.abs()).diff().diff().diff()

def f13_cbsp_017_cash_to_assets_d3(cashneq, assets):
    return _safe_div(cashneq, assets).diff().diff().diff()

def f13_cbsp_018_cash_to_currentassets_d3(cashneq, assetsc):
    return _safe_div(cashneq, assetsc).diff().diff().diff()

def f13_cbsp_019_cash_to_currentliabilities_d3(cashneq, liabilitiesc):
    return _safe_div(cashneq, liabilitiesc).diff().diff().diff()

def f13_cbsp_020_cash_to_debt_d3(cashneq, debt):
    return _safe_div(cashneq, debt).diff().diff().diff()

def f13_cbsp_021_cash_to_debt_current_d3(cashneq, debtc):
    return _safe_div(cashneq, debtc).diff().diff().diff()

def f13_cbsp_022_quick_ratio_d3(cashneq, receivables, liabilitiesc):
    return _safe_div(cashneq + receivables, liabilitiesc).diff().diff().diff()

def f13_cbsp_023_current_ratio_d3(assetsc, liabilitiesc):
    return _safe_div(assetsc, liabilitiesc).diff().diff().diff()

def f13_cbsp_024_workingcapital_to_revenue_ttm_d3(workingcapital, revenue):
    return _safe_div(workingcapital, _ttm(revenue)).diff().diff().diff()

def f13_cbsp_025_workingcapital_to_assets_d3(workingcapital, assets):
    return _safe_div(workingcapital, assets).diff().diff().diff()

def f13_cbsp_026_cash_runway_q_from_fcf_d3(cashneq, fcf):
    burn = (-_ttm(fcf) / 4.0).clip(lower=1e-06)
    return _safe_div(cashneq, burn).clip(upper=40.0).diff().diff().diff()

def f13_cbsp_027_cash_runway_q_from_ocf_d3(cashneq, ncfo):
    burn = (-_ttm(ncfo) / 4.0).clip(lower=1e-06)
    return _safe_div(cashneq, burn).clip(upper=40.0).diff().diff().diff()

def f13_cbsp_028_net_cash_to_equity_d3(cashneq, debt, equity):
    return _safe_div(cashneq - debt, equity.abs()).diff().diff().diff()

def f13_cbsp_029_liquid_assets_to_q_burn_d3(cashneq, receivables, fcf):
    burn = (-_ttm(fcf) / 4.0).clip(lower=1e-06)
    return _safe_div(cashneq + receivables, burn).clip(upper=40.0).diff().diff().diff()

def f13_cbsp_030_net_cash_log_abs_d3(cashneq, debt):
    return _signed_log_abs(cashneq - debt).diff().diff().diff()

def f13_cbsp_031_net_cash_to_assets_d3(cashneq, debt, assets):
    return _safe_div(cashneq - debt, assets).diff().diff().diff()

def f13_cbsp_032_cash_zscore_8q_d3(cashneq):
    return _rolling_zscore(cashneq, 8, 3).diff().diff().diff()

def f13_cbsp_033_cash_qoq_pct_d3(cashneq):
    return _qoq_pct(cashneq).diff().diff().diff()

def f13_cbsp_034_cash_yoy_pct_d3(cashneq):
    return _yoy_pct(cashneq).diff().diff().diff()

def f13_cbsp_035_cash_to_revenue_ttm_d3(cashneq, revenue):
    return _safe_div(cashneq, _ttm(revenue)).diff().diff().diff()

def f13_cbsp_036_cash_minus_currentliabilities_to_assets_d3(cashneq, liabilitiesc, assets):
    return _safe_div(cashneq - liabilitiesc, assets).diff().diff().diff()

def f13_cbsp_037_cash_to_4q_burn_rate_d3(cashneq, fcf):
    burn4 = _ttm(fcf).clip(upper=-1e-06).abs()
    return _safe_div(cashneq, burn4).clip(upper=40.0).diff().diff().diff()

def f13_cbsp_038_cash_to_8q_burn_rate_d3(cashneq, fcf):
    burn8 = fcf.rolling(8, min_periods=4).sum().clip(upper=-1e-06).abs()
    return _safe_div(cashneq, burn8).clip(upper=40.0).diff().diff().diff()

def f13_cbsp_039_cash_share_of_currentassets_d3(cashneq, assetsc):
    return _safe_div(cashneq, assetsc).diff().diff().diff()

def f13_cbsp_040_liquidity_composite_d3(cashneq, receivables, liabilitiesc):
    return _safe_div(cashneq + receivables, liabilitiesc).diff().diff().diff()

def f13_cbsp_041_capex_to_revenue_ttm_d3(capex, revenue):
    return _safe_div(_ttm(capex).abs(), _ttm(revenue)).diff().diff().diff()

def f13_cbsp_042_capex_to_assets_d3(capex, assets):
    return _safe_div(_ttm(capex).abs(), assets).diff().diff().diff()

def f13_cbsp_043_capex_to_ppe_d3(capex, ppnenet):
    return _safe_div(_ttm(capex).abs(), ppnenet).diff().diff().diff()

def f13_cbsp_044_capex_to_depamor_d3(capex, depamor):
    return _safe_div(_ttm(capex).abs(), _ttm(depamor)).diff().diff().diff()

def f13_cbsp_045_capex_yoy_pct_d3(capex):
    return _yoy_pct(_ttm(capex).abs()).diff().diff().diff()

def f13_cbsp_046_capex_qoq_pct_d3(capex):
    return _qoq_pct(capex.abs()).diff().diff().diff()

def f13_cbsp_047_capex_to_ocf_ttm_d3(capex, ncfo):
    return _safe_div(_ttm(capex).abs(), _ttm(ncfo).abs()).diff().diff().diff()

def f13_cbsp_048_capex_intensity_zscore_8q_d3(capex, assets):
    return _rolling_zscore(_safe_div(_ttm(capex).abs(), assets), 8, 3).diff().diff().diff()

def f13_cbsp_049_capex_q_minus_4q_avg_to_4q_avg_d3(capex):
    m = capex.abs().rolling(4, min_periods=2).mean()
    return _safe_div(capex.abs() - m, m).diff().diff().diff()

def f13_cbsp_050_growth_capex_proxy_d3(capex, depamor):
    return (_ttm(capex).abs() - _ttm(depamor)).diff().diff().diff()

def f13_cbsp_051_growth_capex_to_assets_d3(capex, depamor, assets):
    return _safe_div(_ttm(capex).abs() - _ttm(depamor), assets).diff().diff().diff()

def f13_cbsp_052_growth_capex_to_revenue_d3(capex, depamor, revenue):
    return _safe_div(_ttm(capex).abs() - _ttm(depamor), _ttm(revenue)).diff().diff().diff()

def f13_cbsp_053_ncfi_to_assets_d3(ncfi, assets):
    return _safe_div(_ttm(ncfi), assets).diff().diff().diff()

def f13_cbsp_054_ncfi_to_revenue_ttm_d3(ncfi, revenue):
    return _safe_div(_ttm(ncfi), _ttm(revenue)).diff().diff().diff()

def f13_cbsp_055_ncfi_qoq_change_d3(ncfi):
    return ncfi.diff().diff().diff().diff()

def f13_cbsp_056_capex_minus_ocf_to_assets_d3(capex, ncfo, assets):
    return _safe_div(_ttm(capex).abs() - _ttm(ncfo), assets).diff().diff().diff()

def f13_cbsp_057_ncfi_share_of_total_outflows_d3(ncfi, ncfo, ncff):
    total = ncfi.abs() + ncfo.abs() + ncff.abs()
    return _safe_div(ncfi.abs(), total).diff().diff().diff()

def f13_cbsp_058_capex_consistency_8q_d3(capex, assets):
    r = _safe_div(_ttm(capex).abs(), assets)
    return r.rolling(8, min_periods=3).std().diff().diff().diff()

def f13_cbsp_059_capex_to_invcap_d3(capex, equity, debt):
    return _safe_div(_ttm(capex).abs(), equity + debt).diff().diff().diff()

def f13_cbsp_060_growth_capex_yoy_d3(capex, depamor):
    return _yoy(_ttm(capex).abs() - _ttm(depamor)).diff().diff().diff()

def f13_cbsp_061_workingcapital_qoq_change_d3(workingcapital):
    return workingcapital.diff().diff().diff().diff()

def f13_cbsp_062_workingcapital_qoq_change_to_assets_d3(workingcapital, assets):
    return _safe_div(workingcapital.diff(), assets).diff().diff().diff()

def f13_cbsp_063_workingcapital_yoy_change_d3(workingcapital):
    return _yoy(workingcapital).diff().diff().diff()

def f13_cbsp_064_delta_receivables_to_revenue_d3(receivables, revenue):
    return _safe_div(receivables.diff(), revenue.abs()).diff().diff().diff()

def f13_cbsp_065_delta_inventory_to_revenue_d3(inventory, revenue):
    return _safe_div(inventory.diff(), revenue.abs()).diff().diff().diff()

def f13_cbsp_066_delta_payables_to_revenue_d3(payables, revenue):
    return _safe_div(payables.diff(), revenue.abs()).diff().diff().diff()

def f13_cbsp_067_workingcapital_change_to_ocf_d3(workingcapital, ncfo):
    return _safe_div(workingcapital.diff(), ncfo.abs()).diff().diff().diff()

def f13_cbsp_068_wc_swing_8q_std_d3(workingcapital):
    return workingcapital.diff().rolling(8, min_periods=3).std().diff().diff().diff()

def f13_cbsp_069_wc_cumulative_4q_change_to_assets_d3(workingcapital, assets):
    return _safe_div(workingcapital.diff().rolling(4, min_periods=2).sum(), assets).diff().diff().diff()

def f13_cbsp_070_delta_wc_minus_delta_revenue_to_assets_d3(workingcapital, revenue, assets):
    return _safe_div(workingcapital.diff() - revenue.diff(), assets).diff().diff().diff()

def f13_cbsp_071_delta_receivables_share_of_ocf_d3(receivables, ncfo):
    return _safe_div(receivables.diff(), ncfo.abs()).diff().diff().diff()

def f13_cbsp_072_delta_inventory_share_of_ocf_d3(inventory, ncfo):
    return _safe_div(inventory.diff(), ncfo.abs()).diff().diff().diff()

def f13_cbsp_073_delta_deferredrev_to_revenue_d3(deferredrev, revenue):
    return _safe_div(deferredrev.diff(), revenue.abs()).diff().diff().diff()

def f13_cbsp_074_cash_drain_q_count_8q_d3(cashneq):
    return (cashneq.diff() < 0).rolling(8, min_periods=3).sum().diff().diff().diff()

def f13_cbsp_075_delta_currentassets_minus_delta_currentliabs_to_assets_d3(assetsc, liabilitiesc, assets):
    return _safe_div(assetsc.diff() - liabilitiesc.diff(), assets).diff().diff().diff()
CASH_BURN_SNAPSHOT_D3_REGISTRY_001_075 = {'f13_cbsp_001_signed_log_fcf_ttm_d3': {'inputs': ['fcf'], 'func': f13_cbsp_001_signed_log_fcf_ttm_d3}, 'f13_cbsp_002_fcf_to_assets_ttm_d3': {'inputs': ['fcf', 'assets'], 'func': f13_cbsp_002_fcf_to_assets_ttm_d3}, 'f13_cbsp_003_fcf_q_to_assets_d3': {'inputs': ['fcf', 'assets'], 'func': f13_cbsp_003_fcf_q_to_assets_d3}, 'f13_cbsp_004_fcf_q_to_revenue_d3': {'inputs': ['fcf', 'revenue'], 'func': f13_cbsp_004_fcf_q_to_revenue_d3}, 'f13_cbsp_005_ocf_to_assets_ttm_d3': {'inputs': ['ncfo', 'assets'], 'func': f13_cbsp_005_ocf_to_assets_ttm_d3}, 'f13_cbsp_006_ocf_to_equity_ttm_d3': {'inputs': ['ncfo', 'equity'], 'func': f13_cbsp_006_ocf_to_equity_ttm_d3}, 'f13_cbsp_007_signed_log_ncfo_ttm_d3': {'inputs': ['ncfo'], 'func': f13_cbsp_007_signed_log_ncfo_ttm_d3}, 'f13_cbsp_008_capex_to_ocf_ratio_d3': {'inputs': ['capex', 'ncfo'], 'func': f13_cbsp_008_capex_to_ocf_ratio_d3}, 'f13_cbsp_009_fcf_to_ocf_ratio_d3': {'inputs': ['fcf', 'ncfo'], 'func': f13_cbsp_009_fcf_to_ocf_ratio_d3}, 'f13_cbsp_010_ocf_to_netinc_ratio_d3': {'inputs': ['ncfo', 'netinc'], 'func': f13_cbsp_010_ocf_to_netinc_ratio_d3}, 'f13_cbsp_011_burn_intensity_to_assets_d3': {'inputs': ['fcf', 'assets'], 'func': f13_cbsp_011_burn_intensity_to_assets_d3}, 'f13_cbsp_012_ncfo_to_equity_proxy_d3': {'inputs': ['ncfo', 'equity'], 'func': f13_cbsp_012_ncfo_to_equity_proxy_d3}, 'f13_cbsp_013_growth_capex_to_assets_d3': {'inputs': ['capex', 'depamor', 'assets'], 'func': f13_cbsp_013_growth_capex_to_assets_d3}, 'f13_cbsp_014_discretionary_cash_to_revenue_d3': {'inputs': ['ncfo', 'capex', 'intexp', 'revenue'], 'func': f13_cbsp_014_discretionary_cash_to_revenue_d3}, 'f13_cbsp_015_fcf_q_share_of_4q_d3': {'inputs': ['fcf'], 'func': f13_cbsp_015_fcf_q_share_of_4q_d3}, 'f13_cbsp_016_cash_to_equity_d3': {'inputs': ['cashneq', 'equity'], 'func': f13_cbsp_016_cash_to_equity_d3}, 'f13_cbsp_017_cash_to_assets_d3': {'inputs': ['cashneq', 'assets'], 'func': f13_cbsp_017_cash_to_assets_d3}, 'f13_cbsp_018_cash_to_currentassets_d3': {'inputs': ['cashneq', 'assetsc'], 'func': f13_cbsp_018_cash_to_currentassets_d3}, 'f13_cbsp_019_cash_to_currentliabilities_d3': {'inputs': ['cashneq', 'liabilitiesc'], 'func': f13_cbsp_019_cash_to_currentliabilities_d3}, 'f13_cbsp_020_cash_to_debt_d3': {'inputs': ['cashneq', 'debt'], 'func': f13_cbsp_020_cash_to_debt_d3}, 'f13_cbsp_021_cash_to_debt_current_d3': {'inputs': ['cashneq', 'debtc'], 'func': f13_cbsp_021_cash_to_debt_current_d3}, 'f13_cbsp_022_quick_ratio_d3': {'inputs': ['cashneq', 'receivables', 'liabilitiesc'], 'func': f13_cbsp_022_quick_ratio_d3}, 'f13_cbsp_023_current_ratio_d3': {'inputs': ['assetsc', 'liabilitiesc'], 'func': f13_cbsp_023_current_ratio_d3}, 'f13_cbsp_024_workingcapital_to_revenue_ttm_d3': {'inputs': ['workingcapital', 'revenue'], 'func': f13_cbsp_024_workingcapital_to_revenue_ttm_d3}, 'f13_cbsp_025_workingcapital_to_assets_d3': {'inputs': ['workingcapital', 'assets'], 'func': f13_cbsp_025_workingcapital_to_assets_d3}, 'f13_cbsp_026_cash_runway_q_from_fcf_d3': {'inputs': ['cashneq', 'fcf'], 'func': f13_cbsp_026_cash_runway_q_from_fcf_d3}, 'f13_cbsp_027_cash_runway_q_from_ocf_d3': {'inputs': ['cashneq', 'ncfo'], 'func': f13_cbsp_027_cash_runway_q_from_ocf_d3}, 'f13_cbsp_028_net_cash_to_equity_d3': {'inputs': ['cashneq', 'debt', 'equity'], 'func': f13_cbsp_028_net_cash_to_equity_d3}, 'f13_cbsp_029_liquid_assets_to_q_burn_d3': {'inputs': ['cashneq', 'receivables', 'fcf'], 'func': f13_cbsp_029_liquid_assets_to_q_burn_d3}, 'f13_cbsp_030_net_cash_log_abs_d3': {'inputs': ['cashneq', 'debt'], 'func': f13_cbsp_030_net_cash_log_abs_d3}, 'f13_cbsp_031_net_cash_to_assets_d3': {'inputs': ['cashneq', 'debt', 'assets'], 'func': f13_cbsp_031_net_cash_to_assets_d3}, 'f13_cbsp_032_cash_zscore_8q_d3': {'inputs': ['cashneq'], 'func': f13_cbsp_032_cash_zscore_8q_d3}, 'f13_cbsp_033_cash_qoq_pct_d3': {'inputs': ['cashneq'], 'func': f13_cbsp_033_cash_qoq_pct_d3}, 'f13_cbsp_034_cash_yoy_pct_d3': {'inputs': ['cashneq'], 'func': f13_cbsp_034_cash_yoy_pct_d3}, 'f13_cbsp_035_cash_to_revenue_ttm_d3': {'inputs': ['cashneq', 'revenue'], 'func': f13_cbsp_035_cash_to_revenue_ttm_d3}, 'f13_cbsp_036_cash_minus_currentliabilities_to_assets_d3': {'inputs': ['cashneq', 'liabilitiesc', 'assets'], 'func': f13_cbsp_036_cash_minus_currentliabilities_to_assets_d3}, 'f13_cbsp_037_cash_to_4q_burn_rate_d3': {'inputs': ['cashneq', 'fcf'], 'func': f13_cbsp_037_cash_to_4q_burn_rate_d3}, 'f13_cbsp_038_cash_to_8q_burn_rate_d3': {'inputs': ['cashneq', 'fcf'], 'func': f13_cbsp_038_cash_to_8q_burn_rate_d3}, 'f13_cbsp_039_cash_share_of_currentassets_d3': {'inputs': ['cashneq', 'assetsc'], 'func': f13_cbsp_039_cash_share_of_currentassets_d3}, 'f13_cbsp_040_liquidity_composite_d3': {'inputs': ['cashneq', 'receivables', 'liabilitiesc'], 'func': f13_cbsp_040_liquidity_composite_d3}, 'f13_cbsp_041_capex_to_revenue_ttm_d3': {'inputs': ['capex', 'revenue'], 'func': f13_cbsp_041_capex_to_revenue_ttm_d3}, 'f13_cbsp_042_capex_to_assets_d3': {'inputs': ['capex', 'assets'], 'func': f13_cbsp_042_capex_to_assets_d3}, 'f13_cbsp_043_capex_to_ppe_d3': {'inputs': ['capex', 'ppnenet'], 'func': f13_cbsp_043_capex_to_ppe_d3}, 'f13_cbsp_044_capex_to_depamor_d3': {'inputs': ['capex', 'depamor'], 'func': f13_cbsp_044_capex_to_depamor_d3}, 'f13_cbsp_045_capex_yoy_pct_d3': {'inputs': ['capex'], 'func': f13_cbsp_045_capex_yoy_pct_d3}, 'f13_cbsp_046_capex_qoq_pct_d3': {'inputs': ['capex'], 'func': f13_cbsp_046_capex_qoq_pct_d3}, 'f13_cbsp_047_capex_to_ocf_ttm_d3': {'inputs': ['capex', 'ncfo'], 'func': f13_cbsp_047_capex_to_ocf_ttm_d3}, 'f13_cbsp_048_capex_intensity_zscore_8q_d3': {'inputs': ['capex', 'assets'], 'func': f13_cbsp_048_capex_intensity_zscore_8q_d3}, 'f13_cbsp_049_capex_q_minus_4q_avg_to_4q_avg_d3': {'inputs': ['capex'], 'func': f13_cbsp_049_capex_q_minus_4q_avg_to_4q_avg_d3}, 'f13_cbsp_050_growth_capex_proxy_d3': {'inputs': ['capex', 'depamor'], 'func': f13_cbsp_050_growth_capex_proxy_d3}, 'f13_cbsp_051_growth_capex_to_assets_d3': {'inputs': ['capex', 'depamor', 'assets'], 'func': f13_cbsp_051_growth_capex_to_assets_d3}, 'f13_cbsp_052_growth_capex_to_revenue_d3': {'inputs': ['capex', 'depamor', 'revenue'], 'func': f13_cbsp_052_growth_capex_to_revenue_d3}, 'f13_cbsp_053_ncfi_to_assets_d3': {'inputs': ['ncfi', 'assets'], 'func': f13_cbsp_053_ncfi_to_assets_d3}, 'f13_cbsp_054_ncfi_to_revenue_ttm_d3': {'inputs': ['ncfi', 'revenue'], 'func': f13_cbsp_054_ncfi_to_revenue_ttm_d3}, 'f13_cbsp_055_ncfi_qoq_change_d3': {'inputs': ['ncfi'], 'func': f13_cbsp_055_ncfi_qoq_change_d3}, 'f13_cbsp_056_capex_minus_ocf_to_assets_d3': {'inputs': ['capex', 'ncfo', 'assets'], 'func': f13_cbsp_056_capex_minus_ocf_to_assets_d3}, 'f13_cbsp_057_ncfi_share_of_total_outflows_d3': {'inputs': ['ncfi', 'ncfo', 'ncff'], 'func': f13_cbsp_057_ncfi_share_of_total_outflows_d3}, 'f13_cbsp_058_capex_consistency_8q_d3': {'inputs': ['capex', 'assets'], 'func': f13_cbsp_058_capex_consistency_8q_d3}, 'f13_cbsp_059_capex_to_invcap_d3': {'inputs': ['capex', 'equity', 'debt'], 'func': f13_cbsp_059_capex_to_invcap_d3}, 'f13_cbsp_060_growth_capex_yoy_d3': {'inputs': ['capex', 'depamor'], 'func': f13_cbsp_060_growth_capex_yoy_d3}, 'f13_cbsp_061_workingcapital_qoq_change_d3': {'inputs': ['workingcapital'], 'func': f13_cbsp_061_workingcapital_qoq_change_d3}, 'f13_cbsp_062_workingcapital_qoq_change_to_assets_d3': {'inputs': ['workingcapital', 'assets'], 'func': f13_cbsp_062_workingcapital_qoq_change_to_assets_d3}, 'f13_cbsp_063_workingcapital_yoy_change_d3': {'inputs': ['workingcapital'], 'func': f13_cbsp_063_workingcapital_yoy_change_d3}, 'f13_cbsp_064_delta_receivables_to_revenue_d3': {'inputs': ['receivables', 'revenue'], 'func': f13_cbsp_064_delta_receivables_to_revenue_d3}, 'f13_cbsp_065_delta_inventory_to_revenue_d3': {'inputs': ['inventory', 'revenue'], 'func': f13_cbsp_065_delta_inventory_to_revenue_d3}, 'f13_cbsp_066_delta_payables_to_revenue_d3': {'inputs': ['payables', 'revenue'], 'func': f13_cbsp_066_delta_payables_to_revenue_d3}, 'f13_cbsp_067_workingcapital_change_to_ocf_d3': {'inputs': ['workingcapital', 'ncfo'], 'func': f13_cbsp_067_workingcapital_change_to_ocf_d3}, 'f13_cbsp_068_wc_swing_8q_std_d3': {'inputs': ['workingcapital'], 'func': f13_cbsp_068_wc_swing_8q_std_d3}, 'f13_cbsp_069_wc_cumulative_4q_change_to_assets_d3': {'inputs': ['workingcapital', 'assets'], 'func': f13_cbsp_069_wc_cumulative_4q_change_to_assets_d3}, 'f13_cbsp_070_delta_wc_minus_delta_revenue_to_assets_d3': {'inputs': ['workingcapital', 'revenue', 'assets'], 'func': f13_cbsp_070_delta_wc_minus_delta_revenue_to_assets_d3}, 'f13_cbsp_071_delta_receivables_share_of_ocf_d3': {'inputs': ['receivables', 'ncfo'], 'func': f13_cbsp_071_delta_receivables_share_of_ocf_d3}, 'f13_cbsp_072_delta_inventory_share_of_ocf_d3': {'inputs': ['inventory', 'ncfo'], 'func': f13_cbsp_072_delta_inventory_share_of_ocf_d3}, 'f13_cbsp_073_delta_deferredrev_to_revenue_d3': {'inputs': ['deferredrev', 'revenue'], 'func': f13_cbsp_073_delta_deferredrev_to_revenue_d3}, 'f13_cbsp_074_cash_drain_q_count_8q_d3': {'inputs': ['cashneq'], 'func': f13_cbsp_074_cash_drain_q_count_8q_d3}, 'f13_cbsp_075_delta_currentassets_minus_delta_currentliabs_to_assets_d3': {'inputs': ['assetsc', 'liabilitiesc', 'assets'], 'func': f13_cbsp_075_delta_currentassets_minus_delta_currentliabs_to_assets_d3}}