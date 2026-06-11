"""
122_capital_access_stress — Velocity (2nd Derivatives)
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

def cast_226_interest_burden_proxy_vel_5d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_226_interest_burden_proxy_vel_5d
    ECONOMIC RATIONALE: Velocity of interest_burden_proxy. Estimated interest expense relative to free cash flow.
    """
    return ((debt * 0.08) / fcf.replace(0, 1e-9)).diff(5)

def cast_227_interest_burden_proxy_vel_21d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_227_interest_burden_proxy_vel_21d
    ECONOMIC RATIONALE: Velocity of interest_burden_proxy. Estimated interest expense relative to free cash flow.
    """
    return ((debt * 0.08) / fcf.replace(0, 1e-9)).diff(21)

def cast_228_interest_burden_proxy_vel_63d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_228_interest_burden_proxy_vel_63d
    ECONOMIC RATIONALE: Velocity of interest_burden_proxy. Estimated interest expense relative to free cash flow.
    """
    return ((debt * 0.08) / fcf.replace(0, 1e-9)).diff(63)

def cast_229_interest_burden_proxy_vel_126d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_229_interest_burden_proxy_vel_126d
    ECONOMIC RATIONALE: Velocity of interest_burden_proxy. Estimated interest expense relative to free cash flow.
    """
    return ((debt * 0.08) / fcf.replace(0, 1e-9)).diff(126)

def cast_230_interest_burden_proxy_vel_252d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_230_interest_burden_proxy_vel_252d
    ECONOMIC RATIONALE: Velocity of interest_burden_proxy. Estimated interest expense relative to free cash flow.
    """
    return ((debt * 0.08) / fcf.replace(0, 1e-9)).diff(252)

def cast_231_debt_to_equity_z_vel_5d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_231_debt_to_equity_z_vel_5d
    ECONOMIC RATIONALE: Velocity of debt_to_equity_z. Abnormality of current debt-to-equity ratio.
    """
    return (_zscore_rolling(debt / equity.replace(0, 1e-9), 252)).diff(5)

def cast_232_debt_to_equity_z_vel_21d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_232_debt_to_equity_z_vel_21d
    ECONOMIC RATIONALE: Velocity of debt_to_equity_z. Abnormality of current debt-to-equity ratio.
    """
    return (_zscore_rolling(debt / equity.replace(0, 1e-9), 252)).diff(21)

def cast_233_debt_to_equity_z_vel_63d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_233_debt_to_equity_z_vel_63d
    ECONOMIC RATIONALE: Velocity of debt_to_equity_z. Abnormality of current debt-to-equity ratio.
    """
    return (_zscore_rolling(debt / equity.replace(0, 1e-9), 252)).diff(63)

def cast_234_debt_to_equity_z_vel_126d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_234_debt_to_equity_z_vel_126d
    ECONOMIC RATIONALE: Velocity of debt_to_equity_z. Abnormality of current debt-to-equity ratio.
    """
    return (_zscore_rolling(debt / equity.replace(0, 1e-9), 252)).diff(126)

def cast_235_debt_to_equity_z_vel_252d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_235_debt_to_equity_z_vel_252d
    ECONOMIC RATIONALE: Velocity of debt_to_equity_z. Abnormality of current debt-to-equity ratio.
    """
    return (_zscore_rolling(debt / equity.replace(0, 1e-9), 252)).diff(252)

def cast_236_equity_funding_risk_vel_5d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_236_equity_funding_risk_vel_5d
    ECONOMIC RATIONALE: Velocity of equity_funding_risk. Capacity to raise capital via equity issuance.
    """
    return (marketcap / debt.replace(0, 1e-9)).diff(5)

def cast_237_equity_funding_risk_vel_21d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_237_equity_funding_risk_vel_21d
    ECONOMIC RATIONALE: Velocity of equity_funding_risk. Capacity to raise capital via equity issuance.
    """
    return (marketcap / debt.replace(0, 1e-9)).diff(21)

def cast_238_equity_funding_risk_vel_63d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_238_equity_funding_risk_vel_63d
    ECONOMIC RATIONALE: Velocity of equity_funding_risk. Capacity to raise capital via equity issuance.
    """
    return (marketcap / debt.replace(0, 1e-9)).diff(63)

def cast_239_equity_funding_risk_vel_126d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_239_equity_funding_risk_vel_126d
    ECONOMIC RATIONALE: Velocity of equity_funding_risk. Capacity to raise capital via equity issuance.
    """
    return (marketcap / debt.replace(0, 1e-9)).diff(126)

def cast_240_equity_funding_risk_vel_252d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_240_equity_funding_risk_vel_252d
    ECONOMIC RATIONALE: Velocity of equity_funding_risk. Capacity to raise capital via equity issuance.
    """
    return (marketcap / debt.replace(0, 1e-9)).diff(252)

def cast_241_debt_acceleration_vel_5d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_241_debt_acceleration_vel_5d
    ECONOMIC RATIONALE: Velocity of debt_acceleration. Speed of new debt accumulation.
    """
    return (debt.pct_change(63)).diff(5)

def cast_242_debt_acceleration_vel_21d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_242_debt_acceleration_vel_21d
    ECONOMIC RATIONALE: Velocity of debt_acceleration. Speed of new debt accumulation.
    """
    return (debt.pct_change(63)).diff(21)

def cast_243_debt_acceleration_vel_63d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_243_debt_acceleration_vel_63d
    ECONOMIC RATIONALE: Velocity of debt_acceleration. Speed of new debt accumulation.
    """
    return (debt.pct_change(63)).diff(63)

def cast_244_debt_acceleration_vel_126d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_244_debt_acceleration_vel_126d
    ECONOMIC RATIONALE: Velocity of debt_acceleration. Speed of new debt accumulation.
    """
    return (debt.pct_change(63)).diff(126)

def cast_245_debt_acceleration_vel_252d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_245_debt_acceleration_vel_252d
    ECONOMIC RATIONALE: Velocity of debt_acceleration. Speed of new debt accumulation.
    """
    return (debt.pct_change(63)).diff(252)

def cast_246_fcf_debt_service_vel_5d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_246_fcf_debt_service_vel_5d
    ECONOMIC RATIONALE: Velocity of fcf_debt_service. Ability to amortize debt from cash flow.
    """
    return (fcf / debt.replace(0, 1e-9)).diff(5)

def cast_247_fcf_debt_service_vel_21d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_247_fcf_debt_service_vel_21d
    ECONOMIC RATIONALE: Velocity of fcf_debt_service. Ability to amortize debt from cash flow.
    """
    return (fcf / debt.replace(0, 1e-9)).diff(21)

def cast_248_fcf_debt_service_vel_63d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_248_fcf_debt_service_vel_63d
    ECONOMIC RATIONALE: Velocity of fcf_debt_service. Ability to amortize debt from cash flow.
    """
    return (fcf / debt.replace(0, 1e-9)).diff(63)

def cast_249_fcf_debt_service_vel_126d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_249_fcf_debt_service_vel_126d
    ECONOMIC RATIONALE: Velocity of fcf_debt_service. Ability to amortize debt from cash flow.
    """
    return (fcf / debt.replace(0, 1e-9)).diff(126)

def cast_250_fcf_debt_service_vel_252d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_250_fcf_debt_service_vel_252d
    ECONOMIC RATIONALE: Velocity of fcf_debt_service. Ability to amortize debt from cash flow.
    """
    return (fcf / debt.replace(0, 1e-9)).diff(252)

def cast_251_capital_access_score_vel_5d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_251_capital_access_score_vel_5d
    ECONOMIC RATIONALE: Velocity of capital_access_score. Divergence between market valuation and debt growth.
    """
    return (marketcap.pct_change(63) - debt.pct_change(63)).diff(5)

def cast_252_capital_access_score_vel_21d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_252_capital_access_score_vel_21d
    ECONOMIC RATIONALE: Velocity of capital_access_score. Divergence between market valuation and debt growth.
    """
    return (marketcap.pct_change(63) - debt.pct_change(63)).diff(21)

def cast_253_capital_access_score_vel_63d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_253_capital_access_score_vel_63d
    ECONOMIC RATIONALE: Velocity of capital_access_score. Divergence between market valuation and debt growth.
    """
    return (marketcap.pct_change(63) - debt.pct_change(63)).diff(63)

def cast_254_capital_access_score_vel_126d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_254_capital_access_score_vel_126d
    ECONOMIC RATIONALE: Velocity of capital_access_score. Divergence between market valuation and debt growth.
    """
    return (marketcap.pct_change(63) - debt.pct_change(63)).diff(126)

def cast_255_capital_access_score_vel_252d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_255_capital_access_score_vel_252d
    ECONOMIC RATIONALE: Velocity of capital_access_score. Divergence between market valuation and debt growth.
    """
    return (marketcap.pct_change(63) - debt.pct_change(63)).diff(252)

def cast_256_debt_drawdown_impact_vel_5d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_256_debt_drawdown_impact_vel_5d
    ECONOMIC RATIONALE: Velocity of debt_drawdown_impact. Debt load relative to peak firm value.
    """
    return (debt / marketcap.rolling(252).max().replace(0, 1e-9)).diff(5)

def cast_257_debt_drawdown_impact_vel_21d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_257_debt_drawdown_impact_vel_21d
    ECONOMIC RATIONALE: Velocity of debt_drawdown_impact. Debt load relative to peak firm value.
    """
    return (debt / marketcap.rolling(252).max().replace(0, 1e-9)).diff(21)

def cast_258_debt_drawdown_impact_vel_63d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_258_debt_drawdown_impact_vel_63d
    ECONOMIC RATIONALE: Velocity of debt_drawdown_impact. Debt load relative to peak firm value.
    """
    return (debt / marketcap.rolling(252).max().replace(0, 1e-9)).diff(63)

def cast_259_debt_drawdown_impact_vel_126d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_259_debt_drawdown_impact_vel_126d
    ECONOMIC RATIONALE: Velocity of debt_drawdown_impact. Debt load relative to peak firm value.
    """
    return (debt / marketcap.rolling(252).max().replace(0, 1e-9)).diff(126)

def cast_260_debt_drawdown_impact_vel_252d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_260_debt_drawdown_impact_vel_252d
    ECONOMIC RATIONALE: Velocity of debt_drawdown_impact. Debt load relative to peak firm value.
    """
    return (debt / marketcap.rolling(252).max().replace(0, 1e-9)).diff(252)

def cast_261_refinancing_risk_proxy_vel_5d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_261_refinancing_risk_proxy_vel_5d
    ECONOMIC RATIONALE: Velocity of refinancing_risk_proxy. High risk of inability to refinance maturing debt.
    """
    return ((debt > equity).astype(float) * (marketcap < 100e6).astype(float)).diff(5)

def cast_262_refinancing_risk_proxy_vel_21d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_262_refinancing_risk_proxy_vel_21d
    ECONOMIC RATIONALE: Velocity of refinancing_risk_proxy. High risk of inability to refinance maturing debt.
    """
    return ((debt > equity).astype(float) * (marketcap < 100e6).astype(float)).diff(21)

def cast_263_refinancing_risk_proxy_vel_63d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_263_refinancing_risk_proxy_vel_63d
    ECONOMIC RATIONALE: Velocity of refinancing_risk_proxy. High risk of inability to refinance maturing debt.
    """
    return ((debt > equity).astype(float) * (marketcap < 100e6).astype(float)).diff(63)

def cast_264_refinancing_risk_proxy_vel_126d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_264_refinancing_risk_proxy_vel_126d
    ECONOMIC RATIONALE: Velocity of refinancing_risk_proxy. High risk of inability to refinance maturing debt.
    """
    return ((debt > equity).astype(float) * (marketcap < 100e6).astype(float)).diff(126)

def cast_265_refinancing_risk_proxy_vel_252d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_265_refinancing_risk_proxy_vel_252d
    ECONOMIC RATIONALE: Velocity of refinancing_risk_proxy. High risk of inability to refinance maturing debt.
    """
    return ((debt > equity).astype(float) * (marketcap < 100e6).astype(float)).diff(252)

def cast_266_debt_to_assets_momentum_vel_5d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_266_debt_to_assets_momentum_vel_5d
    ECONOMIC RATIONALE: Velocity of debt_to_assets_momentum. Trend in the proportion of assets funded by debt.
    """
    return ((debt/assets).diff(63)).diff(5)

def cast_267_debt_to_assets_momentum_vel_21d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_267_debt_to_assets_momentum_vel_21d
    ECONOMIC RATIONALE: Velocity of debt_to_assets_momentum. Trend in the proportion of assets funded by debt.
    """
    return ((debt/assets).diff(63)).diff(21)

def cast_268_debt_to_assets_momentum_vel_63d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_268_debt_to_assets_momentum_vel_63d
    ECONOMIC RATIONALE: Velocity of debt_to_assets_momentum. Trend in the proportion of assets funded by debt.
    """
    return ((debt/assets).diff(63)).diff(63)

def cast_269_debt_to_assets_momentum_vel_126d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_269_debt_to_assets_momentum_vel_126d
    ECONOMIC RATIONALE: Velocity of debt_to_assets_momentum. Trend in the proportion of assets funded by debt.
    """
    return ((debt/assets).diff(63)).diff(126)

def cast_270_debt_to_assets_momentum_vel_252d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_270_debt_to_assets_momentum_vel_252d
    ECONOMIC RATIONALE: Velocity of debt_to_assets_momentum. Trend in the proportion of assets funded by debt.
    """
    return ((debt/assets).diff(63)).diff(252)

def cast_271_fcf_yield_vs_debt_vel_5d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_271_fcf_yield_vs_debt_vel_5d
    ECONOMIC RATIONALE: Velocity of fcf_yield_vs_debt. Cash flow yield net of debt-to-cap ratio.
    """
    return ((fcf/marketcap) - (debt/marketcap)).diff(5)

def cast_272_fcf_yield_vs_debt_vel_21d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_272_fcf_yield_vs_debt_vel_21d
    ECONOMIC RATIONALE: Velocity of fcf_yield_vs_debt. Cash flow yield net of debt-to-cap ratio.
    """
    return ((fcf/marketcap) - (debt/marketcap)).diff(21)

def cast_273_fcf_yield_vs_debt_vel_63d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_273_fcf_yield_vs_debt_vel_63d
    ECONOMIC RATIONALE: Velocity of fcf_yield_vs_debt. Cash flow yield net of debt-to-cap ratio.
    """
    return ((fcf/marketcap) - (debt/marketcap)).diff(63)

def cast_274_fcf_yield_vs_debt_vel_126d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_274_fcf_yield_vs_debt_vel_126d
    ECONOMIC RATIONALE: Velocity of fcf_yield_vs_debt. Cash flow yield net of debt-to-cap ratio.
    """
    return ((fcf/marketcap) - (debt/marketcap)).diff(126)

def cast_275_fcf_yield_vs_debt_vel_252d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_275_fcf_yield_vs_debt_vel_252d
    ECONOMIC RATIONALE: Velocity of fcf_yield_vs_debt. Cash flow yield net of debt-to-cap ratio.
    """
    return ((fcf/marketcap) - (debt/marketcap)).diff(252)

def cast_276_capital_structure_z_vel_5d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_276_capital_structure_z_vel_5d
    ECONOMIC RATIONALE: Velocity of capital_structure_z. Z-score of debt within the capital structure.
    """
    return (_zscore_rolling(debt/(debt+equity).replace(0, 1e-9), 252)).diff(5)

def cast_277_capital_structure_z_vel_21d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_277_capital_structure_z_vel_21d
    ECONOMIC RATIONALE: Velocity of capital_structure_z. Z-score of debt within the capital structure.
    """
    return (_zscore_rolling(debt/(debt+equity).replace(0, 1e-9), 252)).diff(21)

def cast_278_capital_structure_z_vel_63d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_278_capital_structure_z_vel_63d
    ECONOMIC RATIONALE: Velocity of capital_structure_z. Z-score of debt within the capital structure.
    """
    return (_zscore_rolling(debt/(debt+equity).replace(0, 1e-9), 252)).diff(63)

def cast_279_capital_structure_z_vel_126d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_279_capital_structure_z_vel_126d
    ECONOMIC RATIONALE: Velocity of capital_structure_z. Z-score of debt within the capital structure.
    """
    return (_zscore_rolling(debt/(debt+equity).replace(0, 1e-9), 252)).diff(126)

def cast_280_capital_structure_z_vel_252d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_280_capital_structure_z_vel_252d
    ECONOMIC RATIONALE: Velocity of capital_structure_z. Z-score of debt within the capital structure.
    """
    return (_zscore_rolling(debt/(debt+equity).replace(0, 1e-9), 252)).diff(252)

def cast_281_equity_value_erosion_vel_5d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_281_equity_value_erosion_vel_5d
    ECONOMIC RATIONALE: Velocity of equity_value_erosion. Destruction of book value relative to market price.
    """
    return (equity.diff(252) / marketcap.replace(0, 1e-9)).diff(5)

def cast_282_equity_value_erosion_vel_21d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_282_equity_value_erosion_vel_21d
    ECONOMIC RATIONALE: Velocity of equity_value_erosion. Destruction of book value relative to market price.
    """
    return (equity.diff(252) / marketcap.replace(0, 1e-9)).diff(21)

def cast_283_equity_value_erosion_vel_63d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_283_equity_value_erosion_vel_63d
    ECONOMIC RATIONALE: Velocity of equity_value_erosion. Destruction of book value relative to market price.
    """
    return (equity.diff(252) / marketcap.replace(0, 1e-9)).diff(63)

def cast_284_equity_value_erosion_vel_126d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_284_equity_value_erosion_vel_126d
    ECONOMIC RATIONALE: Velocity of equity_value_erosion. Destruction of book value relative to market price.
    """
    return (equity.diff(252) / marketcap.replace(0, 1e-9)).diff(126)

def cast_285_equity_value_erosion_vel_252d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_285_equity_value_erosion_vel_252d
    ECONOMIC RATIONALE: Velocity of equity_value_erosion. Destruction of book value relative to market price.
    """
    return (equity.diff(252) / marketcap.replace(0, 1e-9)).diff(252)

def cast_286_debt_burden_vol_vel_5d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_286_debt_burden_vol_vel_5d
    ECONOMIC RATIONALE: Velocity of debt_burden_vol. Price volatility amplified by debt-to-market-cap ratio.
    """
    return (close.rolling(21).std() * (debt/marketcap.replace(0, 1e-9))).diff(5)

def cast_287_debt_burden_vol_vel_21d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_287_debt_burden_vol_vel_21d
    ECONOMIC RATIONALE: Velocity of debt_burden_vol. Price volatility amplified by debt-to-market-cap ratio.
    """
    return (close.rolling(21).std() * (debt/marketcap.replace(0, 1e-9))).diff(21)

def cast_288_debt_burden_vol_vel_63d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_288_debt_burden_vol_vel_63d
    ECONOMIC RATIONALE: Velocity of debt_burden_vol. Price volatility amplified by debt-to-market-cap ratio.
    """
    return (close.rolling(21).std() * (debt/marketcap.replace(0, 1e-9))).diff(63)

def cast_289_debt_burden_vol_vel_126d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_289_debt_burden_vol_vel_126d
    ECONOMIC RATIONALE: Velocity of debt_burden_vol. Price volatility amplified by debt-to-market-cap ratio.
    """
    return (close.rolling(21).std() * (debt/marketcap.replace(0, 1e-9))).diff(126)

def cast_290_debt_burden_vol_vel_252d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_290_debt_burden_vol_vel_252d
    ECONOMIC RATIONALE: Velocity of debt_burden_vol. Price volatility amplified by debt-to-market-cap ratio.
    """
    return (close.rolling(21).std() * (debt/marketcap.replace(0, 1e-9))).diff(252)

def cast_291_capital_stress_index_vel_5d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_291_capital_stress_index_vel_5d
    ECONOMIC RATIONALE: Velocity of capital_stress_index. Debt growth relative to cash flow capacity.
    """
    return (debt.pct_change(21) / fcf.rolling(63).mean().abs().replace(0, 1e-9)).diff(5)

def cast_292_capital_stress_index_vel_21d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_292_capital_stress_index_vel_21d
    ECONOMIC RATIONALE: Velocity of capital_stress_index. Debt growth relative to cash flow capacity.
    """
    return (debt.pct_change(21) / fcf.rolling(63).mean().abs().replace(0, 1e-9)).diff(21)

def cast_293_capital_stress_index_vel_63d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_293_capital_stress_index_vel_63d
    ECONOMIC RATIONALE: Velocity of capital_stress_index. Debt growth relative to cash flow capacity.
    """
    return (debt.pct_change(21) / fcf.rolling(63).mean().abs().replace(0, 1e-9)).diff(63)

def cast_294_capital_stress_index_vel_126d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_294_capital_stress_index_vel_126d
    ECONOMIC RATIONALE: Velocity of capital_stress_index. Debt growth relative to cash flow capacity.
    """
    return (debt.pct_change(21) / fcf.rolling(63).mean().abs().replace(0, 1e-9)).diff(126)

def cast_295_capital_stress_index_vel_252d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_295_capital_stress_index_vel_252d
    ECONOMIC RATIONALE: Velocity of capital_stress_index. Debt growth relative to cash flow capacity.
    """
    return (debt.pct_change(21) / fcf.rolling(63).mean().abs().replace(0, 1e-9)).diff(252)

def cast_296_solvency_cushion_vel_5d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_296_solvency_cushion_vel_5d
    ECONOMIC RATIONALE: Velocity of solvency_cushion. Proportion of assets funded by shareholders.
    """
    return (equity / assets.replace(0, 1e-9)).diff(5)

def cast_297_solvency_cushion_vel_21d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_297_solvency_cushion_vel_21d
    ECONOMIC RATIONALE: Velocity of solvency_cushion. Proportion of assets funded by shareholders.
    """
    return (equity / assets.replace(0, 1e-9)).diff(21)

def cast_298_solvency_cushion_vel_63d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_298_solvency_cushion_vel_63d
    ECONOMIC RATIONALE: Velocity of solvency_cushion. Proportion of assets funded by shareholders.
    """
    return (equity / assets.replace(0, 1e-9)).diff(63)

def cast_299_solvency_cushion_vel_126d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_299_solvency_cushion_vel_126d
    ECONOMIC RATIONALE: Velocity of solvency_cushion. Proportion of assets funded by shareholders.
    """
    return (equity / assets.replace(0, 1e-9)).diff(126)

def cast_300_solvency_cushion_vel_252d(assets: pd.Series, close: pd.Series, debt: pd.Series, equity: pd.Series, fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    cast_300_solvency_cushion_vel_252d
    ECONOMIC RATIONALE: Velocity of solvency_cushion. Proportion of assets funded by shareholders.
    """
    return (equity / assets.replace(0, 1e-9)).diff(252)

# ── Registry ──────────────────────────────────────────────────────────────────
V122_REGISTRY_VEL = {
    "cast_226_interest_burden_proxy_vel_5d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_226_interest_burden_proxy_vel_5d},
    "cast_227_interest_burden_proxy_vel_21d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_227_interest_burden_proxy_vel_21d},
    "cast_228_interest_burden_proxy_vel_63d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_228_interest_burden_proxy_vel_63d},
    "cast_229_interest_burden_proxy_vel_126d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_229_interest_burden_proxy_vel_126d},
    "cast_230_interest_burden_proxy_vel_252d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_230_interest_burden_proxy_vel_252d},
    "cast_231_debt_to_equity_z_vel_5d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_231_debt_to_equity_z_vel_5d},
    "cast_232_debt_to_equity_z_vel_21d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_232_debt_to_equity_z_vel_21d},
    "cast_233_debt_to_equity_z_vel_63d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_233_debt_to_equity_z_vel_63d},
    "cast_234_debt_to_equity_z_vel_126d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_234_debt_to_equity_z_vel_126d},
    "cast_235_debt_to_equity_z_vel_252d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_235_debt_to_equity_z_vel_252d},
    "cast_236_equity_funding_risk_vel_5d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_236_equity_funding_risk_vel_5d},
    "cast_237_equity_funding_risk_vel_21d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_237_equity_funding_risk_vel_21d},
    "cast_238_equity_funding_risk_vel_63d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_238_equity_funding_risk_vel_63d},
    "cast_239_equity_funding_risk_vel_126d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_239_equity_funding_risk_vel_126d},
    "cast_240_equity_funding_risk_vel_252d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_240_equity_funding_risk_vel_252d},
    "cast_241_debt_acceleration_vel_5d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_241_debt_acceleration_vel_5d},
    "cast_242_debt_acceleration_vel_21d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_242_debt_acceleration_vel_21d},
    "cast_243_debt_acceleration_vel_63d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_243_debt_acceleration_vel_63d},
    "cast_244_debt_acceleration_vel_126d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_244_debt_acceleration_vel_126d},
    "cast_245_debt_acceleration_vel_252d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_245_debt_acceleration_vel_252d},
    "cast_246_fcf_debt_service_vel_5d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_246_fcf_debt_service_vel_5d},
    "cast_247_fcf_debt_service_vel_21d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_247_fcf_debt_service_vel_21d},
    "cast_248_fcf_debt_service_vel_63d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_248_fcf_debt_service_vel_63d},
    "cast_249_fcf_debt_service_vel_126d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_249_fcf_debt_service_vel_126d},
    "cast_250_fcf_debt_service_vel_252d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_250_fcf_debt_service_vel_252d},
    "cast_251_capital_access_score_vel_5d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_251_capital_access_score_vel_5d},
    "cast_252_capital_access_score_vel_21d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_252_capital_access_score_vel_21d},
    "cast_253_capital_access_score_vel_63d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_253_capital_access_score_vel_63d},
    "cast_254_capital_access_score_vel_126d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_254_capital_access_score_vel_126d},
    "cast_255_capital_access_score_vel_252d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_255_capital_access_score_vel_252d},
    "cast_256_debt_drawdown_impact_vel_5d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_256_debt_drawdown_impact_vel_5d},
    "cast_257_debt_drawdown_impact_vel_21d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_257_debt_drawdown_impact_vel_21d},
    "cast_258_debt_drawdown_impact_vel_63d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_258_debt_drawdown_impact_vel_63d},
    "cast_259_debt_drawdown_impact_vel_126d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_259_debt_drawdown_impact_vel_126d},
    "cast_260_debt_drawdown_impact_vel_252d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_260_debt_drawdown_impact_vel_252d},
    "cast_261_refinancing_risk_proxy_vel_5d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_261_refinancing_risk_proxy_vel_5d},
    "cast_262_refinancing_risk_proxy_vel_21d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_262_refinancing_risk_proxy_vel_21d},
    "cast_263_refinancing_risk_proxy_vel_63d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_263_refinancing_risk_proxy_vel_63d},
    "cast_264_refinancing_risk_proxy_vel_126d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_264_refinancing_risk_proxy_vel_126d},
    "cast_265_refinancing_risk_proxy_vel_252d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_265_refinancing_risk_proxy_vel_252d},
    "cast_266_debt_to_assets_momentum_vel_5d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_266_debt_to_assets_momentum_vel_5d},
    "cast_267_debt_to_assets_momentum_vel_21d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_267_debt_to_assets_momentum_vel_21d},
    "cast_268_debt_to_assets_momentum_vel_63d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_268_debt_to_assets_momentum_vel_63d},
    "cast_269_debt_to_assets_momentum_vel_126d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_269_debt_to_assets_momentum_vel_126d},
    "cast_270_debt_to_assets_momentum_vel_252d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_270_debt_to_assets_momentum_vel_252d},
    "cast_271_fcf_yield_vs_debt_vel_5d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_271_fcf_yield_vs_debt_vel_5d},
    "cast_272_fcf_yield_vs_debt_vel_21d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_272_fcf_yield_vs_debt_vel_21d},
    "cast_273_fcf_yield_vs_debt_vel_63d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_273_fcf_yield_vs_debt_vel_63d},
    "cast_274_fcf_yield_vs_debt_vel_126d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_274_fcf_yield_vs_debt_vel_126d},
    "cast_275_fcf_yield_vs_debt_vel_252d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_275_fcf_yield_vs_debt_vel_252d},
    "cast_276_capital_structure_z_vel_5d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_276_capital_structure_z_vel_5d},
    "cast_277_capital_structure_z_vel_21d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_277_capital_structure_z_vel_21d},
    "cast_278_capital_structure_z_vel_63d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_278_capital_structure_z_vel_63d},
    "cast_279_capital_structure_z_vel_126d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_279_capital_structure_z_vel_126d},
    "cast_280_capital_structure_z_vel_252d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_280_capital_structure_z_vel_252d},
    "cast_281_equity_value_erosion_vel_5d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_281_equity_value_erosion_vel_5d},
    "cast_282_equity_value_erosion_vel_21d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_282_equity_value_erosion_vel_21d},
    "cast_283_equity_value_erosion_vel_63d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_283_equity_value_erosion_vel_63d},
    "cast_284_equity_value_erosion_vel_126d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_284_equity_value_erosion_vel_126d},
    "cast_285_equity_value_erosion_vel_252d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_285_equity_value_erosion_vel_252d},
    "cast_286_debt_burden_vol_vel_5d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_286_debt_burden_vol_vel_5d},
    "cast_287_debt_burden_vol_vel_21d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_287_debt_burden_vol_vel_21d},
    "cast_288_debt_burden_vol_vel_63d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_288_debt_burden_vol_vel_63d},
    "cast_289_debt_burden_vol_vel_126d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_289_debt_burden_vol_vel_126d},
    "cast_290_debt_burden_vol_vel_252d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_290_debt_burden_vol_vel_252d},
    "cast_291_capital_stress_index_vel_5d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_291_capital_stress_index_vel_5d},
    "cast_292_capital_stress_index_vel_21d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_292_capital_stress_index_vel_21d},
    "cast_293_capital_stress_index_vel_63d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_293_capital_stress_index_vel_63d},
    "cast_294_capital_stress_index_vel_126d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_294_capital_stress_index_vel_126d},
    "cast_295_capital_stress_index_vel_252d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_295_capital_stress_index_vel_252d},
    "cast_296_solvency_cushion_vel_5d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_296_solvency_cushion_vel_5d},
    "cast_297_solvency_cushion_vel_21d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_297_solvency_cushion_vel_21d},
    "cast_298_solvency_cushion_vel_63d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_298_solvency_cushion_vel_63d},
    "cast_299_solvency_cushion_vel_126d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_299_solvency_cushion_vel_126d},
    "cast_300_solvency_cushion_vel_252d": {"inputs": ["assets", "close", "debt", "equity", "fcf", "marketcap"], "func": cast_300_solvency_cushion_vel_252d},
}
