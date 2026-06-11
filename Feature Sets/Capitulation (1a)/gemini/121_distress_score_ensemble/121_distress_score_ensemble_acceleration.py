"""
121_distress_score_ensemble — Acceleration (3rd Derivatives)
Domain: distress_score_ensemble
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

def dsen_301_composite_distress_z_accel_5d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_301_composite_distress_z_accel_5d
    ECONOMIC RATIONALE: Acceleration of composite_distress_z. Combined leverage and cash flow distress.
    """
    return (_zscore_rolling(liabs/equity.replace(0, 1e-9) + (ocf < 0).astype(float), 252)).diff(5).diff(_TD_MON)

def dsen_302_composite_distress_z_accel_21d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_302_composite_distress_z_accel_21d
    ECONOMIC RATIONALE: Acceleration of composite_distress_z. Combined leverage and cash flow distress.
    """
    return (_zscore_rolling(liabs/equity.replace(0, 1e-9) + (ocf < 0).astype(float), 252)).diff(21).diff(_TD_MON)

def dsen_303_composite_distress_z_accel_63d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_303_composite_distress_z_accel_63d
    ECONOMIC RATIONALE: Acceleration of composite_distress_z. Combined leverage and cash flow distress.
    """
    return (_zscore_rolling(liabs/equity.replace(0, 1e-9) + (ocf < 0).astype(float), 252)).diff(63).diff(_TD_MON)

def dsen_304_composite_distress_z_accel_126d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_304_composite_distress_z_accel_126d
    ECONOMIC RATIONALE: Acceleration of composite_distress_z. Combined leverage and cash flow distress.
    """
    return (_zscore_rolling(liabs/equity.replace(0, 1e-9) + (ocf < 0).astype(float), 252)).diff(126).diff(_TD_MON)

def dsen_305_composite_distress_z_accel_252d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_305_composite_distress_z_accel_252d
    ECONOMIC RATIONALE: Acceleration of composite_distress_z. Combined leverage and cash flow distress.
    """
    return (_zscore_rolling(liabs/equity.replace(0, 1e-9) + (ocf < 0).astype(float), 252)).diff(252).diff(_TD_MON)

def dsen_306_valuation_solvency_blend_accel_5d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_306_valuation_solvency_blend_accel_5d
    ECONOMIC RATIONALE: Acceleration of valuation_solvency_blend. Valuation drawdown weighted by solvency.
    """
    return ((close/close.rolling(252).max()) * (equity/liabs.replace(0, 1e-9))).diff(5).diff(_TD_MON)

def dsen_307_valuation_solvency_blend_accel_21d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_307_valuation_solvency_blend_accel_21d
    ECONOMIC RATIONALE: Acceleration of valuation_solvency_blend. Valuation drawdown weighted by solvency.
    """
    return ((close/close.rolling(252).max()) * (equity/liabs.replace(0, 1e-9))).diff(21).diff(_TD_MON)

def dsen_308_valuation_solvency_blend_accel_63d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_308_valuation_solvency_blend_accel_63d
    ECONOMIC RATIONALE: Acceleration of valuation_solvency_blend. Valuation drawdown weighted by solvency.
    """
    return ((close/close.rolling(252).max()) * (equity/liabs.replace(0, 1e-9))).diff(63).diff(_TD_MON)

def dsen_309_valuation_solvency_blend_accel_126d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_309_valuation_solvency_blend_accel_126d
    ECONOMIC RATIONALE: Acceleration of valuation_solvency_blend. Valuation drawdown weighted by solvency.
    """
    return ((close/close.rolling(252).max()) * (equity/liabs.replace(0, 1e-9))).diff(126).diff(_TD_MON)

def dsen_310_valuation_solvency_blend_accel_252d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_310_valuation_solvency_blend_accel_252d
    ECONOMIC RATIONALE: Acceleration of valuation_solvency_blend. Valuation drawdown weighted by solvency.
    """
    return ((close/close.rolling(252).max()) * (equity/liabs.replace(0, 1e-9))).diff(252).diff(_TD_MON)

def dsen_311_liquidity_momentum_ensemble_accel_5d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_311_liquidity_momentum_ensemble_accel_5d
    ECONOMIC RATIONALE: Acceleration of liquidity_momentum_ensemble. Combined fundamental and price momentum.
    """
    return (ocf.pct_change(63) + close.pct_change(63)).diff(5).diff(_TD_MON)

def dsen_312_liquidity_momentum_ensemble_accel_21d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_312_liquidity_momentum_ensemble_accel_21d
    ECONOMIC RATIONALE: Acceleration of liquidity_momentum_ensemble. Combined fundamental and price momentum.
    """
    return (ocf.pct_change(63) + close.pct_change(63)).diff(21).diff(_TD_MON)

def dsen_313_liquidity_momentum_ensemble_accel_63d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_313_liquidity_momentum_ensemble_accel_63d
    ECONOMIC RATIONALE: Acceleration of liquidity_momentum_ensemble. Combined fundamental and price momentum.
    """
    return (ocf.pct_change(63) + close.pct_change(63)).diff(63).diff(_TD_MON)

def dsen_314_liquidity_momentum_ensemble_accel_126d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_314_liquidity_momentum_ensemble_accel_126d
    ECONOMIC RATIONALE: Acceleration of liquidity_momentum_ensemble. Combined fundamental and price momentum.
    """
    return (ocf.pct_change(63) + close.pct_change(63)).diff(126).diff(_TD_MON)

def dsen_315_liquidity_momentum_ensemble_accel_252d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_315_liquidity_momentum_ensemble_accel_252d
    ECONOMIC RATIONALE: Acceleration of liquidity_momentum_ensemble. Combined fundamental and price momentum.
    """
    return (ocf.pct_change(63) + close.pct_change(63)).diff(252).diff(_TD_MON)

def dsen_316_distress_regime_indicator_accel_5d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_316_distress_regime_indicator_accel_5d
    ECONOMIC RATIONALE: Acceleration of distress_regime_indicator. Binary flag for structural distress.
    """
    return (((liabs > assets) | (ocf < 0)).astype(float)).diff(5).diff(_TD_MON)

def dsen_317_distress_regime_indicator_accel_21d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_317_distress_regime_indicator_accel_21d
    ECONOMIC RATIONALE: Acceleration of distress_regime_indicator. Binary flag for structural distress.
    """
    return (((liabs > assets) | (ocf < 0)).astype(float)).diff(21).diff(_TD_MON)

def dsen_318_distress_regime_indicator_accel_63d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_318_distress_regime_indicator_accel_63d
    ECONOMIC RATIONALE: Acceleration of distress_regime_indicator. Binary flag for structural distress.
    """
    return (((liabs > assets) | (ocf < 0)).astype(float)).diff(63).diff(_TD_MON)

def dsen_319_distress_regime_indicator_accel_126d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_319_distress_regime_indicator_accel_126d
    ECONOMIC RATIONALE: Acceleration of distress_regime_indicator. Binary flag for structural distress.
    """
    return (((liabs > assets) | (ocf < 0)).astype(float)).diff(126).diff(_TD_MON)

def dsen_320_distress_regime_indicator_accel_252d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_320_distress_regime_indicator_accel_252d
    ECONOMIC RATIONALE: Acceleration of distress_regime_indicator. Binary flag for structural distress.
    """
    return (((liabs > assets) | (ocf < 0)).astype(float)).diff(252).diff(_TD_MON)

def dsen_321_ensemble_vol_risk_accel_5d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_321_ensemble_vol_risk_accel_5d
    ECONOMIC RATIONALE: Acceleration of ensemble_vol_risk. Volatility amplified by financial leverage.
    """
    return (close.rolling(21).std() * (liabs/equity.replace(0, 1e-9))).diff(5).diff(_TD_MON)

def dsen_322_ensemble_vol_risk_accel_21d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_322_ensemble_vol_risk_accel_21d
    ECONOMIC RATIONALE: Acceleration of ensemble_vol_risk. Volatility amplified by financial leverage.
    """
    return (close.rolling(21).std() * (liabs/equity.replace(0, 1e-9))).diff(21).diff(_TD_MON)

def dsen_323_ensemble_vol_risk_accel_63d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_323_ensemble_vol_risk_accel_63d
    ECONOMIC RATIONALE: Acceleration of ensemble_vol_risk. Volatility amplified by financial leverage.
    """
    return (close.rolling(21).std() * (liabs/equity.replace(0, 1e-9))).diff(63).diff(_TD_MON)

def dsen_324_ensemble_vol_risk_accel_126d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_324_ensemble_vol_risk_accel_126d
    ECONOMIC RATIONALE: Acceleration of ensemble_vol_risk. Volatility amplified by financial leverage.
    """
    return (close.rolling(21).std() * (liabs/equity.replace(0, 1e-9))).diff(126).diff(_TD_MON)

def dsen_325_ensemble_vol_risk_accel_252d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_325_ensemble_vol_risk_accel_252d
    ECONOMIC RATIONALE: Acceleration of ensemble_vol_risk. Volatility amplified by financial leverage.
    """
    return (close.rolling(21).std() * (liabs/equity.replace(0, 1e-9))).diff(252).diff(_TD_MON)

def dsen_326_multi_factor_drawdown_accel_5d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_326_multi_factor_drawdown_accel_5d
    ECONOMIC RATIONALE: Acceleration of multi_factor_drawdown. Combined price and equity drawdown.
    """
    return ((close/close.rolling(252).max() - 1) + (equity/equity.rolling(252).max() - 1)).diff(5).diff(_TD_MON)

def dsen_327_multi_factor_drawdown_accel_21d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_327_multi_factor_drawdown_accel_21d
    ECONOMIC RATIONALE: Acceleration of multi_factor_drawdown. Combined price and equity drawdown.
    """
    return ((close/close.rolling(252).max() - 1) + (equity/equity.rolling(252).max() - 1)).diff(21).diff(_TD_MON)

def dsen_328_multi_factor_drawdown_accel_63d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_328_multi_factor_drawdown_accel_63d
    ECONOMIC RATIONALE: Acceleration of multi_factor_drawdown. Combined price and equity drawdown.
    """
    return ((close/close.rolling(252).max() - 1) + (equity/equity.rolling(252).max() - 1)).diff(63).diff(_TD_MON)

def dsen_329_multi_factor_drawdown_accel_126d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_329_multi_factor_drawdown_accel_126d
    ECONOMIC RATIONALE: Acceleration of multi_factor_drawdown. Combined price and equity drawdown.
    """
    return ((close/close.rolling(252).max() - 1) + (equity/equity.rolling(252).max() - 1)).diff(126).diff(_TD_MON)

def dsen_330_multi_factor_drawdown_accel_252d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_330_multi_factor_drawdown_accel_252d
    ECONOMIC RATIONALE: Acceleration of multi_factor_drawdown. Combined price and equity drawdown.
    """
    return ((close/close.rolling(252).max() - 1) + (equity/equity.rolling(252).max() - 1)).diff(252).diff(_TD_MON)

def dsen_331_distress_acceleration_accel_5d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_331_distress_acceleration_accel_5d
    ECONOMIC RATIONALE: Acceleration of distress_acceleration. Acceleration of leverage combined with price decline.
    """
    return ((liabs/equity.replace(0, 1e-9)).diff(63) + close.pct_change(63)).diff(5).diff(_TD_MON)

def dsen_332_distress_acceleration_accel_21d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_332_distress_acceleration_accel_21d
    ECONOMIC RATIONALE: Acceleration of distress_acceleration. Acceleration of leverage combined with price decline.
    """
    return ((liabs/equity.replace(0, 1e-9)).diff(63) + close.pct_change(63)).diff(21).diff(_TD_MON)

def dsen_333_distress_acceleration_accel_63d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_333_distress_acceleration_accel_63d
    ECONOMIC RATIONALE: Acceleration of distress_acceleration. Acceleration of leverage combined with price decline.
    """
    return ((liabs/equity.replace(0, 1e-9)).diff(63) + close.pct_change(63)).diff(63).diff(_TD_MON)

def dsen_334_distress_acceleration_accel_126d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_334_distress_acceleration_accel_126d
    ECONOMIC RATIONALE: Acceleration of distress_acceleration. Acceleration of leverage combined with price decline.
    """
    return ((liabs/equity.replace(0, 1e-9)).diff(63) + close.pct_change(63)).diff(126).diff(_TD_MON)

def dsen_335_distress_acceleration_accel_252d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_335_distress_acceleration_accel_252d
    ECONOMIC RATIONALE: Acceleration of distress_acceleration. Acceleration of leverage combined with price decline.
    """
    return ((liabs/equity.replace(0, 1e-9)).diff(63) + close.pct_change(63)).diff(252).diff(_TD_MON)

def dsen_336_solvency_quality_score_accel_5d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_336_solvency_quality_score_accel_5d
    ECONOMIC RATIONALE: Acceleration of solvency_quality_score. Cash flow coverage of debt adjusted by equity status.
    """
    return (ocf / liabs.replace(0, 1e-9) * (equity > 0).astype(float)).diff(5).diff(_TD_MON)

def dsen_337_solvency_quality_score_accel_21d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_337_solvency_quality_score_accel_21d
    ECONOMIC RATIONALE: Acceleration of solvency_quality_score. Cash flow coverage of debt adjusted by equity status.
    """
    return (ocf / liabs.replace(0, 1e-9) * (equity > 0).astype(float)).diff(21).diff(_TD_MON)

def dsen_338_solvency_quality_score_accel_63d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_338_solvency_quality_score_accel_63d
    ECONOMIC RATIONALE: Acceleration of solvency_quality_score. Cash flow coverage of debt adjusted by equity status.
    """
    return (ocf / liabs.replace(0, 1e-9) * (equity > 0).astype(float)).diff(63).diff(_TD_MON)

def dsen_339_solvency_quality_score_accel_126d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_339_solvency_quality_score_accel_126d
    ECONOMIC RATIONALE: Acceleration of solvency_quality_score. Cash flow coverage of debt adjusted by equity status.
    """
    return (ocf / liabs.replace(0, 1e-9) * (equity > 0).astype(float)).diff(126).diff(_TD_MON)

def dsen_340_solvency_quality_score_accel_252d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_340_solvency_quality_score_accel_252d
    ECONOMIC RATIONALE: Acceleration of solvency_quality_score. Cash flow coverage of debt adjusted by equity status.
    """
    return (ocf / liabs.replace(0, 1e-9) * (equity > 0).astype(float)).diff(252).diff(_TD_MON)

def dsen_341_ensemble_zscore_accel_5d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_341_ensemble_zscore_accel_5d
    ECONOMIC RATIONALE: Acceleration of ensemble_zscore. Integrated balance sheet and income statement distress.
    """
    return (_zscore_rolling(liabs/assets.replace(0, 1e-9) - ocf/assets.replace(0, 1e-9), 252)).diff(5).diff(_TD_MON)

def dsen_342_ensemble_zscore_accel_21d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_342_ensemble_zscore_accel_21d
    ECONOMIC RATIONALE: Acceleration of ensemble_zscore. Integrated balance sheet and income statement distress.
    """
    return (_zscore_rolling(liabs/assets.replace(0, 1e-9) - ocf/assets.replace(0, 1e-9), 252)).diff(21).diff(_TD_MON)

def dsen_343_ensemble_zscore_accel_63d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_343_ensemble_zscore_accel_63d
    ECONOMIC RATIONALE: Acceleration of ensemble_zscore. Integrated balance sheet and income statement distress.
    """
    return (_zscore_rolling(liabs/assets.replace(0, 1e-9) - ocf/assets.replace(0, 1e-9), 252)).diff(63).diff(_TD_MON)

def dsen_344_ensemble_zscore_accel_126d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_344_ensemble_zscore_accel_126d
    ECONOMIC RATIONALE: Acceleration of ensemble_zscore. Integrated balance sheet and income statement distress.
    """
    return (_zscore_rolling(liabs/assets.replace(0, 1e-9) - ocf/assets.replace(0, 1e-9), 252)).diff(126).diff(_TD_MON)

def dsen_345_ensemble_zscore_accel_252d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_345_ensemble_zscore_accel_252d
    ECONOMIC RATIONALE: Acceleration of ensemble_zscore. Integrated balance sheet and income statement distress.
    """
    return (_zscore_rolling(liabs/assets.replace(0, 1e-9) - ocf/assets.replace(0, 1e-9), 252)).diff(252).diff(_TD_MON)

def dsen_346_market_distress_beta_accel_5d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_346_market_distress_beta_accel_5d
    ECONOMIC RATIONALE: Acceleration of market_distress_beta. Market sensitivity weighted by financial risk.
    """
    return (close.pct_change(1).rolling(63).corr(mkt_close.pct_change(1)) * (liabs/equity.replace(0, 1e-9))).diff(5).diff(_TD_MON)

def dsen_347_market_distress_beta_accel_21d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_347_market_distress_beta_accel_21d
    ECONOMIC RATIONALE: Acceleration of market_distress_beta. Market sensitivity weighted by financial risk.
    """
    return (close.pct_change(1).rolling(63).corr(mkt_close.pct_change(1)) * (liabs/equity.replace(0, 1e-9))).diff(21).diff(_TD_MON)

def dsen_348_market_distress_beta_accel_63d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_348_market_distress_beta_accel_63d
    ECONOMIC RATIONALE: Acceleration of market_distress_beta. Market sensitivity weighted by financial risk.
    """
    return (close.pct_change(1).rolling(63).corr(mkt_close.pct_change(1)) * (liabs/equity.replace(0, 1e-9))).diff(63).diff(_TD_MON)

def dsen_349_market_distress_beta_accel_126d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_349_market_distress_beta_accel_126d
    ECONOMIC RATIONALE: Acceleration of market_distress_beta. Market sensitivity weighted by financial risk.
    """
    return (close.pct_change(1).rolling(63).corr(mkt_close.pct_change(1)) * (liabs/equity.replace(0, 1e-9))).diff(126).diff(_TD_MON)

def dsen_350_market_distress_beta_accel_252d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_350_market_distress_beta_accel_252d
    ECONOMIC RATIONALE: Acceleration of market_distress_beta. Market sensitivity weighted by financial risk.
    """
    return (close.pct_change(1).rolling(63).corr(mkt_close.pct_change(1)) * (liabs/equity.replace(0, 1e-9))).diff(252).diff(_TD_MON)

def dsen_351_ensemble_drawdown_rank_accel_5d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_351_ensemble_drawdown_rank_accel_5d
    ECONOMIC RATIONALE: Acceleration of ensemble_drawdown_rank. Rank of combined price and leverage stress.
    """
    return (_rank_pct(close/close.rolling(252).max() + liabs/assets.replace(0, 1e-9), 252)).diff(5).diff(_TD_MON)

def dsen_352_ensemble_drawdown_rank_accel_21d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_352_ensemble_drawdown_rank_accel_21d
    ECONOMIC RATIONALE: Acceleration of ensemble_drawdown_rank. Rank of combined price and leverage stress.
    """
    return (_rank_pct(close/close.rolling(252).max() + liabs/assets.replace(0, 1e-9), 252)).diff(21).diff(_TD_MON)

def dsen_353_ensemble_drawdown_rank_accel_63d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_353_ensemble_drawdown_rank_accel_63d
    ECONOMIC RATIONALE: Acceleration of ensemble_drawdown_rank. Rank of combined price and leverage stress.
    """
    return (_rank_pct(close/close.rolling(252).max() + liabs/assets.replace(0, 1e-9), 252)).diff(63).diff(_TD_MON)

def dsen_354_ensemble_drawdown_rank_accel_126d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_354_ensemble_drawdown_rank_accel_126d
    ECONOMIC RATIONALE: Acceleration of ensemble_drawdown_rank. Rank of combined price and leverage stress.
    """
    return (_rank_pct(close/close.rolling(252).max() + liabs/assets.replace(0, 1e-9), 252)).diff(126).diff(_TD_MON)

def dsen_355_ensemble_drawdown_rank_accel_252d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_355_ensemble_drawdown_rank_accel_252d
    ECONOMIC RATIONALE: Acceleration of ensemble_drawdown_rank. Rank of combined price and leverage stress.
    """
    return (_rank_pct(close/close.rolling(252).max() + liabs/assets.replace(0, 1e-9), 252)).diff(252).diff(_TD_MON)

def dsen_356_distress_reversal_potential_accel_5d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_356_distress_reversal_potential_accel_5d
    ECONOMIC RATIONALE: Acceleration of distress_reversal_potential. Reversal potential for highly levered distressed firms.
    """
    return (close.pct_change(5) * (liabs/equity.replace(0, 1e-9) > 2).astype(float)).diff(5).diff(_TD_MON)

def dsen_357_distress_reversal_potential_accel_21d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_357_distress_reversal_potential_accel_21d
    ECONOMIC RATIONALE: Acceleration of distress_reversal_potential. Reversal potential for highly levered distressed firms.
    """
    return (close.pct_change(5) * (liabs/equity.replace(0, 1e-9) > 2).astype(float)).diff(21).diff(_TD_MON)

def dsen_358_distress_reversal_potential_accel_63d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_358_distress_reversal_potential_accel_63d
    ECONOMIC RATIONALE: Acceleration of distress_reversal_potential. Reversal potential for highly levered distressed firms.
    """
    return (close.pct_change(5) * (liabs/equity.replace(0, 1e-9) > 2).astype(float)).diff(63).diff(_TD_MON)

def dsen_359_distress_reversal_potential_accel_126d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_359_distress_reversal_potential_accel_126d
    ECONOMIC RATIONALE: Acceleration of distress_reversal_potential. Reversal potential for highly levered distressed firms.
    """
    return (close.pct_change(5) * (liabs/equity.replace(0, 1e-9) > 2).astype(float)).diff(126).diff(_TD_MON)

def dsen_360_distress_reversal_potential_accel_252d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_360_distress_reversal_potential_accel_252d
    ECONOMIC RATIONALE: Acceleration of distress_reversal_potential. Reversal potential for highly levered distressed firms.
    """
    return (close.pct_change(5) * (liabs/equity.replace(0, 1e-9) > 2).astype(float)).diff(252).diff(_TD_MON)

def dsen_361_ensemble_liquidity_gap_accel_5d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_361_ensemble_liquidity_gap_accel_5d
    ECONOMIC RATIONALE: Acceleration of ensemble_liquidity_gap. Net cash flow after change in liabilities.
    """
    return (ocf - liabs.diff(63)).diff(5).diff(_TD_MON)

def dsen_362_ensemble_liquidity_gap_accel_21d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_362_ensemble_liquidity_gap_accel_21d
    ECONOMIC RATIONALE: Acceleration of ensemble_liquidity_gap. Net cash flow after change in liabilities.
    """
    return (ocf - liabs.diff(63)).diff(21).diff(_TD_MON)

def dsen_363_ensemble_liquidity_gap_accel_63d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_363_ensemble_liquidity_gap_accel_63d
    ECONOMIC RATIONALE: Acceleration of ensemble_liquidity_gap. Net cash flow after change in liabilities.
    """
    return (ocf - liabs.diff(63)).diff(63).diff(_TD_MON)

def dsen_364_ensemble_liquidity_gap_accel_126d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_364_ensemble_liquidity_gap_accel_126d
    ECONOMIC RATIONALE: Acceleration of ensemble_liquidity_gap. Net cash flow after change in liabilities.
    """
    return (ocf - liabs.diff(63)).diff(126).diff(_TD_MON)

def dsen_365_ensemble_liquidity_gap_accel_252d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_365_ensemble_liquidity_gap_accel_252d
    ECONOMIC RATIONALE: Acceleration of ensemble_liquidity_gap. Net cash flow after change in liabilities.
    """
    return (ocf - liabs.diff(63)).diff(252).diff(_TD_MON)

def dsen_366_structural_fragility_index_accel_5d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_366_structural_fragility_index_accel_5d
    ECONOMIC RATIONALE: Acceleration of structural_fragility_index. Financial leverage relative to price stability.
    """
    return ((liabs/equity.replace(0, 1e-9)) / close.rolling(252).std().replace(0, 1e-9)).diff(5).diff(_TD_MON)

def dsen_367_structural_fragility_index_accel_21d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_367_structural_fragility_index_accel_21d
    ECONOMIC RATIONALE: Acceleration of structural_fragility_index. Financial leverage relative to price stability.
    """
    return ((liabs/equity.replace(0, 1e-9)) / close.rolling(252).std().replace(0, 1e-9)).diff(21).diff(_TD_MON)

def dsen_368_structural_fragility_index_accel_63d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_368_structural_fragility_index_accel_63d
    ECONOMIC RATIONALE: Acceleration of structural_fragility_index. Financial leverage relative to price stability.
    """
    return ((liabs/equity.replace(0, 1e-9)) / close.rolling(252).std().replace(0, 1e-9)).diff(63).diff(_TD_MON)

def dsen_369_structural_fragility_index_accel_126d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_369_structural_fragility_index_accel_126d
    ECONOMIC RATIONALE: Acceleration of structural_fragility_index. Financial leverage relative to price stability.
    """
    return ((liabs/equity.replace(0, 1e-9)) / close.rolling(252).std().replace(0, 1e-9)).diff(126).diff(_TD_MON)

def dsen_370_structural_fragility_index_accel_252d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_370_structural_fragility_index_accel_252d
    ECONOMIC RATIONALE: Acceleration of structural_fragility_index. Financial leverage relative to price stability.
    """
    return ((liabs/equity.replace(0, 1e-9)) / close.rolling(252).std().replace(0, 1e-9)).diff(252).diff(_TD_MON)

def dsen_371_ensemble_tail_risk_accel_5d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_371_ensemble_tail_risk_accel_5d
    ECONOMIC RATIONALE: Acceleration of ensemble_tail_risk. Co-occurrence of price tail events and insolvency.
    """
    return (((close.pct_change(1) < -0.05) & (liabs > equity)).astype(float)).diff(5).diff(_TD_MON)

def dsen_372_ensemble_tail_risk_accel_21d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_372_ensemble_tail_risk_accel_21d
    ECONOMIC RATIONALE: Acceleration of ensemble_tail_risk. Co-occurrence of price tail events and insolvency.
    """
    return (((close.pct_change(1) < -0.05) & (liabs > equity)).astype(float)).diff(21).diff(_TD_MON)

def dsen_373_ensemble_tail_risk_accel_63d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_373_ensemble_tail_risk_accel_63d
    ECONOMIC RATIONALE: Acceleration of ensemble_tail_risk. Co-occurrence of price tail events and insolvency.
    """
    return (((close.pct_change(1) < -0.05) & (liabs > equity)).astype(float)).diff(63).diff(_TD_MON)

def dsen_374_ensemble_tail_risk_accel_126d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_374_ensemble_tail_risk_accel_126d
    ECONOMIC RATIONALE: Acceleration of ensemble_tail_risk. Co-occurrence of price tail events and insolvency.
    """
    return (((close.pct_change(1) < -0.05) & (liabs > equity)).astype(float)).diff(126).diff(_TD_MON)

def dsen_375_ensemble_tail_risk_accel_252d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_375_ensemble_tail_risk_accel_252d
    ECONOMIC RATIONALE: Acceleration of ensemble_tail_risk. Co-occurrence of price tail events and insolvency.
    """
    return (((close.pct_change(1) < -0.05) & (liabs > equity)).astype(float)).diff(252).diff(_TD_MON)

# ── Registry ──────────────────────────────────────────────────────────────────
V121_REGISTRY_ACCEL = {
    "dsen_301_composite_distress_z_accel_5d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_301_composite_distress_z_accel_5d},
    "dsen_302_composite_distress_z_accel_21d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_302_composite_distress_z_accel_21d},
    "dsen_303_composite_distress_z_accel_63d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_303_composite_distress_z_accel_63d},
    "dsen_304_composite_distress_z_accel_126d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_304_composite_distress_z_accel_126d},
    "dsen_305_composite_distress_z_accel_252d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_305_composite_distress_z_accel_252d},
    "dsen_306_valuation_solvency_blend_accel_5d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_306_valuation_solvency_blend_accel_5d},
    "dsen_307_valuation_solvency_blend_accel_21d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_307_valuation_solvency_blend_accel_21d},
    "dsen_308_valuation_solvency_blend_accel_63d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_308_valuation_solvency_blend_accel_63d},
    "dsen_309_valuation_solvency_blend_accel_126d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_309_valuation_solvency_blend_accel_126d},
    "dsen_310_valuation_solvency_blend_accel_252d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_310_valuation_solvency_blend_accel_252d},
    "dsen_311_liquidity_momentum_ensemble_accel_5d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_311_liquidity_momentum_ensemble_accel_5d},
    "dsen_312_liquidity_momentum_ensemble_accel_21d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_312_liquidity_momentum_ensemble_accel_21d},
    "dsen_313_liquidity_momentum_ensemble_accel_63d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_313_liquidity_momentum_ensemble_accel_63d},
    "dsen_314_liquidity_momentum_ensemble_accel_126d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_314_liquidity_momentum_ensemble_accel_126d},
    "dsen_315_liquidity_momentum_ensemble_accel_252d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_315_liquidity_momentum_ensemble_accel_252d},
    "dsen_316_distress_regime_indicator_accel_5d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_316_distress_regime_indicator_accel_5d},
    "dsen_317_distress_regime_indicator_accel_21d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_317_distress_regime_indicator_accel_21d},
    "dsen_318_distress_regime_indicator_accel_63d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_318_distress_regime_indicator_accel_63d},
    "dsen_319_distress_regime_indicator_accel_126d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_319_distress_regime_indicator_accel_126d},
    "dsen_320_distress_regime_indicator_accel_252d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_320_distress_regime_indicator_accel_252d},
    "dsen_321_ensemble_vol_risk_accel_5d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_321_ensemble_vol_risk_accel_5d},
    "dsen_322_ensemble_vol_risk_accel_21d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_322_ensemble_vol_risk_accel_21d},
    "dsen_323_ensemble_vol_risk_accel_63d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_323_ensemble_vol_risk_accel_63d},
    "dsen_324_ensemble_vol_risk_accel_126d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_324_ensemble_vol_risk_accel_126d},
    "dsen_325_ensemble_vol_risk_accel_252d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_325_ensemble_vol_risk_accel_252d},
    "dsen_326_multi_factor_drawdown_accel_5d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_326_multi_factor_drawdown_accel_5d},
    "dsen_327_multi_factor_drawdown_accel_21d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_327_multi_factor_drawdown_accel_21d},
    "dsen_328_multi_factor_drawdown_accel_63d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_328_multi_factor_drawdown_accel_63d},
    "dsen_329_multi_factor_drawdown_accel_126d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_329_multi_factor_drawdown_accel_126d},
    "dsen_330_multi_factor_drawdown_accel_252d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_330_multi_factor_drawdown_accel_252d},
    "dsen_331_distress_acceleration_accel_5d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_331_distress_acceleration_accel_5d},
    "dsen_332_distress_acceleration_accel_21d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_332_distress_acceleration_accel_21d},
    "dsen_333_distress_acceleration_accel_63d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_333_distress_acceleration_accel_63d},
    "dsen_334_distress_acceleration_accel_126d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_334_distress_acceleration_accel_126d},
    "dsen_335_distress_acceleration_accel_252d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_335_distress_acceleration_accel_252d},
    "dsen_336_solvency_quality_score_accel_5d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_336_solvency_quality_score_accel_5d},
    "dsen_337_solvency_quality_score_accel_21d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_337_solvency_quality_score_accel_21d},
    "dsen_338_solvency_quality_score_accel_63d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_338_solvency_quality_score_accel_63d},
    "dsen_339_solvency_quality_score_accel_126d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_339_solvency_quality_score_accel_126d},
    "dsen_340_solvency_quality_score_accel_252d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_340_solvency_quality_score_accel_252d},
    "dsen_341_ensemble_zscore_accel_5d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_341_ensemble_zscore_accel_5d},
    "dsen_342_ensemble_zscore_accel_21d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_342_ensemble_zscore_accel_21d},
    "dsen_343_ensemble_zscore_accel_63d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_343_ensemble_zscore_accel_63d},
    "dsen_344_ensemble_zscore_accel_126d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_344_ensemble_zscore_accel_126d},
    "dsen_345_ensemble_zscore_accel_252d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_345_ensemble_zscore_accel_252d},
    "dsen_346_market_distress_beta_accel_5d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_346_market_distress_beta_accel_5d},
    "dsen_347_market_distress_beta_accel_21d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_347_market_distress_beta_accel_21d},
    "dsen_348_market_distress_beta_accel_63d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_348_market_distress_beta_accel_63d},
    "dsen_349_market_distress_beta_accel_126d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_349_market_distress_beta_accel_126d},
    "dsen_350_market_distress_beta_accel_252d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_350_market_distress_beta_accel_252d},
    "dsen_351_ensemble_drawdown_rank_accel_5d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_351_ensemble_drawdown_rank_accel_5d},
    "dsen_352_ensemble_drawdown_rank_accel_21d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_352_ensemble_drawdown_rank_accel_21d},
    "dsen_353_ensemble_drawdown_rank_accel_63d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_353_ensemble_drawdown_rank_accel_63d},
    "dsen_354_ensemble_drawdown_rank_accel_126d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_354_ensemble_drawdown_rank_accel_126d},
    "dsen_355_ensemble_drawdown_rank_accel_252d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_355_ensemble_drawdown_rank_accel_252d},
    "dsen_356_distress_reversal_potential_accel_5d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_356_distress_reversal_potential_accel_5d},
    "dsen_357_distress_reversal_potential_accel_21d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_357_distress_reversal_potential_accel_21d},
    "dsen_358_distress_reversal_potential_accel_63d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_358_distress_reversal_potential_accel_63d},
    "dsen_359_distress_reversal_potential_accel_126d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_359_distress_reversal_potential_accel_126d},
    "dsen_360_distress_reversal_potential_accel_252d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_360_distress_reversal_potential_accel_252d},
    "dsen_361_ensemble_liquidity_gap_accel_5d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_361_ensemble_liquidity_gap_accel_5d},
    "dsen_362_ensemble_liquidity_gap_accel_21d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_362_ensemble_liquidity_gap_accel_21d},
    "dsen_363_ensemble_liquidity_gap_accel_63d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_363_ensemble_liquidity_gap_accel_63d},
    "dsen_364_ensemble_liquidity_gap_accel_126d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_364_ensemble_liquidity_gap_accel_126d},
    "dsen_365_ensemble_liquidity_gap_accel_252d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_365_ensemble_liquidity_gap_accel_252d},
    "dsen_366_structural_fragility_index_accel_5d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_366_structural_fragility_index_accel_5d},
    "dsen_367_structural_fragility_index_accel_21d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_367_structural_fragility_index_accel_21d},
    "dsen_368_structural_fragility_index_accel_63d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_368_structural_fragility_index_accel_63d},
    "dsen_369_structural_fragility_index_accel_126d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_369_structural_fragility_index_accel_126d},
    "dsen_370_structural_fragility_index_accel_252d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_370_structural_fragility_index_accel_252d},
    "dsen_371_ensemble_tail_risk_accel_5d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_371_ensemble_tail_risk_accel_5d},
    "dsen_372_ensemble_tail_risk_accel_21d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_372_ensemble_tail_risk_accel_21d},
    "dsen_373_ensemble_tail_risk_accel_63d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_373_ensemble_tail_risk_accel_63d},
    "dsen_374_ensemble_tail_risk_accel_126d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_374_ensemble_tail_risk_accel_126d},
    "dsen_375_ensemble_tail_risk_accel_252d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_375_ensemble_tail_risk_accel_252d},
}
