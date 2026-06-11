"""cash_flow_deterioration_trajectory d1 features 001-075 - order-1 difference of corresponding base features.

Each function inlines the base body and wraps the final return value with .diff(). Self-contained; helpers redefined locally per HANDOFF."""
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


def f23_cfdt_001_ncfo_ttm_to_assets_d1(ncfo, assets):
    return _safe_div(_ttm(ncfo), assets).diff()


def f23_cfdt_002_ncfo_margin_ttm_d1(ncfo, revenue):
    return _safe_div(_ttm(ncfo), _ttm(revenue)).diff()


def f23_cfdt_003_ncfo_q_to_revenue_q_d1(ncfo, revenue):
    return _safe_div(ncfo, revenue).diff()


def f23_cfdt_004_ncfo_yoy_pct_ttm_d1(ncfo):
    return _yoy_pct(_ttm(ncfo)).diff()


def f23_cfdt_005_ncfo_qoq_pct_d1(ncfo):
    return _qoq_pct(ncfo).diff()


def f23_cfdt_006_ncfo_ttm_trend_slope_8q_d1(ncfo):
    ttm = _ttm(ncfo)
    m = ttm.rolling(8, min_periods=3).mean()
    return _safe_div(ttm - m, m.abs()).diff()


def f23_cfdt_007_ncfo_margin_decay_yoy_d1(ncfo, revenue):
    m_now = _safe_div(_ttm(ncfo), _ttm(revenue))
    return (m_now - m_now.shift(4)).diff()


def f23_cfdt_008_ncfo_minus_netinc_to_assets_d1(ncfo, netinc, assets):
    return _safe_div(_ttm(ncfo) - _ttm(netinc), assets).diff()


def f23_cfdt_009_log_abs_ncfo_ttm_d1(ncfo):
    return _safe_log_abs(_ttm(ncfo)).diff()


def f23_cfdt_010_neg_ncfo_streak_4q_d1(ncfo):
    neg = (ncfo < 0).astype(float)
    return neg.rolling(4, min_periods=1).sum().diff()


def f23_cfdt_011_ncfo_avg4_to_avg4_lagged_d1(ncfo):
    a = _avg4(ncfo)
    return _safe_div(a, a.shift(4).abs()).diff()


def f23_cfdt_012_ncfo_share_of_ebitda_d1(ncfo, ebitda):
    return _safe_div(_ttm(ncfo), _ttm(ebitda).abs()).diff()


def f23_cfdt_013_ncfo_to_equity_d1(ncfo, equity):
    return _safe_div(_ttm(ncfo), equity).diff()


def f23_cfdt_014_ncfo_to_liabilities_d1(ncfo, liabilities):
    return _safe_div(_ttm(ncfo), liabilities).diff()


def f23_cfdt_015_ncfo_per_share_d1(ncfo, shareswadil):
    return _safe_div(_ttm(ncfo), shareswadil).diff()


def f23_cfdt_016_fcf_margin_ttm_d1(fcf, revenue):
    return _safe_div(_ttm(fcf), _ttm(revenue)).diff()


def f23_cfdt_017_fcf_to_assets_d1(fcf, assets):
    return _safe_div(_ttm(fcf), assets).diff()


def f23_cfdt_018_fcf_yield_proxy_to_equity_d1(fcf, equity):
    return _safe_div(_ttm(fcf), equity).diff()


def f23_cfdt_019_fcf_to_invested_capital_d1(fcf, equity, debt):
    return _safe_div(_ttm(fcf), equity + debt).diff()


def f23_cfdt_020_fcf_per_share_d1(fcf, shareswadil):
    return _safe_div(_ttm(fcf), shareswadil).diff()


def f23_cfdt_021_fcf_yoy_pct_ttm_d1(fcf):
    return _yoy_pct(_ttm(fcf)).diff()


def f23_cfdt_022_fcf_qoq_pct_d1(fcf):
    return _qoq_pct(fcf).diff()


def f23_cfdt_023_neg_fcf_streak_4q_d1(fcf):
    neg = (fcf < 0).astype(float)
    return neg.rolling(4, min_periods=1).sum().diff()


def f23_cfdt_024_neg_fcf_streak_8q_d1(fcf):
    neg = (fcf < 0).astype(float)
    return neg.rolling(8, min_periods=2).sum().diff()


def f23_cfdt_025_fcf_margin_minus_4q_lag_d1(fcf, revenue):
    m_now = _safe_div(_ttm(fcf), _ttm(revenue))
    return (m_now - m_now.shift(4)).diff()


def f23_cfdt_026_fcf_to_debt_d1(fcf, debt):
    return _safe_div(_ttm(fcf), debt).diff()


def f23_cfdt_027_fcf_to_marketcap_proxy_d1(fcf, equity):
    return _safe_div(_ttm(fcf), equity.abs()).diff()


def f23_cfdt_028_fcf_ttm_zscore_8q_d1(fcf):
    return _rolling_zscore(_ttm(fcf), 8, min_periods=3).diff()


def f23_cfdt_029_fcf_avg4_decay_yoy_d1(fcf):
    a = _avg4(fcf)
    return _safe_div(a - a.shift(4), a.shift(4).abs()).diff()


def f23_cfdt_030_log_abs_fcf_ttm_d1(fcf):
    return _safe_log_abs(_ttm(fcf)).diff()


def f23_cfdt_031_capex_to_revenue_ttm_d1(capex, revenue):
    return _safe_div(_ttm(capex).abs(), _ttm(revenue)).diff()


def f23_cfdt_032_capex_to_depamor_ttm_d1(capex, depamor):
    return _safe_div(_ttm(capex).abs(), _ttm(depamor)).diff()


def f23_cfdt_033_capex_to_assets_d1(capex, assets):
    return _safe_div(_ttm(capex).abs(), assets).diff()


def f23_cfdt_034_capex_minus_depamor_to_assets_d1(capex, depamor, assets):
    return _safe_div(_ttm(capex).abs() - _ttm(depamor), assets).diff()


def f23_cfdt_035_capex_ttm_yoy_pct_d1(capex):
    return _yoy_pct(_ttm(capex).abs()).diff()


def f23_cfdt_036_capex_to_ncfo_d1(capex, ncfo):
    return _safe_div(_ttm(capex).abs(), _ttm(ncfo).abs()).diff()


def f23_cfdt_037_depamor_minus_capex_to_revenue_d1(capex, depamor, revenue):
    return _safe_div(_ttm(depamor) - _ttm(capex).abs(), _ttm(revenue)).diff()


def f23_cfdt_038_capex_share_of_opex_d1(capex, opex):
    return _safe_div(_ttm(capex).abs(), _ttm(opex)).diff()


def f23_cfdt_039_capex_to_ppnenet_d1(capex, ppnenet):
    return _safe_div(_ttm(capex).abs(), ppnenet).diff()


def f23_cfdt_040_capex_q_to_revenue_q_d1(capex, revenue):
    return _safe_div(capex.abs(), revenue).diff()


def f23_cfdt_041_capex_qoq_jump_d1(capex):
    return capex.abs().diff().diff()


def f23_cfdt_042_capex_intensity_vs_4q_mean_d1(capex, revenue):
    r = _safe_div(capex.abs(), revenue)
    return (r - r.rolling(4, min_periods=2).mean()).diff()


def f23_cfdt_043_capex_growth_minus_revenue_growth_yoy_d1(capex, revenue):
    return (_yoy_pct(_ttm(capex).abs()) - _yoy_pct(_ttm(revenue))).diff()


def f23_cfdt_044_capex_ttm_zscore_12q_d1(capex):
    return _rolling_zscore(_ttm(capex).abs(), 12, min_periods=4).diff()


def f23_cfdt_045_under_investment_gap_ratio_d1(capex, depamor):
    return _safe_div(_ttm(depamor) - _ttm(capex).abs(), _ttm(depamor).abs()).diff()


def f23_cfdt_046_accrual_ratio_balance_sheet_d1(netinc, ncfo, assets):
    return _safe_div(_ttm(netinc) - _ttm(ncfo), assets).diff()


def f23_cfdt_047_accrual_ratio_to_revenue_d1(netinc, ncfo, revenue):
    return _safe_div(_ttm(netinc) - _ttm(ncfo), _ttm(revenue).abs()).diff()


def f23_cfdt_048_ncfo_to_netinc_quality_d1(ncfo, netinc):
    return _safe_div(_ttm(ncfo), _ttm(netinc).abs()).diff()


def f23_cfdt_049_fcf_to_netinc_conversion_d1(fcf, netinc):
    return _safe_div(_ttm(fcf), _ttm(netinc).abs()).diff()


def f23_cfdt_050_fcf_to_ebitda_conversion_d1(fcf, ebitda):
    return _safe_div(_ttm(fcf), _ttm(ebitda).abs()).diff()


def f23_cfdt_051_ncfo_to_ebitda_conversion_d1(ncfo, ebitda):
    return _safe_div(_ttm(ncfo), _ttm(ebitda).abs()).diff()


def f23_cfdt_052_ncfo_to_opinc_conversion_d1(ncfo, opinc):
    return _safe_div(_ttm(ncfo), _ttm(opinc).abs()).diff()


def f23_cfdt_053_accrual_widening_yoy_d1(netinc, ncfo, assets):
    a = _safe_div(_ttm(netinc) - _ttm(ncfo), assets)
    return (a - a.shift(4)).diff()


def f23_cfdt_054_accrual_zscore_8q_d1(netinc, ncfo, assets):
    a = _safe_div(_ttm(netinc) - _ttm(ncfo), assets)
    return _rolling_zscore(a, 8, min_periods=3).diff()


def f23_cfdt_055_cash_conversion_decay_4q_d1(fcf, netinc):
    c = _safe_div(_ttm(fcf), _ttm(netinc).abs())
    return (c - c.shift(4)).diff()


def f23_cfdt_056_sbcomp_offset_to_ncfo_d1(sbcomp, ncfo):
    return _safe_div(_ttm(sbcomp), _ttm(ncfo).abs()).diff()


def f23_cfdt_057_sbcomp_share_of_revenue_d1(sbcomp, revenue):
    return _safe_div(_ttm(sbcomp), _ttm(revenue)).diff()


def f23_cfdt_058_ncfo_ex_sbcomp_margin_d1(ncfo, sbcomp, revenue):
    return _safe_div(_ttm(ncfo) - _ttm(sbcomp), _ttm(revenue)).diff()


def f23_cfdt_059_sbcomp_growth_minus_ncfo_growth_yoy_d1(sbcomp, ncfo):
    return (_yoy_pct(_ttm(sbcomp)) - _yoy_pct(_ttm(ncfo).abs())).diff()


def f23_cfdt_060_accrual_to_avg_assets_d1(netinc, ncfo, assets):
    avg_a = _avg4(assets)
    return _safe_div(_ttm(netinc) - _ttm(ncfo), avg_a).diff()


def f23_cfdt_061_deltawc_to_revenue_ttm_d1(deltawc, revenue):
    return _safe_div(_ttm(deltawc), _ttm(revenue)).diff()


def f23_cfdt_062_deltawc_to_ncfo_d1(deltawc, ncfo):
    return _safe_div(_ttm(deltawc), _ttm(ncfo).abs()).diff()


def f23_cfdt_063_deltawc_persistent_drag_4q_d1(deltawc):
    drag = (deltawc > 0).astype(float)
    return drag.rolling(4, min_periods=1).sum().diff()


def f23_cfdt_064_workingcapital_qoq_change_to_revenue_d1(workingcapital, revenue):
    return _safe_div(workingcapital.diff(), _ttm(revenue)).diff()


def f23_cfdt_065_receivables_absorbing_cash_to_revenue_d1(receivables, revenue):
    return _safe_div(receivables.diff(), _ttm(revenue)).diff()


def f23_cfdt_066_inventory_absorbing_cash_to_revenue_d1(inventory, revenue):
    return _safe_div(inventory.diff(), _ttm(revenue)).diff()


def f23_cfdt_067_payables_giving_up_cash_to_revenue_d1(payables, revenue):
    return _safe_div(-payables.diff(), _ttm(revenue)).diff()


def f23_cfdt_068_wc_components_cash_drag_sum_d1(receivables, inventory, payables, revenue):
    drag = receivables.diff() + inventory.diff() - payables.diff()
    return _safe_div(drag, _ttm(revenue)).diff()


def f23_cfdt_069_deltawc_growth_yoy_d1(deltawc):
    return _yoy_pct(_ttm(deltawc)).diff()


def f23_cfdt_070_workingcapital_share_of_ncfo_d1(workingcapital, ncfo):
    return _safe_div(workingcapital, _ttm(ncfo).abs()).diff()


def f23_cfdt_071_wc_to_revenue_decay_4q_d1(workingcapital, revenue):
    r = _safe_div(workingcapital, _ttm(revenue))
    return (r - r.shift(4)).diff()


def f23_cfdt_072_deltawc_zscore_8q_d1(deltawc):
    return _rolling_zscore(deltawc, 8, min_periods=3).diff()


def f23_cfdt_073_receivables_inventory_growth_minus_revenue_d1(receivables, inventory, revenue):
    return (_yoy_pct(receivables + inventory) - _yoy_pct(_ttm(revenue))).diff()


def f23_cfdt_074_wc_intensity_qoq_jump_d1(workingcapital, revenue):
    return _safe_div(workingcapital, _ttm(revenue)).diff().diff()


def f23_cfdt_075_persistent_wc_buildup_8q_d1(workingcapital):
    pos = (workingcapital.diff() > 0).astype(float)
    return pos.rolling(8, min_periods=2).sum().diff()


CASH_FLOW_DETERIORATION_TRAJECTORY_D1_REGISTRY_001_075 = {
    "f23_cfdt_001_ncfo_ttm_to_assets_d1": {"inputs": ["ncfo", "assets"], "func": f23_cfdt_001_ncfo_ttm_to_assets_d1},
    "f23_cfdt_002_ncfo_margin_ttm_d1": {"inputs": ["ncfo", "revenue"], "func": f23_cfdt_002_ncfo_margin_ttm_d1},
    "f23_cfdt_003_ncfo_q_to_revenue_q_d1": {"inputs": ["ncfo", "revenue"], "func": f23_cfdt_003_ncfo_q_to_revenue_q_d1},
    "f23_cfdt_004_ncfo_yoy_pct_ttm_d1": {"inputs": ["ncfo"], "func": f23_cfdt_004_ncfo_yoy_pct_ttm_d1},
    "f23_cfdt_005_ncfo_qoq_pct_d1": {"inputs": ["ncfo"], "func": f23_cfdt_005_ncfo_qoq_pct_d1},
    "f23_cfdt_006_ncfo_ttm_trend_slope_8q_d1": {"inputs": ["ncfo"], "func": f23_cfdt_006_ncfo_ttm_trend_slope_8q_d1},
    "f23_cfdt_007_ncfo_margin_decay_yoy_d1": {"inputs": ["ncfo", "revenue"], "func": f23_cfdt_007_ncfo_margin_decay_yoy_d1},
    "f23_cfdt_008_ncfo_minus_netinc_to_assets_d1": {"inputs": ["ncfo", "netinc", "assets"], "func": f23_cfdt_008_ncfo_minus_netinc_to_assets_d1},
    "f23_cfdt_009_log_abs_ncfo_ttm_d1": {"inputs": ["ncfo"], "func": f23_cfdt_009_log_abs_ncfo_ttm_d1},
    "f23_cfdt_010_neg_ncfo_streak_4q_d1": {"inputs": ["ncfo"], "func": f23_cfdt_010_neg_ncfo_streak_4q_d1},
    "f23_cfdt_011_ncfo_avg4_to_avg4_lagged_d1": {"inputs": ["ncfo"], "func": f23_cfdt_011_ncfo_avg4_to_avg4_lagged_d1},
    "f23_cfdt_012_ncfo_share_of_ebitda_d1": {"inputs": ["ncfo", "ebitda"], "func": f23_cfdt_012_ncfo_share_of_ebitda_d1},
    "f23_cfdt_013_ncfo_to_equity_d1": {"inputs": ["ncfo", "equity"], "func": f23_cfdt_013_ncfo_to_equity_d1},
    "f23_cfdt_014_ncfo_to_liabilities_d1": {"inputs": ["ncfo", "liabilities"], "func": f23_cfdt_014_ncfo_to_liabilities_d1},
    "f23_cfdt_015_ncfo_per_share_d1": {"inputs": ["ncfo", "shareswadil"], "func": f23_cfdt_015_ncfo_per_share_d1},
    "f23_cfdt_016_fcf_margin_ttm_d1": {"inputs": ["fcf", "revenue"], "func": f23_cfdt_016_fcf_margin_ttm_d1},
    "f23_cfdt_017_fcf_to_assets_d1": {"inputs": ["fcf", "assets"], "func": f23_cfdt_017_fcf_to_assets_d1},
    "f23_cfdt_018_fcf_yield_proxy_to_equity_d1": {"inputs": ["fcf", "equity"], "func": f23_cfdt_018_fcf_yield_proxy_to_equity_d1},
    "f23_cfdt_019_fcf_to_invested_capital_d1": {"inputs": ["fcf", "equity", "debt"], "func": f23_cfdt_019_fcf_to_invested_capital_d1},
    "f23_cfdt_020_fcf_per_share_d1": {"inputs": ["fcf", "shareswadil"], "func": f23_cfdt_020_fcf_per_share_d1},
    "f23_cfdt_021_fcf_yoy_pct_ttm_d1": {"inputs": ["fcf"], "func": f23_cfdt_021_fcf_yoy_pct_ttm_d1},
    "f23_cfdt_022_fcf_qoq_pct_d1": {"inputs": ["fcf"], "func": f23_cfdt_022_fcf_qoq_pct_d1},
    "f23_cfdt_023_neg_fcf_streak_4q_d1": {"inputs": ["fcf"], "func": f23_cfdt_023_neg_fcf_streak_4q_d1},
    "f23_cfdt_024_neg_fcf_streak_8q_d1": {"inputs": ["fcf"], "func": f23_cfdt_024_neg_fcf_streak_8q_d1},
    "f23_cfdt_025_fcf_margin_minus_4q_lag_d1": {"inputs": ["fcf", "revenue"], "func": f23_cfdt_025_fcf_margin_minus_4q_lag_d1},
    "f23_cfdt_026_fcf_to_debt_d1": {"inputs": ["fcf", "debt"], "func": f23_cfdt_026_fcf_to_debt_d1},
    "f23_cfdt_027_fcf_to_marketcap_proxy_d1": {"inputs": ["fcf", "equity"], "func": f23_cfdt_027_fcf_to_marketcap_proxy_d1},
    "f23_cfdt_028_fcf_ttm_zscore_8q_d1": {"inputs": ["fcf"], "func": f23_cfdt_028_fcf_ttm_zscore_8q_d1},
    "f23_cfdt_029_fcf_avg4_decay_yoy_d1": {"inputs": ["fcf"], "func": f23_cfdt_029_fcf_avg4_decay_yoy_d1},
    "f23_cfdt_030_log_abs_fcf_ttm_d1": {"inputs": ["fcf"], "func": f23_cfdt_030_log_abs_fcf_ttm_d1},
    "f23_cfdt_031_capex_to_revenue_ttm_d1": {"inputs": ["capex", "revenue"], "func": f23_cfdt_031_capex_to_revenue_ttm_d1},
    "f23_cfdt_032_capex_to_depamor_ttm_d1": {"inputs": ["capex", "depamor"], "func": f23_cfdt_032_capex_to_depamor_ttm_d1},
    "f23_cfdt_033_capex_to_assets_d1": {"inputs": ["capex", "assets"], "func": f23_cfdt_033_capex_to_assets_d1},
    "f23_cfdt_034_capex_minus_depamor_to_assets_d1": {"inputs": ["capex", "depamor", "assets"], "func": f23_cfdt_034_capex_minus_depamor_to_assets_d1},
    "f23_cfdt_035_capex_ttm_yoy_pct_d1": {"inputs": ["capex"], "func": f23_cfdt_035_capex_ttm_yoy_pct_d1},
    "f23_cfdt_036_capex_to_ncfo_d1": {"inputs": ["capex", "ncfo"], "func": f23_cfdt_036_capex_to_ncfo_d1},
    "f23_cfdt_037_depamor_minus_capex_to_revenue_d1": {"inputs": ["capex", "depamor", "revenue"], "func": f23_cfdt_037_depamor_minus_capex_to_revenue_d1},
    "f23_cfdt_038_capex_share_of_opex_d1": {"inputs": ["capex", "opex"], "func": f23_cfdt_038_capex_share_of_opex_d1},
    "f23_cfdt_039_capex_to_ppnenet_d1": {"inputs": ["capex", "ppnenet"], "func": f23_cfdt_039_capex_to_ppnenet_d1},
    "f23_cfdt_040_capex_q_to_revenue_q_d1": {"inputs": ["capex", "revenue"], "func": f23_cfdt_040_capex_q_to_revenue_q_d1},
    "f23_cfdt_041_capex_qoq_jump_d1": {"inputs": ["capex"], "func": f23_cfdt_041_capex_qoq_jump_d1},
    "f23_cfdt_042_capex_intensity_vs_4q_mean_d1": {"inputs": ["capex", "revenue"], "func": f23_cfdt_042_capex_intensity_vs_4q_mean_d1},
    "f23_cfdt_043_capex_growth_minus_revenue_growth_yoy_d1": {"inputs": ["capex", "revenue"], "func": f23_cfdt_043_capex_growth_minus_revenue_growth_yoy_d1},
    "f23_cfdt_044_capex_ttm_zscore_12q_d1": {"inputs": ["capex"], "func": f23_cfdt_044_capex_ttm_zscore_12q_d1},
    "f23_cfdt_045_under_investment_gap_ratio_d1": {"inputs": ["capex", "depamor"], "func": f23_cfdt_045_under_investment_gap_ratio_d1},
    "f23_cfdt_046_accrual_ratio_balance_sheet_d1": {"inputs": ["netinc", "ncfo", "assets"], "func": f23_cfdt_046_accrual_ratio_balance_sheet_d1},
    "f23_cfdt_047_accrual_ratio_to_revenue_d1": {"inputs": ["netinc", "ncfo", "revenue"], "func": f23_cfdt_047_accrual_ratio_to_revenue_d1},
    "f23_cfdt_048_ncfo_to_netinc_quality_d1": {"inputs": ["ncfo", "netinc"], "func": f23_cfdt_048_ncfo_to_netinc_quality_d1},
    "f23_cfdt_049_fcf_to_netinc_conversion_d1": {"inputs": ["fcf", "netinc"], "func": f23_cfdt_049_fcf_to_netinc_conversion_d1},
    "f23_cfdt_050_fcf_to_ebitda_conversion_d1": {"inputs": ["fcf", "ebitda"], "func": f23_cfdt_050_fcf_to_ebitda_conversion_d1},
    "f23_cfdt_051_ncfo_to_ebitda_conversion_d1": {"inputs": ["ncfo", "ebitda"], "func": f23_cfdt_051_ncfo_to_ebitda_conversion_d1},
    "f23_cfdt_052_ncfo_to_opinc_conversion_d1": {"inputs": ["ncfo", "opinc"], "func": f23_cfdt_052_ncfo_to_opinc_conversion_d1},
    "f23_cfdt_053_accrual_widening_yoy_d1": {"inputs": ["netinc", "ncfo", "assets"], "func": f23_cfdt_053_accrual_widening_yoy_d1},
    "f23_cfdt_054_accrual_zscore_8q_d1": {"inputs": ["netinc", "ncfo", "assets"], "func": f23_cfdt_054_accrual_zscore_8q_d1},
    "f23_cfdt_055_cash_conversion_decay_4q_d1": {"inputs": ["fcf", "netinc"], "func": f23_cfdt_055_cash_conversion_decay_4q_d1},
    "f23_cfdt_056_sbcomp_offset_to_ncfo_d1": {"inputs": ["sbcomp", "ncfo"], "func": f23_cfdt_056_sbcomp_offset_to_ncfo_d1},
    "f23_cfdt_057_sbcomp_share_of_revenue_d1": {"inputs": ["sbcomp", "revenue"], "func": f23_cfdt_057_sbcomp_share_of_revenue_d1},
    "f23_cfdt_058_ncfo_ex_sbcomp_margin_d1": {"inputs": ["ncfo", "sbcomp", "revenue"], "func": f23_cfdt_058_ncfo_ex_sbcomp_margin_d1},
    "f23_cfdt_059_sbcomp_growth_minus_ncfo_growth_yoy_d1": {"inputs": ["sbcomp", "ncfo"], "func": f23_cfdt_059_sbcomp_growth_minus_ncfo_growth_yoy_d1},
    "f23_cfdt_060_accrual_to_avg_assets_d1": {"inputs": ["netinc", "ncfo", "assets"], "func": f23_cfdt_060_accrual_to_avg_assets_d1},
    "f23_cfdt_061_deltawc_to_revenue_ttm_d1": {"inputs": ["deltawc", "revenue"], "func": f23_cfdt_061_deltawc_to_revenue_ttm_d1},
    "f23_cfdt_062_deltawc_to_ncfo_d1": {"inputs": ["deltawc", "ncfo"], "func": f23_cfdt_062_deltawc_to_ncfo_d1},
    "f23_cfdt_063_deltawc_persistent_drag_4q_d1": {"inputs": ["deltawc"], "func": f23_cfdt_063_deltawc_persistent_drag_4q_d1},
    "f23_cfdt_064_workingcapital_qoq_change_to_revenue_d1": {"inputs": ["workingcapital", "revenue"], "func": f23_cfdt_064_workingcapital_qoq_change_to_revenue_d1},
    "f23_cfdt_065_receivables_absorbing_cash_to_revenue_d1": {"inputs": ["receivables", "revenue"], "func": f23_cfdt_065_receivables_absorbing_cash_to_revenue_d1},
    "f23_cfdt_066_inventory_absorbing_cash_to_revenue_d1": {"inputs": ["inventory", "revenue"], "func": f23_cfdt_066_inventory_absorbing_cash_to_revenue_d1},
    "f23_cfdt_067_payables_giving_up_cash_to_revenue_d1": {"inputs": ["payables", "revenue"], "func": f23_cfdt_067_payables_giving_up_cash_to_revenue_d1},
    "f23_cfdt_068_wc_components_cash_drag_sum_d1": {"inputs": ["receivables", "inventory", "payables", "revenue"], "func": f23_cfdt_068_wc_components_cash_drag_sum_d1},
    "f23_cfdt_069_deltawc_growth_yoy_d1": {"inputs": ["deltawc"], "func": f23_cfdt_069_deltawc_growth_yoy_d1},
    "f23_cfdt_070_workingcapital_share_of_ncfo_d1": {"inputs": ["workingcapital", "ncfo"], "func": f23_cfdt_070_workingcapital_share_of_ncfo_d1},
    "f23_cfdt_071_wc_to_revenue_decay_4q_d1": {"inputs": ["workingcapital", "revenue"], "func": f23_cfdt_071_wc_to_revenue_decay_4q_d1},
    "f23_cfdt_072_deltawc_zscore_8q_d1": {"inputs": ["deltawc"], "func": f23_cfdt_072_deltawc_zscore_8q_d1},
    "f23_cfdt_073_receivables_inventory_growth_minus_revenue_d1": {"inputs": ["receivables", "inventory", "revenue"], "func": f23_cfdt_073_receivables_inventory_growth_minus_revenue_d1},
    "f23_cfdt_074_wc_intensity_qoq_jump_d1": {"inputs": ["workingcapital", "revenue"], "func": f23_cfdt_074_wc_intensity_qoq_jump_d1},
    "f23_cfdt_075_persistent_wc_buildup_8q_d1": {"inputs": ["workingcapital"], "func": f23_cfdt_075_persistent_wc_buildup_8q_d1},
}
