"""revenue_quality_level d3 features 001-075 — order-3 difference of corresponding base features.

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

def _safe_log(s, eps=1e-12):
    if isinstance(s, pd.Series):
        return np.log(s.where(s > eps, np.nan))
    arr = np.where(s > eps, s, np.nan)
    return np.log(arr)

def _safe_log_abs(s, eps=1e-12):
    if isinstance(s, pd.Series):
        a = s.abs()
        return np.log(a.where(a > eps, np.nan))
    a = np.abs(s)
    return np.log(np.where(a > eps, a, np.nan))

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

def _qoq(s):
    return s.diff()

def _qoq_pct(s):
    return _safe_div(s.diff(), s.shift(1).abs())

def f11_rqlv_001_log_revenue_ttm_d3(revenue):
    return _safe_log(_ttm(revenue)).diff().diff().diff()

def f11_rqlv_002_revenue_ttm_to_assets_d3(revenue, assets):
    return _safe_div(_ttm(revenue), assets).diff().diff().diff()

def f11_rqlv_003_revenue_ttm_to_equity_d3(revenue, equity):
    return _safe_div(_ttm(revenue), equity).diff().diff().diff()

def f11_rqlv_004_revenue_ttm_to_invested_capital_d3(revenue, equity, debt):
    return _safe_div(_ttm(revenue), equity + debt).diff().diff().diff()

def f11_rqlv_005_revenue_ttm_to_workingcapital_d3(revenue, workingcapital):
    return _safe_div(_ttm(revenue), workingcapital.abs()).diff().diff().diff()

def f11_rqlv_006_revenue_ttm_to_ppnenet_d3(revenue, ppnenet):
    return _safe_div(_ttm(revenue), ppnenet).diff().diff().diff()

def f11_rqlv_007_revenue_ttm_to_intangibles_d3(revenue, intangibles):
    return _safe_div(_ttm(revenue), intangibles).diff().diff().diff()

def f11_rqlv_008_revenue_ttm_to_opex_d3(revenue, opex):
    return _safe_div(_ttm(revenue), _ttm(opex)).diff().diff().diff()

def f11_rqlv_009_revenue_per_share_ttm_d3(revenue, shareswadil):
    return _safe_div(_ttm(revenue), shareswadil).diff().diff().diff()

def f11_rqlv_010_revenue_per_basic_share_ttm_d3(revenue, shareswa):
    return _safe_div(_ttm(revenue), shareswa).diff().diff().diff()

def f11_rqlv_011_revenue_q_annualized_to_assets_d3(revenue, assets):
    return _safe_div(revenue * 4.0, assets).diff().diff().diff()

def f11_rqlv_012_revenue_q_annualized_minus_ttm_to_ttm_d3(revenue):
    rev_ttm = _ttm(revenue)
    return _safe_div(revenue * 4.0 - rev_ttm, rev_ttm.abs()).diff().diff().diff()

def f11_rqlv_013_latest_q_share_of_ttm_d3(revenue):
    return _safe_div(revenue, _ttm(revenue)).diff().diff().diff()

def f11_rqlv_014_revenue_4q_concentration_hhi_d3(revenue):
    shares = []
    rev_ttm = _ttm(revenue).replace(0, np.nan)
    for lag in range(4):
        shares.append((revenue.shift(lag) / rev_ttm) ** 2)
    return sum(shares).diff().diff().diff()

def f11_rqlv_015_revenue_ttm_to_total_capital_d3(revenue, equity, debt, cashneq):
    return _safe_div(_ttm(revenue), equity + debt - cashneq).diff().diff().diff()

def f11_rqlv_016_receivables_to_revenue_ttm_d3(receivables, revenue):
    return _safe_div(receivables, _ttm(revenue)).diff().diff().diff()

def f11_rqlv_017_days_sales_outstanding_ttm_d3(receivables, revenue):
    return _safe_div(365.0 * receivables, _ttm(revenue)).diff().diff().diff()

def f11_rqlv_018_receivables_to_revenue_q_d3(receivables, revenue):
    return _safe_div(receivables, revenue).diff().diff().diff()

def f11_rqlv_019_receivables_growth_minus_revenue_growth_yoy_d3(receivables, revenue):
    return (_yoy_pct(receivables) - _yoy_pct(_ttm(revenue))).diff().diff().diff()

def f11_rqlv_020_receivables_share_of_assets_d3(receivables, assets):
    return _safe_div(receivables, assets).diff().diff().diff()

def f11_rqlv_021_delta_receivables_to_delta_revenue_yoy_d3(receivables, revenue):
    rev_ttm = _ttm(revenue)
    return _safe_div(_yoy(receivables), _yoy(rev_ttm).abs()).diff().diff().diff()

def f11_rqlv_022_receivables_to_currentassets_d3(receivables, assetsc):
    return _safe_div(receivables, assetsc).diff().diff().diff()

def f11_rqlv_023_receivables_to_workingcapital_d3(receivables, workingcapital):
    return _safe_div(receivables, workingcapital.abs()).diff().diff().diff()

def f11_rqlv_024_receivables_to_cash_d3(receivables, cashneq):
    return _safe_div(receivables, cashneq).diff().diff().diff()

def f11_rqlv_025_dso_qoq_jump_d3(receivables, revenue):
    dso = _safe_div(365.0 * receivables, _ttm(revenue))
    return dso.diff().diff().diff().diff()

def f11_rqlv_026_receivables_zscore_4q_d3(receivables):
    return _rolling_zscore(receivables, 4, min_periods=2).diff().diff().diff()

def f11_rqlv_027_receivables_share_q_minus_ttm_mean_d3(receivables, revenue):
    share_q = _safe_div(receivables, revenue)
    return (share_q - share_q.rolling(4, min_periods=2).mean()).diff().diff().diff()

def f11_rqlv_028_receivables_to_revenue_q_zscore_8q_d3(receivables, revenue):
    ratio = _safe_div(receivables, revenue)
    return _rolling_zscore(ratio, 8, min_periods=3).diff().diff().diff()

def f11_rqlv_029_revenue_minus_opcf_to_revenue_d3(revenue, ncfo):
    return _safe_div(_ttm(revenue) - _ttm(ncfo), _ttm(revenue).abs()).diff().diff().diff()

def f11_rqlv_030_accrual_revenue_share_d3(revenue, ncfo):
    return (1.0 - _safe_div(_ttm(ncfo), _ttm(revenue).abs())).diff().diff().diff()

def f11_rqlv_031_deferredrev_to_revenue_ttm_d3(deferredrev, revenue):
    return _safe_div(deferredrev, _ttm(revenue)).diff().diff().diff()

def f11_rqlv_032_deferredrev_qoq_change_to_revenue_d3(deferredrev, revenue):
    return _safe_div(deferredrev.diff(), revenue.abs()).diff().diff().diff()

def f11_rqlv_033_deferredrev_to_currentliabilities_d3(deferredrev, liabilitiesc):
    return _safe_div(deferredrev, liabilitiesc).diff().diff().diff()

def f11_rqlv_034_deferredrev_growth_minus_revenue_growth_yoy_d3(deferredrev, revenue):
    return (_yoy_pct(deferredrev) - _yoy_pct(_ttm(revenue))).diff().diff().diff()

def f11_rqlv_035_deferredrev_share_of_liabilities_d3(deferredrev, liabilities):
    return _safe_div(deferredrev, liabilities).diff().diff().diff()

def f11_rqlv_036_deferredrev_zscore_8q_d3(deferredrev):
    return _rolling_zscore(deferredrev, 8, min_periods=3).diff().diff().diff()

def f11_rqlv_037_deferredrev_to_marketcap_proxy_d3(deferredrev, equity):
    return _safe_div(deferredrev, equity).diff().diff().diff()

def f11_rqlv_038_deferredrev_qoq_pct_d3(deferredrev):
    return _qoq_pct(deferredrev).diff().diff().diff()

def f11_rqlv_039_deferredrev_decay_4q_d3(deferredrev):
    return _safe_div(deferredrev - deferredrev.shift(4), deferredrev.shift(4).abs()).diff().diff().diff()

def f11_rqlv_040_recurring_revenue_proxy_d3(deferredrev, revenue):
    return _safe_div(deferredrev * 4.0, _ttm(revenue)).diff().diff().diff()

def f11_rqlv_041_gross_margin_ttm_d3(gp, revenue):
    return _safe_div(_ttm(gp), _ttm(revenue)).diff().diff().diff()

def f11_rqlv_042_gross_margin_q_d3(gp, revenue):
    return _safe_div(gp, revenue).diff().diff().diff()

def f11_rqlv_043_gross_margin_q_minus_ttm_d3(gp, revenue):
    return (_safe_div(gp, revenue) - _safe_div(_ttm(gp), _ttm(revenue))).diff().diff().diff()

def f11_rqlv_044_cogs_share_of_revenue_ttm_d3(cor, revenue):
    return _safe_div(_ttm(cor), _ttm(revenue)).diff().diff().diff()

def f11_rqlv_045_cogs_share_of_revenue_q_d3(cor, revenue):
    return _safe_div(cor, revenue).diff().diff().diff()

def f11_rqlv_046_sgna_to_revenue_ttm_d3(sgna, revenue):
    return _safe_div(_ttm(sgna), _ttm(revenue)).diff().diff().diff()

def f11_rqlv_047_rnd_to_revenue_ttm_d3(rnd, revenue):
    return _safe_div(_ttm(rnd), _ttm(revenue)).diff().diff().diff()

def f11_rqlv_048_opex_to_revenue_ttm_d3(opex, revenue):
    return _safe_div(_ttm(opex), _ttm(revenue)).diff().diff().diff()

def f11_rqlv_049_operating_margin_ttm_d3(opinc, revenue):
    return _safe_div(_ttm(opinc), _ttm(revenue)).diff().diff().diff()

def f11_rqlv_050_ebitda_margin_ttm_d3(ebitda, revenue):
    return _safe_div(_ttm(ebitda), _ttm(revenue)).diff().diff().diff()

def f11_rqlv_051_ebit_margin_ttm_d3(ebit, revenue):
    return _safe_div(_ttm(ebit), _ttm(revenue)).diff().diff().diff()

def f11_rqlv_052_fcf_margin_ttm_d3(fcf, revenue):
    return _safe_div(_ttm(fcf), _ttm(revenue)).diff().diff().diff()

def f11_rqlv_053_revenue_minus_opex_share_ttm_d3(revenue, opex):
    return _safe_div(_ttm(revenue) - _ttm(opex), _ttm(revenue).abs()).diff().diff().diff()

def f11_rqlv_054_sgna_growth_minus_revenue_growth_yoy_d3(sgna, revenue):
    return (_yoy_pct(_ttm(sgna)) - _yoy_pct(_ttm(revenue))).diff().diff().diff()

def f11_rqlv_055_rnd_growth_minus_revenue_growth_yoy_d3(rnd, revenue):
    return (_yoy_pct(_ttm(rnd)) - _yoy_pct(_ttm(revenue))).diff().diff().diff()

def f11_rqlv_056_workingcapital_to_revenue_ttm_d3(workingcapital, revenue):
    return _safe_div(workingcapital, _ttm(revenue)).diff().diff().diff()

def f11_rqlv_057_inventory_to_revenue_ttm_d3(inventory, revenue):
    return _safe_div(inventory, _ttm(revenue)).diff().diff().diff()

def f11_rqlv_058_days_inventory_ttm_d3(inventory, cor):
    return _safe_div(365.0 * inventory, _ttm(cor)).diff().diff().diff()

def f11_rqlv_059_inventory_to_revenue_q_d3(inventory, revenue):
    return _safe_div(inventory, revenue).diff().diff().diff()

def f11_rqlv_060_inventory_growth_minus_revenue_growth_yoy_d3(inventory, revenue):
    return (_yoy_pct(inventory) - _yoy_pct(_ttm(revenue))).diff().diff().diff()

def f11_rqlv_061_payables_to_revenue_ttm_d3(payables, revenue):
    return _safe_div(payables, _ttm(revenue)).diff().diff().diff()

def f11_rqlv_062_days_payable_ttm_d3(payables, cor):
    return _safe_div(365.0 * payables, _ttm(cor)).diff().diff().diff()

def f11_rqlv_063_cash_conversion_cycle_ttm_d3(receivables, inventory, payables, revenue, cor):
    dso = _safe_div(365.0 * receivables, _ttm(revenue))
    dio = _safe_div(365.0 * inventory, _ttm(cor))
    dpo = _safe_div(365.0 * payables, _ttm(cor))
    return (dso + dio - dpo).diff().diff().diff()

def f11_rqlv_064_inventory_share_of_currentassets_d3(inventory, assetsc):
    return _safe_div(inventory, assetsc).diff().diff().diff()

def f11_rqlv_065_inventory_zscore_8q_d3(inventory):
    return _rolling_zscore(inventory, 8, min_periods=3).diff().diff().diff()

def f11_rqlv_066_receivables_plus_inventory_to_revenue_ttm_d3(receivables, inventory, revenue):
    return _safe_div(receivables + inventory, _ttm(revenue)).diff().diff().diff()

def f11_rqlv_067_workingcapital_share_of_assets_d3(workingcapital, assets):
    return _safe_div(workingcapital, assets).diff().diff().diff()

def f11_rqlv_068_inventory_obsolescence_proxy_d3(inventory, revenue):
    return (_yoy_pct(inventory) - _yoy_pct(_ttm(revenue))).diff().diff().diff()

def f11_rqlv_069_dio_qoq_jump_d3(inventory, cor):
    dio = _safe_div(365.0 * inventory, _ttm(cor))
    return dio.diff().diff().diff().diff()

def f11_rqlv_070_dpo_qoq_jump_d3(payables, cor):
    dpo = _safe_div(365.0 * payables, _ttm(cor))
    return dpo.diff().diff().diff().diff()

def f11_rqlv_071_revenue_qoq_stddev_4q_d3(revenue):
    return revenue.diff().rolling(4, min_periods=2).std().diff().diff().diff()

def f11_rqlv_072_revenue_qoq_stddev_8q_d3(revenue):
    return revenue.diff().rolling(8, min_periods=3).std().diff().diff().diff()

def f11_rqlv_073_revenue_yoy_stddev_8q_d3(revenue):
    return _yoy(_ttm(revenue)).rolling(8, min_periods=3).std().diff().diff().diff()

def f11_rqlv_074_revenue_cv_8q_d3(revenue):
    m = revenue.rolling(8, min_periods=3).mean()
    sd = revenue.rolling(8, min_periods=3).std()
    return _safe_div(sd, m.abs()).diff().diff().diff()

def f11_rqlv_075_revenue_qoq_max_drop_8q_d3(revenue):
    return revenue.diff().rolling(8, min_periods=3).min().diff().diff().diff()
REVENUE_QUALITY_LEVEL_D3_REGISTRY_001_075 = {'f11_rqlv_001_log_revenue_ttm_d3': {'inputs': ['revenue'], 'func': f11_rqlv_001_log_revenue_ttm_d3}, 'f11_rqlv_002_revenue_ttm_to_assets_d3': {'inputs': ['revenue', 'assets'], 'func': f11_rqlv_002_revenue_ttm_to_assets_d3}, 'f11_rqlv_003_revenue_ttm_to_equity_d3': {'inputs': ['revenue', 'equity'], 'func': f11_rqlv_003_revenue_ttm_to_equity_d3}, 'f11_rqlv_004_revenue_ttm_to_invested_capital_d3': {'inputs': ['revenue', 'equity', 'debt'], 'func': f11_rqlv_004_revenue_ttm_to_invested_capital_d3}, 'f11_rqlv_005_revenue_ttm_to_workingcapital_d3': {'inputs': ['revenue', 'workingcapital'], 'func': f11_rqlv_005_revenue_ttm_to_workingcapital_d3}, 'f11_rqlv_006_revenue_ttm_to_ppnenet_d3': {'inputs': ['revenue', 'ppnenet'], 'func': f11_rqlv_006_revenue_ttm_to_ppnenet_d3}, 'f11_rqlv_007_revenue_ttm_to_intangibles_d3': {'inputs': ['revenue', 'intangibles'], 'func': f11_rqlv_007_revenue_ttm_to_intangibles_d3}, 'f11_rqlv_008_revenue_ttm_to_opex_d3': {'inputs': ['revenue', 'opex'], 'func': f11_rqlv_008_revenue_ttm_to_opex_d3}, 'f11_rqlv_009_revenue_per_share_ttm_d3': {'inputs': ['revenue', 'shareswadil'], 'func': f11_rqlv_009_revenue_per_share_ttm_d3}, 'f11_rqlv_010_revenue_per_basic_share_ttm_d3': {'inputs': ['revenue', 'shareswa'], 'func': f11_rqlv_010_revenue_per_basic_share_ttm_d3}, 'f11_rqlv_011_revenue_q_annualized_to_assets_d3': {'inputs': ['revenue', 'assets'], 'func': f11_rqlv_011_revenue_q_annualized_to_assets_d3}, 'f11_rqlv_012_revenue_q_annualized_minus_ttm_to_ttm_d3': {'inputs': ['revenue'], 'func': f11_rqlv_012_revenue_q_annualized_minus_ttm_to_ttm_d3}, 'f11_rqlv_013_latest_q_share_of_ttm_d3': {'inputs': ['revenue'], 'func': f11_rqlv_013_latest_q_share_of_ttm_d3}, 'f11_rqlv_014_revenue_4q_concentration_hhi_d3': {'inputs': ['revenue'], 'func': f11_rqlv_014_revenue_4q_concentration_hhi_d3}, 'f11_rqlv_015_revenue_ttm_to_total_capital_d3': {'inputs': ['revenue', 'equity', 'debt', 'cashneq'], 'func': f11_rqlv_015_revenue_ttm_to_total_capital_d3}, 'f11_rqlv_016_receivables_to_revenue_ttm_d3': {'inputs': ['receivables', 'revenue'], 'func': f11_rqlv_016_receivables_to_revenue_ttm_d3}, 'f11_rqlv_017_days_sales_outstanding_ttm_d3': {'inputs': ['receivables', 'revenue'], 'func': f11_rqlv_017_days_sales_outstanding_ttm_d3}, 'f11_rqlv_018_receivables_to_revenue_q_d3': {'inputs': ['receivables', 'revenue'], 'func': f11_rqlv_018_receivables_to_revenue_q_d3}, 'f11_rqlv_019_receivables_growth_minus_revenue_growth_yoy_d3': {'inputs': ['receivables', 'revenue'], 'func': f11_rqlv_019_receivables_growth_minus_revenue_growth_yoy_d3}, 'f11_rqlv_020_receivables_share_of_assets_d3': {'inputs': ['receivables', 'assets'], 'func': f11_rqlv_020_receivables_share_of_assets_d3}, 'f11_rqlv_021_delta_receivables_to_delta_revenue_yoy_d3': {'inputs': ['receivables', 'revenue'], 'func': f11_rqlv_021_delta_receivables_to_delta_revenue_yoy_d3}, 'f11_rqlv_022_receivables_to_currentassets_d3': {'inputs': ['receivables', 'assetsc'], 'func': f11_rqlv_022_receivables_to_currentassets_d3}, 'f11_rqlv_023_receivables_to_workingcapital_d3': {'inputs': ['receivables', 'workingcapital'], 'func': f11_rqlv_023_receivables_to_workingcapital_d3}, 'f11_rqlv_024_receivables_to_cash_d3': {'inputs': ['receivables', 'cashneq'], 'func': f11_rqlv_024_receivables_to_cash_d3}, 'f11_rqlv_025_dso_qoq_jump_d3': {'inputs': ['receivables', 'revenue'], 'func': f11_rqlv_025_dso_qoq_jump_d3}, 'f11_rqlv_026_receivables_zscore_4q_d3': {'inputs': ['receivables'], 'func': f11_rqlv_026_receivables_zscore_4q_d3}, 'f11_rqlv_027_receivables_share_q_minus_ttm_mean_d3': {'inputs': ['receivables', 'revenue'], 'func': f11_rqlv_027_receivables_share_q_minus_ttm_mean_d3}, 'f11_rqlv_028_receivables_to_revenue_q_zscore_8q_d3': {'inputs': ['receivables', 'revenue'], 'func': f11_rqlv_028_receivables_to_revenue_q_zscore_8q_d3}, 'f11_rqlv_029_revenue_minus_opcf_to_revenue_d3': {'inputs': ['revenue', 'ncfo'], 'func': f11_rqlv_029_revenue_minus_opcf_to_revenue_d3}, 'f11_rqlv_030_accrual_revenue_share_d3': {'inputs': ['revenue', 'ncfo'], 'func': f11_rqlv_030_accrual_revenue_share_d3}, 'f11_rqlv_031_deferredrev_to_revenue_ttm_d3': {'inputs': ['deferredrev', 'revenue'], 'func': f11_rqlv_031_deferredrev_to_revenue_ttm_d3}, 'f11_rqlv_032_deferredrev_qoq_change_to_revenue_d3': {'inputs': ['deferredrev', 'revenue'], 'func': f11_rqlv_032_deferredrev_qoq_change_to_revenue_d3}, 'f11_rqlv_033_deferredrev_to_currentliabilities_d3': {'inputs': ['deferredrev', 'liabilitiesc'], 'func': f11_rqlv_033_deferredrev_to_currentliabilities_d3}, 'f11_rqlv_034_deferredrev_growth_minus_revenue_growth_yoy_d3': {'inputs': ['deferredrev', 'revenue'], 'func': f11_rqlv_034_deferredrev_growth_minus_revenue_growth_yoy_d3}, 'f11_rqlv_035_deferredrev_share_of_liabilities_d3': {'inputs': ['deferredrev', 'liabilities'], 'func': f11_rqlv_035_deferredrev_share_of_liabilities_d3}, 'f11_rqlv_036_deferredrev_zscore_8q_d3': {'inputs': ['deferredrev'], 'func': f11_rqlv_036_deferredrev_zscore_8q_d3}, 'f11_rqlv_037_deferredrev_to_marketcap_proxy_d3': {'inputs': ['deferredrev', 'equity'], 'func': f11_rqlv_037_deferredrev_to_marketcap_proxy_d3}, 'f11_rqlv_038_deferredrev_qoq_pct_d3': {'inputs': ['deferredrev'], 'func': f11_rqlv_038_deferredrev_qoq_pct_d3}, 'f11_rqlv_039_deferredrev_decay_4q_d3': {'inputs': ['deferredrev'], 'func': f11_rqlv_039_deferredrev_decay_4q_d3}, 'f11_rqlv_040_recurring_revenue_proxy_d3': {'inputs': ['deferredrev', 'revenue'], 'func': f11_rqlv_040_recurring_revenue_proxy_d3}, 'f11_rqlv_041_gross_margin_ttm_d3': {'inputs': ['gp', 'revenue'], 'func': f11_rqlv_041_gross_margin_ttm_d3}, 'f11_rqlv_042_gross_margin_q_d3': {'inputs': ['gp', 'revenue'], 'func': f11_rqlv_042_gross_margin_q_d3}, 'f11_rqlv_043_gross_margin_q_minus_ttm_d3': {'inputs': ['gp', 'revenue'], 'func': f11_rqlv_043_gross_margin_q_minus_ttm_d3}, 'f11_rqlv_044_cogs_share_of_revenue_ttm_d3': {'inputs': ['cor', 'revenue'], 'func': f11_rqlv_044_cogs_share_of_revenue_ttm_d3}, 'f11_rqlv_045_cogs_share_of_revenue_q_d3': {'inputs': ['cor', 'revenue'], 'func': f11_rqlv_045_cogs_share_of_revenue_q_d3}, 'f11_rqlv_046_sgna_to_revenue_ttm_d3': {'inputs': ['sgna', 'revenue'], 'func': f11_rqlv_046_sgna_to_revenue_ttm_d3}, 'f11_rqlv_047_rnd_to_revenue_ttm_d3': {'inputs': ['rnd', 'revenue'], 'func': f11_rqlv_047_rnd_to_revenue_ttm_d3}, 'f11_rqlv_048_opex_to_revenue_ttm_d3': {'inputs': ['opex', 'revenue'], 'func': f11_rqlv_048_opex_to_revenue_ttm_d3}, 'f11_rqlv_049_operating_margin_ttm_d3': {'inputs': ['opinc', 'revenue'], 'func': f11_rqlv_049_operating_margin_ttm_d3}, 'f11_rqlv_050_ebitda_margin_ttm_d3': {'inputs': ['ebitda', 'revenue'], 'func': f11_rqlv_050_ebitda_margin_ttm_d3}, 'f11_rqlv_051_ebit_margin_ttm_d3': {'inputs': ['ebit', 'revenue'], 'func': f11_rqlv_051_ebit_margin_ttm_d3}, 'f11_rqlv_052_fcf_margin_ttm_d3': {'inputs': ['fcf', 'revenue'], 'func': f11_rqlv_052_fcf_margin_ttm_d3}, 'f11_rqlv_053_revenue_minus_opex_share_ttm_d3': {'inputs': ['revenue', 'opex'], 'func': f11_rqlv_053_revenue_minus_opex_share_ttm_d3}, 'f11_rqlv_054_sgna_growth_minus_revenue_growth_yoy_d3': {'inputs': ['sgna', 'revenue'], 'func': f11_rqlv_054_sgna_growth_minus_revenue_growth_yoy_d3}, 'f11_rqlv_055_rnd_growth_minus_revenue_growth_yoy_d3': {'inputs': ['rnd', 'revenue'], 'func': f11_rqlv_055_rnd_growth_minus_revenue_growth_yoy_d3}, 'f11_rqlv_056_workingcapital_to_revenue_ttm_d3': {'inputs': ['workingcapital', 'revenue'], 'func': f11_rqlv_056_workingcapital_to_revenue_ttm_d3}, 'f11_rqlv_057_inventory_to_revenue_ttm_d3': {'inputs': ['inventory', 'revenue'], 'func': f11_rqlv_057_inventory_to_revenue_ttm_d3}, 'f11_rqlv_058_days_inventory_ttm_d3': {'inputs': ['inventory', 'cor'], 'func': f11_rqlv_058_days_inventory_ttm_d3}, 'f11_rqlv_059_inventory_to_revenue_q_d3': {'inputs': ['inventory', 'revenue'], 'func': f11_rqlv_059_inventory_to_revenue_q_d3}, 'f11_rqlv_060_inventory_growth_minus_revenue_growth_yoy_d3': {'inputs': ['inventory', 'revenue'], 'func': f11_rqlv_060_inventory_growth_minus_revenue_growth_yoy_d3}, 'f11_rqlv_061_payables_to_revenue_ttm_d3': {'inputs': ['payables', 'revenue'], 'func': f11_rqlv_061_payables_to_revenue_ttm_d3}, 'f11_rqlv_062_days_payable_ttm_d3': {'inputs': ['payables', 'cor'], 'func': f11_rqlv_062_days_payable_ttm_d3}, 'f11_rqlv_063_cash_conversion_cycle_ttm_d3': {'inputs': ['receivables', 'inventory', 'payables', 'revenue', 'cor'], 'func': f11_rqlv_063_cash_conversion_cycle_ttm_d3}, 'f11_rqlv_064_inventory_share_of_currentassets_d3': {'inputs': ['inventory', 'assetsc'], 'func': f11_rqlv_064_inventory_share_of_currentassets_d3}, 'f11_rqlv_065_inventory_zscore_8q_d3': {'inputs': ['inventory'], 'func': f11_rqlv_065_inventory_zscore_8q_d3}, 'f11_rqlv_066_receivables_plus_inventory_to_revenue_ttm_d3': {'inputs': ['receivables', 'inventory', 'revenue'], 'func': f11_rqlv_066_receivables_plus_inventory_to_revenue_ttm_d3}, 'f11_rqlv_067_workingcapital_share_of_assets_d3': {'inputs': ['workingcapital', 'assets'], 'func': f11_rqlv_067_workingcapital_share_of_assets_d3}, 'f11_rqlv_068_inventory_obsolescence_proxy_d3': {'inputs': ['inventory', 'revenue'], 'func': f11_rqlv_068_inventory_obsolescence_proxy_d3}, 'f11_rqlv_069_dio_qoq_jump_d3': {'inputs': ['inventory', 'cor'], 'func': f11_rqlv_069_dio_qoq_jump_d3}, 'f11_rqlv_070_dpo_qoq_jump_d3': {'inputs': ['payables', 'cor'], 'func': f11_rqlv_070_dpo_qoq_jump_d3}, 'f11_rqlv_071_revenue_qoq_stddev_4q_d3': {'inputs': ['revenue'], 'func': f11_rqlv_071_revenue_qoq_stddev_4q_d3}, 'f11_rqlv_072_revenue_qoq_stddev_8q_d3': {'inputs': ['revenue'], 'func': f11_rqlv_072_revenue_qoq_stddev_8q_d3}, 'f11_rqlv_073_revenue_yoy_stddev_8q_d3': {'inputs': ['revenue'], 'func': f11_rqlv_073_revenue_yoy_stddev_8q_d3}, 'f11_rqlv_074_revenue_cv_8q_d3': {'inputs': ['revenue'], 'func': f11_rqlv_074_revenue_cv_8q_d3}, 'f11_rqlv_075_revenue_qoq_max_drop_8q_d3': {'inputs': ['revenue'], 'func': f11_rqlv_075_revenue_qoq_max_drop_8q_d3}}