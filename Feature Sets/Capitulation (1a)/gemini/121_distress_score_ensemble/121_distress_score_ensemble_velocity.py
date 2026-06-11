"""
121_distress_score_ensemble — Velocity (2nd Derivatives)
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

def dsen_226_composite_distress_z_vel_5d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_226_composite_distress_z_vel_5d
    ECONOMIC RATIONALE: Velocity of composite_distress_z. Combined leverage and cash flow distress.
    """
    return (_zscore_rolling(liabs/equity.replace(0, 1e-9) + (ocf < 0).astype(float), 252)).diff(5)

def dsen_227_composite_distress_z_vel_21d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_227_composite_distress_z_vel_21d
    ECONOMIC RATIONALE: Velocity of composite_distress_z. Combined leverage and cash flow distress.
    """
    return (_zscore_rolling(liabs/equity.replace(0, 1e-9) + (ocf < 0).astype(float), 252)).diff(21)

def dsen_228_composite_distress_z_vel_63d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_228_composite_distress_z_vel_63d
    ECONOMIC RATIONALE: Velocity of composite_distress_z. Combined leverage and cash flow distress.
    """
    return (_zscore_rolling(liabs/equity.replace(0, 1e-9) + (ocf < 0).astype(float), 252)).diff(63)

def dsen_229_composite_distress_z_vel_126d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_229_composite_distress_z_vel_126d
    ECONOMIC RATIONALE: Velocity of composite_distress_z. Combined leverage and cash flow distress.
    """
    return (_zscore_rolling(liabs/equity.replace(0, 1e-9) + (ocf < 0).astype(float), 252)).diff(126)

def dsen_230_composite_distress_z_vel_252d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_230_composite_distress_z_vel_252d
    ECONOMIC RATIONALE: Velocity of composite_distress_z. Combined leverage and cash flow distress.
    """
    return (_zscore_rolling(liabs/equity.replace(0, 1e-9) + (ocf < 0).astype(float), 252)).diff(252)

def dsen_231_valuation_solvency_blend_vel_5d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_231_valuation_solvency_blend_vel_5d
    ECONOMIC RATIONALE: Velocity of valuation_solvency_blend. Valuation drawdown weighted by solvency.
    """
    return ((close/close.rolling(252).max()) * (equity/liabs.replace(0, 1e-9))).diff(5)

def dsen_232_valuation_solvency_blend_vel_21d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_232_valuation_solvency_blend_vel_21d
    ECONOMIC RATIONALE: Velocity of valuation_solvency_blend. Valuation drawdown weighted by solvency.
    """
    return ((close/close.rolling(252).max()) * (equity/liabs.replace(0, 1e-9))).diff(21)

def dsen_233_valuation_solvency_blend_vel_63d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_233_valuation_solvency_blend_vel_63d
    ECONOMIC RATIONALE: Velocity of valuation_solvency_blend. Valuation drawdown weighted by solvency.
    """
    return ((close/close.rolling(252).max()) * (equity/liabs.replace(0, 1e-9))).diff(63)

def dsen_234_valuation_solvency_blend_vel_126d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_234_valuation_solvency_blend_vel_126d
    ECONOMIC RATIONALE: Velocity of valuation_solvency_blend. Valuation drawdown weighted by solvency.
    """
    return ((close/close.rolling(252).max()) * (equity/liabs.replace(0, 1e-9))).diff(126)

def dsen_235_valuation_solvency_blend_vel_252d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_235_valuation_solvency_blend_vel_252d
    ECONOMIC RATIONALE: Velocity of valuation_solvency_blend. Valuation drawdown weighted by solvency.
    """
    return ((close/close.rolling(252).max()) * (equity/liabs.replace(0, 1e-9))).diff(252)

def dsen_236_liquidity_momentum_ensemble_vel_5d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_236_liquidity_momentum_ensemble_vel_5d
    ECONOMIC RATIONALE: Velocity of liquidity_momentum_ensemble. Combined fundamental and price momentum.
    """
    return (ocf.pct_change(63) + close.pct_change(63)).diff(5)

def dsen_237_liquidity_momentum_ensemble_vel_21d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_237_liquidity_momentum_ensemble_vel_21d
    ECONOMIC RATIONALE: Velocity of liquidity_momentum_ensemble. Combined fundamental and price momentum.
    """
    return (ocf.pct_change(63) + close.pct_change(63)).diff(21)

def dsen_238_liquidity_momentum_ensemble_vel_63d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_238_liquidity_momentum_ensemble_vel_63d
    ECONOMIC RATIONALE: Velocity of liquidity_momentum_ensemble. Combined fundamental and price momentum.
    """
    return (ocf.pct_change(63) + close.pct_change(63)).diff(63)

def dsen_239_liquidity_momentum_ensemble_vel_126d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_239_liquidity_momentum_ensemble_vel_126d
    ECONOMIC RATIONALE: Velocity of liquidity_momentum_ensemble. Combined fundamental and price momentum.
    """
    return (ocf.pct_change(63) + close.pct_change(63)).diff(126)

def dsen_240_liquidity_momentum_ensemble_vel_252d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_240_liquidity_momentum_ensemble_vel_252d
    ECONOMIC RATIONALE: Velocity of liquidity_momentum_ensemble. Combined fundamental and price momentum.
    """
    return (ocf.pct_change(63) + close.pct_change(63)).diff(252)

def dsen_241_distress_regime_indicator_vel_5d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_241_distress_regime_indicator_vel_5d
    ECONOMIC RATIONALE: Velocity of distress_regime_indicator. Binary flag for structural distress.
    """
    return (((liabs > assets) | (ocf < 0)).astype(float)).diff(5)

def dsen_242_distress_regime_indicator_vel_21d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_242_distress_regime_indicator_vel_21d
    ECONOMIC RATIONALE: Velocity of distress_regime_indicator. Binary flag for structural distress.
    """
    return (((liabs > assets) | (ocf < 0)).astype(float)).diff(21)

def dsen_243_distress_regime_indicator_vel_63d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_243_distress_regime_indicator_vel_63d
    ECONOMIC RATIONALE: Velocity of distress_regime_indicator. Binary flag for structural distress.
    """
    return (((liabs > assets) | (ocf < 0)).astype(float)).diff(63)

def dsen_244_distress_regime_indicator_vel_126d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_244_distress_regime_indicator_vel_126d
    ECONOMIC RATIONALE: Velocity of distress_regime_indicator. Binary flag for structural distress.
    """
    return (((liabs > assets) | (ocf < 0)).astype(float)).diff(126)

def dsen_245_distress_regime_indicator_vel_252d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_245_distress_regime_indicator_vel_252d
    ECONOMIC RATIONALE: Velocity of distress_regime_indicator. Binary flag for structural distress.
    """
    return (((liabs > assets) | (ocf < 0)).astype(float)).diff(252)

def dsen_246_ensemble_vol_risk_vel_5d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_246_ensemble_vol_risk_vel_5d
    ECONOMIC RATIONALE: Velocity of ensemble_vol_risk. Volatility amplified by financial leverage.
    """
    return (close.rolling(21).std() * (liabs/equity.replace(0, 1e-9))).diff(5)

def dsen_247_ensemble_vol_risk_vel_21d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_247_ensemble_vol_risk_vel_21d
    ECONOMIC RATIONALE: Velocity of ensemble_vol_risk. Volatility amplified by financial leverage.
    """
    return (close.rolling(21).std() * (liabs/equity.replace(0, 1e-9))).diff(21)

def dsen_248_ensemble_vol_risk_vel_63d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_248_ensemble_vol_risk_vel_63d
    ECONOMIC RATIONALE: Velocity of ensemble_vol_risk. Volatility amplified by financial leverage.
    """
    return (close.rolling(21).std() * (liabs/equity.replace(0, 1e-9))).diff(63)

def dsen_249_ensemble_vol_risk_vel_126d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_249_ensemble_vol_risk_vel_126d
    ECONOMIC RATIONALE: Velocity of ensemble_vol_risk. Volatility amplified by financial leverage.
    """
    return (close.rolling(21).std() * (liabs/equity.replace(0, 1e-9))).diff(126)

def dsen_250_ensemble_vol_risk_vel_252d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_250_ensemble_vol_risk_vel_252d
    ECONOMIC RATIONALE: Velocity of ensemble_vol_risk. Volatility amplified by financial leverage.
    """
    return (close.rolling(21).std() * (liabs/equity.replace(0, 1e-9))).diff(252)

def dsen_251_multi_factor_drawdown_vel_5d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_251_multi_factor_drawdown_vel_5d
    ECONOMIC RATIONALE: Velocity of multi_factor_drawdown. Combined price and equity drawdown.
    """
    return ((close/close.rolling(252).max() - 1) + (equity/equity.rolling(252).max() - 1)).diff(5)

def dsen_252_multi_factor_drawdown_vel_21d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_252_multi_factor_drawdown_vel_21d
    ECONOMIC RATIONALE: Velocity of multi_factor_drawdown. Combined price and equity drawdown.
    """
    return ((close/close.rolling(252).max() - 1) + (equity/equity.rolling(252).max() - 1)).diff(21)

def dsen_253_multi_factor_drawdown_vel_63d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_253_multi_factor_drawdown_vel_63d
    ECONOMIC RATIONALE: Velocity of multi_factor_drawdown. Combined price and equity drawdown.
    """
    return ((close/close.rolling(252).max() - 1) + (equity/equity.rolling(252).max() - 1)).diff(63)

def dsen_254_multi_factor_drawdown_vel_126d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_254_multi_factor_drawdown_vel_126d
    ECONOMIC RATIONALE: Velocity of multi_factor_drawdown. Combined price and equity drawdown.
    """
    return ((close/close.rolling(252).max() - 1) + (equity/equity.rolling(252).max() - 1)).diff(126)

def dsen_255_multi_factor_drawdown_vel_252d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_255_multi_factor_drawdown_vel_252d
    ECONOMIC RATIONALE: Velocity of multi_factor_drawdown. Combined price and equity drawdown.
    """
    return ((close/close.rolling(252).max() - 1) + (equity/equity.rolling(252).max() - 1)).diff(252)

def dsen_256_distress_acceleration_vel_5d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_256_distress_acceleration_vel_5d
    ECONOMIC RATIONALE: Velocity of distress_acceleration. Acceleration of leverage combined with price decline.
    """
    return ((liabs/equity.replace(0, 1e-9)).diff(63) + close.pct_change(63)).diff(5)

def dsen_257_distress_acceleration_vel_21d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_257_distress_acceleration_vel_21d
    ECONOMIC RATIONALE: Velocity of distress_acceleration. Acceleration of leverage combined with price decline.
    """
    return ((liabs/equity.replace(0, 1e-9)).diff(63) + close.pct_change(63)).diff(21)

def dsen_258_distress_acceleration_vel_63d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_258_distress_acceleration_vel_63d
    ECONOMIC RATIONALE: Velocity of distress_acceleration. Acceleration of leverage combined with price decline.
    """
    return ((liabs/equity.replace(0, 1e-9)).diff(63) + close.pct_change(63)).diff(63)

def dsen_259_distress_acceleration_vel_126d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_259_distress_acceleration_vel_126d
    ECONOMIC RATIONALE: Velocity of distress_acceleration. Acceleration of leverage combined with price decline.
    """
    return ((liabs/equity.replace(0, 1e-9)).diff(63) + close.pct_change(63)).diff(126)

def dsen_260_distress_acceleration_vel_252d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_260_distress_acceleration_vel_252d
    ECONOMIC RATIONALE: Velocity of distress_acceleration. Acceleration of leverage combined with price decline.
    """
    return ((liabs/equity.replace(0, 1e-9)).diff(63) + close.pct_change(63)).diff(252)

def dsen_261_solvency_quality_score_vel_5d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_261_solvency_quality_score_vel_5d
    ECONOMIC RATIONALE: Velocity of solvency_quality_score. Cash flow coverage of debt adjusted by equity status.
    """
    return (ocf / liabs.replace(0, 1e-9) * (equity > 0).astype(float)).diff(5)

def dsen_262_solvency_quality_score_vel_21d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_262_solvency_quality_score_vel_21d
    ECONOMIC RATIONALE: Velocity of solvency_quality_score. Cash flow coverage of debt adjusted by equity status.
    """
    return (ocf / liabs.replace(0, 1e-9) * (equity > 0).astype(float)).diff(21)

def dsen_263_solvency_quality_score_vel_63d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_263_solvency_quality_score_vel_63d
    ECONOMIC RATIONALE: Velocity of solvency_quality_score. Cash flow coverage of debt adjusted by equity status.
    """
    return (ocf / liabs.replace(0, 1e-9) * (equity > 0).astype(float)).diff(63)

def dsen_264_solvency_quality_score_vel_126d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_264_solvency_quality_score_vel_126d
    ECONOMIC RATIONALE: Velocity of solvency_quality_score. Cash flow coverage of debt adjusted by equity status.
    """
    return (ocf / liabs.replace(0, 1e-9) * (equity > 0).astype(float)).diff(126)

def dsen_265_solvency_quality_score_vel_252d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_265_solvency_quality_score_vel_252d
    ECONOMIC RATIONALE: Velocity of solvency_quality_score. Cash flow coverage of debt adjusted by equity status.
    """
    return (ocf / liabs.replace(0, 1e-9) * (equity > 0).astype(float)).diff(252)

def dsen_266_ensemble_zscore_vel_5d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_266_ensemble_zscore_vel_5d
    ECONOMIC RATIONALE: Velocity of ensemble_zscore. Integrated balance sheet and income statement distress.
    """
    return (_zscore_rolling(liabs/assets.replace(0, 1e-9) - ocf/assets.replace(0, 1e-9), 252)).diff(5)

def dsen_267_ensemble_zscore_vel_21d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_267_ensemble_zscore_vel_21d
    ECONOMIC RATIONALE: Velocity of ensemble_zscore. Integrated balance sheet and income statement distress.
    """
    return (_zscore_rolling(liabs/assets.replace(0, 1e-9) - ocf/assets.replace(0, 1e-9), 252)).diff(21)

def dsen_268_ensemble_zscore_vel_63d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_268_ensemble_zscore_vel_63d
    ECONOMIC RATIONALE: Velocity of ensemble_zscore. Integrated balance sheet and income statement distress.
    """
    return (_zscore_rolling(liabs/assets.replace(0, 1e-9) - ocf/assets.replace(0, 1e-9), 252)).diff(63)

def dsen_269_ensemble_zscore_vel_126d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_269_ensemble_zscore_vel_126d
    ECONOMIC RATIONALE: Velocity of ensemble_zscore. Integrated balance sheet and income statement distress.
    """
    return (_zscore_rolling(liabs/assets.replace(0, 1e-9) - ocf/assets.replace(0, 1e-9), 252)).diff(126)

def dsen_270_ensemble_zscore_vel_252d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_270_ensemble_zscore_vel_252d
    ECONOMIC RATIONALE: Velocity of ensemble_zscore. Integrated balance sheet and income statement distress.
    """
    return (_zscore_rolling(liabs/assets.replace(0, 1e-9) - ocf/assets.replace(0, 1e-9), 252)).diff(252)

def dsen_271_market_distress_beta_vel_5d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_271_market_distress_beta_vel_5d
    ECONOMIC RATIONALE: Velocity of market_distress_beta. Market sensitivity weighted by financial risk.
    """
    return (close.pct_change(1).rolling(63).corr(mkt_close.pct_change(1)) * (liabs/equity.replace(0, 1e-9))).diff(5)

def dsen_272_market_distress_beta_vel_21d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_272_market_distress_beta_vel_21d
    ECONOMIC RATIONALE: Velocity of market_distress_beta. Market sensitivity weighted by financial risk.
    """
    return (close.pct_change(1).rolling(63).corr(mkt_close.pct_change(1)) * (liabs/equity.replace(0, 1e-9))).diff(21)

def dsen_273_market_distress_beta_vel_63d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_273_market_distress_beta_vel_63d
    ECONOMIC RATIONALE: Velocity of market_distress_beta. Market sensitivity weighted by financial risk.
    """
    return (close.pct_change(1).rolling(63).corr(mkt_close.pct_change(1)) * (liabs/equity.replace(0, 1e-9))).diff(63)

def dsen_274_market_distress_beta_vel_126d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_274_market_distress_beta_vel_126d
    ECONOMIC RATIONALE: Velocity of market_distress_beta. Market sensitivity weighted by financial risk.
    """
    return (close.pct_change(1).rolling(63).corr(mkt_close.pct_change(1)) * (liabs/equity.replace(0, 1e-9))).diff(126)

def dsen_275_market_distress_beta_vel_252d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_275_market_distress_beta_vel_252d
    ECONOMIC RATIONALE: Velocity of market_distress_beta. Market sensitivity weighted by financial risk.
    """
    return (close.pct_change(1).rolling(63).corr(mkt_close.pct_change(1)) * (liabs/equity.replace(0, 1e-9))).diff(252)

def dsen_276_ensemble_drawdown_rank_vel_5d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_276_ensemble_drawdown_rank_vel_5d
    ECONOMIC RATIONALE: Velocity of ensemble_drawdown_rank. Rank of combined price and leverage stress.
    """
    return (_rank_pct(close/close.rolling(252).max() + liabs/assets.replace(0, 1e-9), 252)).diff(5)

def dsen_277_ensemble_drawdown_rank_vel_21d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_277_ensemble_drawdown_rank_vel_21d
    ECONOMIC RATIONALE: Velocity of ensemble_drawdown_rank. Rank of combined price and leverage stress.
    """
    return (_rank_pct(close/close.rolling(252).max() + liabs/assets.replace(0, 1e-9), 252)).diff(21)

def dsen_278_ensemble_drawdown_rank_vel_63d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_278_ensemble_drawdown_rank_vel_63d
    ECONOMIC RATIONALE: Velocity of ensemble_drawdown_rank. Rank of combined price and leverage stress.
    """
    return (_rank_pct(close/close.rolling(252).max() + liabs/assets.replace(0, 1e-9), 252)).diff(63)

def dsen_279_ensemble_drawdown_rank_vel_126d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_279_ensemble_drawdown_rank_vel_126d
    ECONOMIC RATIONALE: Velocity of ensemble_drawdown_rank. Rank of combined price and leverage stress.
    """
    return (_rank_pct(close/close.rolling(252).max() + liabs/assets.replace(0, 1e-9), 252)).diff(126)

def dsen_280_ensemble_drawdown_rank_vel_252d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_280_ensemble_drawdown_rank_vel_252d
    ECONOMIC RATIONALE: Velocity of ensemble_drawdown_rank. Rank of combined price and leverage stress.
    """
    return (_rank_pct(close/close.rolling(252).max() + liabs/assets.replace(0, 1e-9), 252)).diff(252)

def dsen_281_distress_reversal_potential_vel_5d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_281_distress_reversal_potential_vel_5d
    ECONOMIC RATIONALE: Velocity of distress_reversal_potential. Reversal potential for highly levered distressed firms.
    """
    return (close.pct_change(5) * (liabs/equity.replace(0, 1e-9) > 2).astype(float)).diff(5)

def dsen_282_distress_reversal_potential_vel_21d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_282_distress_reversal_potential_vel_21d
    ECONOMIC RATIONALE: Velocity of distress_reversal_potential. Reversal potential for highly levered distressed firms.
    """
    return (close.pct_change(5) * (liabs/equity.replace(0, 1e-9) > 2).astype(float)).diff(21)

def dsen_283_distress_reversal_potential_vel_63d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_283_distress_reversal_potential_vel_63d
    ECONOMIC RATIONALE: Velocity of distress_reversal_potential. Reversal potential for highly levered distressed firms.
    """
    return (close.pct_change(5) * (liabs/equity.replace(0, 1e-9) > 2).astype(float)).diff(63)

def dsen_284_distress_reversal_potential_vel_126d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_284_distress_reversal_potential_vel_126d
    ECONOMIC RATIONALE: Velocity of distress_reversal_potential. Reversal potential for highly levered distressed firms.
    """
    return (close.pct_change(5) * (liabs/equity.replace(0, 1e-9) > 2).astype(float)).diff(126)

def dsen_285_distress_reversal_potential_vel_252d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_285_distress_reversal_potential_vel_252d
    ECONOMIC RATIONALE: Velocity of distress_reversal_potential. Reversal potential for highly levered distressed firms.
    """
    return (close.pct_change(5) * (liabs/equity.replace(0, 1e-9) > 2).astype(float)).diff(252)

def dsen_286_ensemble_liquidity_gap_vel_5d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_286_ensemble_liquidity_gap_vel_5d
    ECONOMIC RATIONALE: Velocity of ensemble_liquidity_gap. Net cash flow after change in liabilities.
    """
    return (ocf - liabs.diff(63)).diff(5)

def dsen_287_ensemble_liquidity_gap_vel_21d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_287_ensemble_liquidity_gap_vel_21d
    ECONOMIC RATIONALE: Velocity of ensemble_liquidity_gap. Net cash flow after change in liabilities.
    """
    return (ocf - liabs.diff(63)).diff(21)

def dsen_288_ensemble_liquidity_gap_vel_63d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_288_ensemble_liquidity_gap_vel_63d
    ECONOMIC RATIONALE: Velocity of ensemble_liquidity_gap. Net cash flow after change in liabilities.
    """
    return (ocf - liabs.diff(63)).diff(63)

def dsen_289_ensemble_liquidity_gap_vel_126d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_289_ensemble_liquidity_gap_vel_126d
    ECONOMIC RATIONALE: Velocity of ensemble_liquidity_gap. Net cash flow after change in liabilities.
    """
    return (ocf - liabs.diff(63)).diff(126)

def dsen_290_ensemble_liquidity_gap_vel_252d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_290_ensemble_liquidity_gap_vel_252d
    ECONOMIC RATIONALE: Velocity of ensemble_liquidity_gap. Net cash flow after change in liabilities.
    """
    return (ocf - liabs.diff(63)).diff(252)

def dsen_291_structural_fragility_index_vel_5d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_291_structural_fragility_index_vel_5d
    ECONOMIC RATIONALE: Velocity of structural_fragility_index. Financial leverage relative to price stability.
    """
    return ((liabs/equity.replace(0, 1e-9)) / close.rolling(252).std().replace(0, 1e-9)).diff(5)

def dsen_292_structural_fragility_index_vel_21d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_292_structural_fragility_index_vel_21d
    ECONOMIC RATIONALE: Velocity of structural_fragility_index. Financial leverage relative to price stability.
    """
    return ((liabs/equity.replace(0, 1e-9)) / close.rolling(252).std().replace(0, 1e-9)).diff(21)

def dsen_293_structural_fragility_index_vel_63d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_293_structural_fragility_index_vel_63d
    ECONOMIC RATIONALE: Velocity of structural_fragility_index. Financial leverage relative to price stability.
    """
    return ((liabs/equity.replace(0, 1e-9)) / close.rolling(252).std().replace(0, 1e-9)).diff(63)

def dsen_294_structural_fragility_index_vel_126d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_294_structural_fragility_index_vel_126d
    ECONOMIC RATIONALE: Velocity of structural_fragility_index. Financial leverage relative to price stability.
    """
    return ((liabs/equity.replace(0, 1e-9)) / close.rolling(252).std().replace(0, 1e-9)).diff(126)

def dsen_295_structural_fragility_index_vel_252d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_295_structural_fragility_index_vel_252d
    ECONOMIC RATIONALE: Velocity of structural_fragility_index. Financial leverage relative to price stability.
    """
    return ((liabs/equity.replace(0, 1e-9)) / close.rolling(252).std().replace(0, 1e-9)).diff(252)

def dsen_296_ensemble_tail_risk_vel_5d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_296_ensemble_tail_risk_vel_5d
    ECONOMIC RATIONALE: Velocity of ensemble_tail_risk. Co-occurrence of price tail events and insolvency.
    """
    return (((close.pct_change(1) < -0.05) & (liabs > equity)).astype(float)).diff(5)

def dsen_297_ensemble_tail_risk_vel_21d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_297_ensemble_tail_risk_vel_21d
    ECONOMIC RATIONALE: Velocity of ensemble_tail_risk. Co-occurrence of price tail events and insolvency.
    """
    return (((close.pct_change(1) < -0.05) & (liabs > equity)).astype(float)).diff(21)

def dsen_298_ensemble_tail_risk_vel_63d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_298_ensemble_tail_risk_vel_63d
    ECONOMIC RATIONALE: Velocity of ensemble_tail_risk. Co-occurrence of price tail events and insolvency.
    """
    return (((close.pct_change(1) < -0.05) & (liabs > equity)).astype(float)).diff(63)

def dsen_299_ensemble_tail_risk_vel_126d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_299_ensemble_tail_risk_vel_126d
    ECONOMIC RATIONALE: Velocity of ensemble_tail_risk. Co-occurrence of price tail events and insolvency.
    """
    return (((close.pct_change(1) < -0.05) & (liabs > equity)).astype(float)).diff(126)

def dsen_300_ensemble_tail_risk_vel_252d(assets: pd.Series, close: pd.Series, equity: pd.Series, liabs: pd.Series, mkt_close: pd.Series, ocf: pd.Series) -> pd.Series:
    """
    dsen_300_ensemble_tail_risk_vel_252d
    ECONOMIC RATIONALE: Velocity of ensemble_tail_risk. Co-occurrence of price tail events and insolvency.
    """
    return (((close.pct_change(1) < -0.05) & (liabs > equity)).astype(float)).diff(252)

# ── Registry ──────────────────────────────────────────────────────────────────
V121_REGISTRY_VEL = {
    "dsen_226_composite_distress_z_vel_5d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_226_composite_distress_z_vel_5d},
    "dsen_227_composite_distress_z_vel_21d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_227_composite_distress_z_vel_21d},
    "dsen_228_composite_distress_z_vel_63d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_228_composite_distress_z_vel_63d},
    "dsen_229_composite_distress_z_vel_126d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_229_composite_distress_z_vel_126d},
    "dsen_230_composite_distress_z_vel_252d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_230_composite_distress_z_vel_252d},
    "dsen_231_valuation_solvency_blend_vel_5d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_231_valuation_solvency_blend_vel_5d},
    "dsen_232_valuation_solvency_blend_vel_21d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_232_valuation_solvency_blend_vel_21d},
    "dsen_233_valuation_solvency_blend_vel_63d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_233_valuation_solvency_blend_vel_63d},
    "dsen_234_valuation_solvency_blend_vel_126d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_234_valuation_solvency_blend_vel_126d},
    "dsen_235_valuation_solvency_blend_vel_252d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_235_valuation_solvency_blend_vel_252d},
    "dsen_236_liquidity_momentum_ensemble_vel_5d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_236_liquidity_momentum_ensemble_vel_5d},
    "dsen_237_liquidity_momentum_ensemble_vel_21d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_237_liquidity_momentum_ensemble_vel_21d},
    "dsen_238_liquidity_momentum_ensemble_vel_63d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_238_liquidity_momentum_ensemble_vel_63d},
    "dsen_239_liquidity_momentum_ensemble_vel_126d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_239_liquidity_momentum_ensemble_vel_126d},
    "dsen_240_liquidity_momentum_ensemble_vel_252d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_240_liquidity_momentum_ensemble_vel_252d},
    "dsen_241_distress_regime_indicator_vel_5d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_241_distress_regime_indicator_vel_5d},
    "dsen_242_distress_regime_indicator_vel_21d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_242_distress_regime_indicator_vel_21d},
    "dsen_243_distress_regime_indicator_vel_63d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_243_distress_regime_indicator_vel_63d},
    "dsen_244_distress_regime_indicator_vel_126d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_244_distress_regime_indicator_vel_126d},
    "dsen_245_distress_regime_indicator_vel_252d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_245_distress_regime_indicator_vel_252d},
    "dsen_246_ensemble_vol_risk_vel_5d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_246_ensemble_vol_risk_vel_5d},
    "dsen_247_ensemble_vol_risk_vel_21d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_247_ensemble_vol_risk_vel_21d},
    "dsen_248_ensemble_vol_risk_vel_63d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_248_ensemble_vol_risk_vel_63d},
    "dsen_249_ensemble_vol_risk_vel_126d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_249_ensemble_vol_risk_vel_126d},
    "dsen_250_ensemble_vol_risk_vel_252d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_250_ensemble_vol_risk_vel_252d},
    "dsen_251_multi_factor_drawdown_vel_5d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_251_multi_factor_drawdown_vel_5d},
    "dsen_252_multi_factor_drawdown_vel_21d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_252_multi_factor_drawdown_vel_21d},
    "dsen_253_multi_factor_drawdown_vel_63d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_253_multi_factor_drawdown_vel_63d},
    "dsen_254_multi_factor_drawdown_vel_126d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_254_multi_factor_drawdown_vel_126d},
    "dsen_255_multi_factor_drawdown_vel_252d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_255_multi_factor_drawdown_vel_252d},
    "dsen_256_distress_acceleration_vel_5d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_256_distress_acceleration_vel_5d},
    "dsen_257_distress_acceleration_vel_21d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_257_distress_acceleration_vel_21d},
    "dsen_258_distress_acceleration_vel_63d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_258_distress_acceleration_vel_63d},
    "dsen_259_distress_acceleration_vel_126d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_259_distress_acceleration_vel_126d},
    "dsen_260_distress_acceleration_vel_252d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_260_distress_acceleration_vel_252d},
    "dsen_261_solvency_quality_score_vel_5d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_261_solvency_quality_score_vel_5d},
    "dsen_262_solvency_quality_score_vel_21d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_262_solvency_quality_score_vel_21d},
    "dsen_263_solvency_quality_score_vel_63d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_263_solvency_quality_score_vel_63d},
    "dsen_264_solvency_quality_score_vel_126d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_264_solvency_quality_score_vel_126d},
    "dsen_265_solvency_quality_score_vel_252d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_265_solvency_quality_score_vel_252d},
    "dsen_266_ensemble_zscore_vel_5d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_266_ensemble_zscore_vel_5d},
    "dsen_267_ensemble_zscore_vel_21d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_267_ensemble_zscore_vel_21d},
    "dsen_268_ensemble_zscore_vel_63d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_268_ensemble_zscore_vel_63d},
    "dsen_269_ensemble_zscore_vel_126d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_269_ensemble_zscore_vel_126d},
    "dsen_270_ensemble_zscore_vel_252d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_270_ensemble_zscore_vel_252d},
    "dsen_271_market_distress_beta_vel_5d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_271_market_distress_beta_vel_5d},
    "dsen_272_market_distress_beta_vel_21d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_272_market_distress_beta_vel_21d},
    "dsen_273_market_distress_beta_vel_63d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_273_market_distress_beta_vel_63d},
    "dsen_274_market_distress_beta_vel_126d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_274_market_distress_beta_vel_126d},
    "dsen_275_market_distress_beta_vel_252d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_275_market_distress_beta_vel_252d},
    "dsen_276_ensemble_drawdown_rank_vel_5d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_276_ensemble_drawdown_rank_vel_5d},
    "dsen_277_ensemble_drawdown_rank_vel_21d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_277_ensemble_drawdown_rank_vel_21d},
    "dsen_278_ensemble_drawdown_rank_vel_63d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_278_ensemble_drawdown_rank_vel_63d},
    "dsen_279_ensemble_drawdown_rank_vel_126d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_279_ensemble_drawdown_rank_vel_126d},
    "dsen_280_ensemble_drawdown_rank_vel_252d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_280_ensemble_drawdown_rank_vel_252d},
    "dsen_281_distress_reversal_potential_vel_5d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_281_distress_reversal_potential_vel_5d},
    "dsen_282_distress_reversal_potential_vel_21d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_282_distress_reversal_potential_vel_21d},
    "dsen_283_distress_reversal_potential_vel_63d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_283_distress_reversal_potential_vel_63d},
    "dsen_284_distress_reversal_potential_vel_126d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_284_distress_reversal_potential_vel_126d},
    "dsen_285_distress_reversal_potential_vel_252d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_285_distress_reversal_potential_vel_252d},
    "dsen_286_ensemble_liquidity_gap_vel_5d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_286_ensemble_liquidity_gap_vel_5d},
    "dsen_287_ensemble_liquidity_gap_vel_21d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_287_ensemble_liquidity_gap_vel_21d},
    "dsen_288_ensemble_liquidity_gap_vel_63d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_288_ensemble_liquidity_gap_vel_63d},
    "dsen_289_ensemble_liquidity_gap_vel_126d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_289_ensemble_liquidity_gap_vel_126d},
    "dsen_290_ensemble_liquidity_gap_vel_252d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_290_ensemble_liquidity_gap_vel_252d},
    "dsen_291_structural_fragility_index_vel_5d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_291_structural_fragility_index_vel_5d},
    "dsen_292_structural_fragility_index_vel_21d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_292_structural_fragility_index_vel_21d},
    "dsen_293_structural_fragility_index_vel_63d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_293_structural_fragility_index_vel_63d},
    "dsen_294_structural_fragility_index_vel_126d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_294_structural_fragility_index_vel_126d},
    "dsen_295_structural_fragility_index_vel_252d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_295_structural_fragility_index_vel_252d},
    "dsen_296_ensemble_tail_risk_vel_5d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_296_ensemble_tail_risk_vel_5d},
    "dsen_297_ensemble_tail_risk_vel_21d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_297_ensemble_tail_risk_vel_21d},
    "dsen_298_ensemble_tail_risk_vel_63d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_298_ensemble_tail_risk_vel_63d},
    "dsen_299_ensemble_tail_risk_vel_126d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_299_ensemble_tail_risk_vel_126d},
    "dsen_300_ensemble_tail_risk_vel_252d": {"inputs": ["assets", "close", "equity", "liabs", "mkt_close", "ocf"], "func": dsen_300_ensemble_tail_risk_vel_252d},
}
