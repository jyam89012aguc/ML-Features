"""debt_buildup_trajectory d2 features - order-2 difference of corresponding base features.

Each function inlines the base body and wraps the return value with .diff().diff().
Self-contained; helpers redefined locally per HANDOFF.
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



def f24_dbtj_001_log_debt_ttm_avg_d2(debt):
    return (_safe_log(_avg4(debt))).diff().diff()

def f24_dbtj_002_log_net_debt_ttm_avg_d2(debt, cashneq):
    return (_safe_log_abs(_avg4(debt - cashneq))).diff().diff()

def f24_dbtj_003_log_debt_minus_log_cash_ttm_d2(debt, cashneq):
    return (_safe_log(_avg4(debt)) - _safe_log(_avg4(cashneq))).diff().diff()

def f24_dbtj_004_debt_to_assets_avg4_d2(debt, assets):
    return (_safe_div(_avg4(debt), _avg4(assets))).diff().diff()

def f24_dbtj_005_debt_to_equity_avg4_d2(debt, equity):
    return (_safe_div(_avg4(debt), _avg4(equity))).diff().diff()

def f24_dbtj_006_debt_to_capital_avg4_d2(debt, equity):
    return (_safe_div(_avg4(debt), _avg4(debt) + _avg4(equity))).diff().diff()

def f24_dbtj_007_liabilities_to_assets_avg4_d2(liabilities, assets):
    return (_safe_div(_avg4(liabilities), _avg4(assets))).diff().diff()

def f24_dbtj_008_debt_to_tangible_equity_avg4_d2(debt, equity, intangibles):
    return (_safe_div(_avg4(debt), _avg4(equity - intangibles))).diff().diff()

def f24_dbtj_009_net_debt_to_equity_avg4_d2(debt, cashneq, equity):
    return (_safe_div(_avg4(debt - cashneq), _avg4(equity))).diff().diff()

def f24_dbtj_010_net_debt_to_assets_avg4_d2(debt, cashneq, assets):
    return (_safe_div(_avg4(debt - cashneq), _avg4(assets))).diff().diff()

def f24_dbtj_011_debt_yoy_pct_smoothed_d2(debt):
    return (_yoy_pct(_avg4(debt))).diff().diff()

def f24_dbtj_012_debt_qoq_pct_smoothed_4q_d2(debt):
    return (_avg4(_qoq_pct(debt))).diff().diff()

def f24_dbtj_013_debt_cagr_8q_d2(debt):
    return (_safe_div(_safe_log(debt) - _safe_log(debt.shift(8)), 8.0)).diff().diff()

def f24_dbtj_014_debt_cagr_12q_d2(debt):
    return (_safe_div(_safe_log(debt) - _safe_log(debt.shift(12)), 12.0)).diff().diff()

def f24_dbtj_015_debt_trend_slope_8q_d2(debt):
    return (_safe_log(_avg4(debt)).diff(8)).diff().diff()

def f24_dbtj_016_net_debt_yoy_change_to_assets_d2(debt, cashneq, assets):
    return (_safe_div((debt - cashneq) - (debt.shift(4) - cashneq.shift(4)), assets.abs())).diff().diff()

def f24_dbtj_017_debt_growth_minus_revenue_growth_yoy_d2(debt, revenue):
    return (_yoy_pct(_avg4(debt)) - _yoy_pct(_ttm(revenue))).diff().diff()

def f24_dbtj_018_debt_growth_minus_asset_growth_yoy_d2(debt, assets):
    return (_yoy_pct(_avg4(debt)) - _yoy_pct(_avg4(assets))).diff().diff()

def f24_dbtj_019_debt_growth_minus_equity_growth_yoy_d2(debt, equity):
    return (_yoy_pct(_avg4(debt)) - _yoy_pct(_avg4(equity))).diff().diff()

def f24_dbtj_020_debt_growth_minus_ebitda_growth_yoy_d2(debt, ebitda):
    return (_yoy_pct(_avg4(debt)) - _yoy_pct(_ttm(ebitda))).diff().diff()

def f24_dbtj_021_consecutive_quarters_debt_growth_8q_d2(debt):
    return ((debt.diff() > 0).astype(float).rolling(8, min_periods=2).sum()).diff().diff()

def f24_dbtj_022_debt_trend_persistence_12q_d2(debt):
    return ((_safe_log(debt).diff() > 0).astype(float).rolling(12, min_periods=3).mean()).diff().diff()

def f24_dbtj_023_debtc_share_of_debt_avg4_d2(debtc, debt):
    return (_safe_div(_avg4(debtc), _avg4(debt))).diff().diff()

def f24_dbtj_024_debtnc_share_of_debt_avg4_d2(debtnc, debt):
    return (_safe_div(_avg4(debtnc), _avg4(debt))).diff().diff()

def f24_dbtj_025_st_debt_share_change_yoy_d2(debtc, debt):
    return (_safe_div(debtc, debt) - _safe_div(debtc.shift(4), debt.shift(4))).diff().diff()

def f24_dbtj_026_debtc_to_assets_trend_d2(debtc, assets):
    return (_safe_div(_avg4(debtc), _avg4(assets))).diff().diff()

def f24_dbtj_027_debtc_yoy_pct_smoothed_d2(debtc):
    return (_yoy_pct(_avg4(debtc))).diff().diff()

def f24_dbtj_028_debtc_growing_faster_than_debtnc_d2(debtc, debtnc):
    return (_yoy_pct(_avg4(debtc)) - _yoy_pct(_avg4(debtnc))).diff().diff()

def f24_dbtj_029_refinancing_wall_8q_d2(debtc, debt):
    return (_safe_div(_avg4(debtc), _avg4(debt)).rolling(8, min_periods=3).max()).diff().diff()

def f24_dbtj_030_st_debt_concentration_trend_zscore_d2(debtc, debt):
    return (_rolling_zscore(_safe_div(debtc, debt), 12, min_periods=4)).diff().diff()

def f24_dbtj_031_debtc_to_cash_avg4_d2(debtc, cashneq):
    return (_safe_div(_avg4(debtc), _avg4(cashneq))).diff().diff()

def f24_dbtj_032_debtc_to_currentassets_avg4_d2(debtc, assetsc):
    return (_safe_div(_avg4(debtc), _avg4(assetsc))).diff().diff()

def f24_dbtj_033_debt_to_ebitda_ttm_d2(debt, ebitda):
    return (_safe_div(_avg4(debt), _ttm(ebitda))).diff().diff()

def f24_dbtj_034_net_debt_to_ebitda_ttm_d2(debt, cashneq, ebitda):
    return (_safe_div(_avg4(debt - cashneq), _ttm(ebitda))).diff().diff()

def f24_dbtj_035_debt_to_ocf_ttm_d2(debt, ncfo):
    return (_safe_div(_avg4(debt), _ttm(ncfo))).diff().diff()

def f24_dbtj_036_debt_to_fcf_ttm_d2(debt, fcf):
    return (_safe_div(_avg4(debt), _ttm(fcf))).diff().diff()

def f24_dbtj_037_debt_to_ebit_ttm_d2(debt, ebit):
    return (_safe_div(_avg4(debt), _ttm(ebit))).diff().diff()

def f24_dbtj_038_debt_to_opinc_ttm_d2(debt, opinc):
    return (_safe_div(_avg4(debt), _ttm(opinc))).diff().diff()

def f24_dbtj_039_interest_coverage_ebit_ttm_d2(ebit, intexp):
    return (_safe_div(_ttm(ebit), _ttm(intexp))).diff().diff()

def f24_dbtj_040_interest_coverage_ebitda_ttm_d2(ebitda, intexp):
    return (_safe_div(_ttm(ebitda), _ttm(intexp))).diff().diff()

def f24_dbtj_041_interest_coverage_ocf_ttm_d2(ncfo, intexp):
    return (_safe_div(_ttm(ncfo), _ttm(intexp))).diff().diff()

def f24_dbtj_042_interest_coverage_yoy_change_d2(ebit, intexp):
    return (_safe_div(_ttm(ebit), _ttm(intexp)) - _safe_div(_ttm(ebit).shift(4), _ttm(intexp).shift(4))).diff().diff()

def f24_dbtj_043_cost_of_debt_proxy_avg4_d2(intexp, debt):
    return (_safe_div(_ttm(intexp), _avg4(debt))).diff().diff()

def f24_dbtj_044_cost_of_debt_yoy_change_d2(intexp, debt):
    return (_safe_div(_ttm(intexp), _avg4(debt)) - _safe_div(_ttm(intexp).shift(4), _avg4(debt).shift(4))).diff().diff()

def f24_dbtj_045_debt_service_capacity_4q_d2(ncfo, intexp, debtc):
    return (_safe_div(_ttm(ncfo), _ttm(intexp) + debtc)).diff().diff()

def f24_dbtj_046_ebitda_minus_interest_to_debt_d2(ebitda, intexp, debt):
    return (_safe_div(_ttm(ebitda) - _ttm(intexp), _avg4(debt))).diff().diff()

def f24_dbtj_047_fcf_minus_interest_to_debt_d2(fcf, intexp, debt):
    return (_safe_div(_ttm(fcf) - _ttm(intexp), _avg4(debt))).diff().diff()

def f24_dbtj_048_coverage_erosion_persistence_8q_d2(ebit, intexp):
    return ((_safe_div(_ttm(ebit), _ttm(intexp)).diff() < 0).astype(float).rolling(8, min_periods=3).mean()).diff().diff()

def f24_dbtj_049_cash_to_debt_avg4_d2(cashneq, debt):
    return (_safe_div(_avg4(cashneq), _avg4(debt))).diff().diff()

def f24_dbtj_050_cash_to_debtc_avg4_d2(cashneq, debtc):
    return (_safe_div(_avg4(cashneq), _avg4(debtc))).diff().diff()

def f24_dbtj_051_cash_runway_quarters_vs_intexp_d2(cashneq, intexp):
    return (_safe_div(cashneq, _avg4(intexp))).diff().diff()

def f24_dbtj_052_liquid_assets_to_debtc_d2(cashneq, investments, debtc):
    return (_safe_div(_avg4(cashneq + investments), _avg4(debtc))).diff().diff()

def f24_dbtj_053_currentratio_avg4_d2(assetsc, liabilitiesc):
    return (_safe_div(_avg4(assetsc), _avg4(liabilitiesc))).diff().diff()

def f24_dbtj_054_quickratio_proxy_avg4_d2(assetsc, inventory, liabilitiesc):
    return (_safe_div(_avg4(assetsc - inventory), _avg4(liabilitiesc))).diff().diff()

def f24_dbtj_055_cash_ratio_avg4_d2(cashneq, liabilitiesc):
    return (_safe_div(_avg4(cashneq), _avg4(liabilitiesc))).diff().diff()

def f24_dbtj_056_currentratio_trend_8q_slope_d2(assetsc, liabilitiesc):
    return (_safe_div(_avg4(assetsc), _avg4(liabilitiesc)).diff(8)).diff().diff()

def f24_dbtj_057_cash_to_debt_zscore_12q_d2(cashneq, debt):
    return (_rolling_zscore(_safe_div(cashneq, debt), 12, min_periods=4)).diff().diff()

def f24_dbtj_058_cash_minus_debtc_to_assets_d2(cashneq, debtc, assets):
    return (_safe_div(_avg4(cashneq - debtc), _avg4(assets))).diff().diff()

def f24_dbtj_059_equity_to_debt_avg4_d2(equity, debt):
    return (_safe_div(_avg4(equity), _avg4(debt))).diff().diff()

def f24_dbtj_060_tangible_equity_to_debt_avg4_d2(equity, intangibles, debt):
    return (_safe_div(_avg4(equity - intangibles), _avg4(debt))).diff().diff()

def f24_dbtj_061_equity_yoy_decline_pct_d2(equity):
    return (-_yoy_pct(_avg4(equity))).diff().diff()

def f24_dbtj_062_equity_trend_slope_8q_d2(equity):
    return (_safe_log_abs(_avg4(equity)).diff(8)).diff().diff()

def f24_dbtj_063_consecutive_quarters_equity_decline_8q_d2(equity):
    return ((equity.diff() < 0).astype(float).rolling(8, min_periods=2).sum()).diff().diff()

def f24_dbtj_064_negative_equity_indicator_avg4_d2(equity):
    return ((_avg4(equity) < 0).astype(float)).diff().diff()

def f24_dbtj_065_goodwill_intangibles_share_of_assets_d2(intangibles, assets):
    return (_safe_div(_avg4(intangibles), _avg4(assets))).diff().diff()

def f24_dbtj_066_intangible_inflation_vs_equity_d2(intangibles, equity):
    return (_safe_div(_avg4(intangibles), _avg4(equity))).diff().diff()

def f24_dbtj_067_retearn_to_debt_trend_d2(retearn, debt):
    return (_safe_div(_avg4(retearn), _avg4(debt))).diff().diff()

def f24_dbtj_068_retearn_yoy_decline_pct_d2(retearn):
    return (-_yoy_pct(_avg4(retearn))).diff().diff()

def f24_dbtj_069_ncff_ttm_to_assets_d2(ncff, assets):
    return (_safe_div(_ttm(ncff), _avg4(assets))).diff().diff()

def f24_dbtj_070_ncff_positive_persistence_8q_d2(ncff):
    return ((ncff > 0).astype(float).rolling(8, min_periods=2).mean()).diff().diff()

def f24_dbtj_071_debt_issuance_proxy_4q_sum_d2(debt):
    return (debt.diff().clip(lower=0).rolling(4, min_periods=1).sum()).diff().diff()

def f24_dbtj_072_debt_repayment_proxy_4q_sum_d2(debt):
    return ((-debt.diff().clip(upper=0)).rolling(4, min_periods=1).sum()).diff().diff()

def f24_dbtj_073_net_debt_issuance_4q_d2(debt):
    return (debt.diff().rolling(4, min_periods=1).sum()).diff().diff()

def f24_dbtj_074_debt_issuance_to_assets_4q_d2(debt, assets):
    return (_safe_div(debt.diff().clip(lower=0).rolling(4, min_periods=1).sum(), _avg4(assets))).diff().diff()

def f24_dbtj_075_debt_issuance_to_capex_4q_d2(debt, capex):
    return (_safe_div(debt.diff().clip(lower=0).rolling(4, min_periods=1).sum(), _ttm(capex).abs())).diff().diff()


DEBT_BUILDUP_TRAJECTORY_D2_REGISTRY_001_075 = {
    "f24_dbtj_001_log_debt_ttm_avg_d2": {"inputs": ["debt"], "func": f24_dbtj_001_log_debt_ttm_avg_d2},
    "f24_dbtj_002_log_net_debt_ttm_avg_d2": {"inputs": ["debt", "cashneq"], "func": f24_dbtj_002_log_net_debt_ttm_avg_d2},
    "f24_dbtj_003_log_debt_minus_log_cash_ttm_d2": {"inputs": ["debt", "cashneq"], "func": f24_dbtj_003_log_debt_minus_log_cash_ttm_d2},
    "f24_dbtj_004_debt_to_assets_avg4_d2": {"inputs": ["debt", "assets"], "func": f24_dbtj_004_debt_to_assets_avg4_d2},
    "f24_dbtj_005_debt_to_equity_avg4_d2": {"inputs": ["debt", "equity"], "func": f24_dbtj_005_debt_to_equity_avg4_d2},
    "f24_dbtj_006_debt_to_capital_avg4_d2": {"inputs": ["debt", "equity"], "func": f24_dbtj_006_debt_to_capital_avg4_d2},
    "f24_dbtj_007_liabilities_to_assets_avg4_d2": {"inputs": ["liabilities", "assets"], "func": f24_dbtj_007_liabilities_to_assets_avg4_d2},
    "f24_dbtj_008_debt_to_tangible_equity_avg4_d2": {"inputs": ["debt", "equity", "intangibles"], "func": f24_dbtj_008_debt_to_tangible_equity_avg4_d2},
    "f24_dbtj_009_net_debt_to_equity_avg4_d2": {"inputs": ["debt", "cashneq", "equity"], "func": f24_dbtj_009_net_debt_to_equity_avg4_d2},
    "f24_dbtj_010_net_debt_to_assets_avg4_d2": {"inputs": ["debt", "cashneq", "assets"], "func": f24_dbtj_010_net_debt_to_assets_avg4_d2},
    "f24_dbtj_011_debt_yoy_pct_smoothed_d2": {"inputs": ["debt"], "func": f24_dbtj_011_debt_yoy_pct_smoothed_d2},
    "f24_dbtj_012_debt_qoq_pct_smoothed_4q_d2": {"inputs": ["debt"], "func": f24_dbtj_012_debt_qoq_pct_smoothed_4q_d2},
    "f24_dbtj_013_debt_cagr_8q_d2": {"inputs": ["debt"], "func": f24_dbtj_013_debt_cagr_8q_d2},
    "f24_dbtj_014_debt_cagr_12q_d2": {"inputs": ["debt"], "func": f24_dbtj_014_debt_cagr_12q_d2},
    "f24_dbtj_015_debt_trend_slope_8q_d2": {"inputs": ["debt"], "func": f24_dbtj_015_debt_trend_slope_8q_d2},
    "f24_dbtj_016_net_debt_yoy_change_to_assets_d2": {"inputs": ["debt", "cashneq", "assets"], "func": f24_dbtj_016_net_debt_yoy_change_to_assets_d2},
    "f24_dbtj_017_debt_growth_minus_revenue_growth_yoy_d2": {"inputs": ["debt", "revenue"], "func": f24_dbtj_017_debt_growth_minus_revenue_growth_yoy_d2},
    "f24_dbtj_018_debt_growth_minus_asset_growth_yoy_d2": {"inputs": ["debt", "assets"], "func": f24_dbtj_018_debt_growth_minus_asset_growth_yoy_d2},
    "f24_dbtj_019_debt_growth_minus_equity_growth_yoy_d2": {"inputs": ["debt", "equity"], "func": f24_dbtj_019_debt_growth_minus_equity_growth_yoy_d2},
    "f24_dbtj_020_debt_growth_minus_ebitda_growth_yoy_d2": {"inputs": ["debt", "ebitda"], "func": f24_dbtj_020_debt_growth_minus_ebitda_growth_yoy_d2},
    "f24_dbtj_021_consecutive_quarters_debt_growth_8q_d2": {"inputs": ["debt"], "func": f24_dbtj_021_consecutive_quarters_debt_growth_8q_d2},
    "f24_dbtj_022_debt_trend_persistence_12q_d2": {"inputs": ["debt"], "func": f24_dbtj_022_debt_trend_persistence_12q_d2},
    "f24_dbtj_023_debtc_share_of_debt_avg4_d2": {"inputs": ["debtc", "debt"], "func": f24_dbtj_023_debtc_share_of_debt_avg4_d2},
    "f24_dbtj_024_debtnc_share_of_debt_avg4_d2": {"inputs": ["debtnc", "debt"], "func": f24_dbtj_024_debtnc_share_of_debt_avg4_d2},
    "f24_dbtj_025_st_debt_share_change_yoy_d2": {"inputs": ["debtc", "debt"], "func": f24_dbtj_025_st_debt_share_change_yoy_d2},
    "f24_dbtj_026_debtc_to_assets_trend_d2": {"inputs": ["debtc", "assets"], "func": f24_dbtj_026_debtc_to_assets_trend_d2},
    "f24_dbtj_027_debtc_yoy_pct_smoothed_d2": {"inputs": ["debtc"], "func": f24_dbtj_027_debtc_yoy_pct_smoothed_d2},
    "f24_dbtj_028_debtc_growing_faster_than_debtnc_d2": {"inputs": ["debtc", "debtnc"], "func": f24_dbtj_028_debtc_growing_faster_than_debtnc_d2},
    "f24_dbtj_029_refinancing_wall_8q_d2": {"inputs": ["debtc", "debt"], "func": f24_dbtj_029_refinancing_wall_8q_d2},
    "f24_dbtj_030_st_debt_concentration_trend_zscore_d2": {"inputs": ["debtc", "debt"], "func": f24_dbtj_030_st_debt_concentration_trend_zscore_d2},
    "f24_dbtj_031_debtc_to_cash_avg4_d2": {"inputs": ["debtc", "cashneq"], "func": f24_dbtj_031_debtc_to_cash_avg4_d2},
    "f24_dbtj_032_debtc_to_currentassets_avg4_d2": {"inputs": ["debtc", "assetsc"], "func": f24_dbtj_032_debtc_to_currentassets_avg4_d2},
    "f24_dbtj_033_debt_to_ebitda_ttm_d2": {"inputs": ["debt", "ebitda"], "func": f24_dbtj_033_debt_to_ebitda_ttm_d2},
    "f24_dbtj_034_net_debt_to_ebitda_ttm_d2": {"inputs": ["debt", "cashneq", "ebitda"], "func": f24_dbtj_034_net_debt_to_ebitda_ttm_d2},
    "f24_dbtj_035_debt_to_ocf_ttm_d2": {"inputs": ["debt", "ncfo"], "func": f24_dbtj_035_debt_to_ocf_ttm_d2},
    "f24_dbtj_036_debt_to_fcf_ttm_d2": {"inputs": ["debt", "fcf"], "func": f24_dbtj_036_debt_to_fcf_ttm_d2},
    "f24_dbtj_037_debt_to_ebit_ttm_d2": {"inputs": ["debt", "ebit"], "func": f24_dbtj_037_debt_to_ebit_ttm_d2},
    "f24_dbtj_038_debt_to_opinc_ttm_d2": {"inputs": ["debt", "opinc"], "func": f24_dbtj_038_debt_to_opinc_ttm_d2},
    "f24_dbtj_039_interest_coverage_ebit_ttm_d2": {"inputs": ["ebit", "intexp"], "func": f24_dbtj_039_interest_coverage_ebit_ttm_d2},
    "f24_dbtj_040_interest_coverage_ebitda_ttm_d2": {"inputs": ["ebitda", "intexp"], "func": f24_dbtj_040_interest_coverage_ebitda_ttm_d2},
    "f24_dbtj_041_interest_coverage_ocf_ttm_d2": {"inputs": ["ncfo", "intexp"], "func": f24_dbtj_041_interest_coverage_ocf_ttm_d2},
    "f24_dbtj_042_interest_coverage_yoy_change_d2": {"inputs": ["ebit", "intexp"], "func": f24_dbtj_042_interest_coverage_yoy_change_d2},
    "f24_dbtj_043_cost_of_debt_proxy_avg4_d2": {"inputs": ["intexp", "debt"], "func": f24_dbtj_043_cost_of_debt_proxy_avg4_d2},
    "f24_dbtj_044_cost_of_debt_yoy_change_d2": {"inputs": ["intexp", "debt"], "func": f24_dbtj_044_cost_of_debt_yoy_change_d2},
    "f24_dbtj_045_debt_service_capacity_4q_d2": {"inputs": ["ncfo", "intexp", "debtc"], "func": f24_dbtj_045_debt_service_capacity_4q_d2},
    "f24_dbtj_046_ebitda_minus_interest_to_debt_d2": {"inputs": ["ebitda", "intexp", "debt"], "func": f24_dbtj_046_ebitda_minus_interest_to_debt_d2},
    "f24_dbtj_047_fcf_minus_interest_to_debt_d2": {"inputs": ["fcf", "intexp", "debt"], "func": f24_dbtj_047_fcf_minus_interest_to_debt_d2},
    "f24_dbtj_048_coverage_erosion_persistence_8q_d2": {"inputs": ["ebit", "intexp"], "func": f24_dbtj_048_coverage_erosion_persistence_8q_d2},
    "f24_dbtj_049_cash_to_debt_avg4_d2": {"inputs": ["cashneq", "debt"], "func": f24_dbtj_049_cash_to_debt_avg4_d2},
    "f24_dbtj_050_cash_to_debtc_avg4_d2": {"inputs": ["cashneq", "debtc"], "func": f24_dbtj_050_cash_to_debtc_avg4_d2},
    "f24_dbtj_051_cash_runway_quarters_vs_intexp_d2": {"inputs": ["cashneq", "intexp"], "func": f24_dbtj_051_cash_runway_quarters_vs_intexp_d2},
    "f24_dbtj_052_liquid_assets_to_debtc_d2": {"inputs": ["cashneq", "investments", "debtc"], "func": f24_dbtj_052_liquid_assets_to_debtc_d2},
    "f24_dbtj_053_currentratio_avg4_d2": {"inputs": ["assetsc", "liabilitiesc"], "func": f24_dbtj_053_currentratio_avg4_d2},
    "f24_dbtj_054_quickratio_proxy_avg4_d2": {"inputs": ["assetsc", "inventory", "liabilitiesc"], "func": f24_dbtj_054_quickratio_proxy_avg4_d2},
    "f24_dbtj_055_cash_ratio_avg4_d2": {"inputs": ["cashneq", "liabilitiesc"], "func": f24_dbtj_055_cash_ratio_avg4_d2},
    "f24_dbtj_056_currentratio_trend_8q_slope_d2": {"inputs": ["assetsc", "liabilitiesc"], "func": f24_dbtj_056_currentratio_trend_8q_slope_d2},
    "f24_dbtj_057_cash_to_debt_zscore_12q_d2": {"inputs": ["cashneq", "debt"], "func": f24_dbtj_057_cash_to_debt_zscore_12q_d2},
    "f24_dbtj_058_cash_minus_debtc_to_assets_d2": {"inputs": ["cashneq", "debtc", "assets"], "func": f24_dbtj_058_cash_minus_debtc_to_assets_d2},
    "f24_dbtj_059_equity_to_debt_avg4_d2": {"inputs": ["equity", "debt"], "func": f24_dbtj_059_equity_to_debt_avg4_d2},
    "f24_dbtj_060_tangible_equity_to_debt_avg4_d2": {"inputs": ["equity", "intangibles", "debt"], "func": f24_dbtj_060_tangible_equity_to_debt_avg4_d2},
    "f24_dbtj_061_equity_yoy_decline_pct_d2": {"inputs": ["equity"], "func": f24_dbtj_061_equity_yoy_decline_pct_d2},
    "f24_dbtj_062_equity_trend_slope_8q_d2": {"inputs": ["equity"], "func": f24_dbtj_062_equity_trend_slope_8q_d2},
    "f24_dbtj_063_consecutive_quarters_equity_decline_8q_d2": {"inputs": ["equity"], "func": f24_dbtj_063_consecutive_quarters_equity_decline_8q_d2},
    "f24_dbtj_064_negative_equity_indicator_avg4_d2": {"inputs": ["equity"], "func": f24_dbtj_064_negative_equity_indicator_avg4_d2},
    "f24_dbtj_065_goodwill_intangibles_share_of_assets_d2": {"inputs": ["intangibles", "assets"], "func": f24_dbtj_065_goodwill_intangibles_share_of_assets_d2},
    "f24_dbtj_066_intangible_inflation_vs_equity_d2": {"inputs": ["intangibles", "equity"], "func": f24_dbtj_066_intangible_inflation_vs_equity_d2},
    "f24_dbtj_067_retearn_to_debt_trend_d2": {"inputs": ["retearn", "debt"], "func": f24_dbtj_067_retearn_to_debt_trend_d2},
    "f24_dbtj_068_retearn_yoy_decline_pct_d2": {"inputs": ["retearn"], "func": f24_dbtj_068_retearn_yoy_decline_pct_d2},
    "f24_dbtj_069_ncff_ttm_to_assets_d2": {"inputs": ["ncff", "assets"], "func": f24_dbtj_069_ncff_ttm_to_assets_d2},
    "f24_dbtj_070_ncff_positive_persistence_8q_d2": {"inputs": ["ncff"], "func": f24_dbtj_070_ncff_positive_persistence_8q_d2},
    "f24_dbtj_071_debt_issuance_proxy_4q_sum_d2": {"inputs": ["debt"], "func": f24_dbtj_071_debt_issuance_proxy_4q_sum_d2},
    "f24_dbtj_072_debt_repayment_proxy_4q_sum_d2": {"inputs": ["debt"], "func": f24_dbtj_072_debt_repayment_proxy_4q_sum_d2},
    "f24_dbtj_073_net_debt_issuance_4q_d2": {"inputs": ["debt"], "func": f24_dbtj_073_net_debt_issuance_4q_d2},
    "f24_dbtj_074_debt_issuance_to_assets_4q_d2": {"inputs": ["debt", "assets"], "func": f24_dbtj_074_debt_issuance_to_assets_4q_d2},
    "f24_dbtj_075_debt_issuance_to_capex_4q_d2": {"inputs": ["debt", "capex"], "func": f24_dbtj_075_debt_issuance_to_capex_4q_d2},
}
