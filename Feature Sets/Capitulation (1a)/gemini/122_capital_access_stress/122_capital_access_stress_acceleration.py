"""
122_capital_access_stress — Acceleration (3rd Derivatives)
Domain: capital_access_stress
Asset class: Equities
Target context: Capitulation
"""
import numpy as np
import pandas as pd

# ── Utility helpers ──────────────────────────────────────────────────────────
_TD_YEAR = 252
_TD_HALF = 126
_TD_QTR = 63
_TD_MON = 21
_TD_WEEK = 5
_EPS = 1e-9

def _safe_div(a: pd.Series, b: pd.Series) -> pd.Series:
    return a / b.replace(0, _EPS)

def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).mean()

def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).max()

def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).min()

def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).std().fillna(0)

def _zscore_rolling(s: pd.Series, w: int) -> pd.Series:
    m = _rolling_mean(s, w)
    sd = _rolling_std(s, w)
    return _safe_div((s - m), sd)

def _rank_pct(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).rank(pct=True)

# ── Feature functions ────────────────────────────────────────────────────────

def cast_301_interest_burden_proxy_accel_5d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_301_interest_burden_proxy_accel_5d
    ECONOMIC RATIONALE: Acceleration of interest_burden_proxy. Estimated interest expense relative to free cash flow.
    """
    return ((debt * 0.08) / fcf.replace(0, 1e-9)).diff(5).diff(_TD_MON)

def cast_302_interest_burden_proxy_accel_21d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_302_interest_burden_proxy_accel_21d
    ECONOMIC RATIONALE: Acceleration of interest_burden_proxy. Estimated interest expense relative to free cash flow.
    """
    return ((debt * 0.08) / fcf.replace(0, 1e-9)).diff(21).diff(_TD_MON)

def cast_303_interest_burden_proxy_accel_63d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_303_interest_burden_proxy_accel_63d
    ECONOMIC RATIONALE: Acceleration of interest_burden_proxy. Estimated interest expense relative to free cash flow.
    """
    return ((debt * 0.08) / fcf.replace(0, 1e-9)).diff(63).diff(_TD_MON)

def cast_304_interest_burden_proxy_accel_126d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_304_interest_burden_proxy_accel_126d
    ECONOMIC RATIONALE: Acceleration of interest_burden_proxy. Estimated interest expense relative to free cash flow.
    """
    return ((debt * 0.08) / fcf.replace(0, 1e-9)).diff(126).diff(_TD_MON)

def cast_305_interest_burden_proxy_accel_252d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_305_interest_burden_proxy_accel_252d
    ECONOMIC RATIONALE: Acceleration of interest_burden_proxy. Estimated interest expense relative to free cash flow.
    """
    return ((debt * 0.08) / fcf.replace(0, 1e-9)).diff(252).diff(_TD_MON)

def cast_306_debt_to_equity_z_accel_5d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_306_debt_to_equity_z_accel_5d
    ECONOMIC RATIONALE: Acceleration of debt_to_equity_z. Abnormality of current debt-to-equity ratio.
    """
    return (_zscore_rolling(debt / equity.replace(0, 1e-9), 252)).diff(5).diff(_TD_MON)

def cast_307_debt_to_equity_z_accel_21d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_307_debt_to_equity_z_accel_21d
    ECONOMIC RATIONALE: Acceleration of debt_to_equity_z. Abnormality of current debt-to-equity ratio.
    """
    return (_zscore_rolling(debt / equity.replace(0, 1e-9), 252)).diff(21).diff(_TD_MON)

def cast_308_debt_to_equity_z_accel_63d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_308_debt_to_equity_z_accel_63d
    ECONOMIC RATIONALE: Acceleration of debt_to_equity_z. Abnormality of current debt-to-equity ratio.
    """
    return (_zscore_rolling(debt / equity.replace(0, 1e-9), 252)).diff(63).diff(_TD_MON)

def cast_309_debt_to_equity_z_accel_126d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_309_debt_to_equity_z_accel_126d
    ECONOMIC RATIONALE: Acceleration of debt_to_equity_z. Abnormality of current debt-to-equity ratio.
    """
    return (_zscore_rolling(debt / equity.replace(0, 1e-9), 252)).diff(126).diff(_TD_MON)

def cast_310_debt_to_equity_z_accel_252d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_310_debt_to_equity_z_accel_252d
    ECONOMIC RATIONALE: Acceleration of debt_to_equity_z. Abnormality of current debt-to-equity ratio.
    """
    return (_zscore_rolling(debt / equity.replace(0, 1e-9), 252)).diff(252).diff(_TD_MON)

def cast_311_equity_funding_risk_accel_5d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_311_equity_funding_risk_accel_5d
    ECONOMIC RATIONALE: Acceleration of equity_funding_risk. Capacity to raise capital via equity issuance.
    """
    return (marketcap / debt.replace(0, 1e-9)).diff(5).diff(_TD_MON)

def cast_312_equity_funding_risk_accel_21d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_312_equity_funding_risk_accel_21d
    ECONOMIC RATIONALE: Acceleration of equity_funding_risk. Capacity to raise capital via equity issuance.
    """
    return (marketcap / debt.replace(0, 1e-9)).diff(21).diff(_TD_MON)

def cast_313_equity_funding_risk_accel_63d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_313_equity_funding_risk_accel_63d
    ECONOMIC RATIONALE: Acceleration of equity_funding_risk. Capacity to raise capital via equity issuance.
    """
    return (marketcap / debt.replace(0, 1e-9)).diff(63).diff(_TD_MON)

def cast_314_equity_funding_risk_accel_126d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_314_equity_funding_risk_accel_126d
    ECONOMIC RATIONALE: Acceleration of equity_funding_risk. Capacity to raise capital via equity issuance.
    """
    return (marketcap / debt.replace(0, 1e-9)).diff(126).diff(_TD_MON)

def cast_315_equity_funding_risk_accel_252d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_315_equity_funding_risk_accel_252d
    ECONOMIC RATIONALE: Acceleration of equity_funding_risk. Capacity to raise capital via equity issuance.
    """
    return (marketcap / debt.replace(0, 1e-9)).diff(252).diff(_TD_MON)

def cast_316_debt_acceleration_accel_5d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_316_debt_acceleration_accel_5d
    ECONOMIC RATIONALE: Acceleration of debt_acceleration. Speed of new debt accumulation.
    """
    return (debt.pct_change(63)).diff(5).diff(_TD_MON)

def cast_317_debt_acceleration_accel_21d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_317_debt_acceleration_accel_21d
    ECONOMIC RATIONALE: Acceleration of debt_acceleration. Speed of new debt accumulation.
    """
    return (debt.pct_change(63)).diff(21).diff(_TD_MON)

def cast_318_debt_acceleration_accel_63d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_318_debt_acceleration_accel_63d
    ECONOMIC RATIONALE: Acceleration of debt_acceleration. Speed of new debt accumulation.
    """
    return (debt.pct_change(63)).diff(63).diff(_TD_MON)

def cast_319_debt_acceleration_accel_126d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_319_debt_acceleration_accel_126d
    ECONOMIC RATIONALE: Acceleration of debt_acceleration. Speed of new debt accumulation.
    """
    return (debt.pct_change(63)).diff(126).diff(_TD_MON)

def cast_320_debt_acceleration_accel_252d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_320_debt_acceleration_accel_252d
    ECONOMIC RATIONALE: Acceleration of debt_acceleration. Speed of new debt accumulation.
    """
    return (debt.pct_change(63)).diff(252).diff(_TD_MON)

def cast_321_fcf_debt_service_accel_5d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_321_fcf_debt_service_accel_5d
    ECONOMIC RATIONALE: Acceleration of fcf_debt_service. Ability to amortize debt from cash flow.
    """
    return (fcf / debt.replace(0, 1e-9)).diff(5).diff(_TD_MON)

def cast_322_fcf_debt_service_accel_21d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_322_fcf_debt_service_accel_21d
    ECONOMIC RATIONALE: Acceleration of fcf_debt_service. Ability to amortize debt from cash flow.
    """
    return (fcf / debt.replace(0, 1e-9)).diff(21).diff(_TD_MON)

def cast_323_fcf_debt_service_accel_63d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_323_fcf_debt_service_accel_63d
    ECONOMIC RATIONALE: Acceleration of fcf_debt_service. Ability to amortize debt from cash flow.
    """
    return (fcf / debt.replace(0, 1e-9)).diff(63).diff(_TD_MON)

def cast_324_fcf_debt_service_accel_126d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_324_fcf_debt_service_accel_126d
    ECONOMIC RATIONALE: Acceleration of fcf_debt_service. Ability to amortize debt from cash flow.
    """
    return (fcf / debt.replace(0, 1e-9)).diff(126).diff(_TD_MON)

def cast_325_fcf_debt_service_accel_252d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_325_fcf_debt_service_accel_252d
    ECONOMIC RATIONALE: Acceleration of fcf_debt_service. Ability to amortize debt from cash flow.
    """
    return (fcf / debt.replace(0, 1e-9)).diff(252).diff(_TD_MON)

def cast_326_capital_access_score_accel_5d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_326_capital_access_score_accel_5d
    ECONOMIC RATIONALE: Acceleration of capital_access_score. Divergence between market valuation and debt growth.
    """
    return (marketcap.pct_change(63) - debt.pct_change(63)).diff(5).diff(_TD_MON)

def cast_327_capital_access_score_accel_21d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_327_capital_access_score_accel_21d
    ECONOMIC RATIONALE: Acceleration of capital_access_score. Divergence between market valuation and debt growth.
    """
    return (marketcap.pct_change(63) - debt.pct_change(63)).diff(21).diff(_TD_MON)

def cast_328_capital_access_score_accel_63d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_328_capital_access_score_accel_63d
    ECONOMIC RATIONALE: Acceleration of capital_access_score. Divergence between market valuation and debt growth.
    """
    return (marketcap.pct_change(63) - debt.pct_change(63)).diff(63).diff(_TD_MON)

def cast_329_capital_access_score_accel_126d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_329_capital_access_score_accel_126d
    ECONOMIC RATIONALE: Acceleration of capital_access_score. Divergence between market valuation and debt growth.
    """
    return (marketcap.pct_change(63) - debt.pct_change(63)).diff(126).diff(_TD_MON)

def cast_330_capital_access_score_accel_252d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_330_capital_access_score_accel_252d
    ECONOMIC RATIONALE: Acceleration of capital_access_score. Divergence between market valuation and debt growth.
    """
    return (marketcap.pct_change(63) - debt.pct_change(63)).diff(252).diff(_TD_MON)

def cast_331_debt_drawdown_impact_accel_5d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_331_debt_drawdown_impact_accel_5d
    ECONOMIC RATIONALE: Acceleration of debt_drawdown_impact. Debt load relative to peak firm value.
    """
    return (debt / marketcap.rolling(252).max().replace(0, 1e-9)).diff(5).diff(_TD_MON)

def cast_332_debt_drawdown_impact_accel_21d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_332_debt_drawdown_impact_accel_21d
    ECONOMIC RATIONALE: Acceleration of debt_drawdown_impact. Debt load relative to peak firm value.
    """
    return (debt / marketcap.rolling(252).max().replace(0, 1e-9)).diff(21).diff(_TD_MON)

def cast_333_debt_drawdown_impact_accel_63d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_333_debt_drawdown_impact_accel_63d
    ECONOMIC RATIONALE: Acceleration of debt_drawdown_impact. Debt load relative to peak firm value.
    """
    return (debt / marketcap.rolling(252).max().replace(0, 1e-9)).diff(63).diff(_TD_MON)

def cast_334_debt_drawdown_impact_accel_126d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_334_debt_drawdown_impact_accel_126d
    ECONOMIC RATIONALE: Acceleration of debt_drawdown_impact. Debt load relative to peak firm value.
    """
    return (debt / marketcap.rolling(252).max().replace(0, 1e-9)).diff(126).diff(_TD_MON)

def cast_335_debt_drawdown_impact_accel_252d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_335_debt_drawdown_impact_accel_252d
    ECONOMIC RATIONALE: Acceleration of debt_drawdown_impact. Debt load relative to peak firm value.
    """
    return (debt / marketcap.rolling(252).max().replace(0, 1e-9)).diff(252).diff(_TD_MON)

def cast_336_refinancing_risk_proxy_accel_5d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_336_refinancing_risk_proxy_accel_5d
    ECONOMIC RATIONALE: Acceleration of refinancing_risk_proxy. High risk of inability to refinance maturing debt.
    """
    return ((debt > equity).astype(float) * (marketcap < 100e6).astype(float)).diff(5).diff(_TD_MON)

def cast_337_refinancing_risk_proxy_accel_21d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_337_refinancing_risk_proxy_accel_21d
    ECONOMIC RATIONALE: Acceleration of refinancing_risk_proxy. High risk of inability to refinance maturing debt.
    """
    return ((debt > equity).astype(float) * (marketcap < 100e6).astype(float)).diff(21).diff(_TD_MON)

def cast_338_refinancing_risk_proxy_accel_63d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_338_refinancing_risk_proxy_accel_63d
    ECONOMIC RATIONALE: Acceleration of refinancing_risk_proxy. High risk of inability to refinance maturing debt.
    """
    return ((debt > equity).astype(float) * (marketcap < 100e6).astype(float)).diff(63).diff(_TD_MON)

def cast_339_refinancing_risk_proxy_accel_126d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_339_refinancing_risk_proxy_accel_126d
    ECONOMIC RATIONALE: Acceleration of refinancing_risk_proxy. High risk of inability to refinance maturing debt.
    """
    return ((debt > equity).astype(float) * (marketcap < 100e6).astype(float)).diff(126).diff(_TD_MON)

def cast_340_refinancing_risk_proxy_accel_252d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_340_refinancing_risk_proxy_accel_252d
    ECONOMIC RATIONALE: Acceleration of refinancing_risk_proxy. High risk of inability to refinance maturing debt.
    """
    return ((debt > equity).astype(float) * (marketcap < 100e6).astype(float)).diff(252).diff(_TD_MON)

def cast_341_debt_to_assets_momentum_accel_5d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_341_debt_to_assets_momentum_accel_5d
    ECONOMIC RATIONALE: Acceleration of debt_to_assets_momentum. Trend in the proportion of assets funded by debt.
    """
    return ((debt/assets).diff(63)).diff(5).diff(_TD_MON)

def cast_342_debt_to_assets_momentum_accel_21d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_342_debt_to_assets_momentum_accel_21d
    ECONOMIC RATIONALE: Acceleration of debt_to_assets_momentum. Trend in the proportion of assets funded by debt.
    """
    return ((debt/assets).diff(63)).diff(21).diff(_TD_MON)

def cast_343_debt_to_assets_momentum_accel_63d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_343_debt_to_assets_momentum_accel_63d
    ECONOMIC RATIONALE: Acceleration of debt_to_assets_momentum. Trend in the proportion of assets funded by debt.
    """
    return ((debt/assets).diff(63)).diff(63).diff(_TD_MON)

def cast_344_debt_to_assets_momentum_accel_126d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_344_debt_to_assets_momentum_accel_126d
    ECONOMIC RATIONALE: Acceleration of debt_to_assets_momentum. Trend in the proportion of assets funded by debt.
    """
    return ((debt/assets).diff(63)).diff(126).diff(_TD_MON)

def cast_345_debt_to_assets_momentum_accel_252d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_345_debt_to_assets_momentum_accel_252d
    ECONOMIC RATIONALE: Acceleration of debt_to_assets_momentum. Trend in the proportion of assets funded by debt.
    """
    return ((debt/assets).diff(63)).diff(252).diff(_TD_MON)

def cast_346_fcf_yield_vs_debt_accel_5d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_346_fcf_yield_vs_debt_accel_5d
    ECONOMIC RATIONALE: Acceleration of fcf_yield_vs_debt. Cash flow yield net of debt-to-cap ratio.
    """
    return ((fcf/marketcap) - (debt/marketcap)).diff(5).diff(_TD_MON)

def cast_347_fcf_yield_vs_debt_accel_21d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_347_fcf_yield_vs_debt_accel_21d
    ECONOMIC RATIONALE: Acceleration of fcf_yield_vs_debt. Cash flow yield net of debt-to-cap ratio.
    """
    return ((fcf/marketcap) - (debt/marketcap)).diff(21).diff(_TD_MON)

def cast_348_fcf_yield_vs_debt_accel_63d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_348_fcf_yield_vs_debt_accel_63d
    ECONOMIC RATIONALE: Acceleration of fcf_yield_vs_debt. Cash flow yield net of debt-to-cap ratio.
    """
    return ((fcf/marketcap) - (debt/marketcap)).diff(63).diff(_TD_MON)

def cast_349_fcf_yield_vs_debt_accel_126d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_349_fcf_yield_vs_debt_accel_126d
    ECONOMIC RATIONALE: Acceleration of fcf_yield_vs_debt. Cash flow yield net of debt-to-cap ratio.
    """
    return ((fcf/marketcap) - (debt/marketcap)).diff(126).diff(_TD_MON)

def cast_350_fcf_yield_vs_debt_accel_252d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_350_fcf_yield_vs_debt_accel_252d
    ECONOMIC RATIONALE: Acceleration of fcf_yield_vs_debt. Cash flow yield net of debt-to-cap ratio.
    """
    return ((fcf/marketcap) - (debt/marketcap)).diff(252).diff(_TD_MON)

def cast_351_capital_structure_z_accel_5d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_351_capital_structure_z_accel_5d
    ECONOMIC RATIONALE: Acceleration of capital_structure_z. Z-score of debt within the capital structure.
    """
    return (_zscore_rolling(debt/(debt+equity).replace(0, 1e-9), 252)).diff(5).diff(_TD_MON)

def cast_352_capital_structure_z_accel_21d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_352_capital_structure_z_accel_21d
    ECONOMIC RATIONALE: Acceleration of capital_structure_z. Z-score of debt within the capital structure.
    """
    return (_zscore_rolling(debt/(debt+equity).replace(0, 1e-9), 252)).diff(21).diff(_TD_MON)

def cast_353_capital_structure_z_accel_63d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_353_capital_structure_z_accel_63d
    ECONOMIC RATIONALE: Acceleration of capital_structure_z. Z-score of debt within the capital structure.
    """
    return (_zscore_rolling(debt/(debt+equity).replace(0, 1e-9), 252)).diff(63).diff(_TD_MON)

def cast_354_capital_structure_z_accel_126d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_354_capital_structure_z_accel_126d
    ECONOMIC RATIONALE: Acceleration of capital_structure_z. Z-score of debt within the capital structure.
    """
    return (_zscore_rolling(debt/(debt+equity).replace(0, 1e-9), 252)).diff(126).diff(_TD_MON)

def cast_355_capital_structure_z_accel_252d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_355_capital_structure_z_accel_252d
    ECONOMIC RATIONALE: Acceleration of capital_structure_z. Z-score of debt within the capital structure.
    """
    return (_zscore_rolling(debt/(debt+equity).replace(0, 1e-9), 252)).diff(252).diff(_TD_MON)

def cast_356_equity_value_erosion_accel_5d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_356_equity_value_erosion_accel_5d
    ECONOMIC RATIONALE: Acceleration of equity_value_erosion. Destruction of book value relative to market price.
    """
    return (equity.diff(252) / marketcap.replace(0, 1e-9)).diff(5).diff(_TD_MON)

def cast_357_equity_value_erosion_accel_21d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_357_equity_value_erosion_accel_21d
    ECONOMIC RATIONALE: Acceleration of equity_value_erosion. Destruction of book value relative to market price.
    """
    return (equity.diff(252) / marketcap.replace(0, 1e-9)).diff(21).diff(_TD_MON)

def cast_358_equity_value_erosion_accel_63d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_358_equity_value_erosion_accel_63d
    ECONOMIC RATIONALE: Acceleration of equity_value_erosion. Destruction of book value relative to market price.
    """
    return (equity.diff(252) / marketcap.replace(0, 1e-9)).diff(63).diff(_TD_MON)

def cast_359_equity_value_erosion_accel_126d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_359_equity_value_erosion_accel_126d
    ECONOMIC RATIONALE: Acceleration of equity_value_erosion. Destruction of book value relative to market price.
    """
    return (equity.diff(252) / marketcap.replace(0, 1e-9)).diff(126).diff(_TD_MON)

def cast_360_equity_value_erosion_accel_252d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_360_equity_value_erosion_accel_252d
    ECONOMIC RATIONALE: Acceleration of equity_value_erosion. Destruction of book value relative to market price.
    """
    return (equity.diff(252) / marketcap.replace(0, 1e-9)).diff(252).diff(_TD_MON)

def cast_361_debt_burden_vol_accel_5d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_361_debt_burden_vol_accel_5d
    ECONOMIC RATIONALE: Acceleration of debt_burden_vol. Price volatility amplified by debt-to-market-cap ratio.
    """
    return (close.rolling(21).std() * (debt/marketcap.replace(0, 1e-9))).diff(5).diff(_TD_MON)

def cast_362_debt_burden_vol_accel_21d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_362_debt_burden_vol_accel_21d
    ECONOMIC RATIONALE: Acceleration of debt_burden_vol. Price volatility amplified by debt-to-market-cap ratio.
    """
    return (close.rolling(21).std() * (debt/marketcap.replace(0, 1e-9))).diff(21).diff(_TD_MON)

def cast_363_debt_burden_vol_accel_63d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_363_debt_burden_vol_accel_63d
    ECONOMIC RATIONALE: Acceleration of debt_burden_vol. Price volatility amplified by debt-to-market-cap ratio.
    """
    return (close.rolling(21).std() * (debt/marketcap.replace(0, 1e-9))).diff(63).diff(_TD_MON)

def cast_364_debt_burden_vol_accel_126d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_364_debt_burden_vol_accel_126d
    ECONOMIC RATIONALE: Acceleration of debt_burden_vol. Price volatility amplified by debt-to-market-cap ratio.
    """
    return (close.rolling(21).std() * (debt/marketcap.replace(0, 1e-9))).diff(126).diff(_TD_MON)

def cast_365_debt_burden_vol_accel_252d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_365_debt_burden_vol_accel_252d
    ECONOMIC RATIONALE: Acceleration of debt_burden_vol. Price volatility amplified by debt-to-market-cap ratio.
    """
    return (close.rolling(21).std() * (debt/marketcap.replace(0, 1e-9))).diff(252).diff(_TD_MON)

def cast_366_capital_stress_index_accel_5d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_366_capital_stress_index_accel_5d
    ECONOMIC RATIONALE: Acceleration of capital_stress_index. Debt growth relative to cash flow capacity.
    """
    return (debt.pct_change(21) / fcf.rolling(63).mean().abs().replace(0, 1e-9)).diff(5).diff(_TD_MON)

def cast_367_capital_stress_index_accel_21d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_367_capital_stress_index_accel_21d
    ECONOMIC RATIONALE: Acceleration of capital_stress_index. Debt growth relative to cash flow capacity.
    """
    return (debt.pct_change(21) / fcf.rolling(63).mean().abs().replace(0, 1e-9)).diff(21).diff(_TD_MON)

def cast_368_capital_stress_index_accel_63d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_368_capital_stress_index_accel_63d
    ECONOMIC RATIONALE: Acceleration of capital_stress_index. Debt growth relative to cash flow capacity.
    """
    return (debt.pct_change(21) / fcf.rolling(63).mean().abs().replace(0, 1e-9)).diff(63).diff(_TD_MON)

def cast_369_capital_stress_index_accel_126d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_369_capital_stress_index_accel_126d
    ECONOMIC RATIONALE: Acceleration of capital_stress_index. Debt growth relative to cash flow capacity.
    """
    return (debt.pct_change(21) / fcf.rolling(63).mean().abs().replace(0, 1e-9)).diff(126).diff(_TD_MON)

def cast_370_capital_stress_index_accel_252d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_370_capital_stress_index_accel_252d
    ECONOMIC RATIONALE: Acceleration of capital_stress_index. Debt growth relative to cash flow capacity.
    """
    return (debt.pct_change(21) / fcf.rolling(63).mean().abs().replace(0, 1e-9)).diff(252).diff(_TD_MON)

def cast_371_solvency_cushion_accel_5d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_371_solvency_cushion_accel_5d
    ECONOMIC RATIONALE: Acceleration of solvency_cushion. Proportion of assets funded by shareholders.
    """
    return (equity / assets.replace(0, 1e-9)).diff(5).diff(_TD_MON)

def cast_372_solvency_cushion_accel_21d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_372_solvency_cushion_accel_21d
    ECONOMIC RATIONALE: Acceleration of solvency_cushion. Proportion of assets funded by shareholders.
    """
    return (equity / assets.replace(0, 1e-9)).diff(21).diff(_TD_MON)

def cast_373_solvency_cushion_accel_63d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_373_solvency_cushion_accel_63d
    ECONOMIC RATIONALE: Acceleration of solvency_cushion. Proportion of assets funded by shareholders.
    """
    return (equity / assets.replace(0, 1e-9)).diff(63).diff(_TD_MON)

def cast_374_solvency_cushion_accel_126d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_374_solvency_cushion_accel_126d
    ECONOMIC RATIONALE: Acceleration of solvency_cushion. Proportion of assets funded by shareholders.
    """
    return (equity / assets.replace(0, 1e-9)).diff(126).diff(_TD_MON)

def cast_375_solvency_cushion_accel_252d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_375_solvency_cushion_accel_252d
    ECONOMIC RATIONALE: Acceleration of solvency_cushion. Proportion of assets funded by shareholders.
    """
    return (equity / assets.replace(0, 1e-9)).diff(252).diff(_TD_MON)

# ── Registry ──────────────────────────────────────────────────────────────────
V122_REGISTRY_ACCEL = {
    "cast_301_interest_burden_proxy_accel_5d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_301_interest_burden_proxy_accel_5d},
    "cast_302_interest_burden_proxy_accel_21d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_302_interest_burden_proxy_accel_21d},
    "cast_303_interest_burden_proxy_accel_63d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_303_interest_burden_proxy_accel_63d},
    "cast_304_interest_burden_proxy_accel_126d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_304_interest_burden_proxy_accel_126d},
    "cast_305_interest_burden_proxy_accel_252d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_305_interest_burden_proxy_accel_252d},
    "cast_306_debt_to_equity_z_accel_5d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_306_debt_to_equity_z_accel_5d},
    "cast_307_debt_to_equity_z_accel_21d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_307_debt_to_equity_z_accel_21d},
    "cast_308_debt_to_equity_z_accel_63d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_308_debt_to_equity_z_accel_63d},
    "cast_309_debt_to_equity_z_accel_126d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_309_debt_to_equity_z_accel_126d},
    "cast_310_debt_to_equity_z_accel_252d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_310_debt_to_equity_z_accel_252d},
    "cast_311_equity_funding_risk_accel_5d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_311_equity_funding_risk_accel_5d},
    "cast_312_equity_funding_risk_accel_21d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_312_equity_funding_risk_accel_21d},
    "cast_313_equity_funding_risk_accel_63d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_313_equity_funding_risk_accel_63d},
    "cast_314_equity_funding_risk_accel_126d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_314_equity_funding_risk_accel_126d},
    "cast_315_equity_funding_risk_accel_252d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_315_equity_funding_risk_accel_252d},
    "cast_316_debt_acceleration_accel_5d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_316_debt_acceleration_accel_5d},
    "cast_317_debt_acceleration_accel_21d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_317_debt_acceleration_accel_21d},
    "cast_318_debt_acceleration_accel_63d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_318_debt_acceleration_accel_63d},
    "cast_319_debt_acceleration_accel_126d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_319_debt_acceleration_accel_126d},
    "cast_320_debt_acceleration_accel_252d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_320_debt_acceleration_accel_252d},
    "cast_321_fcf_debt_service_accel_5d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_321_fcf_debt_service_accel_5d},
    "cast_322_fcf_debt_service_accel_21d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_322_fcf_debt_service_accel_21d},
    "cast_323_fcf_debt_service_accel_63d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_323_fcf_debt_service_accel_63d},
    "cast_324_fcf_debt_service_accel_126d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_324_fcf_debt_service_accel_126d},
    "cast_325_fcf_debt_service_accel_252d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_325_fcf_debt_service_accel_252d},
    "cast_326_capital_access_score_accel_5d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_326_capital_access_score_accel_5d},
    "cast_327_capital_access_score_accel_21d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_327_capital_access_score_accel_21d},
    "cast_328_capital_access_score_accel_63d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_328_capital_access_score_accel_63d},
    "cast_329_capital_access_score_accel_126d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_329_capital_access_score_accel_126d},
    "cast_330_capital_access_score_accel_252d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_330_capital_access_score_accel_252d},
    "cast_331_debt_drawdown_impact_accel_5d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_331_debt_drawdown_impact_accel_5d},
    "cast_332_debt_drawdown_impact_accel_21d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_332_debt_drawdown_impact_accel_21d},
    "cast_333_debt_drawdown_impact_accel_63d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_333_debt_drawdown_impact_accel_63d},
    "cast_334_debt_drawdown_impact_accel_126d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_334_debt_drawdown_impact_accel_126d},
    "cast_335_debt_drawdown_impact_accel_252d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_335_debt_drawdown_impact_accel_252d},
    "cast_336_refinancing_risk_proxy_accel_5d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_336_refinancing_risk_proxy_accel_5d},
    "cast_337_refinancing_risk_proxy_accel_21d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_337_refinancing_risk_proxy_accel_21d},
    "cast_338_refinancing_risk_proxy_accel_63d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_338_refinancing_risk_proxy_accel_63d},
    "cast_339_refinancing_risk_proxy_accel_126d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_339_refinancing_risk_proxy_accel_126d},
    "cast_340_refinancing_risk_proxy_accel_252d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_340_refinancing_risk_proxy_accel_252d},
    "cast_341_debt_to_assets_momentum_accel_5d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_341_debt_to_assets_momentum_accel_5d},
    "cast_342_debt_to_assets_momentum_accel_21d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_342_debt_to_assets_momentum_accel_21d},
    "cast_343_debt_to_assets_momentum_accel_63d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_343_debt_to_assets_momentum_accel_63d},
    "cast_344_debt_to_assets_momentum_accel_126d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_344_debt_to_assets_momentum_accel_126d},
    "cast_345_debt_to_assets_momentum_accel_252d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_345_debt_to_assets_momentum_accel_252d},
    "cast_346_fcf_yield_vs_debt_accel_5d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_346_fcf_yield_vs_debt_accel_5d},
    "cast_347_fcf_yield_vs_debt_accel_21d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_347_fcf_yield_vs_debt_accel_21d},
    "cast_348_fcf_yield_vs_debt_accel_63d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_348_fcf_yield_vs_debt_accel_63d},
    "cast_349_fcf_yield_vs_debt_accel_126d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_349_fcf_yield_vs_debt_accel_126d},
    "cast_350_fcf_yield_vs_debt_accel_252d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_350_fcf_yield_vs_debt_accel_252d},
    "cast_351_capital_structure_z_accel_5d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_351_capital_structure_z_accel_5d},
    "cast_352_capital_structure_z_accel_21d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_352_capital_structure_z_accel_21d},
    "cast_353_capital_structure_z_accel_63d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_353_capital_structure_z_accel_63d},
    "cast_354_capital_structure_z_accel_126d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_354_capital_structure_z_accel_126d},
    "cast_355_capital_structure_z_accel_252d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_355_capital_structure_z_accel_252d},
    "cast_356_equity_value_erosion_accel_5d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_356_equity_value_erosion_accel_5d},
    "cast_357_equity_value_erosion_accel_21d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_357_equity_value_erosion_accel_21d},
    "cast_358_equity_value_erosion_accel_63d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_358_equity_value_erosion_accel_63d},
    "cast_359_equity_value_erosion_accel_126d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_359_equity_value_erosion_accel_126d},
    "cast_360_equity_value_erosion_accel_252d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_360_equity_value_erosion_accel_252d},
    "cast_361_debt_burden_vol_accel_5d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_361_debt_burden_vol_accel_5d},
    "cast_362_debt_burden_vol_accel_21d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_362_debt_burden_vol_accel_21d},
    "cast_363_debt_burden_vol_accel_63d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_363_debt_burden_vol_accel_63d},
    "cast_364_debt_burden_vol_accel_126d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_364_debt_burden_vol_accel_126d},
    "cast_365_debt_burden_vol_accel_252d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_365_debt_burden_vol_accel_252d},
    "cast_366_capital_stress_index_accel_5d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_366_capital_stress_index_accel_5d},
    "cast_367_capital_stress_index_accel_21d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_367_capital_stress_index_accel_21d},
    "cast_368_capital_stress_index_accel_63d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_368_capital_stress_index_accel_63d},
    "cast_369_capital_stress_index_accel_126d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_369_capital_stress_index_accel_126d},
    "cast_370_capital_stress_index_accel_252d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_370_capital_stress_index_accel_252d},
    "cast_371_solvency_cushion_accel_5d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_371_solvency_cushion_accel_5d},
    "cast_372_solvency_cushion_accel_21d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_372_solvency_cushion_accel_21d},
    "cast_373_solvency_cushion_accel_63d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_373_solvency_cushion_accel_63d},
    "cast_374_solvency_cushion_accel_126d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_374_solvency_cushion_accel_126d},
    "cast_375_solvency_cushion_accel_252d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_375_solvency_cushion_accel_252d},
}
